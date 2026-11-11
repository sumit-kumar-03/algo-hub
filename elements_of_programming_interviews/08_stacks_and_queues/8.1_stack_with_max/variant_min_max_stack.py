"""
EPI 8.1 Extra Variant - Stack with Min and Max
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Caching an aggregate alongside each stack entry so it can be
read in O(1) time and restored for free on pop.

Problem:
Design a stack that supports push, pop, top and empty, plus min and max,
which return the smallest and largest elements currently on the stack.
Every operation must run in O(1) time.

Constraints:
- pop(), top(), min() and max() on an empty stack must raise IndexError
- Duplicate and negative values are allowed

How it works:
1. Store (element, min_so_far, max_so_far) triples on an internal list
2. push(x): append (x, min(x, current min), max(x, current max)), or
   (x, x, x) if the stack is empty
3. pop() and top() read the element of the last triple
4. min() and max() read the cached values of the last triple

Example:
push(3), push(1), push(4) -> min() == 1, max() == 4
pop() -> 4 -> max() == 3; pop() -> 1 -> min() == 3
"""

from typing import List, Tuple


class MinMaxStack:
    def __init__(self) -> None:
        # TODO: Choose the internal storage
        pass

    def empty(self) -> bool:
        """
        Returns True if the stack has no elements.

        Time Complexity: O(1)
        """
        # TODO: Implement empty
        pass

    def push(self, x: int) -> None:
        """
        Pushes x onto the stack.

        Time Complexity: O(1)
        Space Complexity: O(n) overall for the stack
        """
        # TODO: Implement push
        pass

    def pop(self) -> int:
        """
        Removes and returns the top element.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        # TODO: Implement pop
        pass

    def top(self) -> int:
        """
        Returns the top element without removing it.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        # TODO: Implement top
        pass

    def min(self) -> int:
        """
        Returns the smallest element on the stack.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        # TODO: Implement min
        pass

    def max(self) -> int:
        """
        Returns the largest element on the stack.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        # TODO: Implement max
        pass


def raises_index_error(fn) -> bool:
    """Returns True if calling fn raises IndexError."""
    try:
        fn()
    except IndexError:
        return True
    return False


def test_min_max_stack():
    """Test cases for the min-max stack"""

    # Test case 1: New stack is empty and raises on reads
    s = MinMaxStack()
    assert s.empty() is True
    assert raises_index_error(s.pop) and raises_index_error(s.top)
    assert raises_index_error(s.min) and raises_index_error(s.max)
    print("✓ Test 1 passed: Empty stack")

    # Test case 2: Min and max track pushes
    s.push(3)
    assert s.min() == 3 and s.max() == 3
    s.push(1)
    s.push(4)
    assert s.min() == 1 and s.max() == 4 and s.top() == 4
    assert s.empty() is False
    print("✓ Test 2 passed: Min and max track pushes")

    # Test case 3: Both are restored after pops
    assert s.pop() == 4
    assert s.min() == 1 and s.max() == 3
    assert s.pop() == 1
    assert s.min() == 3 and s.max() == 3
    print("✓ Test 3 passed: Min and max restored after pops")

    # Test case 4: Duplicate extremes
    s.push(3)
    s.push(3)
    assert s.pop() == 3
    assert s.min() == 3 and s.max() == 3
    print("✓ Test 4 passed: Duplicate extremes")

    # Test case 5: Negatives
    s.push(-7)
    s.push(10)
    s.push(-2)
    assert s.min() == -7 and s.max() == 10
    assert s.pop() == -2 and s.pop() == 10
    assert s.min() == -7 and s.max() == 3
    print("✓ Test 5 passed: Negative values")

    # Test case 6: Drain to empty
    while not s.empty():
        s.pop()
    assert raises_index_error(s.min)
    print("✓ Test 6 passed: Drained stack raises again")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_max_stack()
