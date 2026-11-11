"""
EPI 11.1 - Search a Sorted Array for First Occurrence of k

Problem:
Given a sorted array A that may contain duplicates and a key k, return the
index of the first element equal to k, or -1 if k does not appear.

Constraints:
- Must run in O(log n) time
- 0 <= len(A) <= 10^5
- A is sorted in ascending order

How it works (binary search that keeps going left):
1. left, right = 0, len(A) - 1; result = -1
2. While left <= right:
   - mid = (left + right) // 2
   - A[mid] > k: right = mid - 1
   - A[mid] < k: left = mid + 1
   - A[mid] == k: record result = mid, then keep searching left (right = mid - 1)
3. Return result

Example 1:
Input: A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], k = 108
Output: 3

Example 2:
Input: A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], k = 285
Output: 6
"""

from typing import List


class Solution:
    def search_first_of_k(self, A: List[int], k: int) -> int:
        """
        Finds the first index of k in a sorted array.

        Args:
            A: Sorted array, possibly with duplicates
            k: Key to search for

        Returns:
            Index of the first occurrence of k, or -1 if absent

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search for first occurrence
        pass


def test_search_first_of_k():
    """Test cases for first-occurrence binary search"""
    solution = Solution()
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

    # Test case 1: Duplicate key in the middle
    assert solution.search_first_of_k(A, 108) == 3
    print("✓ Test 1 passed: First 108 at index 3")

    # Test case 2: Key repeated three times
    assert solution.search_first_of_k(A, 285) == 6
    print("✓ Test 2 passed: First 285 at index 6")

    # Test case 3: Key at the beginning
    assert solution.search_first_of_k(A, -14) == 0
    print("✓ Test 3 passed: Key at beginning")

    # Test case 4: Key at the end
    assert solution.search_first_of_k(A, 401) == 9
    print("✓ Test 4 passed: Key at end")

    # Test case 5: Key absent
    assert solution.search_first_of_k(A, 3) == -1
    print("✓ Test 5 passed: Key not found")

    # Test case 6: Empty array
    assert solution.search_first_of_k([], 1) == -1
    print("✓ Test 6 passed: Empty array")

    # Test case 7: Every element equals k
    assert solution.search_first_of_k([7, 7, 7, 7, 7], 7) == 0
    print("✓ Test 7 passed: All elements equal")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_search_first_of_k()
