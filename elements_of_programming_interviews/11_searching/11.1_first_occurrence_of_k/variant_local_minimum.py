"""
EPI 11.1 Variant - Find a Local Minimum

Problem:
A is an unsorted array of n integers with A[0] >= A[1] and
A[n - 2] <= A[n - 1]. An index i is a local minimum if A[i] is less than or
equal to each of its neighbors (A[i - 1] and A[i + 1], where they exist).
Return the index of any local minimum.

Constraints:
- 2 <= len(A) <= 10^5
- A[0] >= A[1] and A[n - 2] <= A[n - 1], so a local minimum always exists
- Must run in O(log n) time
- Several answers may be valid; any one is accepted

How it works (binary search on the slope):
1. left, right = 0, len(A) - 1
2. While left < right:
   - mid = (left + right) // 2
   - If A[mid] > A[mid + 1], the values go down to the right, so a local
     minimum exists in [mid + 1, right]: left = mid + 1
   - Otherwise a local minimum exists in [left, mid]: right = mid
3. Return left

Example 1:
Input: A = [9, 7, 3, 5, 8]
Output: 2
Explanation: 3 <= 7 and 3 <= 5.

Example 2:
Input: A = [5, 2, 4, 1, 6]
Output: 1 or 3
Explanation: Both A[1] = 2 and A[3] = 1 are local minima.
"""

from typing import List


class Solution:
    def find_local_minimum(self, A: List[int]) -> int:
        """
        Finds the index of some local minimum.

        Args:
            A: Array with A[0] >= A[1] and A[-2] <= A[-1]

        Returns:
            Index i such that A[i] <= its neighbors

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on the slope
        pass


def _is_local_min(A: List[int], i: int) -> bool:
    if not isinstance(i, int) or not 0 <= i < len(A):
        return False
    left_ok = i == 0 or A[i] <= A[i - 1]
    right_ok = i == len(A) - 1 or A[i] <= A[i + 1]
    return left_ok and right_ok


def test_find_local_minimum():
    """Test cases for finding a local minimum"""
    solution = Solution()

    # Test case 1: Single valley
    A1 = [9, 7, 3, 5, 8]
    assert _is_local_min(A1, solution.find_local_minimum(A1)) is True
    print("✓ Test 1 passed: Single valley")

    # Test case 2: Two valleys, either is fine
    A2 = [5, 2, 4, 1, 6]
    assert _is_local_min(A2, solution.find_local_minimum(A2)) is True
    print("✓ Test 2 passed: Two valleys")

    # Test case 3: Smallest valid array
    A3 = [4, 4]
    assert _is_local_min(A3, solution.find_local_minimum(A3)) is True
    print("✓ Test 3 passed: Length 2")

    # Test case 4: Plateaus
    A4 = [3, 3, 3, 3, 3]
    assert _is_local_min(A4, solution.find_local_minimum(A4)) is True
    print("✓ Test 4 passed: All equal")

    # Test case 5: Zigzag
    A5 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 11]
    assert _is_local_min(A5, solution.find_local_minimum(A5)) is True
    print("✓ Test 5 passed: Zigzag")

    # Test case 6: Long descent then ascent
    A6 = list(range(1000, 0, -1)) + list(range(2, 1000))
    assert _is_local_min(A6, solution.find_local_minimum(A6)) is True
    print("✓ Test 6 passed: Large V shape")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_local_minimum()
