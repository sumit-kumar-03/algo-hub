"""
EPI 11.1 Extra Variant - Count Values in a Range
(Practice problem, not in the book. Difficulty: Easy)
Builds on: binary search that keeps going after a match to find a boundary
(the first index satisfying a condition), not just any matching index.

Problem:
Given a sorted array A (duplicates allowed) and two integers lo <= hi,
return how many elements x of A satisfy lo <= x <= hi. Neither lo nor hi
needs to appear in A.

Constraints:
- 0 <= len(A) <= 10^5; A is sorted in ascending order
- lo <= hi
- O(log n) time, O(1) space; do not scan the matching block
- Do not use the bisect module (write the boundary searches yourself)

How it works (two boundary searches):
1. left_edge = first index i with A[i] >= lo (len(A) if none)
2. right_edge = first index i with A[i] > hi (len(A) if none)
3. Both are "first index where a monotone condition becomes true" searches;
   the answer is right_edge - left_edge

Example 1:
Input: A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13], lo = 2, hi = 7
Output: 6
Explanation: 2, 2, 4, 4, 4, 7.

Example 2:
Input: A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13], lo = 5, hi = 6
Output: 0
"""

from typing import List


class Solution:
    def count_in_range(self, A: List[int], lo: int, hi: int) -> int:
        """
        Counts elements of a sorted array that lie in [lo, hi].

        Args:
            A: Sorted array, possibly with duplicates
            lo: Lower bound (inclusive)
            hi: Upper bound (inclusive), hi >= lo

        Returns:
            Number of elements x with lo <= x <= hi

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement with two boundary binary searches
        pass


def test_count_in_range():
    """Test cases for counting values in a range"""
    solution = Solution()
    A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13]

    # Test case 1: Both bounds present
    assert solution.count_in_range(A, 2, 7) == 6
    print("✓ Test 1 passed: [2, 7] -> 6")

    # Test case 2: Neither bound present, nothing inside
    assert solution.count_in_range(A, 5, 6) == 0
    print("✓ Test 2 passed: [5, 6] -> 0")

    # Test case 3: Bounds outside the array range
    assert solution.count_in_range(A, -100, 100) == 10
    assert solution.count_in_range(A, 14, 20) == 0
    assert solution.count_in_range(A, -5, 0) == 0
    print("✓ Test 3 passed: Bounds outside the array")

    # Test case 4: lo == hi counts one value's duplicates
    assert solution.count_in_range(A, 4, 4) == 3
    assert solution.count_in_range(A, 3, 3) == 0
    print("✓ Test 4 passed: Single-value range")

    # Test case 5: Empty array
    assert solution.count_in_range([], 0, 10) == 0
    print("✓ Test 5 passed: Empty array")

    # Test case 6: All elements equal, negatives
    assert solution.count_in_range([-3] * 9, -3, -3) == 9
    assert solution.count_in_range([-3] * 9, -2, 5) == 0
    print("✓ Test 6 passed: All equal")

    # Test case 7: Many ranges against a linear count
    B = sorted((i * 31) % 50 - 25 for i in range(400))
    for lo in range(-30, 31, 4):
        for hi in range(lo, 31, 5):
            assert solution.count_in_range(B, lo, hi) == sum(lo <= x <= hi for x in B)
    print("✓ Test 7 passed: Many ranges")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_in_range()
