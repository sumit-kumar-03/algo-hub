"""
EPI 19.6 Extra Variant - Writer-Preference Readers-Writers Lock
(Practice problem, not in the book. Difficulty: Medium)
Builds on: The readers-writers lock from the main problem, with the
preference flipped (the "second" readers-writers problem) so writers
cannot be starved by a steady stream of readers.

Problem:
Build a readers-writers lock where writers have priority. Many readers may
hold the lock together and a writer needs it alone, as before. The
difference: as soon as any writer is waiting, newly arriving readers must
block, even if other readers are currently reading. Readers already inside
finish normally; once they leave, the waiting writer(s) go first, and
blocked readers enter only when no writer is active or waiting.

Constraints:
- Many readers may hold the lock at once; a writer holds it alone
- A waiting writer blocks new readers (writer preference)
- When several writers are waiting, they all run (one at a time) before
  any blocked reader enters
- No busy waiting
- Target: O(1) bookkeeping per call besides waiting

How it works:
1. One Condition guards three counters: active_readers, waiting_writers,
   and a boolean writer_active
2. acquire_read: wait while writer_active or waiting_writers > 0; then
   active_readers += 1
3. acquire_write: waiting_writers += 1; wait while writer_active or
   active_readers > 0; then waiting_writers -= 1, writer_active = True
4. Both releases update the counters and notify_all

Example 1:
Input: R1 is reading; W calls acquire_write (blocks); R2 calls
       acquire_read
Output: R2 blocks (unlike the main problem); when R1 releases, W enters;
        when W releases, R2 enters

Example 2:
Input: W1 is writing; R1 waits; W2 waits; W1 releases
Output: W2 enters before R1
"""

import threading
import time
from typing import Callable, List


class WriterPreferenceLock:
    def __init__(self) -> None:
        # TODO: Set up the condition and the counters
        pass

    def acquire_read(self) -> None:
        """
        Enters as a reader. Blocks while a writer is active or waiting.

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement acquire_read
        pass

    def release_read(self) -> None:
        """Leaves as a reader and wakes waiting threads if needed."""
        # TODO: Implement release_read
        pass

    def acquire_write(self) -> None:
        """
        Enters as the only writer. Blocks while any reader or writer is
        active.

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


def test_writer_preference_lock():
    """Test cases for the writer-preference readers-writers lock"""

    # Test case 1: Readers share the lock when no writer is around
    rw = WriterPreferenceLock()
    barrier = threading.Barrier(3, timeout=2.0)
    met: List[bool] = []

    def reader() -> None:
        rw.acquire_read()
        try:
            barrier.wait()
            met.append(True)
        except threading.BrokenBarrierError:
            met.append(False)
        finally:
            rw.release_read()

    threads = [start_daemon(reader) for _ in range(3)]
    for t in threads:
        t.join(3.0)
    assert met == [True, True, True]
    print("✓ Test 1 passed: Readers share the lock")

    # Test case 2: A writer excludes readers and other writers
    rw = WriterPreferenceLock()
    rw.acquire_write()
    r_in, w_in = threading.Event(), threading.Event()
    start_daemon(lambda: (rw.acquire_read(), r_in.set(), rw.release_read()))
    start_daemon(lambda: (rw.acquire_write(), w_in.set(), rw.release_write()))
    time.sleep(0.2)
    assert not r_in.is_set() and not w_in.is_set(), "entered during a write"
    rw.release_write()
    assert r_in.wait(2.0) and w_in.wait(2.0)
    print("✓ Test 2 passed: Writer is exclusive")

    # Test case 3: Writer preference - a new reader waits behind a writer
    rw = WriterPreferenceLock()
    rw.acquire_read()  # R1
    order: List[str] = []
    w_in, r2_in = threading.Event(), threading.Event()

    def waiting_writer() -> None:
        rw.acquire_write()
        order.append("W")
        w_in.set()
        time.sleep(0.05)
        rw.release_write()

    def late_reader() -> None:
        rw.acquire_read()
        order.append("R2")
        r2_in.set()
        rw.release_read()

    start_daemon(waiting_writer)
    time.sleep(0.1)  # the writer is now waiting for R1
    start_daemon(late_reader)
    assert not r2_in.wait(0.2), "new reader overtook a waiting writer"
    rw.release_read()  # R1 leaves
    assert w_in.wait(2.0) and r2_in.wait(2.0)
    assert order == ["W", "R2"]
    print("✓ Test 3 passed: Waiting writer blocks new readers")

    # Test case 4: All waiting writers go before blocked readers
    rw = WriterPreferenceLock()
    rw.acquire_write()  # W1
    order = []
    done: List[threading.Event] = []

    def make(kind: str) -> Callable[[], None]:
        ev = threading.Event()
        done.append(ev)

        def run() -> None:
            if kind == "R":
                rw.acquire_read()
                order.append("R")
                rw.release_read()
            else:
                rw.acquire_write()
                order.append("W")
                time.sleep(0.02)
                rw.release_write()
            ev.set()

        return run

    start_daemon(make("R"))
    time.sleep(0.05)
    start_daemon(make("W"))
    time.sleep(0.05)
    start_daemon(make("W"))
    time.sleep(0.1)
    rw.release_write()
    assert all(ev.wait(2.0) for ev in done)
    assert order == ["W", "W", "R"], order
    print("✓ Test 4 passed: Writers W2, W3 run before the waiting reader")

    # Test case 5: Stress - mutual exclusion and no lost writes
    rw = WriterPreferenceLock()
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
    test_writer_preference_lock()
