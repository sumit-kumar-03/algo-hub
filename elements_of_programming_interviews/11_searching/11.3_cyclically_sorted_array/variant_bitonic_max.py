"""
EPI 11.3 Variant - Maximum of an Ascending-Then-Descending Array

Problem:
An array A consists of a strictly increasing run followed by a strictly
decreasing run (either run may be empty). Return the maximum element.

Constraints:
- 1 <= len(A) <= 10^5
- Strictly increasing then strictly decreasing (no equal neighbors)
- Must run in O(log n) time

How it works (binary search on the slope):
1. left, right = 0, len(A) - 1
2. While left < right:
   - mid = (left + right) // 2
   - A[mid] < A[mid + 1]: still climbing, so the peak is right of mid
     (left = mid + 1)
   - Otherwise the peak is at mid or to its left (right = mid)
3. Return A[left]

Example 1:
Input: A = [1, 4, 8, 12, 9, 3]
Output: 12

Example 2:
Input: A = [10, 7, 2]
Output: 10
Explanation: The increasing run has length 1.
"""

from typing import List


class Solution:
    def find_peak_max(self, A: List[int]) -> int:
        """
        Finds the maximum of a strictly ascending-then-descending array.

        Args:
            A: Strictly increasing then strictly decreasing array

        Returns:
            The maximum value

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on the slope
        pass


def test_find_peak_max():
    """Test cases for the maximum of a bitonic array"""
    solution = Solution()

    # Test case 1: Peak in the middle
    assert solution.find_peak_max([1, 4, 8, 12, 9, 3]) == 12
    print("✓ Test 1 passed: Peak in middle")

    # Test case 2: Strictly decreasing
    assert solution.find_peak_max([10, 7, 2]) == 10
    print("✓ Test 2 passed: Decreasing only")

    # Test case 3: Strictly increasing
    assert solution.find_peak_max([-5, 0, 3, 99]) == 99
    print("✓ Test 3 passed: Increasing only")

    # Test case 4: Single element
    assert solution.find_peak_max([7]) == 7
    print("✓ Test 4 passed: Single element")

    # Test case 5: Peak right before the end
    assert solution.find_peak_max([1, 2, 3, 4, 5, 6, 2]) == 6
    print("✓ Test 5 passed: Peak near end")

    # Test case 6: Every peak position in a larger array
    for peak in range(50):
        A = list(range(peak + 1)) + list(range(peak - 1, -60, -1))
        assert solution.find_peak_max(A) == peak
    print("✓ Test 6 passed: All peak positions")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_peak_max()
