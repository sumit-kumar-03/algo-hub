"""
EPI 15.4 Variant - Generate the Power Set of a Multiset

Problem:
Given a list of integers that may contain repeated values (a multiset),
return every distinct sub-multiset. Two subsets that contain the same
values with the same multiplicities count as the same subset and must
appear only once. Neither the order of the subsets nor the order of
elements inside a subset matters.

Constraints:
- 0 <= len(A) <= 16
- Skip duplicates during the search rather than filtering a full 2^n
  enumeration with a set, if you can

How it works (group equal values):
1. Sort A (or count each distinct value)
2. For each distinct value v that occurs c times, branch on how many
   copies to take: 0, 1, ..., c
3. Recurse to the next distinct value; at the end record the subset
The number of results is the product of (c + 1) over distinct values.

Example 1:
Input: A = [1, 2, 3, 2]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 2], [2, 3],
         [1, 2, 2], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]]
(any order)
Explanation: 2 * 3 * 2 = 12 distinct sub-multisets.

Example 2:
Input: A = [4, 4]
Output: [[], [4], [4, 4]]
"""

from typing import List


class Solution:
    def generate_power_set_with_duplicates(self, A: List[int]) -> List[List[int]]:
        """
        Generates all distinct sub-multisets of a multiset.

        Args:
            A: List of integers, possibly with repeats

        Returns:
            List of distinct sub-multisets, in any order

        Time Complexity: O(n * R) where R is the number of distinct subsets
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement duplicate-aware power set generation
        pass


def normalize(subsets: List[List[int]]) -> List[tuple]:
    """Sorts each subset and the list of subsets for order-free comparison."""
    return sorted(tuple(sorted(s)) for s in subsets)


def test_generate_power_set_with_duplicates():
    """Test cases for power set of a multiset"""
    import itertools

    solution = Solution()

    def expected(A: List[int]) -> List[tuple]:
        return sorted(
            {tuple(sorted(c)) for r in range(len(A) + 1) for c in itertools.combinations(A, r)}
        )

    # Test case 1: Empty multiset
    assert normalize(solution.generate_power_set_with_duplicates([])) == [()]
    print("✓ Test 1 passed: [] -> [[]]")

    # Test case 2: Two equal values
    result2 = solution.generate_power_set_with_duplicates([4, 4])
    assert normalize(result2) == [(), (4,), (4, 4)] and len(result2) == 3
    print("✓ Test 2 passed: [4, 4] -> [[], [4], [4, 4]]")

    # Test case 3: Book example
    result3 = solution.generate_power_set_with_duplicates([1, 2, 3, 2])
    assert len(result3) == 12 and normalize(result3) == expected([1, 2, 3, 2])
    print("✓ Test 3 passed: [1, 2, 3, 2] -> 12 subsets")

    # Test case 4: No duplicates behaves like a normal power set
    result4 = solution.generate_power_set_with_duplicates([3, 1, 2])
    assert len(result4) == 8 and normalize(result4) == expected([3, 1, 2])
    print("✓ Test 4 passed: [3, 1, 2] -> 8 subsets")

    # Test case 5: Many repeats: (3 + 1) * (2 + 1) * (1 + 1) = 24
    data5 = [7, -1, 7, 0, -1, 7]
    result5 = solution.generate_power_set_with_duplicates(data5)
    assert len(result5) == 24 and normalize(result5) == expected(data5)
    print("✓ Test 5 passed: [7, -1, 7, 0, -1, 7] -> 24 subsets")

    # Test case 6: Same value repeated five times -> 6 subsets
    result6 = solution.generate_power_set_with_duplicates([2] * 5)
    assert normalize(result6) == [tuple([2] * k) for k in range(6)] and len(result6) == 6
    print("✓ Test 6 passed: [2] * 5 -> 6 subsets")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_generate_power_set_with_duplicates()
