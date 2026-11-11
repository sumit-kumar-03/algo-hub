"""
EPI 11.3 - Search a Cyclically Sorted Array

Problem:
An array is cyclically sorted if rotating it by some amount makes it sorted.
Given a cyclically sorted array of distinct elements, return the index of its
smallest element.

Constraints:
- 1 <= len(A) <= 10^5
- All elements are distinct
- Must run in O(log n) time

How it works (binary search against the right end):
1. left, right = 0, len(A) - 1
2. While left < right:
   - mid = (left + right) // 2
   - A[mid] > A[right]: the drop is to the right of mid, so left = mid + 1
   - Otherwise the minimum is in [left, mid], so right = mid
3. Return left

Example 1:
Input: A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
Output: 4
Explanation: A[4] = 103 is the smallest; rotating left by 4 sorts the array.

Example 2:
Input: A = [1, 2, 3, 4]
Output: 0
Explanation: Not rotated at all.
"""

from typing import List


class Solution:
    def search_smallest(self, A: List[int]) -> int:
        """
        Finds the index of the smallest element in a cyclically sorted array.

        Args:
            A: Cyclically sorted array of distinct elements

        Returns:
            Index of the minimum element

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search comparing with the right end
        pass


def test_search_smallest():
    """Test cases for the minimum of a cyclically sorted array"""
    solution = Solution()

    # Test case 1: Book example
    A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    assert solution.search_smallest(A) == 4
    print("✓ Test 1 passed: Book example -> 4")

    # Test case 2: Not rotated
    assert solution.search_smallest([1, 2, 3, 4]) == 0
    print("✓ Test 2 passed: Not rotated")

    # Test case 3: Single element
    assert solution.search_smallest([42]) == 0
    print("✓ Test 3 passed: Single element")

    # Test case 4: Minimum is the last element
    assert solution.search_smallest([2, 3, 4, 5, 1]) == 4
    print("✓ Test 4 passed: Minimum at end")

    # Test case 5: Two elements, rotated
    assert solution.search_smallest([9, -3]) == 1
    print("✓ Test 5 passed: Two elements")

    # Test case 6: Every rotation of a larger array
    base = list(range(0, 100, 3))
    for shift in range(len(base)):
        rotated = base[shift:] + base[:shift]
        assert solution.search_smallest(rotated) == (len(base) - shift) % len(base)
    print("✓ Test 6 passed: All rotations of a 34-element array")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_search_smallest()
