"""
EPI 19.3 Extra Variant - Round-Robin Printing with k Threads
(Practice problem, not in the book. Difficulty: Medium)
Builds on: The two-thread turn monitor, generalized from a boolean turn to
a turn index shared by k threads.

Problem:
Start k worker threads numbered 0..k-1. Worker i is responsible for the
numbers x in 1..n with (x - 1) % k == i, so with k = 3 worker 0 owns
1, 4, 7, ..., worker 1 owns 2, 5, 8, ..., and worker 2 owns 3, 6, 9, ....
Coordinate the workers so that, together, they call emit(1), emit(2),
..., emit(n) in increasing order. Return only after every worker thread
has finished.

Constraints:
- 1 <= k <= 16, 0 <= n <= 10^4
- Exactly k worker threads; each emits only its own numbers
- Workers that own no numbers (k > n) must still start and exit cleanly
- No busy waiting
- Target: O(n) emits; each wake-up of a worker should be useful most of
  the time (one condition per worker, or notify_all with a turn check)

How it works:
1. Shared state: the next number to emit, guarded by a Condition
2. Worker i loops over its numbers x = i + 1, i + 1 + k, ...:
   wait until next == x, emit x, set next = x + 1, notify_all
3. The caller starts all k workers and joins them

Example 1:
Input: n = 7, k = 3
Output: emit(1..7) in order; worker 0 emits 1, 4, 7, worker 1 emits 2, 5
and worker 2 emits 3, 6

Example 2:
Input: n = 2, k = 4
Output: emit(1), emit(2); workers 2 and 3 emit nothing and exit
"""

import threading
from typing import Callable, Dict, List


class Solution:
    def print_round_robin(
        self, n: int, k: int, emit: Callable[[int], None]
    ) -> None:
        """
        Starts k workers that together emit 1..n in order, then joins them.

        Args:
            n: Largest number to emit
            k: Number of worker threads
            emit: Callback invoked once per number

        Time Complexity: O(n) emits (plus wake-ups)
        Space Complexity: O(k) for the threads
        """
        # TODO: Implement round-robin printing with k threads
        pass


def collect(n: int, k: int):
    """Runs print_round_robin and returns (values, thread id per value)."""
    out: List[int] = []
    owners: List[int] = []

    def emit(x: int) -> None:
        out.append(x)
        owners.append(threading.get_ident())

    t = threading.Thread(
        target=lambda: Solution().print_round_robin(n, k, emit), daemon=True
    )
    t.start()
    t.join(10.0)
    assert not t.is_alive(), "print_round_robin did not finish (deadlock?)"
    return out, owners


def test_round_robin_threads():
    """Test cases for round-robin printing"""

    # Test case 1: k = 3, n = 7
    out, _ = collect(7, 3)
    assert out == list(range(1, 8))
    print("✓ Test 1 passed: n = 7, k = 3")

    # Test case 2: k = 1 (single worker) and n = 0
    assert collect(5, 1)[0] == [1, 2, 3, 4, 5]
    assert collect(0, 4)[0] == []
    print("✓ Test 2 passed: k = 1 and n = 0")

    # Test case 3: More workers than numbers
    assert collect(2, 6)[0] == [1, 2]
    print("✓ Test 3 passed: k > n")

    # Test case 4: Ownership follows (x - 1) % k
    n, k = 40, 4
    out, owners = collect(n, k)
    assert out == list(range(1, n + 1))
    worker_of: Dict[int, set] = {}
    for x, tid in zip(out, owners):
        worker_of.setdefault((x - 1) % k, set()).add(tid)
    assert all(len(s) == 1 for s in worker_of.values())
    all_ids = set().union(*worker_of.values())
    assert len(all_ids) == k and threading.get_ident() not in all_ids
    print("✓ Test 4 passed: k = 4 workers own their residues")

    # Test case 5: Many workers, longer run
    assert collect(1600, 16)[0] == list(range(1, 1601))
    print("✓ Test 5 passed: n = 1600, k = 16")

    # Test case 6: Repeated runs with different k
    for rep in range(15):
        k = rep % 5 + 2
        assert collect(30, k)[0] == list(range(1, 31))
    print("✓ Test 6 passed: 15 repeated runs with k = 2..6")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_round_robin_threads()
