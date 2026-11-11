"""
EPI 11.8 - Find the kth Largest Element

Problem:
Given an array of distinct numbers and an integer k (1-based), return the kth
largest element: k = 1 is the maximum and k = len(A) is the minimum. You may
rearrange A in place.

Constraints:
- 1 <= k <= len(A) <= 10^5
- All elements are distinct
- Expected O(n) time, O(1) extra space (randomized selection)
- Do not fully sort the array

How it works (quickselect):
1. left, right = 0, len(A) - 1
2. Pick a random pivot in [left, right] and partition so that elements
   greater than the pivot come first, then the pivot, then smaller elements
3. Let p be the pivot's new index:
   - p == k - 1: return A[p]
   - p > k - 1: continue in [left, p - 1]
   - p < k - 1: continue in [p + 1, right]

Example 1:
Input: A = [3, 2, 1, 5, 4], k = 3
Output: 3

Example 2:
Input: A = [3, 1, -1, 2], k = 4
Output: -1
Explanation: The 4th largest of 4 elements is the minimum.
"""

from typing import List


class Solution:
    def find_kth_largest(self, A: List[int], k: int) -> int:
        """
        Finds the kth largest element using randomized partitioning.

        Args:
            A: Array of distinct numbers (may be reordered)
            k: 1-based rank from the top

        Returns:
            The kth largest value

        Time Complexity: O(n) expected, O(n^2) worst case
        Space Complexity: O(1)
        """
        # TODO: Implement quickselect with a random pivot
        pass


def test_find_kth_largest():
    """Test cases for the kth largest element"""
    solution = Solution()

    # Test case 1: Book example, all ranks
    for k, expected in [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]:
        assert solution.find_kth_largest([3, 2, 1, 5, 4], k) == expected
    print("✓ Test 1 passed: [3, 2, 1, 5, 4] for k = 1..5")

    # Test case 2: Negative values
    assert solution.find_kth_largest([3, 1, -1, 2], 4) == -1
    assert solution.find_kth_largest([3, 1, -1, 2], 2) == 2
    print("✓ Test 2 passed: Negatives")

    # Test case 3: Single element
    assert solution.find_kth_largest([42], 1) == 42
    print("✓ Test 3 passed: Single element")

    # Test case 4: Already sorted ascending and descending
    assert solution.find_kth_largest(list(range(100)), 10) == 90
    assert solution.find_kth_largest(list(range(99, -1, -1)), 10) == 90
    print("✓ Test 4 passed: Sorted inputs")

    # Test case 5: Larger array, every rank checked against sorting
    data = [(i * 7919) % 10007 for i in range(1, 301)]  # distinct
    ranked = sorted(data, reverse=True)
    for k in range(1, len(data) + 1):
        assert solution.find_kth_largest(list(data), k) == ranked[k - 1]
    print("✓ Test 5 passed: 300 distinct values, all ranks")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_kth_largest()
