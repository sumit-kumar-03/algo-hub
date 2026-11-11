"""
EPI 19.9 - Test the Collatz Conjecture in Parallel

Problem:
The Collatz conjecture says that repeatedly applying "if x is even, halve
it; otherwise replace it with 3x + 1" eventually reaches 1 from any
positive integer. Write a checker that verifies every integer in [1, U]
using the machine's cores, while never running more than n workers at once.

Constraints:
- Every integer in [1, U] is checked exactly once
- At most num_workers checks run concurrently
- Per-number work is tiny, so handing out one number at a time costs more
  in coordination than it saves; hand out intervals instead
- Equal static splits can leave cores idle when some intervals are slower,
  so use a shared queue of moderate-sized chunks
- U may be 0 (nothing to check) and need not be a multiple of chunk_size
- Use a thread pool: the tests pass closures as `check`, which a process
  pool cannot pickle (the book uses processes to sidestep the GIL; that is
  a worthwhile follow-up once the threaded version works)

How it works:
1. collatz_check(x): follow the sequence until it hits 1 (True), or
   revisits a value it already saw (a cycle -> False)
2. Split [1, U] into chunks of chunk_size (the last chunk may be shorter)
3. Submit the chunks to a pool with num_workers workers (e.g.
   concurrent.futures); each worker checks every number in its chunk
4. Gather and return the numbers that failed, in increasing order

Example:
parallel_check(10000, num_workers=4, chunk_size=500) -> []  (no counterexample)
parallel_check(300, 4, 50, check=lambda x: x % 97 != 0) -> [97, 194, 291]
"""

import threading
import time
from collections import Counter
from typing import Callable, List, Optional


class Solution:
    def collatz_check(self, x: int) -> bool:
        """
        Returns True if the Collatz sequence starting at x reaches 1, or
        False if it falls into a cycle that misses 1.

        Args:
            x: Positive integer
        """
        # TODO: Implement collatz_check
        pass

    def parallel_check(
        self,
        upper: int,
        num_workers: int,
        chunk_size: int,
        check: Optional[Callable[[int], bool]] = None,
    ) -> List[int]:
        """
        Checks every integer in [1, upper] in parallel.

        Args:
            upper: U, the largest integer to check (0 means nothing to check)
            num_workers: Maximum number of concurrently running workers
            chunk_size: Number of consecutive integers per unit of work
            check: Per-number predicate; defaults to self.collatz_check

        Returns:
            Sorted list of integers in [1, upper] for which check is False

        Time Complexity: O(total check work / num_workers) ideally
        Space Complexity: O(upper / chunk_size) queued chunks
        """
        # TODO: Implement parallel_check
        pass


def test_parallel_collatz():
    """Test cases for the parallel Collatz checker"""
    sol = Solution()

    # Test case 1: Single-number checks
    assert sol.collatz_check(1) is True
    assert sol.collatz_check(27) is True  # famous long trajectory (111 steps)
    assert all(sol.collatz_check(x) is True for x in range(1, 2001))
    print("✓ Test 1 passed: collatz_check on 1..2000")

    # Test case 2: No counterexamples in [1, 20000]
    assert sol.parallel_check(20000, num_workers=4, chunk_size=500) == []
    print("✓ Test 2 passed: No counterexamples up to 20000")

    # Test case 3: Every number is checked exactly once (uneven last chunk)
    seen: Counter = Counter()
    seen_lock = threading.Lock()

    def recording_check(x: int) -> bool:
        with seen_lock:
            seen[x] += 1
        return True

    assert sol.parallel_check(1003, num_workers=3, chunk_size=100,
                              check=recording_check) == []
    assert set(seen) == set(range(1, 1004))
    assert all(c == 1 for c in seen.values())
    print("✓ Test 3 passed: Each of 1..1003 checked exactly once")

    # Test case 4: Failures are reported in sorted order
    failing = sol.parallel_check(300, num_workers=4, chunk_size=7,
                                 check=lambda x: x % 97 != 0)
    assert failing == [97, 194, 291]
    print("✓ Test 4 passed: Failing numbers reported in order")

    # Test case 5: Concurrency is capped at num_workers (and actually used)
    active = {"now": 0, "peak": 0}
    active_lock = threading.Lock()

    def slow_check(x: int) -> bool:
        with active_lock:
            active["now"] += 1
            active["peak"] = max(active["peak"], active["now"])
        time.sleep(0.002)
        with active_lock:
            active["now"] -= 1
        return True

    assert sol.parallel_check(200, num_workers=3, chunk_size=10,
                              check=slow_check) == []
    assert 2 <= active["peak"] <= 3, f"peak concurrency {active['peak']}"
    print("✓ Test 5 passed: At most num_workers checks at once")

    # Test case 6: Edge cases
    assert sol.parallel_check(0, num_workers=2, chunk_size=10) == []
    assert sol.parallel_check(1, num_workers=2, chunk_size=10) == []
    assert sol.parallel_check(5, num_workers=8, chunk_size=1000,
                              check=lambda x: x != 5) == [5]
    print("✓ Test 6 passed: Edge cases (U = 0, U = 1, chunk > U)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_parallel_collatz()
