"""
EPI 13.1 - Compute the Intersection of Two Sorted Arrays

Problem:
Given two sorted arrays, return a new sorted array containing the elements
present in both. The result must not contain duplicates, even if the inputs do.

Constraints:
- 0 <= len(A), len(B) <= 10^5
- Both arrays are sorted in ascending order
- Aim for O(m + n) time with two pointers (or O(m log n) with binary search
  when one array is much smaller)

How it works (two pointers):
1. i, j = 0, 0
2. While i < len(A) and j < len(B):
   - A[i] == B[j]: append it if it differs from the last appended value;
     advance both
   - A[i] < B[j]: advance i
   - otherwise: advance j
3. Return the result

Example 1:
Input: A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12], B = [5, 5, 6, 8, 8, 9, 10, 10]
Output: [5, 6, 8]

Example 2:
Input: A = [1, 2], B = [3, 4]
Output: []
"""

from typing import List


class Solution:
    def intersect_two_sorted_arrays(self, A: List[int], B: List[int]) -> List[int]:
        """
        Computes the duplicate-free intersection of two sorted arrays.

        Args:
            A: First sorted array
            B: Second sorted array

        Returns:
            Sorted list of distinct values present in both A and B

        Time Complexity: O(m + n)
        Space Complexity: O(1) extra, excluding the output
        """
        # TODO: Implement sorted-array intersection
        pass


def test_intersect_two_sorted_arrays():
    """Test cases for sorted-array intersection"""
    solution = Solution()

    # Test case 1: Book example with duplicates
    A1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B1 = [5, 5, 6, 8, 8, 9, 10, 10]
    assert solution.intersect_two_sorted_arrays(A1, B1) == [5, 6, 8]
    print("✓ Test 1 passed: Book example -> [5, 6, 8]")

    # Test case 2: No common elements
    assert solution.intersect_two_sorted_arrays([1, 2], [3, 4]) == []
    print("✓ Test 2 passed: No overlap")

    # Test case 3: One array empty
    assert solution.intersect_two_sorted_arrays([], [1, 2, 3]) == []
    print("✓ Test 3 passed: Empty array")

    # Test case 4: Repeated single value
    assert solution.intersect_two_sorted_arrays([1, 1, 1], [1, 1]) == [1]
    print("✓ Test 4 passed: Duplicates collapsed")

    # Test case 5: Identical arrays
    assert solution.intersect_two_sorted_arrays([-3, 0, 4], [-3, 0, 4]) == [-3, 0, 4]
    print("✓ Test 5 passed: Identical arrays")

    # Test case 6: Very different lengths
    assert solution.intersect_two_sorted_arrays([50], list(range(100))) == [50]
    print("✓ Test 6 passed: Different lengths")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_intersect_two_sorted_arrays()
