"""
EPI 15.3 Variant - Generate Permutations When the Array Has Duplicates

Problem:
Given an array of integers that may contain repeated values, return every
distinct permutation of it. No permutation may appear more than once; the
order in which permutations are listed does not matter.

Constraints:
- 0 <= len(A) <= 8
- Avoid generating duplicates and then filtering them out with a set if
  you can; skip them during the search instead

How it works (sorted backtracking with skips):
1. Sort A and keep a `used` flag per index
2. Build the permutation one position at a time; for each index i not yet
   used, skip it if A[i] == A[i - 1] and index i - 1 is not used (this
   forces equal values to be placed in their original order, so each
   distinct arrangement is produced once)
3. When the permutation has length n, record a copy
Alternative: count occurrences of each value and recurse over the
distinct values with a remaining-count map.

Example 1:
Input: A = [2, 2, 3, 0]
Output: [[2, 2, 0, 3], [2, 2, 3, 0], [2, 0, 2, 3], [2, 0, 3, 2],
         [2, 3, 2, 0], [2, 3, 0, 2], [0, 2, 2, 3], [0, 2, 3, 2],
         [0, 3, 2, 2], [3, 2, 2, 0], [3, 2, 0, 2], [3, 0, 2, 2]]
(any order)
Explanation: 4! / 2! = 12 distinct permutations.

Example 2:
Input: A = [1, 1, 1]
Output: [[1, 1, 1]]
"""

from typing import List


class Solution:
    def permutations_with_duplicates(self, A: List[int]) -> List[List[int]]:
        """
        Generates all distinct permutations of an array that may have duplicates.

        Args:
            A: List of integers, possibly with repeats

        Returns:
            List of distinct permutations, in any order

        Time Complexity: O(n * P) where P is the number of distinct permutations
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement duplicate-aware permutation generation
        pass


def normalize(perms: List[List[int]]) -> List[tuple]:
    """Sorts permutations so results can be compared regardless of order."""
    return sorted(tuple(p) for p in perms)


def test_permutations_with_duplicates():
    """Test cases for permutations with duplicates"""
    import itertools

    solution = Solution()

    def expected(data: List[int]) -> List[tuple]:
        return sorted(set(itertools.permutations(data)))

    # Test case 1: Empty array
    assert normalize(solution.permutations_with_duplicates([])) == [()]
    print("✓ Test 1 passed: [] -> [[]]")

    # Test case 2: All equal
    assert normalize(solution.permutations_with_duplicates([1, 1, 1])) == [(1, 1, 1)]
    print("✓ Test 2 passed: [1, 1, 1] -> [[1, 1, 1]]")

    # Test case 3: Book example, 12 distinct permutations, none repeated
    result3 = solution.permutations_with_duplicates([2, 2, 3, 0])
    assert len(result3) == 12 and normalize(result3) == expected([2, 2, 3, 0])
    print("✓ Test 3 passed: [2, 2, 3, 0] -> 12 distinct permutations")

    # Test case 4: Distinct input behaves like plain permutations
    result4 = solution.permutations_with_duplicates([3, 1, 2])
    assert len(result4) == 6 and normalize(result4) == expected([3, 1, 2])
    print("✓ Test 4 passed: [3, 1, 2] -> 6 permutations")

    # Test case 5: Two pairs of duplicates
    result5 = solution.permutations_with_duplicates([1, 2, 1, 2])
    assert len(result5) == 6 and normalize(result5) == expected([1, 2, 1, 2])
    print("✓ Test 5 passed: [1, 2, 1, 2] -> 6 permutations")

    # Test case 6: Larger multiset: 8! / (3! * 2! * 2!) = 1680
    data6 = [5, 5, 5, -1, -1, 0, 0, 9]
    result6 = solution.permutations_with_duplicates(data6)
    assert len(result6) == 1680 and normalize(result6) == expected(data6)
    print("✓ Test 6 passed: 8-element multiset -> 1680 permutations")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_permutations_with_duplicates()
