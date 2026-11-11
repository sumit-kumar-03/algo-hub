"""
EPI 17.7 - Compute the Maximum Water Trapped by a Pair of Vertical Lines

Problem:
Entry A[i] is the height of a vertical line drawn at x = i. Any two lines
i < j, together with the x-axis, form a container holding
(j - i) * min(A[i], A[j]) units of water. Return the largest amount of
water any pair of lines can hold (0 if there are fewer than two lines).

Constraints:
- 0 <= len(A) <= 10^5, 0 <= A[i] <= 10^4
- O(n) time, O(1) space

How it works (two pointers moving inward):
1. i = 0, j = n - 1, best = 0
2. While i < j:
   - best = max(best, (j - i) * min(A[i], A[j]))
   - Move the shorter line inward (if A[i] < A[j]: i += 1, else j -= 1).
     The shorter line can never do better with a narrower partner, so it
     can be discarded.
3. Return best

Example 1:
Input: A = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
Output: 48
Explanation: Lines 4 and 16 (both height 4) are 12 apart: 12 * 4 = 48.

Example 2:
Input: A = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
"""

from typing import List


class Solution:
    def get_max_trapped_water(self, A: List[int]) -> int:
        """
        Computes the most water trapped between two vertical lines.

        Args:
            A: Heights of the vertical lines

        Returns:
            Maximum water held by any pair of lines

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement two-pointer max water
        pass


def test_get_max_trapped_water():
    """Test cases for maximum trapped water"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.get_max_trapped_water([1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]) == 48
    print("✓ Test 1 passed: book example -> 48")

    # Test case 2: Classic example
    assert solution.get_max_trapped_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("✓ Test 2 passed: [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49")

    # Test case 3: Two lines
    assert solution.get_max_trapped_water([1, 1]) == 1
    print("✓ Test 3 passed: [1, 1] -> 1")

    # Test case 4: Single line holds nothing
    assert solution.get_max_trapped_water([5]) == 0
    print("✓ Test 4 passed: [5] -> 0")

    # Test case 5: Widest pair is best
    assert solution.get_max_trapped_water([4, 3, 2, 1, 4]) == 16
    print("✓ Test 5 passed: [4, 3, 2, 1, 4] -> 16")

    # Test case 6: Tall middle line does not help
    assert solution.get_max_trapped_water([1, 2, 1]) == 2
    print("✓ Test 6 passed: [1, 2, 1] -> 2")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_get_max_trapped_water()
