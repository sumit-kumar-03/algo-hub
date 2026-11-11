"""
EPI 11.8 Variant - kth Largest Element with Duplicates

Problem:
Same as 11.8, but the array may contain duplicates. The kth largest element
is the value at position k - 1 after a stable descending sort, so equal values
each occupy their own rank. For example, in [5, 5, 3] the 1st and 2nd largest
are both 5 and the 3rd largest is 3.

Constraints:
- 1 <= k <= len(A) <= 10^5
- Duplicates allowed (possibly many)
- Expected O(n) time; do not fully sort the array

How it works (three-way quickselect):
1. Pick a random pivot and partition [left, right] into three groups:
   greater than pivot, equal to pivot, less than pivot
2. Let the equal group occupy indices [lo, hi]:
   - k - 1 < lo: continue in the "greater" part
   - k - 1 > hi: continue in the "less" part
   - Otherwise the pivot value is the answer
(A two-way partition can degrade to O(n^2) when many values are equal.)

Example 1:
Input: A = [3, 5, 1, 5, 3, 3], k = 2
Output: 5

Example 2:
Input: A = [3, 5, 1, 5, 3, 3], k = 5
Output: 3
"""

from typing import List


class Solution:
    def find_kth_largest(self, A: List[int], k: int) -> int:
        """
        Finds the kth largest value when duplicates are allowed.

        Args:
            A: Array of numbers, possibly with duplicates (may be reordered)
            k: 1-based rank from the top

        Returns:
            The value at index k - 1 of A sorted in descending order

        Time Complexity: O(n) expected
        Space Complexity: O(1)
        """
        # TODO: Implement quickselect with a three-way partition
        pass


def test_find_kth_largest_with_duplicates():
    """Test cases for the kth largest element with duplicates"""
    solution = Solution()
    A = [3, 5, 1, 5, 3, 3]

    # Test case 1: Inside a duplicate block at the top
    assert solution.find_kth_largest(list(A), 2) == 5
    print("✓ Test 1 passed: k = 2 -> 5")

    # Test case 2: Inside a duplicate block in the middle
    assert solution.find_kth_largest(list(A), 5) == 3
    print("✓ Test 2 passed: k = 5 -> 3")

    # Test case 3: Every rank
    expected = sorted(A, reverse=True)
    for k in range(1, len(A) + 1):
        assert solution.find_kth_largest(list(A), k) == expected[k - 1]
    print("✓ Test 3 passed: All ranks")

    # Test case 4: All equal
    assert solution.find_kth_largest([7] * 50, 33) == 7
    print("✓ Test 4 passed: All equal")

    # Test case 5: Many duplicates, larger array
    data = [(i * 31) % 7 for i in range(500)]
    ranked = sorted(data, reverse=True)
    for k in (1, 72, 73, 250, 428, 429, 500):
        assert solution.find_kth_largest(list(data), k) == ranked[k - 1]
    print("✓ Test 5 passed: 500 values with 7 distinct")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_kth_largest_with_duplicates()
