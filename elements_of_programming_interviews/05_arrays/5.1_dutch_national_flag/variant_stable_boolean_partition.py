"""
EPI 5.1 Variant - Boolean Partition Keeping True Objects in Order

Problem:
Given an array of objects with Boolean keys, rearrange it in place so that
all objects whose key is False come before all objects whose key is True,
and the objects with key True keep their original relative order. (The
order of the False objects does not matter.) Each object is a
(key, label) tuple; the key is item[0].

Constraints:
- Must run in O(n) time and use O(1) extra space
- 0 <= len(A) <= 10^5

How it works (fill True objects from the back):
1. Keep a write pointer `write` = len(A) - 1
2. Scan i from the back to the front; whenever A[i] has key True, swap it
   into A[write] and decrement write
3. True objects are placed right to left in the order they are met, so
   their relative order is preserved; False objects end up in front

Example 1:
Input: A = [(True, 'a'), (False, 'b'), (True, 'c'), (False, 'd'), (True, 'e')]
Output: [(False, 'b'), (False, 'd'), (True, 'a'), (True, 'c'), (True, 'e')]
        (False objects may appear in any order)
Explanation: The True objects stay in the order a, c, e.

Example 2:
Input: A = [(True, 'x'), (False, 'y')]
Output: [(False, 'y'), (True, 'x')]
Explanation: The single False object moves to the front.
"""

from typing import Any, List, Tuple


class Solution:
    def stable_true_partition(self, A: List[Tuple[bool, Any]]) -> None:
        """
        Moves False-keyed objects first, keeping True-keyed objects in order.

        Args:
            A: List of (bool key, label) tuples

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Boolean partition that keeps True objects in order
        pass


def check_partition(original: List[Tuple[bool, Any]], A: List[Tuple[bool, Any]]) -> bool:
    """Checks False-first, same multiset, and True objects in original order."""
    if sorted(original, key=repr) != sorted(A, key=repr):
        return False
    num_false = sum(1 for key, _ in original if not key)
    if any(key for key, _ in A[:num_false]):
        return False
    return A[num_false:] == [item for item in original if item[0]]


def test_stable_true_partition():
    """Test cases for Boolean partition that keeps True objects in order"""
    solution = Solution()

    # Test case 1: Book-style mix
    A1 = [(True, "a"), (False, "b"), (True, "c"), (False, "d"), (True, "e")]
    original1 = list(A1)
    solution.stable_true_partition(A1)
    assert check_partition(original1, A1)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Two elements swapped
    A2 = [(True, "x"), (False, "y")]
    solution.stable_true_partition(A2)
    assert A2 == [(False, "y"), (True, "x")]
    print(f"✓ Test 2 passed: {A2}")

    # Test case 3: Long alternating sequence
    A3 = [(i % 2 == 0, i) for i in range(15)]
    original3 = list(A3)
    solution.stable_true_partition(A3)
    assert check_partition(original3, A3)
    print("✓ Test 3 passed: Alternating keys, True objects keep order")

    # Test case 4: All True (order must be unchanged)
    A4 = [(True, 3), (True, 1), (True, 2)]
    solution.stable_true_partition(A4)
    assert A4 == [(True, 3), (True, 1), (True, 2)]
    print("✓ Test 4 passed: All True stays unchanged")

    # Test case 5: All False and empty
    A5 = [(False, 1), (False, 2)]
    solution.stable_true_partition(A5)
    A6: List[Tuple[bool, Any]] = []
    solution.stable_true_partition(A6)
    assert sorted(A5) == [(False, 1), (False, 2)] and A6 == []
    print("✓ Test 5 passed: All False and empty array")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_stable_true_partition()
