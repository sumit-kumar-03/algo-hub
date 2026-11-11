"""
EPI 19.3 - Implement Synchronization for Two Interleaving Threads

Problem:
Two threads run at the same time. One is responsible for the odd numbers
1, 3, 5, ... and the other for the even numbers 2, 4, 6, ... up to n.
Coordinate them so that, together, they emit every number from 1 to n in
strictly increasing order.

Constraints:
- Exactly two worker threads: one emits only odd numbers, the other only even
- No busy waiting: a thread whose turn it isn't must block, not spin
- n >= 0 (n == 0 emits nothing)
- print_in_order() returns only after both worker threads have finished

How it works:
1. A monitor (a lock plus a condition variable) stores whose turn it is
2. wait_turn(turn): block on the condition until the stored turn equals turn
3. toggle_turn(): flip the stored turn and notify the waiting thread
4. Each worker loops over its numbers: wait for its turn, emit, toggle

Example:
n = 6 -> emit is called with 1, 2, 3, 4, 5, 6 (odds from one thread,
evens from the other)
"""

import threading
from typing import Callable, List


class OddEvenMonitor:
    ODD_TURN = True
    EVEN_TURN = False

    def __init__(self) -> None:
        # TODO: Set up the condition variable and start with the odd turn
        pass

    def wait_turn(self, turn: bool) -> None:
        """
        Blocks the calling thread until it is `turn`'s turn.

        Returns immediately if it already is.
        """
        # TODO: Implement wait_turn
        pass

    def toggle_turn(self) -> None:
        """
        Hands the turn to the other thread and wakes it up.
        """
        # TODO: Implement toggle_turn
        pass


class Solution:
    def print_in_order(self, n: int, emit: Callable[[int], None]) -> None:
        """
        Starts an odd thread and an even thread that together call
        emit(1), emit(2), ..., emit(n) in order, then waits for both.

        Args:
            n: Largest number to emit
            emit: Callback invoked once per number (e.g. print)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement print_in_order using OddEvenMonitor
        pass


def run_with_timeout(fn: Callable[[], None], timeout: float = 5.0) -> bool:
    """Runs fn on a daemon thread; returns True if it finished in time."""
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    t.join(timeout)
    return not t.is_alive()


def collect(n: int) -> List[int]:
    """Runs print_in_order(n) and returns everything emitted."""
    out: List[int] = []

    def emit(i: int) -> None:
        out.append(i)

    finished = run_with_timeout(lambda: Solution().print_in_order(n, emit))
    assert finished, "print_in_order did not finish (deadlock?)"
    return out


def test_interleaving_threads():
    """Test cases for two interleaving threads"""

    # Test case 1: Monitor starts with the odd turn and toggles
    m = OddEvenMonitor()
    assert run_with_timeout(lambda: m.wait_turn(OddEvenMonitor.ODD_TURN), 1.0)
    m.toggle_turn()
    assert run_with_timeout(lambda: m.wait_turn(OddEvenMonitor.EVEN_TURN), 1.0)
    blocked = not run_with_timeout(
        lambda: m.wait_turn(OddEvenMonitor.ODD_TURN), 0.2
    )
    assert blocked, "wait_turn should block when it is not that thread's turn"
    m.toggle_turn()  # releases the blocked waiter
    print("✓ Test 1 passed: Monitor blocks and toggles turns")

    # Test case 2: Small n
    assert collect(6) == [1, 2, 3, 4, 5, 6]
    print("✓ Test 2 passed: n = 6 emits 1..6 in order")

    # Test case 3: The book's case, n = 100
    assert collect(100) == list(range(1, 101))
    print("✓ Test 3 passed: n = 100 emits 1..100 in order")

    # Test case 4: Edge cases n = 0 and n = 1 (odd count)
    assert collect(0) == []
    assert collect(1) == [1]
    assert collect(7) == list(range(1, 8))
    print("✓ Test 4 passed: n = 0, 1, 7")

    # Test case 5: Odds and evens come from two distinct worker threads
    owner = {}

    def emit_with_thread(i: int) -> None:
        owner[i] = threading.get_ident()

    assert run_with_timeout(
        lambda: Solution().print_in_order(20, emit_with_thread)
    )
    assert sorted(owner) == list(range(1, 21))
    odd_threads = {owner[i] for i in range(1, 21, 2)}
    even_threads = {owner[i] for i in range(2, 21, 2)}
    assert len(odd_threads) == 1 and len(even_threads) == 1
    assert odd_threads != even_threads
    assert threading.get_ident() not in odd_threads | even_threads
    print("✓ Test 5 passed: Odds and evens run on two separate threads")

    # Test case 6: Repeated runs stay ordered
    for _ in range(20):
        assert collect(50) == list(range(1, 51))
    print("✓ Test 6 passed: 20 repeated runs are always in order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_interleaving_threads()
