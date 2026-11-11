"""
EPI 8.8 - Implement a Queue Using Stacks

Problem:
Implement a FIFO queue with enqueue and dequeue, using only stacks as the
underlying storage (Python lists restricted to append, pop from the end,
and emptiness checks).

Constraints:
- dequeue() on an empty queue must raise IndexError
- O(1) amortized time per operation; O(m) total for m operations

How it works (two stacks):
1. Keep an "enqueue" stack and a "dequeue" stack
2. enqueue(x): push x onto the enqueue stack
3. dequeue(): if the dequeue stack is empty, pop every element from the
   enqueue stack and push it onto the dequeue stack (this reverses the
   order, putting the oldest element on top); then pop from it
4. Each element is moved at most once, so the cost is amortized O(1)

Example 1:
Input: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
Output: 1, 2, 3

Example 2:
Input: dequeue() on a new queue
Output: IndexError
"""


class Queue:
    def __init__(self) -> None:
        # TODO: Create the two stacks
        pass

    def enqueue(self, x: int) -> None:
        """
        Adds x to the back of the queue.

        Time Complexity: O(1)
        Space Complexity: O(n) overall for the queue
        """
        # TODO: Implement enqueue
        pass

    def dequeue(self) -> int:
        """
        Removes and returns the element at the front of the queue.

        Raises:
            IndexError: If the queue is empty

        Time Complexity: O(1) amortized
        """
        # TODO: Implement dequeue
        pass


def raises_index_error(fn) -> bool:
    """Returns True if calling fn raises IndexError."""
    try:
        fn()
    except IndexError:
        return True
    return False


def test_queue_from_stacks():
    """Test cases for the queue built from stacks"""

    # Test case 1: Empty queue raises
    q = Queue()
    assert raises_index_error(q.dequeue)
    print("✓ Test 1 passed: Empty queue raises IndexError")

    # Test case 2: Simple FIFO order
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    print("✓ Test 2 passed: FIFO order")

    # Test case 3: Interleaved operations
    q.enqueue(4)
    q.enqueue(5)
    assert q.dequeue() == 4
    q.enqueue(6)
    q.enqueue(7)
    assert q.dequeue() == 5
    assert q.dequeue() == 6
    assert q.dequeue() == 7
    print("✓ Test 3 passed: Interleaved enqueue/dequeue")

    # Test case 4: Drained queue raises again
    assert raises_index_error(q.dequeue)
    print("✓ Test 4 passed: Drained queue raises IndexError")

    # Test case 5: Large sequence
    q = Queue()
    for i in range(1000):
        q.enqueue(i)
    assert [q.dequeue() for _ in range(500)] == list(range(500))
    for i in range(1000, 1200):
        q.enqueue(i)
    assert [q.dequeue() for _ in range(700)] == list(range(500, 1200))
    print("✓ Test 5 passed: Large sequence")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_queue_from_stacks()
