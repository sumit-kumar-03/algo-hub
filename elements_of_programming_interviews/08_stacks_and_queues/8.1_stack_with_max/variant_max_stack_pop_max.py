"""
EPI 8.1 Extra Variant - Stack with Pop-Max
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Answering max queries on a stack, now also removing the
maximum from the middle of the stack.

Problem:
Design a stack of integers that supports:
- push(x): push x
- pop(): remove and return the top element
- top(): return the top element
- peek_max(): return the largest element
- pop_max(): remove and return the largest element; if several elements
  share the largest value, remove the one closest to the top
The per-element (element, max) trick no longer suffices, because pop_max
removes an element below the top. Make every operation O(log n).

Constraints:
- pop(), top(), peek_max() and pop_max() on an empty stack must raise
  IndexError
- Up to 10^5 operations
- O(log n) time per operation (amortized is fine), O(n) space

How it works (one option):
1. Give each pushed element an increasing id; keep the stack as a list
   of (id, value) and a max-heap of (-value, -id)
2. Keep a set of ids that have been removed by either kind of pop
3. top()/pop(): discard removed entries from the end of the list first;
   peek_max()/pop_max(): discard removed entries from the heap top first
4. Removing through one structure records the id so the other skips it
   later (lazy deletion); each entry is discarded at most once

Example:
push(5), push(1), push(5) -> top() == 5, pop_max() == 5 (the upper 5),
top() == 1, peek_max() == 5, pop() == 1, top() == 5
"""

from typing import List


class PopMaxStack:
    def __init__(self) -> None:
        # TODO: Choose the internal storage
        pass

    def push(self, x: int) -> None:
        """
        Pushes x onto the stack.

        Time Complexity: O(log n)
        """
        # TODO: Implement push
        pass

    def pop(self) -> int:
        """
        Removes and returns the top element.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(log n) amortized
        """
        # TODO: Implement pop
        pass

    def top(self) -> int:
        """
        Returns the top element without removing it.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(log n) amortized
        """
        # TODO: Implement top
        pass

    def peek_max(self) -> int:
        """
        Returns the largest element without removing it.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(log n) amortized
        """
        # TODO: Implement peek_max
        pass

    def pop_max(self) -> int:
        """
        Removes and returns the largest element (topmost one on ties).

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(log n) amortized
        """
        # TODO: Implement pop_max
        pass


def raises_index_error(fn) -> bool:
    """Returns True if calling fn raises IndexError."""
    try:
        fn()
    except IndexError:
        return True
    return False


def test_pop_max_stack():
    """Test cases for the pop-max stack"""

    # Test case 1: Empty stack raises everywhere
    s = PopMaxStack()
    assert raises_index_error(s.pop) and raises_index_error(s.top)
    assert raises_index_error(s.peek_max) and raises_index_error(s.pop_max)
    print("✓ Test 1 passed: Empty stack")

    # Test case 2: Classic sequence, topmost max removed on ties
    s.push(5)
    s.push(1)
    s.push(5)
    assert s.top() == 5 and s.pop_max() == 5
    assert s.top() == 1 and s.peek_max() == 5
    assert s.pop() == 1 and s.top() == 5
    print("✓ Test 2 passed: Topmost max removed first")

    # Test case 3: pop_max from the bottom, then the stack shrinks normally
    s = PopMaxStack()
    for x in (9, 2, 4):
        s.push(x)
    assert s.pop_max() == 9
    assert s.peek_max() == 4 and s.pop() == 4 and s.pop() == 2
    assert raises_index_error(s.top)
    print("✓ Test 3 passed: Max removed from the bottom")

    # Test case 4: pop removes the max, peek_max falls back
    s = PopMaxStack()
    for x in (1, 3, 7):
        s.push(x)
    assert s.pop() == 7 and s.peek_max() == 3
    assert s.pop_max() == 3 and s.top() == 1
    print("✓ Test 4 passed: pop of the max updates peek_max")

    # Test case 5: Negative values
    s = PopMaxStack()
    for x in (-4, -9, -1, -1):
        s.push(x)
    assert s.pop_max() == -1 and s.top() == -1
    assert s.pop_max() == -1 and s.top() == -9 and s.peek_max() == -4
    print("✓ Test 5 passed: Negative values")

    # Test case 6: Randomized comparison with a plain list
    import random

    rng = random.Random(13)
    s = PopMaxStack()
    model: List[int] = []
    for _ in range(5000):
        op = rng.randrange(5)
        if op <= 1 or not model:
            x = rng.randint(-20, 20)
            s.push(x)
            model.append(x)
        elif op == 2:
            assert s.pop() == model.pop()
        elif op == 3:
            m = max(model)
            idx = len(model) - 1 - model[::-1].index(m)
            del model[idx]
            assert s.pop_max() == m
        else:
            assert s.top() == model[-1] and s.peek_max() == max(model)
    print("✓ Test 6 passed: Matches a plain list")

    # Test case 7: Large workload runs quickly
    s = PopMaxStack()
    for x in range(50000):
        s.push(x)
    assert all(s.pop_max() == x for x in range(49999, 25000, -1))
    assert s.top() == 25000 and s.peek_max() == 25000
    print("✓ Test 7 passed: 5 * 10^4 pushes and pop_max calls")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_pop_max_stack()
