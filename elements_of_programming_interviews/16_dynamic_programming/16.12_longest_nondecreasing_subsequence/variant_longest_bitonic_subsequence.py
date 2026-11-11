"""
EPI 16.12 Variant - Longest Bitonic Subsequence

Problem:
A sequence (a0, ..., a_{k-1}) is bitonic if it strictly increases up to some
position and strictly decreases after it (either part may be empty, so
purely increasing or purely decreasing sequences count). Given an array A,
return the indices (i0 < i1 < ... < i_{k-1}) of a longest subsequence whose
values are bitonic. Any longest answer is accepted.

Constraints:
- 0 <= len(A) <= 2000
- O(n^2) time

How it works (two LIS passes):
1. inc[i] = longest strictly increasing subsequence ending at i
   (left-to-right pass)
2. dec[i] = longest strictly decreasing subsequence starting at i
   (right-to-left pass)
3. The peak k maximizes inc[k] + dec[k] - 1
4. Rebuild both halves with predecessor links and join them at the peak

Example 1:
Input: A = [1, 11, 2, 10, 4, 5, 2, 1]
Output: [0, 2, 4, 5, 6, 7]
Explanation: 1 < 2 < 4 < 5 > 2 > 1

Example 2:
Input: A = [3, 2, 1]
Output: [0, 1, 2]
"""

from typing import List


class Solution:
    def longest_bitonic_subsequence(self, A: List[int]) -> List[int]:
        """
        Finds the indices of a longest bitonic subsequence.

        Args:
            A: Input numbers

        Returns:
            Increasing list of indices whose values rise then fall

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        # TODO: Implement longest bitonic subsequence
        pass


def is_bitonic(values: List[int]) -> bool:
    """Strictly increasing, then strictly decreasing."""
    k = 0
    while k + 1 < len(values) and values[k] < values[k + 1]:
        k += 1
    return all(values[i] > values[i + 1] for i in range(k, len(values) - 1))


def is_valid_answer(indices, A: List[int], expected_length: int) -> bool:
    """Checks the indices are increasing, in range, bitonic, and optimal."""
    return (
        isinstance(indices, list)
        and len(indices) == expected_length
        and all(0 <= i < len(A) for i in indices)
        and all(a < b for a, b in zip(indices, indices[1:]))
        and is_bitonic([A[i] for i in indices])
    )


def test_longest_bitonic_subsequence():
    """Test cases for longest bitonic subsequence"""
    solution = Solution()

    cases = [
        ([1, 11, 2, 10, 4, 5, 2, 1], 6),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9], 6),
        ([1, 2, 3], 3),
        ([3, 2, 1], 3),
        ([2, 2, 2], 1),
        ([7], 1),
        ([], 0),
    ]
    for n, (A, expected) in enumerate(cases, 1):
        result = solution.longest_bitonic_subsequence(A)
        assert is_valid_answer(result, A, expected)
        print(f"✓ Test {n} passed: {A} -> length {expected}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_bitonic_subsequence()
