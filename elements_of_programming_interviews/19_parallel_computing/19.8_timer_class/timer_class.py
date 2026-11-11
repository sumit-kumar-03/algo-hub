"""
EPI 19.8 - Implement a Timer Class

Problem:
A calendar server needs to fire tasks (send an email, send an SMS, ...)
when events come due. Build a Timer that manages deferred tasks, each
identified by a unique name. It must support:
(1) scheduling a named task to start on its own thread at a given time in
    the future, and
(2) canceling a named task; canceling is a no-op if the task already
    started.

Constraints:
- Each task runs on its own thread, so a slow task never delays others
- Tasks start in order of their scheduled time, not insertion order
- Scheduling a task earlier than everything pending must still fire on time
- cancel() returns True only if it prevented the task from starting
- shutdown() stops the timer; pending tasks never start afterward

How it works:
1. Data structures: a min-heap of (run_at, name) plus a hash table from
   name to its pending entry (for O(1) lookup on cancel)
2. A dispatcher thread sleeps on a condition variable until the earliest
   run_at, then pops due entries and starts each on a new thread
3. schedule()/cancel() update both structures under one lock and notify
   the dispatcher so it can recompute its wake-up time
4. Canceled entries can be removed lazily: skip heap entries whose name
   is no longer in the hash table

Example:
timer.schedule("b", task_b, 0.2); timer.schedule("a", task_a, 0.1)
-> task_a starts ~0.1s later, task_b ~0.2s later
timer.cancel("b") before 0.2s -> True, task_b never runs
"""

import threading
import time
from typing import Callable, List


class Timer:
    def __init__(self) -> None:
        # TODO: Create the heap, the name -> entry table, the lock/condition,
        # and start the dispatcher thread (daemon)
        pass

    def schedule(self, name: str, task: Callable[[], None], delay: float) -> None:
        """
        Schedules task to start on a new thread `delay` seconds from now.

        Args:
            name: Unique identifier for the task
            task: Zero-argument callable to run
            delay: Seconds from now (>= 0)

        Time Complexity: O(log n) for n pending tasks
        """
        # TODO: Implement schedule
        pass

    def cancel(self, name: str) -> bool:
        """
        Cancels the pending task called name.

        Returns:
            True if the task was pending and will now never run; False if it
            already started, was already canceled, or is unknown

        Time Complexity: O(1) with lazy deletion (O(log n) with eager removal)
        """
        # TODO: Implement cancel
        pass

    def shutdown(self) -> None:
        """
        Stops the dispatcher. Tasks that have not started will not start.
        """
        # TODO: Implement shutdown
        pass


def test_timer_class():
    """Test cases for the Timer class"""

    # Test case 1: A task starts after its delay, not before
    timer = Timer()
    fired = threading.Event()
    start = time.monotonic()
    fired_at: List[float] = []

    def task1() -> None:
        fired_at.append(time.monotonic() - start)
        fired.set()

    timer.schedule("t1", task1, 0.15)
    assert not fired.wait(0.05), "task fired too early"
    assert fired.wait(1.0), "task never fired"
    assert 0.12 <= fired_at[0] < 0.8
    timer.shutdown()
    print("✓ Test 1 passed: Task fires after its delay")

    # Test case 2: Tasks run in time order, even if scheduled out of order
    timer = Timer()
    order: List[str] = []
    order_lock = threading.Lock()
    done = threading.Event()

    def make(label: str) -> Callable[[], None]:
        def run() -> None:
            with order_lock:
                order.append(label)
                if len(order) == 3:
                    done.set()
        return run

    timer.schedule("c", make("c"), 0.30)
    timer.schedule("b", make("b"), 0.18)
    timer.schedule("a", make("a"), 0.05)  # new earliest: dispatcher must wake
    assert done.wait(2.0), "not all tasks fired"
    assert order == ["a", "b", "c"]
    timer.shutdown()
    print("✓ Test 2 passed: Tasks fire in scheduled-time order")

    # Test case 3: Canceling a pending task prevents it from running
    timer = Timer()
    ran: List[str] = []
    other = threading.Event()
    timer.schedule("x", lambda: ran.append("x"), 0.15)
    timer.schedule("y", other.set, 0.25)
    assert timer.cancel("x") is True
    assert other.wait(1.0)
    time.sleep(0.05)
    assert ran == []
    assert timer.cancel("x") is False  # already canceled
    timer.shutdown()
    print("✓ Test 3 passed: Cancel before start")

    # Test case 4: Canceling a started task or an unknown name is ignored
    timer = Timer()
    started = threading.Event()
    timer.schedule("z", started.set, 0.02)
    assert started.wait(1.0)
    assert timer.cancel("z") is False
    assert timer.cancel("does-not-exist") is False
    timer.shutdown()
    print("✓ Test 4 passed: Cancel after start / unknown name returns False")

    # Test case 5: Each task runs on its own thread; a slow task blocks nobody
    timer = Timer()
    slow_started = threading.Event()
    fast_done = threading.Event()
    idents: List[int] = []
    start = time.monotonic()
    fast_at: List[float] = []

    def slow() -> None:
        idents.append(threading.get_ident())
        slow_started.set()
        time.sleep(0.5)

    def fast() -> None:
        idents.append(threading.get_ident())
        fast_at.append(time.monotonic() - start)
        fast_done.set()

    timer.schedule("slow", slow, 0.02)
    timer.schedule("fast", fast, 0.10)
    assert slow_started.wait(1.0) and fast_done.wait(1.0)
    assert fast_at[0] < 0.4, "fast task was delayed by the slow one"
    assert len(set(idents)) == 2
    assert threading.get_ident() not in idents
    timer.shutdown()
    print("✓ Test 5 passed: Tasks run on separate threads")

    # Test case 6: shutdown() prevents pending tasks from starting
    timer = Timer()
    late: List[str] = []
    timer.schedule("late", lambda: late.append("late"), 0.1)
    timer.shutdown()
    time.sleep(0.25)
    assert late == []
    print("✓ Test 6 passed: Shutdown drops pending tasks")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_timer_class()
