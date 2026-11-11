"""
EPI 13.1 Extra Variant - Intersection of Sorted Arrays Keeping Duplicates
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the two-pointer walk over two sorted arrays, without the
"skip values already appended" step.

Problem:
Given two arrays sorted in ascending order, return a sorted array holding
every value common to both, repeated as many times as it appears in BOTH
arrays (that is, min(count in A, count in B) times).

Constraints:
- 0 <= len(A), len(B) <= 10^5
- Both arrays are sorted in ascending order
- O(m + n) time, O(1) extra space excluding the output

How it works (two pointers):
1. i, j = 0, 0
2. If A[i] == B[j], append the value and advance BOTH pointers, so each
   copy is matched with exactly one copy from the other array
3. Otherwise advance the pointer at the smaller value
4. Stop when either array is exhausted

Example 1:
Input: A = [1, 2, 2, 2, 3], B = [2, 2, 3, 3, 4]
Output: [2, 2, 3]
Explanation: 2 appears 3 and 2 times, so it is kept twice; 3 is kept once.

Example 2:
Input: A = [1, 1], B = [1]
Output: [1]
"""

from typing import List


class Solution:
    def intersect_with_multiplicity(self, A: List[int], B: List[int]) -> List[int]:
        """
        Computes the multiset intersection of two sorted arrays.

        Args:
            A: First sorted array
            B: Second sorted array

        Returns:
            Sorted list of common values, each repeated min(countA, countB) times

        Time Complexity: O(m + n)
        Space Complexity: O(1) extra, excluding the output
        """
        # TODO: Implement multiset intersection with two pointers
        pass


def test_intersect_with_multiplicity():
    """Test cases for multiset intersection of sorted arrays"""
    solution = Solution()

    # Test case 1: Duplicates kept up to the smaller count
    assert solution.intersect_with_multiplicity([1, 2, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 2, 3]
    print("✓ Test 1 passed: [1,2,2,2,3] & [2,2,3,3,4] -> [2, 2, 3]")

    # Test case 2: Unequal counts of the only common value
    assert solution.intersect_with_multiplicity([1, 1], [1]) == [1]
    print("✓ Test 2 passed: [1,1] & [1] -> [1]")

    # Test case 3: Nothing in common
    assert solution.intersect_with_multiplicity([1, 3, 5], [2, 4, 6]) == []
    print("✓ Test 3 passed: Disjoint -> []")

    # Test case 4: Empty input
    assert solution.intersect_with_multiplicity([], [1, 2]) == []
    assert solution.intersect_with_multiplicity([], []) == []
    print("✓ Test 4 passed: Empty -> []")

    # Test case 5: Identical arrays
    assert solution.intersect_with_multiplicity([4, 4, 7], [4, 4, 7]) == [4, 4, 7]
    print("✓ Test 5 passed: Identical arrays")

    # Test case 6: Negative numbers
    assert solution.intersect_with_multiplicity([-5, -5, -1, 0, 0], [-5, -1, -1, 0, 0, 0]) == [-5, -1, 0, 0]
    print("✓ Test 6 passed: Negative values")

    # Test case 7: Very different lengths
    A = list(range(0, 1000, 3))
    B = [3, 3, 6, 999, 1000]
    assert solution.intersect_with_multiplicity(A, B) == [3, 6, 999]
    print("✓ Test 7 passed: Long vs short array")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_intersect_with_multiplicity()
