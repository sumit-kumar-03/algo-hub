"""
EPI 15.4 - Generate the Power Set

Problem:
Given a set of distinct integers (as a list), return its power set: every
subset, from the empty set up to the whole set. Each subset must appear
exactly once. Neither the order of the subsets nor the order of elements
inside a subset matters.

Constraints:
- 0 <= len(S) <= 16
- All entries are distinct
- There are 2^n subsets, so O(n * 2^n) time is optimal

How it works (include / exclude recursion):
1. helper(i, chosen): decide for element S[i] whether it is in the subset
2. If i == n, record a copy of `chosen`
3. Otherwise recurse once without S[i] and once with S[i] appended
Alternative: loop over every integer mask in [0, 2^n) and take the
elements whose bits are set.

Example 1:
Input: S = [0, 1, 2]
Output: [[], [0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
(any order)

Example 2:
Input: S = []
Output: [[]]
Explanation: The empty set has exactly one subset, itself.
"""

from typing import List


class Solution:
    def generate_power_set(self, S: List[int]) -> List[List[int]]:
        """
        Generates all subsets of a set of distinct integers.

        Args:
            S: List of distinct integers

        Returns:
            List of all 2^n subsets, in any order

        Time Complexity: O(n * 2^n)
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement power set generation
        pass


def normalize(subsets: List[List[int]]) -> List[tuple]:
    """Sorts each subset and the list of subsets for order-free comparison."""
    return sorted(tuple(sorted(s)) for s in subsets)


def test_generate_power_set():
    """Test cases for power set generation"""
    import itertools

    solution = Solution()

    def expected(S: List[int]) -> List[tuple]:
        return sorted(
            tuple(sorted(c)) for r in range(len(S) + 1) for c in itertools.combinations(S, r)
        )

    # Test case 1: Empty set
    assert normalize(solution.generate_power_set([])) == [()]
    print("✓ Test 1 passed: [] -> [[]]")

    # Test case 2: Single element
    assert normalize(solution.generate_power_set([5])) == [(), (5,)]
    print("✓ Test 2 passed: [5] -> [[], [5]]")

    # Test case 3: Book example
    result3 = solution.generate_power_set([0, 1, 2])
    assert len(result3) == 8 and normalize(result3) == expected([0, 1, 2])
    print("✓ Test 3 passed: [0, 1, 2] -> 8 subsets")

    # Test case 4: Unsorted values with negatives
    data4 = [9, -3, 4, 0]
    result4 = solution.generate_power_set(data4)
    assert len(result4) == 16 and normalize(result4) == expected(data4)
    print("✓ Test 4 passed: [9, -3, 4, 0] -> 16 subsets")

    # Test case 5: Ten elements -> 1024 distinct subsets
    data5 = list(range(10))
    result5 = solution.generate_power_set(data5)
    assert len(result5) == 1024 and normalize(result5) == expected(data5)
    print("✓ Test 5 passed: 10 elements -> 1024 subsets")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_generate_power_set()
