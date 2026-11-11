"""
EPI 5.18 Extra Variant - Counterclockwise Spiral Ordering
(Practice problem, not in the book. Difficulty: Easy)
Builds on: peeling an m x n array one boundary layer at a time with four
shrinking bounds.

Problem:
Given an m x n 2D array (not necessarily square), return its entries in
counterclockwise spiral order: start at the top-left corner, go down the
first column, right along the bottom row, up the last column, left along
the top row, then repeat on the next inner layer until every entry has
been visited exactly once.

Constraints:
- 0 <= m, n <= 1000 (an empty matrix gives an empty list)
- Must run in O(m * n) time, O(1) extra space beyond the output

How it works (shrinking boundaries, rotated direction order):
1. top = 0, bottom = m - 1, left = 0, right = n - 1
2. While top <= bottom and left <= right:
   - Left column top to bottom; then left += 1
   - Bottom row left to right (if left <= right); then bottom -= 1
   - Right column bottom to top (if top <= bottom and left <= right);
     then right -= 1
   - Top row right to left (if left <= right and top <= bottom);
     then top += 1
3. The guards stop a single leftover row or column from being read twice

Example 1:
Input: [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
Output: [1, 4, 7, 8, 9, 6, 3, 2, 5]
Explanation: Down, right, up, left around the edge, then the center.

Example 2:
Input: [[1, 2, 3, 4],
        [5, 6, 7, 8]]
Output: [1, 5, 6, 7, 8, 4, 3, 2]
"""

from typing import List


class Solution:
    def counterclockwise_spiral(self, matrix: List[List[int]]) -> List[int]:
        """
        Lists the entries of an m x n matrix in counterclockwise spiral order.

        Args:
            matrix: m x n 2D array

        Returns:
            The m * n entries in counterclockwise spiral order

        Time Complexity: O(m * n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement counterclockwise spiral ordering
        pass


def make_matrix(m: int, n: int) -> List[List[int]]:
    """Builds an m x n matrix holding 1..m*n in row-major order."""
    return [[n * i + j + 1 for j in range(n)] for i in range(m)]


def test_counterclockwise_spiral():
    """Test cases for counterclockwise spiral ordering"""
    solution = Solution()

    # Test case 1: 3 x 3
    assert solution.counterclockwise_spiral(make_matrix(3, 3)) == [1, 4, 7, 8, 9, 6, 3, 2, 5]
    print("✓ Test 1 passed: 3 x 3")

    # Test case 2: Wide 2 x 4
    assert solution.counterclockwise_spiral(make_matrix(2, 4)) == [1, 5, 6, 7, 8, 4, 3, 2]
    print("✓ Test 2 passed: 2 x 4")

    # Test case 3: 4 x 4 with an inner ring
    expected = [1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2, 6, 10, 11, 7]
    assert solution.counterclockwise_spiral(make_matrix(4, 4)) == expected
    print("✓ Test 3 passed: 4 x 4")

    # Test case 4: Single row, single column, single cell, empty
    assert solution.counterclockwise_spiral(make_matrix(1, 4)) == [1, 2, 3, 4]
    assert solution.counterclockwise_spiral(make_matrix(3, 1)) == [1, 2, 3]
    assert solution.counterclockwise_spiral([[7]]) == [7]
    assert solution.counterclockwise_spiral([]) == []
    print("✓ Test 4 passed: 1 x 4, 3 x 1, 1 x 1, empty")

    # Test case 5: Tall 5 x 3 (inner layer is a single column)
    expected = [1, 4, 7, 10, 13, 14, 15, 12, 9, 6, 3, 2, 5, 8, 11]
    assert solution.counterclockwise_spiral(make_matrix(5, 3)) == expected
    print("✓ Test 5 passed: 5 x 3")

    # Test case 6: Wide 3 x 5 (inner layer is a single row)
    expected = [1, 6, 11, 12, 13, 14, 15, 10, 5, 4, 3, 2, 7, 8, 9]
    assert solution.counterclockwise_spiral(make_matrix(3, 5)) == expected
    print("✓ Test 6 passed: 3 x 5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_counterclockwise_spiral()
