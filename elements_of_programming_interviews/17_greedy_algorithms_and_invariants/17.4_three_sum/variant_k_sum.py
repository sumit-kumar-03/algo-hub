"""
EPI 17.4 Variant - The k-Sum Problem

Problem:
Generalize 3-sum: given an array, a target t, and a count k >= 1, decide
whether some k entries of the array add up to t. As in the main problem,
the same entry may be used more than once.

Constraints:
- 0 <= len(A) <= 100, 1 <= k <= 10
- O(n^(k-1)) time with sorting + two pointers at the innermost level
  (k = 1 is a lookup, k = 2 is two pointers)

How it works (recursion that peels off one element at a time):
1. Sort A (duplicates can be dropped since reuse is allowed)
2. k_sum(start, target, k):
   - k == 1: is target in A[start:]?
   - k == 2: two pointers on A[start:], repeats allowed
   - otherwise try each A[i] (i >= start) as the smallest element and
     recurse with k_sum(i, target - A[i], k - 1)
   Starting from i rather than 0 avoids re-checking permutations

Example 1:
Input: A = [11, 2, 5, 7, 3], t = 21, k = 3
Output: True

Example 2:
Input: A = [2, 7], t = 18, k = 4
Output: True
Explanation: 2 + 2 + 7 + 7
"""

from typing import List


class Solution:
    def has_k_sum(self, A: List[int], t: int, k: int) -> bool:
        """
        Checks whether k entries (repeats allowed) sum to t.

        Args:
            A: Input integers
            t: Target sum
            k: Number of entries to add (k >= 1)

        Returns:
            True if such entries exist, False otherwise

        Time Complexity: O(n^(k-1)) for k >= 2
        Space Complexity: O(k) recursion depth beyond sorting
        """
        # TODO: Implement k-sum
        pass


def test_has_k_sum():
    """Test cases for the k-sum problem"""
    solution = Solution()

    # Test case 1: k = 3 matches 3-sum
    assert solution.has_k_sum([11, 2, 5, 7, 3], 21, 3) is True
    print("✓ Test 1 passed: [11, 2, 5, 7, 3], 21, k=3 -> True")

    # Test case 2: k = 3, not reachable
    assert solution.has_k_sum([11, 2, 5, 7, 3], 22, 3) is False
    print("✓ Test 2 passed: [11, 2, 5, 7, 3], 22, k=3 -> False")

    # Test case 3: k = 1 is membership
    assert solution.has_k_sum([3, 5], 5, 1) is True
    assert solution.has_k_sum([3, 5], 1, 1) is False
    print("✓ Test 3 passed: k=1 membership")

    # Test case 4: Reuse with k = 3
    assert solution.has_k_sum([3, 5], 11, 3) is True
    print("✓ Test 4 passed: [3, 5], 11, k=3 -> True")

    # Test case 5: k = 4 with reuse
    assert solution.has_k_sum([2, 7], 18, 4) is True
    print("✓ Test 5 passed: [2, 7], 18, k=4 -> True")

    # Test case 6: k = 4, no combination
    assert solution.has_k_sum([2, 7], 17, 4) is False
    print("✓ Test 6 passed: [2, 7], 17, k=4 -> False")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_has_k_sum()
