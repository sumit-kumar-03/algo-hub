"""
EPI 8.1 Extra Variant - Stack with Bulk Increment
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Storing extra bookkeeping next to each stack entry and
settling it lazily when the entry is popped.

Problem:
Design a bounded stack of integers that holds at most capacity elements
and supports:
- push(x): push x; if the stack is full, do nothing
- pop(): remove and return the top element (IndexError if empty)
- increment(k, val): add val to each of the bottom k elements (all of
  them if there are fewer than k)
Every operation must run in O(1) time, including increment.

Constraints:
- 1 <= capacity <= 10^4
- k >= 1; val and the elements may be negative
- O(1) time per operation, O(capacity) space

How it works:
1. Keep the elements in a list plus a parallel list inc of pending
   additions, where inc[i] applies to element i and to everything below
   it
2. increment(k, val): add val to inc[min(k, size) - 1]
3. pop(): the answer is element + inc[top]; before discarding the top,
   pass inc[top] down to inc[top - 1] so the elements below still get it
4. push(x): append x with a pending addition of 0

Example:
capacity = 3: push(1), push(2), push(3), push(4) (ignored),
increment(5, 100), increment(2, 10) -> pop() == 103, pop() == 112,
pop() == 111
"""

from typing import List


class IncrementStack:
    def __init__(self, capacity: int) -> None:
        """
        Creates an empty stack holding at most capacity elements.

        Args:
            capacity: Maximum number of elements
        """
        # TODO: Choose the internal storage
        pass

    def push(self, x: int) -> None:
        """
        Pushes x unless the stack is full.

        Time Complexity: O(1)
        """
        # TODO: Implement push
        pass

    def pop(self) -> int:
        """
        Removes and returns the top element, including pending increments.

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        # TODO: Implement pop
        pass

    def increment(self, k: int, val: int) -> None:
        """
        Adds val to each of the bottom k elements.

        Args:
            k: Number of bottom elements to change (at least 1)
            val: Amount to add

        Time Complexity: O(1)
        """
        # TODO: Implement lazy increment
        pass


def raises_index_error(fn) -> bool:
    """Returns True if calling fn raises IndexError."""
    try:
        fn()
    except IndexError:
        return True
    return False


def test_increment_stack():
    """Test cases for the bulk-increment stack"""

    # Test case 1: Classic sequence with an ignored push
    s = IncrementStack(3)
    for x in (1, 2, 3, 4):
        s.push(x)
    s.increment(5, 100)
    s.increment(2, 10)
    assert s.pop() == 103 and s.pop() == 112 and s.pop() == 111
    print("✓ Test 1 passed: Increments applied to the bottom elements")

    # Test case 2: Empty stack raises; increment on empty is a no-op
    assert raises_index_error(s.pop)
    s.increment(3, 5)
    s.push(7)
    assert s.pop() == 7
    print("✓ Test 2 passed: Empty stack behavior")

    # Test case 3: Increments do not affect elements pushed later
    s = IncrementStack(5)
    s.push(1)
    s.increment(1, 50)
    s.push(2)
    assert s.pop() == 2 and s.pop() == 51
    print("✓ Test 3 passed: Later pushes are unaffected")

    # Test case 4: Pending increments survive pops and new pushes
    s = IncrementStack(4)
    for x in (0, 0, 0):
        s.push(x)
    s.increment(3, 1)  # all three
    assert s.pop() == 1
    s.push(10)
    s.increment(1, -4)  # bottom only
    assert s.pop() == 10 and s.pop() == 1 and s.pop() == -3
    print("✓ Test 4 passed: Pending increments carried down correctly")

    # Test case 5: Capacity of one
    s = IncrementStack(1)
    s.push(5)
    s.push(6)
    s.increment(10, 2)
    assert s.pop() == 7
    assert raises_index_error(s.pop)
    print("✓ Test 5 passed: Capacity one")

    # Test case 6: Randomized comparison with a direct simulation
    import random

    rng = random.Random(5)
    s = IncrementStack(8)
    model: List[int] = []
    for _ in range(3000):
        op = rng.randrange(3)
        if op == 0:
            x = rng.randint(-50, 50)
            s.push(x)
            if len(model) < 8:
                model.append(x)
        elif op == 1:
            if model:
                assert s.pop() == model.pop()
            else:
                assert raises_index_error(s.pop)
        else:
            k, val = rng.randint(1, 10), rng.randint(-9, 9)
            s.increment(k, val)
            for i in range(min(k, len(model))):
                model[i] += val
    print("✓ Test 6 passed: Matches a direct simulation")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_increment_stack()
