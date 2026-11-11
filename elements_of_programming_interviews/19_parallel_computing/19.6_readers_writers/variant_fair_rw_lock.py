"""
EPI 19.6 Extra Variant - Fair (First-Come, First-Served) Readers-Writers Lock
(Practice problem, not in the book. Difficulty: Hard)
Builds on: The readers-writers lock, solving the "third" readers-writers
problem: neither readers nor writers may starve, because requests are
admitted strictly in arrival order.

Problem:
Build a readers-writers lock that admits threads in the order they
called acquire_read / acquire_write. Readers still share: a run of
consecutive readers in the arrival order may all be inside together. But
a thread never enters ahead of a thread that arrived before it. Examples:
- A reader that arrives while a writer is waiting must wait for that
  writer (no reader preference).
- A writer that arrives while readers are waiting behind an active writer
  must wait for those readers (no writer preference).

Constraints:
- Readers share; a writer is alone
- Entry order equals arrival order (ties between readers that entered
  together don't matter)
- No busy waiting
- Target: O(1) bookkeeping per call besides waiting

How it works (ticket lock on top of a condition variable):
1. Under one Condition, hand each arriving thread a ticket number
   (next_ticket += 1) and keep now_serving, the ticket allowed to enter
2. A reader waits until now_serving == its ticket and no writer is
   active; it then increments active_readers and advances now_serving,
   so the next ticket (maybe another reader) can try immediately
3. A writer waits until now_serving == its ticket, no writer is active
   and active_readers == 0; it then sets writer_active and advances
   now_serving
4. Releases update the counters and notify_all

Example 1:
Input: R1 reading; W arrives (waits); R2 arrives
Output: R2 waits (W arrived first); R1 leaves -> W enters; W leaves -> R2
        enters

Example 2:
Input: W1 writing; R1 arrives; W2 arrives; R2 arrives; W1 releases
Output: R1 enters; W2 waits for R1; R2 waits for W2 (arrival order is
        R1, W2, R2)
"""

import threading
import time
from typing import Callable, List


class FairReadWriteLock:
    def __init__(self) -> None:
        # TODO: Set up the condition, the ticket counters and the state
        pass

    def acquire_read(self) -> None:
        """
        Enters as a reader once every earlier arrival has entered and no
        writer is active.

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement acquire_read
        pass

    def release_read(self) -> None:
        """Leaves as a reader and wakes waiting threads."""
        # TODO: Implement release_read
        pass

    def acquire_write(self) -> None:
        """
        Enters as the only writer once every earlier arrival has entered
        and the lock is completely free.

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement acquire_write
        pass

    def release_write(self) -> None:
        """Leaves as a writer and wakes waiting threads."""
        # TODO: Implement release_write
        pass


def start_daemon(fn: Callable[[], None]) -> threading.Thread:
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    return t


class Actor:
    """A thread that acquires the lock, records entry, then waits to leave."""

    def __init__(self, rw: FairReadWriteLock, kind: str, name: str, log: List[str]):
        self.entered = threading.Event()
        self.may_leave = threading.Event()
        self.left = threading.Event()

        def run() -> None:
            if kind == "R":
                rw.acquire_read()
            else:
                rw.acquire_write()
            log.append(name)
            self.entered.set()
            self.may_leave.wait(5.0)
            if kind == "R":
                rw.release_read()
            else:
                rw.release_write()
            self.left.set()

        start_daemon(run)
        time.sleep(0.08)  # fixes the arrival order of the next actor

    def leave(self) -> None:
        self.may_leave.set()
        assert self.left.wait(2.0), "release did not return"


def test_fair_rw_lock():
    """Test cases for the first-come, first-served readers-writers lock"""

    # Test case 1: Readers share; a writer is alone
    rw = FairReadWriteLock()
    log: List[str] = []
    r1 = Actor(rw, "R", "R1", log)
    r2 = Actor(rw, "R", "R2", log)
    assert r1.entered.is_set() and r2.entered.is_set(), "readers did not share"
    w = Actor(rw, "W", "W", log)
    assert not w.entered.wait(0.1), "writer entered while readers were inside"
    r1.leave()
    assert not w.entered.wait(0.1)
    r2.leave()
    assert w.entered.wait(1.0)
    w.leave()
    print("✓ Test 1 passed: Readers share, writer waits for all of them")

    # Test case 2: No reader preference - a new reader queues behind a writer
    rw = FairReadWriteLock()
    log = []
    r1 = Actor(rw, "R", "R1", log)
    w = Actor(rw, "W", "W", log)
    r2 = Actor(rw, "R", "R2", log)
    assert r1.entered.is_set()
    assert not w.entered.is_set() and not r2.entered.is_set()
    r1.leave()
    assert w.entered.wait(1.0)
    assert not r2.entered.wait(0.1), "reader entered during a write"
    w.leave()
    assert r2.entered.wait(1.0)
    r2.leave()
    assert log == ["R1", "W", "R2"]
    print("✓ Test 2 passed: Reader arriving after a writer waits for it")

    # Test case 3: No writer preference - arrival order R1, W2, R2
    rw = FairReadWriteLock()
    log = []
    w1 = Actor(rw, "W", "W1", log)
    r1 = Actor(rw, "R", "R1", log)
    w2 = Actor(rw, "W", "W2", log)
    r2 = Actor(rw, "R", "R2", log)
    assert log == ["W1"]
    w1.leave()
    assert r1.entered.wait(1.0)
    assert not w2.entered.wait(0.1) and not r2.entered.is_set()
    r1.leave()
    assert w2.entered.wait(1.0)
    assert not r2.entered.wait(0.1)
    w2.leave()
    assert r2.entered.wait(1.0)
    r2.leave()
    assert log == ["W1", "R1", "W2", "R2"]
    print("✓ Test 3 passed: W1, R1, W2, R2 enter in arrival order")

    # Test case 4: Consecutive waiting readers enter together
    rw = FairReadWriteLock()
    log = []
    w1 = Actor(rw, "W", "W1", log)
    readers = [Actor(rw, "R", f"R{i}", log) for i in range(3)]
    w2 = Actor(rw, "W", "W2", log)
    w1.leave()
    assert all(r.entered.wait(1.0) for r in readers), "readers did not batch"
    assert not w2.entered.wait(0.1)
    for r in readers:
        r.leave()
    assert w2.entered.wait(1.0)
    w2.leave()
    assert log[0] == "W1" and sorted(log[1:4]) == ["R0", "R1", "R2"]
    assert log[4] == "W2"
    print("✓ Test 4 passed: A run of readers enters together")

    # Test case 5: Stress - mutual exclusion and no lost writes
    rw = FairReadWriteLock()
    state = {"readers": 0, "writers": 0, "value": 0}
    state_lock = threading.Lock()
    violations: List[str] = []

    def stress_reader() -> None:
        for _ in range(100):
            rw.acquire_read()
            with state_lock:
                state["readers"] += 1
                if state["writers"]:
                    violations.append("reader overlapped a writer")
            time.sleep(0)
            with state_lock:
                state["readers"] -= 1
            rw.release_read()

    def stress_writer() -> None:
        for _ in range(50):
            rw.acquire_write()
            with state_lock:
                state["writers"] += 1
                if state["writers"] > 1 or state["readers"]:
                    violations.append("writer was not exclusive")
            v = state["value"]
            time.sleep(0)
            state["value"] = v + 1
            with state_lock:
                state["writers"] -= 1
            rw.release_write()

    threads = [start_daemon(stress_reader) for _ in range(4)]
    threads += [start_daemon(stress_writer) for _ in range(4)]
    for t in threads:
        t.join(10.0)
    assert not any(t.is_alive() for t in threads), "stress test hung"
    assert violations == [], violations[:3]
    assert state["value"] == 200
    print("✓ Test 5 passed: Stress test with 4 readers and 4 writers")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fair_rw_lock()
