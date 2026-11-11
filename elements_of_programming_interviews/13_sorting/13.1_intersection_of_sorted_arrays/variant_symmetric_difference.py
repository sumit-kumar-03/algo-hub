"""
EPI 13.1 Extra Variant - Symmetric Difference of Two Sorted Arrays
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the two-pointer walk with duplicate skipping, but emitting the
values the intersection would discard and discarding the ones it keeps.

Problem:
Given two arrays sorted in ascending order (possibly with duplicates),
return a sorted array of the distinct values that appear in exactly one of
the two arrays.

Constraints:
- 0 <= len(A), len(B) <= 10^5
- Both arrays are sorted in ascending order
- O(m + n) time, O(1) extra space excluding the output

How it works (two pointers):
1. i, j = 0, 0
2. Compare A[i] and B[j]:
   - equal: the value is in both, so skip every copy of it in both arrays
   - A[i] smaller: A[i] is not in B; append it, then skip its copies in A
   - B[j] smaller: symmetric
3. When one array runs out, append the remaining distinct values of the
   other
4. Skipping all copies at once is what keeps the output duplicate-free

Example 1:
Input: A = [1, 2, 2, 3, 5], B = [2, 4, 5, 5, 6]
Output: [1, 3, 4, 6]

Example 2:
Input: A = [7, 7], B = []
Output: [7]
"""

from typing import List


class Solution:
    def symmetric_difference(self, A: List[int], B: List[int]) -> List[int]:
        """
        Computes the distinct values present in exactly one sorted array.

        Args:
            A: First sorted array
            B: Second sorted array

        Returns:
            Sorted list of distinct values in A or B but not both

        Time Complexity: O(m + n)
        Space Complexity: O(1) extra, excluding the output
        """
        # TODO: Implement symmetric difference with two pointers
        pass


def test_symmetric_difference():
    """Test cases for symmetric difference of sorted arrays"""
    solution = Solution()

    # Test case 1: Mixed overlap
    assert solution.symmetric_difference([1, 2, 2, 3, 5], [2, 4, 5, 5, 6]) == [1, 3, 4, 6]
    print("✓ Test 1 passed: -> [1, 3, 4, 6]")

    # Test case 2: One side empty, duplicates collapse
    assert solution.symmetric_difference([7, 7], []) == [7]
    assert solution.symmetric_difference([], [1, 1, 2]) == [1, 2]
    print("✓ Test 2 passed: One empty side")

    # Test case 3: Identical value sets (different counts) -> empty
    assert solution.symmetric_difference([1, 1, 2], [1, 2, 2, 2]) == []
    print("✓ Test 3 passed: Same value sets -> []")

    # Test case 4: Both empty
    assert solution.symmetric_difference([], []) == []
    print("✓ Test 4 passed: Both empty -> []")

    # Test case 5: Disjoint arrays interleave
    assert solution.symmetric_difference([1, 3, 3, 5], [2, 4, 4]) == [1, 2, 3, 4, 5]
    print("✓ Test 5 passed: Disjoint -> sorted distinct union")

    # Test case 6: Negatives and a long tail in one array
    assert solution.symmetric_difference([-3, -1, 0], [-3, 0, 8, 8, 9]) == [-1, 8, 9]
    print("✓ Test 6 passed: Negatives and tail")

    # Test case 7: Larger arrays checked with sets
    A = sorted((i * 7) % 50 for i in range(80))
    B = sorted((i * 3) % 40 + 20 for i in range(60))
    assert solution.symmetric_difference(A, B) == sorted(set(A) ^ set(B))
    print("✓ Test 7 passed: Matches set symmetric difference")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_symmetric_difference()
