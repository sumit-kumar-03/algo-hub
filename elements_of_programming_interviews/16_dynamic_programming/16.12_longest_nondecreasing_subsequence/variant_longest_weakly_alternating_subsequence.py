"""
EPI 16.12 Variant - Longest Weakly Alternating Subsequence

Problem:
A sequence is weakly alternating if no three consecutive terms are strictly
increasing or strictly decreasing (the sequence keeps changing direction,
starting either up or down). Given an array A of distinct numbers, return
the indices (i0 < i1 < ... < i_{k-1}) of a longest subsequence whose values
are weakly alternating. Any longest answer is accepted.

Constraints:
- 0 <= len(A) <= 2000, values are distinct
- O(n^2) time (an O(n) greedy also exists)

How it works (DP on the last index and last direction):
1. up[i] / down[i] = longest weakly alternating subsequence ending at i whose
   last step went up / down (a single element counts as length 1 for both)
2. For j < i: if A[j] < A[i], up[i] = max(up[i], down[j] + 1);
   if A[j] > A[i], down[i] = max(down[i], up[j] + 1)
3. Keep predecessors and rebuild the overall longest

Example 1:
Input: A = [1, 7, 4, 9, 2, 5]
Output: [0, 1, 2, 3, 4, 5]
Explanation: 1 < 7 > 4 < 9 > 2 < 5 already zigzags.

Example 2:
Input: A = [1, 2, 3, 4, 5]
Output: [0, 4] (any two indices)
"""

from typing import List


class Solution:
    def longest_weakly_alternating_subsequence(self, A: List[int]) -> List[int]:
        """
        Finds the indices of a longest weakly alternating subsequence.

        Args:
            A: Input numbers (distinct)

        Returns:
            Increasing list of indices whose values never have three
            consecutive increasing or decreasing terms

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        # TODO: Implement longest weakly alternating subsequence DP
        pass


def is_weakly_alternating(values: List[int]) -> bool:
    """No three consecutive terms strictly increasing or strictly decreasing."""
    return all(
        not (values[i] < values[i + 1] < values[i + 2])
        and not (values[i] > values[i + 1] > values[i + 2])
        for i in range(len(values) - 2)
    )


def is_valid_answer(indices, A: List[int], expected_length: int) -> bool:
    """Checks the indices are increasing, in range, weakly alternating, optimal."""
    return (
        isinstance(indices, list)
        and len(indices) == expected_length
        and all(0 <= i < len(A) for i in indices)
        and all(a < b for a, b in zip(indices, indices[1:]))
        and is_weakly_alternating([A[i] for i in indices])
    )


def test_longest_weakly_alternating_subsequence():
    """Test cases for longest weakly alternating subsequence"""
    solution = Solution()

    cases = [
        ([1, 7, 4, 9, 2, 5], 6),
        ([1, 2, 3, 4, 5], 2),
        ([1, 5, 4, 9, 2], 5),
        ([1, 17, 5, 10, 13, 15, 11, 6, 16, 8], 7),
        ([3], 1),
        ([], 0),
    ]
    for n, (A, expected) in enumerate(cases, 1):
        result = solution.longest_weakly_alternating_subsequence(A)
        assert is_valid_answer(result, A, expected)
        print(f"✓ Test {n} passed: {A} -> length {expected}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_weakly_alternating_subsequence()
