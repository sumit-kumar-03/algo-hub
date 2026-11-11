"""
EPI 13.2 Extra Variant - Sorted Squares of a Sorted Array
(Practice problem, not in the book. Difficulty: Easy)
Builds on: filling the output from the back by repeatedly taking the
larger of two candidates, exactly as in the in-place merge.

Problem:
Given an integer array A sorted in ascending order (it may contain negative
numbers), return a new array of the squares of its entries, also sorted in
ascending order.

Constraints:
- 0 <= len(A) <= 10^5
- -10^4 <= A[i] <= 10^4
- O(n) time; squaring and then sorting is O(n log n) and misses the point

How it works (two ends, fill from the back):
1. The largest square comes from one of the two ends of A (the most
   negative or the most positive entry)
2. Keep left = 0, right = n - 1 and write = n - 1
3. Write the larger of A[left]^2 and A[right]^2 into result[write], move
   that end inward, and step write left
4. The negative part and the positive part of A are each sorted runs of
   squares, so this is really a merge of two sorted sequences

Example 1:
Input: A = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Example 2:
Input: A = [-5, -2, -1]
Output: [1, 4, 25]
"""

from typing import List


class Solution:
    def sorted_squares(self, A: List[int]) -> List[int]:
        """
        Returns the squares of a sorted array in sorted order.

        Args:
            A: Array sorted in ascending order

        Returns:
            New list of the squared values in ascending order

        Time Complexity: O(n)
        Space Complexity: O(1) extra, excluding the output
        """
        # TODO: Implement two-pointer sorted squares
        pass


def test_sorted_squares():
    """Test cases for sorted squares"""
    solution = Solution()

    # Test case 1: Mixed signs
    assert solution.sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    print("✓ Test 1 passed: [-7, -3, 2, 3, 11] -> [4, 9, 9, 49, 121]")

    # Test case 2: All negative
    assert solution.sorted_squares([-5, -2, -1]) == [1, 4, 25]
    print("✓ Test 2 passed: All negative")

    # Test case 3: All nonnegative
    assert solution.sorted_squares([0, 1, 4]) == [0, 1, 16]
    print("✓ Test 3 passed: All nonnegative")

    # Test case 4: Empty and single
    assert solution.sorted_squares([]) == []
    assert solution.sorted_squares([-3]) == [9]
    print("✓ Test 4 passed: Empty / single")

    # Test case 5: Symmetric values give duplicate squares
    assert solution.sorted_squares([-2, -2, 0, 2, 2]) == [0, 4, 4, 4, 4]
    print("✓ Test 5 passed: Symmetric duplicates")

    # Test case 6: Extremes
    assert solution.sorted_squares([-10000, 10000]) == [10**8, 10**8]
    print("✓ Test 6 passed: Extremes")

    # Test case 7: Larger input versus sort
    A = sorted((i * 37) % 201 - 100 for i in range(150))
    assert solution.sorted_squares(A) == sorted(x * x for x in A)
    print("✓ Test 7 passed: Matches sorted(x * x)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_sorted_squares()
