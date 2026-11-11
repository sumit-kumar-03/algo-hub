"""
EPI 8.7 - Implement a Circular Queue

Problem:
Implement a FIFO queue backed by a Python list used as a fixed-size array,
with head and tail indices that wrap around. The constructor takes the
initial capacity. Support enqueue, dequeue, and size. When the array is
full, grow it so the queue can hold any number of elements.

Constraints:
- capacity >= 1
- dequeue() on an empty queue must raise IndexError
- dequeue is O(1); enqueue is O(1) amortized (resize by a constant factor)

How it works (array with wrap-around indices):
1. Keep the array, a head index, a tail index, and an element count
2. enqueue(x): if the array is full, copy the elements out in queue order
   (head to end, then start to head), place them at the front of a larger
   array, and reset head = 0, tail = count; then write x at tail and
   advance tail modulo the array length
3. dequeue(): read the value at head and advance head modulo the length
4. The count distinguishes a full queue from an empty one (head == tail
   in both cases)

Example 1:
Input: Queue(2); enqueue(1), enqueue(2), dequeue(), enqueue(3), enqueue(4)
Output: dequeue() -> 1, then dequeues return 2, 3, 4
Explanation: enqueue(3) wraps around; enqueue(4) triggers a resize.

Example 2:
Input: Queue(1); dequeue()
Output: IndexError
"""

from typing import List, Optional


class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        """
        Creates an empty queue backed by an array of the given capacity.

        Args:
            capacity: Initial size of the underlying array (>= 1)
        """
        # TODO: Set up the array, head, tail, and element count
        pass

    def enqueue(self, x: int) -> None:
        """
        Adds x to the back of the queue, resizing the array if it is full.

        Time Complexity: O(1) amortized
        Space Complexity: O(n) overall for the queue
        """
        # TODO: Implement enqueue
        pass

    def dequeue(self) -> int:
        """
        Removes and returns the element at the front of the queue.

        Raises:
            IndexError: If the queue is empty

        Time Complexity: O(1)
        """
        # TODO: Implement dequeue
        pass

    def size(self) -> int:
        """
        Returns the number of elements currently in the queue.

        Time Complexity: O(1)
        """
        # TODO: Implement size
        pass


def raises_index_error(fn) -> bool:
    """Returns True if calling fn raises IndexError."""
    try:
        fn()
    except IndexError:
        return True
    return False


def test_circular_queue():
    """Test cases for the circular queue"""

    # Test case 1: New queue is empty and dequeue raises
    q = Queue(2)
    assert q.size() == 0
    assert raises_index_error(q.dequeue)
    print("✓ Test 1 passed: Empty queue")

    # Test case 2: FIFO order within capacity
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.dequeue() == 1
    assert q.size() == 1
    print("✓ Test 2 passed: FIFO order")

    # Test case 3: Wrap-around followed by a resize
    q.enqueue(3)  # wraps to index 0
    q.enqueue(4)  # array full -> resize
    assert q.size() == 3
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [2, 3, 4]
    assert q.size() == 0
    print("✓ Test 3 passed: Wrap-around and resize keep order")

    # Test case 4: Capacity 1 grows to hold many elements
    q = Queue(1)
    for i in range(100):
        q.enqueue(i)
    assert q.size() == 100
    assert [q.dequeue() for _ in range(100)] == list(range(100))
    assert raises_index_error(q.dequeue)
    print("✓ Test 4 passed: Growth from capacity 1")

    # Test case 5: Interleaved operations with repeated wrapping
    q = Queue(3)
    expected: List[int] = []
    out: List[Optional[int]] = []
    next_value = 0
    for step in range(50):
        for _ in range(2):
            q.enqueue(next_value)
            expected.append(next_value)
            next_value += 1
        out.append(q.dequeue())
        if step % 3 == 0:
            out.append(q.dequeue())
    while q.size():
        out.append(q.dequeue())
    assert out == expected
    print("✓ Test 5 passed: Interleaved enqueue/dequeue")

    # Test case 6: Size tracks exact counts after draining and refilling
    q = Queue(4)
    for i in range(4):
        q.enqueue(i)
    q.dequeue()
    q.dequeue()
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    assert q.size() == 5
    assert [q.dequeue() for _ in range(5)] == [2, 3, 10, 11, 12]
    print("✓ Test 6 passed: Resize while wrapped")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_circular_queue()
