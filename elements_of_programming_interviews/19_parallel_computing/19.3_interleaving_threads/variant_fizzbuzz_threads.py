"""
EPI 19.3 Extra Variant - FizzBuzz with Four Threads
(Practice problem, not in the book. Difficulty: Medium)
Builds on: A shared turn monitor; instead of alternating, the owner of
each turn is computed from the current number, and four threads compete.

Problem:
A FizzBuzz object is created with n. Four threads share it:
- thread A calls fizz(emit) and emits "fizz" for multiples of 3 only
- thread B calls buzz(emit) and emits "buzz" for multiples of 5 only
- thread C calls fizzbuzz(emit) and emits "fizzbuzz" for multiples of 15
- thread D calls number(emit) and emits str(i) for all other i
For i = 1..n in order, exactly one thread must emit the right token for
i, so the combined output is the classic FizzBuzz sequence.

Constraints:
- 0 <= n <= 10^4
- Each method is called exactly once, each from its own thread, and the
  threads may start in any order
- No busy waiting
- Target: O(n) emits

How it works:
1. Shared state: the current i (starting at 1), guarded by a Condition
2. A helper owner(i) returns which of the four kinds handles i
3. Each method loops: wait until i > n or owner(i) is its kind; if i > n,
   return; otherwise emit its token, increment i, notify_all

Example 1:
Input: n = 5
Output: "1", "2", "fizz", "4", "buzz"

Example 2:
Input: n = 15
Output: "1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz",
        "11", "fizz", "13", "14", "fizzbuzz"
"""

import threading
from typing import Callable, List


class FizzBuzz:
    def __init__(self, n: int) -> None:
        """
        Args:
            n: Last number of the sequence
        """
        # TODO: Store n and set up the shared state
        pass

    def fizz(self, emit: Callable[[str], None]) -> None:
        """Emits "fizz" for each i divisible by 3 but not 5."""
        # TODO: Implement fizz
        pass

    def buzz(self, emit: Callable[[str], None]) -> None:
        """Emits "buzz" for each i divisible by 5 but not 3."""
        # TODO: Implement buzz
        pass

    def fizzbuzz(self, emit: Callable[[str], None]) -> None:
        """Emits "fizzbuzz" for each i divisible by 15."""
        # TODO: Implement fizzbuzz
        pass

    def number(self, emit: Callable[[str], None]) -> None:
        """
        Emits str(i) for each i divisible by neither 3 nor 5.

        Time Complexity: O(n) per method overall
        Space Complexity: O(1)
        """
        # TODO: Implement number
        pass


def expected(n: int) -> List[str]:
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("fizzbuzz")
        elif i % 3 == 0:
            out.append("fizz")
        elif i % 5 == 0:
            out.append("buzz")
        else:
            out.append(str(i))
    return out


def run(n: int, order: str = "fbzn", record_threads: bool = False):
    """Starts the four methods on daemon threads in the given order."""
    out: List[str] = []
    owners: List[int] = []

    def emit(token: str) -> None:
        out.append(token)
        owners.append(threading.get_ident())

    fb = FizzBuzz(n)
    method = {"f": fb.fizz, "b": fb.buzz, "z": fb.fizzbuzz, "n": fb.number}
    threads = [
        threading.Thread(target=method[c], args=(emit,), daemon=True) for c in order
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join(5.0)
    assert not any(t.is_alive() for t in threads), "threads did not finish"
    return (out, owners) if record_threads else out


def test_fizzbuzz_threads():
    """Test cases for four-thread FizzBuzz"""

    # Test case 1: n = 5
    assert run(5) == ["1", "2", "fizz", "4", "buzz"]
    print("✓ Test 1 passed: n = 5")

    # Test case 2: n = 15 includes fizzbuzz
    assert run(15) == expected(15)
    print("✓ Test 2 passed: n = 15")

    # Test case 3: n = 0, 1, 2 (some threads never emit but must exit)
    assert run(0) == []
    assert run(1) == ["1"]
    assert run(2) == ["1", "2"]
    print("✓ Test 3 passed: Tiny n, idle threads exit")

    # Test case 4: Start order does not matter
    for order in ["nzbf", "zfnb", "bnfz"]:
        assert run(31, order) == expected(31), order
    print("✓ Test 4 passed: Different start orders")

    # Test case 5: Each token kind comes from its own single thread
    out, owners = run(60, record_threads=True)
    assert out == expected(60)
    kinds = {}
    for token, tid in zip(out, owners):
        kind = token if not token.isdigit() else "number"
        kinds.setdefault(kind, set()).add(tid)
    assert all(len(s) == 1 for s in kinds.values()) and len(kinds) == 4
    assert len(set().union(*kinds.values())) == 4
    print("✓ Test 5 passed: Four distinct threads, one per token kind")

    # Test case 6: Larger n and repeated runs
    assert run(1500) == expected(1500)
    for _ in range(10):
        assert run(45, "zbfn") == expected(45)
    print("✓ Test 6 passed: n = 1500 and 10 repeated runs")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fizzbuzz_threads()
