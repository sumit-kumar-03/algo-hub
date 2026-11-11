"""
EPI 16.12 - Find the Longest Nondecreasing Subsequence

Problem:
Given an array of numbers, return the length of a longest subsequence whose
elements never decrease from left to right. A subsequence keeps the
original order but its elements need not be adjacent.

Constraints:
- 0 <= len(A) <= 10^4
- O(n^2) time with the basic DP (O(n log n) is possible)

How it works (DP on the last element):
1. L[i] = length of the longest nondecreasing subsequence ending at A[i]
2. L[i] = 1 + max(L[j] for j < i with A[j] <= A[i]), or 1 if there is no
   such j
3. Return max(L), or 0 for an empty array
(Faster: keep tails[k] = smallest possible last value of a nondecreasing
subsequence of length k + 1 and binary search with bisect_right.)

Example 1:
Input: A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
Output: 4
Explanation: e.g. [0, 4, 10, 14] or [0, 2, 6, 9]

Example 2:
Input: A = [3, 3, 3]
Output: 3
Explanation: Equal values are allowed (nondecreasing, not increasing).
"""

from typing import List


class Solution:
    def longest_nondecreasing_subsequence_length(self, A: List[int]) -> int:
        """
        Computes the length of a longest nondecreasing subsequence.

        Args:
            A: Input numbers

        Returns:
            Length of a longest nondecreasing subsequence

        Time Complexity: O(n^2) (O(n log n) with patience sorting)
        Space Complexity: O(n)
        """
        # TODO: Implement longest nondecreasing subsequence DP
        pass


def test_longest_nondecreasing_subsequence_length():
    """Test cases for longest nondecreasing subsequence"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.longest_nondecreasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]) == 4
    print("✓ Test 1 passed: book example -> 4")

    # Test case 2: Empty array
    assert solution.longest_nondecreasing_subsequence_length([]) == 0
    print("✓ Test 2 passed: [] -> 0")

    # Test case 3: Single element
    assert solution.longest_nondecreasing_subsequence_length([5]) == 1
    print("✓ Test 3 passed: [5] -> 1")

    # Test case 4: Duplicates count
    assert solution.longest_nondecreasing_subsequence_length([3, 3, 3]) == 3
    print("✓ Test 4 passed: [3, 3, 3] -> 3")

    # Test case 5: Strictly decreasing
    assert solution.longest_nondecreasing_subsequence_length([5, 4, 3, 2, 1]) == 1
    print("✓ Test 5 passed: decreasing -> 1")

    # Test case 6: Mixed with duplicates
    assert solution.longest_nondecreasing_subsequence_length([1, 3, 2, 2, 4, 1, 5]) == 5
    print("✓ Test 6 passed: [1, 3, 2, 2, 4, 1, 5] -> 5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_nondecreasing_subsequence_length()
