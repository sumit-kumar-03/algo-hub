"""
EPI 11.1 Variant - Interval Enclosing k

Problem:
Given a sorted array A and a key k, return [L, U] where L is the index of the
first occurrence of k and U is the index of the last occurrence. If k is not
in A, return [-1, -1].

Constraints:
- Must run in O(log n) time
- 0 <= len(A) <= 10^5
- A is sorted in ascending order

How it works (two binary searches):
1. Binary search for the first occurrence: on a match, record it and keep
   searching left
2. Binary search for the last occurrence: on a match, record it and keep
   searching right
3. Return [first, last] (both -1 if k is absent)

Example 1:
Input: A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13], k = 11
Output: [7, 8]

Example 2:
Input: A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13], k = 5
Output: [-1, -1]
"""

from typing import List


class Solution:
    def search_range(self, A: List[int], k: int) -> List[int]:
        """
        Finds the first and last indices of k in a sorted array.

        Args:
            A: Sorted array, possibly with duplicates
            k: Key to search for

        Returns:
            [first index, last index], or [-1, -1] if k is absent

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement two binary searches
        pass


def test_search_range():
    """Test cases for the interval enclosing k"""
    solution = Solution()
    A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13]

    # Test case 1: Book example
    assert solution.search_range(A, 11) == [7, 8]
    print("✓ Test 1 passed: k = 11 -> [7, 8]")

    # Test case 2: Triple run
    assert solution.search_range(A, 4) == [3, 5]
    print("✓ Test 2 passed: k = 4 -> [3, 5]")

    # Test case 3: Single occurrence
    assert solution.search_range(A, 13) == [9, 9]
    print("✓ Test 3 passed: Single occurrence at end")

    # Test case 4: Absent key
    assert solution.search_range(A, 5) == [-1, -1]
    print("✓ Test 4 passed: Absent key")

    # Test case 5: Empty array
    assert solution.search_range([], 1) == [-1, -1]
    print("✓ Test 5 passed: Empty array")

    # Test case 6: Whole array is k
    assert solution.search_range([3, 3, 3, 3], 3) == [0, 3]
    print("✓ Test 6 passed: All elements equal k")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_search_range()
