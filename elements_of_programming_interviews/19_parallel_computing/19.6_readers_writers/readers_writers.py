"""
EPI 19.6 - The Readers-Writers Problem

Problem:
A shared object is read and written by many threads. Any number of readers
may use it at the same time, but a writer needs exclusive access: while a
writer is active, no other writer and no reader may touch the object.
Guarding it with one plain mutex is too strict, because it makes a reader
wait for another reader. Build a lock for the "first" readers-writers
problem: a reader is never kept waiting while the object is already open
for reading.

Constraints:
- Many readers may hold the lock at once
- A writer holds the lock alone (no readers, no other writers)
- Reader preference: if readers are active, a newly arriving reader gets
  in immediately, even if a writer is already waiting
- No busy waiting: blocked threads wait on a condition variable

How it works:
1. Keep a count of active readers, guarded by an internal lock
2. Readers bump the count on entry and decrement it (and notify) on exit
3. A writer first takes a writer lock (one writer at a time), then waits
   on a condition until the reader count drops to 0, keeping readers out
   while it writes
4. Releasing the write side lets waiting readers and writers proceed

Example:
R1 acquires read; R2 acquires read immediately (both reading);
W calls acquire_write and blocks; R1, R2 release -> W proceeds.
"""

import threading
import time
from typing import Callable, List


class ReadWriteLock:
    def __init__(self) -> None:
        # TODO: Set up the internal locks/conditions and the reader count
        pass

    def acquire_read(self) -> None:
        """
        Enters the shared object as a reader. Blocks only while a writer
        is active.
        """
        # TODO: Implement acquire_read
        pass

    def release_read(self) -> None:
        """
        Leaves the shared object as a reader and wakes a waiting writer
        if this was the last reader.
        """
        # TODO: Implement release_read
        pass

    def acquire_write(self) -> None:
        """
        Enters the shared object as the only writer. Blocks while any
        reader or another writer is active.
        """
        # TODO: Implement acquire_write
        pass

    def release_write(self) -> None:
        """
        Leaves the shared object as a writer.
        """
        # TODO: Implement release_write
        pass


def start_daemon(fn: Callable[[], None]) -> threading.Thread:
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    return t


def test_readers_writers():
    """Test cases for the readers-writers lock"""

    # Test case 1: Several readers hold the lock at the same time
    rw = ReadWriteLock()
    barrier = threading.Barrier(3, timeout=2.0)
    met: List[bool] = []

    def reader() -> None:
        rw.acquire_read()
        try:
            barrier.wait()  # only succeeds if all 3 are inside together
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

    # Test case 2: A writer waits for an active reader
    rw = ReadWriteLock()
    rw.acquire_read()
    writer_in = threading.Event()

    def writer() -> None:
        rw.acquire_write()
        writer_in.set()
        rw.release_write()

    start_daemon(writer)
    assert not writer_in.wait(0.2), "writer entered while a reader was active"
    rw.release_read()
    assert writer_in.wait(2.0), "writer never entered after reader left"
    print("✓ Test 2 passed: Writer waits for readers")

    # Test case 3: Readers and writers wait for an active writer
    rw = ReadWriteLock()
    rw.acquire_write()
    reader_in = threading.Event()
    writer2_in = threading.Event()

    def reader2() -> None:
        rw.acquire_read()
        reader_in.set()
        rw.release_read()

    def writer2() -> None:
        rw.acquire_write()
        writer2_in.set()
        rw.release_write()

    start_daemon(reader2)
    start_daemon(writer2)
    time.sleep(0.2)
    assert not reader_in.is_set(), "reader entered during a write"
    assert not writer2_in.is_set(), "second writer entered during a write"
    rw.release_write()
    assert reader_in.wait(2.0) and writer2_in.wait(2.0)
    print("✓ Test 3 passed: A writer excludes readers and writers")

    # Test case 4: Reader preference - a new reader skips a waiting writer
    rw = ReadWriteLock()
    rw.acquire_read()  # R1
    w_in = threading.Event()
    r2_in = threading.Event()
    r2_may_leave = threading.Event()

    def waiting_writer() -> None:
        rw.acquire_write()
        w_in.set()
        rw.release_write()

    def late_reader() -> None:
        rw.acquire_read()
        r2_in.set()
        r2_may_leave.wait(3.0)
        rw.release_read()

    start_daemon(waiting_writer)
    time.sleep(0.1)  # let the writer start waiting
    start_daemon(late_reader)
    assert r2_in.wait(1.0), "new reader was blocked behind a waiting writer"
    assert not w_in.is_set()
    rw.release_read()  # R1 leaves; R2 still reading
    assert not w_in.wait(0.1), "writer entered while R2 was reading"
    r2_may_leave.set()
    assert w_in.wait(2.0), "writer never entered"
    print("✓ Test 4 passed: Reader preference")

    # Test case 5: Stress - no reader sees a writer, no two writers overlap
    rw = ReadWriteLock()
    state = {"readers": 0, "writers": 0, "value": 0}
    state_lock = threading.Lock()
    violations: List[str] = []
    n_writers, writes_each = 4, 50

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
        for _ in range(writes_each):
            rw.acquire_write()
            with state_lock:
                state["writers"] += 1
                if state["writers"] > 1 or state["readers"]:
                    violations.append("writer was not exclusive")
            v = state["value"]
            time.sleep(0)
            state["value"] = v + 1  # unsafe unless writers are exclusive
            with state_lock:
                state["writers"] -= 1
            rw.release_write()

    threads = [start_daemon(stress_reader) for _ in range(4)]
    threads += [start_daemon(stress_writer) for _ in range(n_writers)]
    for t in threads:
        t.join(10.0)
    assert not any(t.is_alive() for t in threads), "stress test hung"
    assert violations == [], violations[:3]
    assert state["value"] == n_writers * writes_each
    print("✓ Test 5 passed: Stress test with 4 readers and 4 writers")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_readers_writers()
