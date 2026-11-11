"""
EPI 15.3 - Generate Permutations

Problem:
Given an array of distinct integers, return every permutation of it. Each
permutation must appear exactly once; the order in which permutations are
listed does not matter.

Constraints:
- 0 <= len(A) <= 8
- All entries of A are distinct
- There are n! permutations, so O(n * n!) time is optimal

How it works (swap-based backtracking):
1. permute(i): every permutation of A[i:] with A[:i] fixed
2. If i reaches the last index (or the end), record a copy of A
3. Otherwise, for each j from i to n - 1: swap A[i] and A[j] so A[j] takes
   position i, recurse on i + 1, then swap back to restore A
Alternative: start from the sorted array and repeatedly apply
"next permutation" until it wraps around.

Example 1:
Input: A = [7, 3, 5]
Output: [[7, 3, 5], [7, 5, 3], [3, 7, 5], [3, 5, 7], [5, 3, 7], [5, 7, 3]]
(any order)

Example 2:
Input: A = [2, 3, 5, 7]
Output: all 24 orderings of the four numbers (any order)
"""

from typing import List


class Solution:
    def permutations(self, A: List[int]) -> List[List[int]]:
        """
        Generates all permutations of an array of distinct integers.

        Args:
            A: List of distinct integers

        Returns:
            List of all permutations, in any order

        Time Complexity: O(n * n!)
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement swap-based permutation generation
        pass


def normalize(perms: List[List[int]]) -> List[tuple]:
    """Sorts permutations so results can be compared regardless of order."""
    return sorted(tuple(p) for p in perms)


def test_permutations():
    """Test cases for generating permutations"""
    import itertools

    solution = Solution()

    # Test case 1: Empty array has one permutation (the empty one)
    assert normalize(solution.permutations([])) == [()]
    print("✓ Test 1 passed: [] -> [[]]")

    # Test case 2: Single element
    assert normalize(solution.permutations([4])) == [(4,)]
    print("✓ Test 2 passed: [4] -> [[4]]")

    # Test case 3: Book example
    result3 = solution.permutations([7, 3, 5])
    assert normalize(result3) == sorted(itertools.permutations([7, 3, 5]))
    print("✓ Test 3 passed: [7, 3, 5] -> 6 permutations")

    # Test case 4: Four elements, no duplicates in the output
    result4 = solution.permutations([2, 3, 5, 7])
    assert len(result4) == 24
    assert normalize(result4) == sorted(itertools.permutations([2, 3, 5, 7]))
    print("✓ Test 4 passed: [2, 3, 5, 7] -> 24 distinct permutations")

    # Test case 5: Negative numbers and unsorted input
    data5 = [0, -1, 9, 4, -6]
    result5 = solution.permutations(data5)
    assert len(result5) == 120
    assert normalize(result5) == sorted(itertools.permutations(data5))
    print("✓ Test 5 passed: 5 elements -> 120 distinct permutations")

    # Test case 6: Seven elements
    result6 = solution.permutations(list(range(7)))
    assert len(result6) == 5040 and len(set(map(tuple, result6))) == 5040
    assert all(sorted(p) == list(range(7)) for p in result6)
    print("✓ Test 6 passed: 7 elements -> 5040 distinct permutations")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_permutations()
