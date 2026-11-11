"""
EPI 19.3 Extra Variant - Zero, Odd, Even with Three Threads
(Practice problem, not in the book. Difficulty: Medium)
Builds on: The odd/even turn monitor, extended to three threads where the
next turn depends on the number just emitted.

Problem:
A ZeroEvenOdd object is created with n. Three threads share it:
- thread Z calls zero(emit) and may only emit 0
- thread O calls odd(emit) and may only emit odd numbers
- thread E calls even(emit) and may only emit even numbers
Together they must emit 0, 1, 0, 2, 0, 3, ..., 0, n: a zero before every
number from 1 to n, in order. The threads may be started in any order.

Constraints:
- 0 <= n <= 10^4
- Each method is called exactly once, each from its own thread
- No busy waiting
- Target: O(n) total work

How it works:
1. Shared state: the next number k (starting at 1) and whose turn it is:
   "zero", "odd" or "even", all guarded by one threading.Condition
2. zero: for each of n rounds, wait for "zero", emit 0, then hand the turn
   to "odd" or "even" depending on the parity of k; notify_all
3. odd / even: for each of its numbers, wait for its turn, emit k, bump
   k, hand the turn back to "zero"; notify_all

Example 1:
Input: n = 2
Output: emit is called with 0, 1, 0, 2

Example 2:
Input: n = 5
Output: emit is called with 0, 1, 0, 2, 0, 3, 0, 4, 0, 5
"""

import threading
from typing import Callable, List


class ZeroEvenOdd:
    def __init__(self, n: int) -> None:
        """
        Args:
            n: Largest number to emit
        """
        # TODO: Store n and set up the shared turn state
        pass

    def zero(self, emit: Callable[[int], None]) -> None:
        """
        Emits 0 exactly n times, each just before the next positive number.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement zero
        pass

    def odd(self, emit: Callable[[int], None]) -> None:
        """
        Emits 1, 3, 5, ... (up to n), each when it is that number's turn.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement odd
        pass

    def even(self, emit: Callable[[int], None]) -> None:
        """
        Emits 2, 4, 6, ... (up to n), each when it is that number's turn.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement even
        pass


def expected(n: int) -> List[int]:
    out: List[int] = []
    for k in range(1, n + 1):
        out += [0, k]
    return out


def run(n: int, order: str = "zoe", record_threads: bool = False):
    """Starts the three methods on daemon threads in the given order."""
    out: List[int] = []
    owners: List[int] = []

    def emit(x: int) -> None:
        out.append(x)
        owners.append(threading.get_ident())

    obj = ZeroEvenOdd(n)
    method = {"z": obj.zero, "o": obj.odd, "e": obj.even}
    threads = [
        threading.Thread(target=method[c], args=(emit,), daemon=True) for c in order
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join(5.0)
    assert not any(t.is_alive() for t in threads), "threads did not finish"
    return (out, owners) if record_threads else out


def test_zero_even_odd():
    """Test cases for zero/odd/even threads"""

    # Test case 1: n = 2
    assert run(2) == [0, 1, 0, 2]
    print("✓ Test 1 passed: n = 2")

    # Test case 2: n = 0 and n = 1
    assert run(0) == []
    assert run(1) == [0, 1]
    print("✓ Test 2 passed: n = 0 and n = 1")

    # Test case 3: Every start order works
    for order in ["zoe", "zeo", "oze", "oez", "ezo", "eoz"]:
        assert run(5, order) == expected(5), order
    print("✓ Test 3 passed: All 6 start orders give 0 1 0 2 ... 0 5")

    # Test case 4: Each value comes from the right thread
    out, owners = run(30, "eoz", record_threads=True)
    assert out == expected(30)
    by_kind = {"zero": set(), "odd": set(), "even": set()}
    for x, tid in zip(out, owners):
        kind = "zero" if x == 0 else ("odd" if x % 2 else "even")
        by_kind[kind].add(tid)
    assert all(len(s) == 1 for s in by_kind.values())
    assert len(set().union(*by_kind.values())) == 3
    print("✓ Test 4 passed: Zeros, odds and evens come from 3 distinct threads")

    # Test case 5: Larger n
    assert run(2000) == expected(2000)
    print("✓ Test 5 passed: n = 2000")

    # Test case 6: Repeated runs are always in order
    for k in range(20):
        assert run(15, ["zoe", "eoz", "oez"][k % 3]) == expected(15)
    print("✓ Test 6 passed: 20 repeated runs stay in order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_zero_even_odd()
