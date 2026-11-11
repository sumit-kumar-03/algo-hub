"""
EPI 5.1 Variant - Partition Objects with Boolean Keys

Problem:
Given an array of objects with Boolean keys, rearrange it in place so that
all objects whose key is False come before all objects whose key is True.
Each object is a (key, label) tuple; the key is item[0]. The relative
order within each group does not matter.

Constraints:
- Must run in O(n) time and use O(1) extra space
- 0 <= len(A) <= 10^5

How it works (two pointers from both ends):
1. left = 0, right = len(A) - 1
2. Advance left past False keys; retreat right past True keys
3. If left < right, swap A[left] and A[right] and continue

Example 1:
Input: A = [(True, 'a'), (False, 'b'), (True, 'c'), (False, 'd')]
Output: [(False, 'd'), (False, 'b'), (True, 'c'), (True, 'a')] (one valid answer)
Explanation: Both False objects come before both True objects.

Example 2:
Input: A = [(False, 'a'), (False, 'b')]
Output: [(False, 'a'), (False, 'b')]
Explanation: Nothing needs to move.
"""

from typing import Any, List, Tuple


class Solution:
    def partition_boolean(self, A: List[Tuple[bool, Any]]) -> None:
        """
        Moves all False-keyed objects before all True-keyed objects.

        Args:
            A: List of (bool key, label) tuples

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Boolean partition
        pass


def is_false_first(A: List[Tuple[bool, Any]]) -> bool:
    """Checks that no False key appears after a True key."""
    seen_true = False
    for key, _ in A:
        if key:
            seen_true = True
        elif seen_true:
            return False
    return True


def test_partition_boolean():
    """Test cases for Boolean partition"""
    solution = Solution()

    # Test case 1: Interleaved keys
    A1 = [(True, "a"), (False, "b"), (True, "c"), (False, "d")]
    original1 = sorted(A1)
    solution.partition_boolean(A1)
    assert sorted(A1) == original1 and is_false_first(A1)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: All True then all False (fully reversed)
    A2 = [(True, i) for i in range(5)] + [(False, i) for i in range(5)]
    original2 = sorted(A2)
    solution.partition_boolean(A2)
    assert sorted(A2) == original2 and is_false_first(A2)
    print("✓ Test 2 passed: True block followed by False block")

    # Test case 3: Already partitioned
    A3 = [(False, "a"), (False, "b"), (True, "c")]
    solution.partition_boolean(A3)
    assert sorted(A3) == [(False, "a"), (False, "b"), (True, "c")] and is_false_first(A3)
    print("✓ Test 3 passed: Already partitioned")

    # Test case 4: Single key value
    A4 = [(True, "x"), (True, "y")]
    solution.partition_boolean(A4)
    assert sorted(A4) == [(True, "x"), (True, "y")]
    print("✓ Test 4 passed: All True")

    # Test case 5: Empty array
    A5: List[Tuple[bool, Any]] = []
    solution.partition_boolean(A5)
    assert A5 == []
    print("✓ Test 5 passed: Empty array")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_partition_boolean()
