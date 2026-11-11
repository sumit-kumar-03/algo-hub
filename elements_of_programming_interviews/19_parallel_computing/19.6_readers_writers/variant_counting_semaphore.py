"""
EPI 19.6 Extra Variant - Build a Counting Semaphore from a Condition
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Guarding a shared counter with a lock and blocking on a
condition variable until the counter allows entry, as the readers-writers
lock does with its reader count.

Problem:
Implement a counting semaphore without using threading.Semaphore. It is
created with a number of permits. acquire() takes one permit, blocking
while none are available. release() returns one permit and wakes one
waiting thread. This lets at most `permits` threads be inside a guarded
region at once (for example, a pool of database connections).

Constraints:
- 0 <= permits <= 1000 at creation; release() may raise the count above
  the initial value (it is not a bounded semaphore)
- Use threading.Lock / threading.Condition only (no threading.Semaphore)
- No busy waiting
- Target: O(1) per call besides waiting

How it works:
1. Keep an integer count guarded by a threading.Condition
2. acquire: with the condition held, wait while count == 0, then
   decrement
3. release: with the condition held, increment and notify one waiter

Example 1:
Input: CountingSemaphore(2); threads T1, T2, T3 each call acquire()
Output: T1 and T2 get in at once; T3 blocks until T1 or T2 calls release()

Example 2:
Input: CountingSemaphore(0); T1 calls acquire(), main calls release()
Output: T1 blocks until the release, then proceeds
"""

import threading
import time
from typing import Callable, List


class CountingSemaphore:
    def __init__(self, permits: int) -> None:
        """
        Args:
            permits: Initial number of available permits
        """
        # TODO: Set up the permit count and the condition variable
        pass

    def acquire(self) -> None:
        """
        Takes one permit, blocking while none are available.

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement acquire
        pass

    def release(self) -> None:
        """
        Returns one permit and wakes a waiting thread, if any.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement release
        pass


def start_daemon(fn: Callable[[], None]) -> threading.Thread:
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    return t


def test_counting_semaphore():
    """Test cases for the counting semaphore"""

    # Test case 1: Permits are handed out without blocking
    sem = CountingSemaphore(2)
    got_two = threading.Event()

    def take_two() -> None:
        sem.acquire()
        sem.acquire()
        got_two.set()

    start_daemon(take_two)
    assert got_two.wait(1.0), "two acquires with two permits blocked"
    print("✓ Test 1 passed: Two permits, two acquires")

    # Test case 2: A third acquire blocks until a release
    third_in = threading.Event()

    def take_third() -> None:
        sem.acquire()
        third_in.set()

    start_daemon(take_third)
    assert not third_in.wait(0.2), "acquire succeeded with no permits left"
    sem.release()
    assert third_in.wait(1.0), "release did not wake the waiter"
    print("✓ Test 2 passed: Acquire blocks at 0 and release wakes it")

    # Test case 3: Zero initial permits
    sem0 = CountingSemaphore(0)
    in0 = threading.Event()
    start_daemon(lambda: (sem0.acquire(), in0.set()))
    assert not in0.wait(0.2)
    sem0.release()
    assert in0.wait(1.0)
    print("✓ Test 3 passed: Zero permits until a release")

    # Test case 4: Each release admits exactly one waiter
    sem1 = CountingSemaphore(0)
    entered: List[int] = []
    for i in range(3):
        start_daemon(lambda i=i: (sem1.acquire(), entered.append(i)))
    time.sleep(0.1)
    assert entered == []
    sem1.release()
    time.sleep(0.2)
    assert len(entered) == 1, f"one release let {len(entered)} threads in"
    sem1.release()
    sem1.release()
    deadline = time.time() + 2.0
    while len(entered) < 3 and time.time() < deadline:
        time.sleep(0.01)
    assert sorted(entered) == [0, 1, 2]
    print("✓ Test 4 passed: One release, one waiter admitted")

    # Test case 5: Stress - never more than `permits` threads inside
    permits = 3
    sem = CountingSemaphore(permits)
    state = {"inside": 0, "max": 0, "done": 0}
    lock = threading.Lock()

    def worker() -> None:
        for _ in range(50):
            sem.acquire()
            with lock:
                state["inside"] += 1
                state["max"] = max(state["max"], state["inside"])
            time.sleep(0.0005)
            with lock:
                state["inside"] -= 1
            sem.release()
        with lock:
            state["done"] += 1

    threads = [start_daemon(worker) for _ in range(10)]
    for t in threads:
        t.join(10.0)
    assert state["done"] == 10, "stress test hung"
    assert 1 <= state["max"] <= permits, f"max inside was {state['max']}"
    print("✓ Test 5 passed: 10 threads, never more than 3 inside")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_counting_semaphore()
