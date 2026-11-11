"""
EPI 19.3 Extra Variant - Ping-Pong Threads
(Practice problem, not in the book. Difficulty: Easy)
Builds on: A monitor (lock + condition variable) that tracks whose turn it
is, so two threads strictly alternate.

Problem:
A PingPong object is created with a count n. Two threads share it: one
thread calls ping(emit) and the other calls pong(emit). ping must call
emit("ping") n times and pong must call emit("pong") n times, and the
combined output must be "ping", "pong", "ping", "pong", ... (always
starting with "ping"), no matter which thread starts first.

Constraints:
- 0 <= n <= 10^4
- Each method is called exactly once, each from its own thread
- No busy waiting: a thread whose turn it isn't must block
- Target: O(n) total work

How it works:
1. Store a boolean "ping's turn" guarded by a threading.Condition
2. ping: n times, wait until it is ping's turn, emit, flip the flag,
   notify
3. pong: the same with the flag reversed

Example 1:
Input: n = 2, the pong thread happens to start first
Output: emit is called with "ping", "pong", "ping", "pong"

Example 2:
Input: n = 0
Output: emit is never called; both methods return immediately
"""

import threading
from typing import Callable, List


class PingPong:
    def __init__(self, n: int) -> None:
        """
        Args:
            n: Number of times each of "ping" and "pong" is emitted
        """
        # TODO: Store n and set up the condition variable and turn flag
        pass

    def ping(self, emit: Callable[[str], None]) -> None:
        """
        Emits "ping" n times, each time waiting for its turn.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement ping
        pass

    def pong(self, emit: Callable[[str], None]) -> None:
        """
        Emits "pong" n times, each time waiting for its turn.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement pong
        pass


def run_threads(targets: List[Callable[[], None]], timeout: float = 5.0) -> bool:
    """Runs each target on a daemon thread; True if all finish in time."""
    threads = [threading.Thread(target=t, daemon=True) for t in targets]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout)
    return not any(t.is_alive() for t in threads)


def play(n: int, pong_first: bool = False) -> List[str]:
    """Runs ping and pong on two threads and returns the emitted words."""
    out: List[str] = []
    game = PingPong(n)
    targets = [lambda: game.ping(out.append), lambda: game.pong(out.append)]
    if pong_first:
        targets.reverse()
    assert run_threads(targets), "ping/pong did not finish (deadlock?)"
    return out


def test_ping_pong():
    """Test cases for ping-pong threads"""

    # Test case 1: n = 1
    assert play(1) == ["ping", "pong"]
    print("✓ Test 1 passed: n = 1")

    # Test case 2: n = 0 emits nothing
    assert play(0) == []
    print("✓ Test 2 passed: n = 0")

    # Test case 3: Pong thread started first still waits for ping
    assert play(3, pong_first=True) == ["ping", "pong"] * 3
    print("✓ Test 3 passed: Pong started first, ping still leads")

    # Test case 4: Pong is blocked until ping has gone
    game = PingPong(1)
    out: List[str] = []
    assert not run_threads([lambda: game.pong(out.append)], timeout=0.3)
    assert out == [], "pong emitted before ping"
    assert run_threads([lambda: game.ping(out.append)])
    print("✓ Test 4 passed: Pong blocks without ping")

    # Test case 5: Long rally
    assert play(1000) == ["ping", "pong"] * 1000
    print("✓ Test 5 passed: n = 1000 alternates correctly")

    # Test case 6: Repeated runs with both start orders
    for k in range(20):
        assert play(25, pong_first=k % 2 == 1) == ["ping", "pong"] * 25
    print("✓ Test 6 passed: 20 repeated runs stay in order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_ping_pong()
