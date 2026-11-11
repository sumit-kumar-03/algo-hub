"""
EPI 16.12 Variant - Longest Convex Subsequence

Problem:
A sequence (a0, ..., a_{k-1}) is convex if every interior term is below the
average of its neighbors: a_i < (a_{i-1} + a_{i+1}) / 2 for 1 <= i <= k - 2.
Any sequence of length 1 or 2 is convex. Given an array A of integers,
return the indices (i0 < i1 < ... < i_{k-1}) of a longest subsequence whose
values are convex. Any longest answer is accepted.

Constraints:
- 0 <= len(A) <= 300
- O(n^3) time (DP over pairs of last two indices)

How it works (DP on the last two indices):
1. best[j][i] = longest convex subsequence whose last two indices are j < i
   (at least 2)
2. best[j][i] = max(2, best[k][j] + 1 for k < j with
   2 * A[j] < A[k] + A[i])
3. Track predecessors, take the best pair, and rebuild

Example 1:
Input: A = [5, 3, 2, 3, 5]
Output: [0, 1, 2, 3, 4]
Explanation: Each interior value sits below the average of its neighbors.

Example 2:
Input: A = [1, 2, 3, 4]
Output: [0, 1, 3] (or another 3-index answer)
Explanation: A straight line is not strictly convex, so no 4-term answer.
"""

from typing import List


class Solution:
    def longest_convex_subsequence(self, A: List[int]) -> List[int]:
        """
        Finds the indices of a longest convex subsequence.

        Args:
            A: Input integers

        Returns:
            Increasing list of indices whose values form a convex sequence

        Time Complexity: O(n^3)
        Space Complexity: O(n^2)
        """
        # TODO: Implement longest convex subsequence DP
        pass


def is_convex(values: List[int]) -> bool:
    """Every interior term is strictly below the average of its neighbors."""
    return all(2 * values[i] < values[i - 1] + values[i + 1] for i in range(1, len(values) - 1))


def is_valid_answer(indices, A: List[int], expected_length: int) -> bool:
    """Checks the indices are increasing, in range, convex, and optimal."""
    return (
        isinstance(indices, list)
        and len(indices) == expected_length
        and all(0 <= i < len(A) for i in indices)
        and all(a < b for a, b in zip(indices, indices[1:]))
        and is_convex([A[i] for i in indices])
    )


def test_longest_convex_subsequence():
    """Test cases for longest convex subsequence"""
    solution = Solution()

    cases = [
        ([5, 3, 2, 3, 5], 5),
        ([1, 2, 3, 4], 3),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9], 5),
        ([10, 1, 9, 2, 8, 4, 7], 5),
        ([4], 1),
        ([], 0),
    ]
    for n, (A, expected) in enumerate(cases, 1):
        result = solution.longest_convex_subsequence(A)
        assert is_valid_answer(result, A, expected)
        print(f"✓ Test {n} passed: {A} -> length {expected}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_convex_subsequence()
