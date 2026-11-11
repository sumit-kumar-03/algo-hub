"""
EPI 12.3 Extra Variant - First Unique Value in a Stream
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the LRU cache's combination of a hash table with an ordered
(doubly linked) structure that supports O(1) removal from the middle.

Problem:
Design a class that receives a stream of values one at a time and can
report, at any moment, the earliest-arriving value that has so far appeared
exactly once.
- add(value): record one more occurrence of value.
- first_unique(): return the earliest value that has been added exactly
  once so far, or None if there is no such value.

Constraints:
- Up to 10^5 operations
- Values are hashable (ints in the tests)
- O(1) time per operation (amortized is fine); scanning the whole history in
  first_unique() is too slow

How it works:
1. Keep an insertion-ordered set (or doubly linked list plus a hash table
   from value to list node) of values currently seen exactly once
2. Keep a hash set of values seen two or more times
3. add(value): if it is new, append it to the ordered structure; if it is in
   the ordered structure, remove it there and mark it as repeated; if it is
   already repeated, do nothing
4. first_unique() returns the front of the ordered structure

Example 1:
Input: add(2); add(3); add(5); first_unique(); add(2); first_unique();
       add(3); first_unique()
Output: 2, then 3, then 5

Example 2:
Input: add(7); add(7); first_unique()
Output: None
"""

from typing import Hashable, Optional


class FirstUnique:
    def __init__(self):
        """
        Initializes an empty tracker.
        """
        # TODO: Initialize the data structures
        pass

    def add(self, value: Hashable) -> None:
        """
        Records one more occurrence of value.

        Args:
            value: The value arriving on the stream

        Time Complexity: O(1)
        Space Complexity: O(1) per call; O(d) total for d distinct values
        """
        # TODO: Implement add
        pass

    def first_unique(self) -> Optional[Hashable]:
        """
        Returns the earliest value that has appeared exactly once.

        Returns:
            That value, or None if every value seen so far has repeated

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement first_unique
        pass


def test_first_unique():
    """Test cases for the first unique value tracker"""

    # Test case 1: Example from the statement
    fu = FirstUnique()
    fu.add(2)
    fu.add(3)
    fu.add(5)
    assert fu.first_unique() == 2
    fu.add(2)
    assert fu.first_unique() == 3
    fu.add(3)
    assert fu.first_unique() == 5
    print("✓ Test 1 passed: Front advances as values repeat")

    # Test case 2: Empty tracker
    fu = FirstUnique()
    assert fu.first_unique() is None
    print("✓ Test 2 passed: Empty -> None")

    # Test case 3: Every value repeated
    fu = FirstUnique()
    fu.add(7)
    fu.add(7)
    assert fu.first_unique() is None
    print("✓ Test 3 passed: All repeated -> None")

    # Test case 4: A third occurrence does not bring a value back
    fu = FirstUnique()
    fu.add(1)
    fu.add(1)
    fu.add(1)
    fu.add(4)
    assert fu.first_unique() == 4
    print("✓ Test 4 passed: Repeated stays repeated")

    # Test case 5: Removing from the middle keeps the order of the rest
    fu = FirstUnique()
    for v in [10, 20, 30, 40]:
        fu.add(v)
    fu.add(20)
    fu.add(10)
    assert fu.first_unique() == 30
    fu.add(30)
    assert fu.first_unique() == 40
    print("✓ Test 5 passed: Middle removals")

    # Test case 6: Zero and negative values are valid
    fu = FirstUnique()
    fu.add(0)
    fu.add(-1)
    assert fu.first_unique() == 0
    fu.add(0)
    assert fu.first_unique() == -1
    print("✓ Test 6 passed: 0 and negative values")

    # Test case 7: Larger stream against a straightforward recount
    fu = FirstUnique()
    stream = [(i * 7919) % 50 for i in range(300)]
    counts = {}
    order = []
    for v in stream:
        fu.add(v)
        if v not in counts:
            order.append(v)
        counts[v] = counts.get(v, 0) + 1
        expected = next((x for x in order if counts[x] == 1), None)
        assert fu.first_unique() == expected
    print("✓ Test 7 passed: 300-value stream matches recount")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_first_unique()
