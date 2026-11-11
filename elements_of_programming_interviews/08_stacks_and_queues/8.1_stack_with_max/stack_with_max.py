"""
EPI 8.1 - Implement a Stack with Max API

Problem:
Design a stack that supports push, pop and empty, plus a max operation that
returns the largest element currently on the stack. All operations must
run in O(1) time.

Constraints:
- pop() and max() on an empty stack must raise IndexError
- Duplicate values are allowed

How it works:
1. Store (element, max_so_far) pairs on an internal list
2. push(x): append (x, max(x, current max)) - or (x, x) if empty
3. pop(): remove and return the top element
4. max(): return the max stored with the top element

Example:
push(2), push(5), push(1) -> max() == 5
pop() -> 1, pop() -> 5 -> max() == 2
"""

from typing import List, Tuple


class Stack:
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

    def max(self) -> int:
        """
        Returns the largest element on the stack.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        # TODO: Implement max
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

    def push(self, x: int) -> None:
        """
        Pushes x onto the stack.

        Time Complexity: O(1)
        Space Complexity: O(n) overall for the stack
        """
        # TODO: Implement push
        pass


def raises_index_error(fn) -> bool:
    """Returns True if calling fn raises IndexError."""
    try:
        fn()
    except IndexError:
        return True
    return False


def test_stack_with_max():
    """Test cases for stack with max implementation"""

    # Test case 1: New stack is empty
    s = Stack()
    assert s.empty() is True
    print("✓ Test 1 passed: New stack is empty")

    # Test case 2: Empty stack raises on pop and max
    assert raises_index_error(s.pop)
    assert raises_index_error(s.max)
    print("✓ Test 2 passed: pop/max on empty stack raise IndexError")

    # Test case 3: Max tracks pushes
    s.push(2)
    assert s.max() == 2
    s.push(5)
    assert s.max() == 5
    s.push(1)
    assert s.max() == 5
    assert s.empty() is False
    print("✓ Test 3 passed: Max tracks pushes")

    # Test case 4: Max is restored after pops
    assert s.pop() == 1
    assert s.max() == 5
    assert s.pop() == 5
    assert s.max() == 2
    print("✓ Test 4 passed: Max restored after pops")

    # Test case 5: Duplicate maximums
    s.push(7)
    s.push(7)
    assert s.pop() == 7
    assert s.max() == 7
    assert s.pop() == 7
    assert s.max() == 2
    print("✓ Test 5 passed: Duplicate maximums")

    # Test case 6: Negative values
    s.pop()
    s.push(-3)
    s.push(-8)
    assert s.max() == -3
    assert s.pop() == -8 and s.pop() == -3
    assert s.empty() is True
    print("✓ Test 6 passed: Negative values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_stack_with_max()
