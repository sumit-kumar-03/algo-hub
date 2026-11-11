"""
EPI 19.6 Extra Variant - Bounded Blocking Queue (Producers and Consumers)
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Protecting shared state with a lock and making threads wait on
condition variables until the state lets them proceed; here there are two
waiting conditions ("not full" and "not empty") instead of one.

Problem:
Implement a thread-safe FIFO queue with a fixed capacity, without using
the queue module. put(item) adds an item at the back, blocking while the
queue is full. take() removes and returns the item at the front, blocking
while the queue is empty. size() returns the current number of items.
Producers and consumers may run on any number of threads.

Constraints:
- 1 <= capacity <= 10^4
- Use threading.Lock / threading.Condition and a collections.deque (or a
  list); do not use queue.Queue or threading.Semaphore
- No busy waiting; never lose or duplicate an item
- Target: O(1) per operation besides waiting

How it works:
1. A deque holds the items; one lock is shared by two conditions,
   not_full and not_empty
2. put: wait on not_full while len == capacity, append, notify not_empty
3. take: wait on not_empty while len == 0, popleft, notify not_full
4. size: read len under the lock

Example 1:
Input: q = BoundedBlockingQueue(2); put(1); put(2); a third thread calls
       put(3); main calls take()
Output: put(3) blocks until take() returns 1; then the queue holds 2, 3

Example 2:
Input: q = BoundedBlockingQueue(1); a consumer thread calls take(); main
       calls put(7)
Output: the consumer blocks until put(7), then receives 7
"""

import threading
from typing import Any, Callable, List


class BoundedBlockingQueue:
    def __init__(self, capacity: int) -> None:
        """
        Args:
            capacity: Maximum number of items held at once
        """
        # TODO: Set up storage, the lock and the two conditions
        pass

    def put(self, item: Any) -> None:
        """
        Appends item, blocking while the queue is full.

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement put
        pass

    def take(self) -> Any:
        """
        Removes and returns the oldest item, blocking while empty.

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement take
        pass

    def size(self) -> int:
        """
        Returns the number of items currently in the queue.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement size
        pass


def start_daemon(fn: Callable[[], None]) -> threading.Thread:
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    return t


def test_bounded_blocking_queue():
    """Test cases for the bounded blocking queue"""

    # Test case 1: FIFO order on a single thread
    q = BoundedBlockingQueue(3)
    for x in (1, 2, 3):
        q.put(x)
    assert q.size() == 3
    assert [q.take(), q.take(), q.take()] == [1, 2, 3]
    assert q.size() == 0
    print("✓ Test 1 passed: FIFO order and size")

    # Test case 2: put blocks while full
    q = BoundedBlockingQueue(2)
    q.put("a")
    q.put("b")
    put_done = threading.Event()
    start_daemon(lambda: (q.put("c"), put_done.set()))
    assert not put_done.wait(0.2), "put succeeded on a full queue"
    assert q.take() == "a"
    assert put_done.wait(1.0), "take did not wake the blocked producer"
    assert q.size() == 2 and q.take() == "b" and q.take() == "c"
    print("✓ Test 2 passed: put blocks when full")

    # Test case 3: take blocks while empty
    q = BoundedBlockingQueue(1)
    got: List[Any] = []
    taken = threading.Event()
    start_daemon(lambda: (got.append(q.take()), taken.set()))
    assert not taken.wait(0.2), "take returned on an empty queue"
    q.put(7)
    assert taken.wait(1.0) and got == [7]
    print("✓ Test 3 passed: take blocks when empty")

    # Test case 4: Capacity 1 hand-off keeps order
    q = BoundedBlockingQueue(1)
    received: List[int] = []
    consumer = start_daemon(lambda: [received.append(q.take()) for _ in range(200)])
    for i in range(200):
        q.put(i)
    consumer.join(5.0)
    assert not consumer.is_alive() and received == list(range(200))
    print("✓ Test 4 passed: Capacity-1 hand-off of 200 items in order")

    # Test case 5: Many producers and consumers, nothing lost or duplicated
    q = BoundedBlockingQueue(5)
    n_prod, n_cons, per = 4, 4, 250
    results: List[int] = []
    res_lock = threading.Lock()
    max_size = [0]

    def producer(p: int) -> None:
        for i in range(per):
            q.put(p * per + i)
            max_size[0] = max(max_size[0], q.size())

    def consumer_fn() -> None:
        for _ in range(per):
            x = q.take()
            with res_lock:
                results.append(x)

    threads = [start_daemon(lambda p=p: producer(p)) for p in range(n_prod)]
    threads += [start_daemon(consumer_fn) for _ in range(n_cons)]
    for t in threads:
        t.join(10.0)
    assert not any(t.is_alive() for t in threads), "stress test hung"
    assert sorted(results) == list(range(n_prod * per))
    assert max_size[0] <= 5 and q.size() == 0
    print("✓ Test 5 passed: 4 producers, 4 consumers, 1000 items exactly once")

    # Test case 6: Per-producer order is preserved for a single consumer
    q = BoundedBlockingQueue(3)
    seen: List[int] = []

    def single_consumer() -> None:
        for _ in range(300):
            seen.append(q.take())

    c = start_daemon(single_consumer)
    ps = [
        start_daemon(lambda p=p: [q.put(p * 1000 + i) for i in range(100)])
        for p in range(3)
    ]
    for t in ps + [c]:
        t.join(5.0)
    assert not c.is_alive() and len(seen) == 300
    for p in range(3):
        mine = [x for x in seen if x // 1000 == p]
        assert mine == sorted(mine) and len(mine) == 100
    print("✓ Test 6 passed: Each producer's items stay in order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_bounded_blocking_queue()
