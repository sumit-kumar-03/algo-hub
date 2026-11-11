"""
EPI 11.1 Variant - First Element Greater Than k

Problem:
Given a sorted array A (duplicates allowed) and a key k, return the index of
the first element that is strictly greater than k, or -1 if no such element
exists.

Constraints:
- Must run in O(log n) time
- 0 <= len(A) <= 10^5
- A is sorted in ascending order

How it works (binary search that keeps going left):
1. left, right = 0, len(A) - 1; result = -1
2. While left <= right:
   - mid = (left + right) // 2
   - A[mid] > k: record result = mid, then search left (right = mid - 1)
   - Otherwise: left = mid + 1
3. Return result

Example 1:
Input: A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], k = 285
Output: 9

Example 2:
Input: A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], k = -13
Output: 1
"""

from typing import List


class Solution:
    def search_first_greater(self, A: List[int], k: int) -> int:
        """
        Finds the first index whose value is greater than k.

        Args:
            A: Sorted array, possibly with duplicates
            k: Key to compare against

        Returns:
            Index of the first element > k, or -1 if none

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search for the first element greater than k
        pass


def test_search_first_greater():
    """Test cases for first element greater than k"""
    solution = Solution()
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

    # Test case 1: Key with duplicates
    assert solution.search_first_greater(A, 285) == 9
    print("✓ Test 1 passed: k = 285 -> 9")

    # Test case 2: Key absent, falls between elements
    assert solution.search_first_greater(A, -13) == 1
    print("✓ Test 2 passed: k = -13 -> 1")

    # Test case 3: Key smaller than everything
    assert solution.search_first_greater(A, -100) == 0
    print("✓ Test 3 passed: Key below all elements")

    # Test case 4: Key equal to the last element
    assert solution.search_first_greater(A, 401) == -1
    print("✓ Test 4 passed: No greater element")

    # Test case 5: Empty array
    assert solution.search_first_greater([], 5) == -1
    print("✓ Test 5 passed: Empty array")

    # Test case 6: Duplicate run at the start
    assert solution.search_first_greater([108, 108, 108, 200], 108) == 3
    print("✓ Test 6 passed: Skips a duplicate run")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_search_first_greater()
