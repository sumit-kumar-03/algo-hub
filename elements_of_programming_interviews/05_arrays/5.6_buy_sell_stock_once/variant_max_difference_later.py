"""
EPI 5.6 Extra Variant - Maximum Difference with a Forced Trade
(Practice problem, not in the book. Difficulty: Easy)
Builds on: a single left-to-right pass that remembers the smallest value
seen so far.

Problem:
Given an array A of at least two integers, return the largest value of
A[j] - A[i] over all index pairs with i < j (strictly). Unlike the stock
problem, you must pick a pair: if the array only goes down, the answer is
negative (the least bad drop), and buying and selling on the same day is
not allowed.

Constraints:
- 2 <= len(A) <= 10^5; values may be negative
- Must run in O(n) time and O(1) extra space

How it works:
1. min_so_far = A[0], best = A[1] - A[0]
2. For j from 1 to n - 1:
   - best = max(best, A[j] - min_so_far)  (min_so_far covers only i < j)
   - min_so_far = min(min_so_far, A[j])
3. Return best

Example 1:
Input: A = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: A[4] - A[1] = 6 - 1.

Example 2:
Input: A = [5, 4, 3, 2]
Output: -1
Explanation: Every pair goes down; the smallest drop is 1.
"""

from typing import List


class Solution:
    def max_difference(self, A: List[int]) -> int:
        """
        Finds the maximum of A[j] - A[i] over i < j.

        Args:
            A: List of at least two integers

        Returns:
            The largest later-minus-earlier difference (may be negative)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement maximum difference with i < j
        pass


def test_max_difference():
    """Test cases for maximum difference with a forced trade"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.max_difference([7, 1, 5, 3, 6, 4]) == 5
    print("✓ Test 1 passed: [7, 1, 5, 3, 6, 4] -> 5")

    # Test case 2: Strictly decreasing gives a negative answer
    assert solution.max_difference([5, 4, 3, 2]) == -1
    assert solution.max_difference([10, 1]) == -9
    print("✓ Test 2 passed: Decreasing -> -1, [10, 1] -> -9")

    # Test case 3: Two elements and equal values
    assert solution.max_difference([1, 2]) == 1
    assert solution.max_difference([3, 3, 3]) == 0
    print("✓ Test 3 passed: [1, 2] -> 1, [3, 3, 3] -> 0")

    # Test case 4: Negatives; the best pair is not the global min/max
    assert solution.max_difference([10, -5, 3]) == 8
    assert solution.max_difference([9, 11, 8, 5, 7, 10]) == 5
    print("✓ Test 4 passed: Negatives and interior pairs")

    # Test case 5: The global minimum is last and must not be used as i
    assert solution.max_difference([4, 6, 1]) == 2
    print("✓ Test 5 passed: [4, 6, 1] -> 2")

    # Test case 6: Large decreasing input
    A = list(range(100000, 0, -1))
    assert solution.max_difference(A) == -1
    A = list(range(100000, 0, -2))
    assert solution.max_difference(A) == -2
    print("✓ Test 6 passed: 100,000 decreasing values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_difference()
