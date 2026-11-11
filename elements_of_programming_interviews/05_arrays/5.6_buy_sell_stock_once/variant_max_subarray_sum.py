"""
EPI 5.6 Extra Variant - Maximum Subarray Sum
(Practice problem, not in the book. Difficulty: Medium)
Builds on: buy low, sell high in one pass. The sum of A[i:j] is
P[j] - P[i] for prefix sums P, so the best subarray is the best "trade"
on the prefix-sum sequence.

Problem:
Given a non-empty array of integers, return the largest sum of a
non-empty contiguous subarray. If every value is negative, the answer is
the largest single value (you must pick at least one element).

Constraints:
- 1 <= len(A) <= 10^5; -10^4 <= A[i] <= 10^4
- Must run in O(n) time and O(1) extra space

How it works (track the smallest prefix sum seen so far):
1. prefix = 0, min_prefix = 0, best = -infinity
2. For each x in A:
   - prefix += x
   - best = max(best, prefix - min_prefix)  (sell today, bought at the
     cheapest earlier prefix)
   - min_prefix = min(min_prefix, prefix)
3. Return best
(Equivalently, Kadane: current = max(x, current + x); best = max(best,
current).)

Example 1:
Input: A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] sums to 6.

Example 2:
Input: A = [-3, -1, -2]
Output: -1
Explanation: Every subarray is negative; [-1] is the least negative.
"""

from typing import List


class Solution:
    def max_subarray_sum(self, A: List[int]) -> int:
        """
        Finds the largest sum of a non-empty contiguous subarray.

        Args:
            A: Non-empty list of integers

        Returns:
            The maximum subarray sum

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement maximum subarray sum
        pass


def test_max_subarray_sum():
    """Test cases for maximum subarray sum"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("✓ Test 1 passed: Classic example -> 6")

    # Test case 2: All negative
    assert solution.max_subarray_sum([-3, -1, -2]) == -1
    print("✓ Test 2 passed: All negative -> -1")

    # Test case 3: Single element
    assert solution.max_subarray_sum([5]) == 5
    assert solution.max_subarray_sum([-7]) == -7
    print("✓ Test 3 passed: Single element")

    # Test case 4: All positive takes the whole array
    assert solution.max_subarray_sum([1, 2, 3, 4]) == 10
    print("✓ Test 4 passed: All positive -> 10")

    # Test case 5: A dip worth crossing vs one that is not
    assert solution.max_subarray_sum([5, -2, 5]) == 8
    assert solution.max_subarray_sum([5, -6, 5]) == 5
    assert solution.max_subarray_sum([0, -1, 0]) == 0
    print("✓ Test 5 passed: Crossing dips")

    # Test case 6: Large alternating input
    A = [10000 if i % 2 == 0 else -9999 for i in range(100001)]
    assert solution.max_subarray_sum(A) == 10000 + 50000 * 1
    print("✓ Test 6 passed: 100,001 alternating values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_subarray_sum()
