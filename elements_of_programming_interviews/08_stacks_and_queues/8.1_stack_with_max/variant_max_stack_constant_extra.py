"""
EPI 8.1 Extra Variant - Stack with Max Using One Extra Variable
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Restoring the previous maximum on pop, but encoding it in the
stored values instead of storing a second value per entry.

Problem:
Implement a stack of integers with push, pop, top, empty and max, all in
O(1) time, storing exactly one integer per element plus a single integer
variable for the current maximum. Storing (element, max) pairs or keeping
a second stack is not allowed.

Constraints:
- Elements are Python ints (no overflow concerns)
- pop(), top() and max() on an empty stack must raise IndexError
- O(1) time per operation; one stored integer per element plus O(1) extra

How it works:
1. Keep current_max and a list of encoded entries
2. push(x): if the stack is empty, store x and set current_max = x. If
   x > current_max, store 2 * x - current_max (which is greater than x)
   and set current_max = x. Otherwise store x.
3. An entry larger than current_max marks a push that raised the max:
   the real element is current_max, and the old max is recovered as
   2 * current_max - entry
4. pop() and top() decode the top entry the same way; pop() also restores
   the old maximum when it removes such a marker

Example:
push(3), push(7), push(5) -> max() == 7
pop() -> 5, pop() -> 7 -> max() == 3
"""

from typing import List


class MaxStack:
    def __init__(self) -> None:
        # TODO: Choose the internal storage (one int per element + current max)
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


def test_max_stack_constant_extra():
    """Test cases for the encoded max stack"""

    # Test case 1: Empty stack raises
    s = MaxStack()
    assert s.empty() is True
    assert raises_index_error(s.pop) and raises_index_error(s.top)
    assert raises_index_error(s.max)
    print("✓ Test 1 passed: Empty stack")

    # Test case 2: Max rises and is restored
    s.push(3)
    s.push(7)
    s.push(5)
    assert s.max() == 7 and s.top() == 5
    assert s.pop() == 5 and s.top() == 7 and s.pop() == 7
    assert s.max() == 3 and s.top() == 3
    print("✓ Test 2 passed: Max restored after popping it")

    # Test case 3: Equal values do not raise the max
    s.push(3)
    s.push(3)
    assert s.pop() == 3 and s.max() == 3
    assert s.pop() == 3 and s.max() == 3
    print("✓ Test 3 passed: Repeated maximums")

    # Test case 4: Negative values and a rising sequence
    s = MaxStack()
    for x in (-10, -5, -7, 0, 2):
        s.push(x)
    assert s.max() == 2
    assert [s.pop() for _ in range(5)] == [2, 0, -7, -5, -10]
    assert s.empty() is True
    print("✓ Test 4 passed: Negatives and rising values")

    # Test case 5: Each element is stored as a single plain int
    s = MaxStack()
    for x in (4, 9, 1):
        s.push(x)
    containers = [v for v in vars(s).values() if isinstance(v, list)]
    assert len(containers) == 1 and len(containers[0]) == 3
    assert all(type(v) is int for v in containers[0])
    print("✓ Test 5 passed: One list holding one int per element")

    # Test case 6: Randomized comparison with a plain list
    import random

    rng = random.Random(11)
    s = MaxStack()
    model: List[int] = []
    for _ in range(4000):
        if model and rng.random() < 0.45:
            assert s.pop() == model.pop()
        else:
            x = rng.randint(-100, 100)
            s.push(x)
            model.append(x)
        if model:
            assert s.max() == max(model) and s.top() == model[-1]
        else:
            assert s.empty() is True
    print("✓ Test 6 passed: Matches a plain list")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_stack_constant_extra()
