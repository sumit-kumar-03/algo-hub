"""
EPI 16.12 Variant - Longest Alternating Subsequence

Problem:
A sequence (a0, a1, ..., a_{k-1}) is alternating if a_i < a_{i+1} for even
i and a_i > a_{i+1} for odd i, i.e. it starts by going up and then zigzags:
a0 < a1 > a2 < a3 > ... Given an array A, return the indices
(i0 < i1 < ... < i_{k-1}) of a longest subsequence whose values are
alternating. Any longest answer is accepted.

Constraints:
- 0 <= len(A) <= 2000
- O(n^2) time

How it works (DP on the last index and position parity):
1. best[i][p] = longest alternating subsequence ending at index i whose
   length has parity p (the parity tells whether the next step goes up
   or down)
2. Extend from every j < i: if the last position of the path ending at j is
   even, A[j] < A[i] is required; if odd, A[j] > A[i]
3. Track predecessors and rebuild the overall longest

Example 1:
Input: A = [1, 5, 4]
Output: [0, 1, 2]
Explanation: 1 < 5 > 4

Example 2:
Input: A = [5, 4, 3, 2, 1]
Output: [0] (any single index)
Explanation: The first step must go up, which never happens.
"""

from typing import List


class Solution:
    def longest_alternating_subsequence(self, A: List[int]) -> List[int]:
        """
        Finds the indices of a longest alternating subsequence.

        Args:
            A: Input numbers

        Returns:
            Increasing list of indices whose values alternate up/down

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        # TODO: Implement longest alternating subsequence DP
        pass


def is_alternating(values: List[int]) -> bool:
    """a0 < a1 > a2 < a3 > ..."""
    return all(
        values[i] < values[i + 1] if i % 2 == 0 else values[i] > values[i + 1]
        for i in range(len(values) - 1)
    )


def is_valid_answer(indices, A: List[int], expected_length: int) -> bool:
    """Checks the indices are increasing, in range, alternating, and optimal."""
    return (
        isinstance(indices, list)
        and len(indices) == expected_length
        and all(0 <= i < len(A) for i in indices)
        and all(a < b for a, b in zip(indices, indices[1:]))
        and is_alternating([A[i] for i in indices])
    )


def test_longest_alternating_subsequence():
    """Test cases for longest alternating subsequence"""
    solution = Solution()

    cases = [
        ([1, 5, 4], 3),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9], 10),
        ([1, 2, 3, 4, 5], 2),
        ([5, 4, 3, 2, 1], 1),
        ([3, 1, 4, 1, 5, 9, 2, 6], 6),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
        ([], 0),
    ]
    for n, (A, expected) in enumerate(cases, 1):
        result = solution.longest_alternating_subsequence(A)
        assert is_valid_answer(result, A, expected)
        print(f"✓ Test {n} passed: {A} -> length {expected}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_alternating_subsequence()
