"""
EPI 5.18 - Compute the Spiral Ordering of a 2D Array

Problem:
Given an n x n 2D array, return its entries in spiral order: start at the
top-left corner, go right along the first row, down the last column, left
along the bottom row, up the first column, then repeat on the next inner
layer until every entry has been visited.

Constraints:
- 0 <= n <= 1000 (an empty matrix gives an empty list)
- Must run in O(n^2) time

How it works (peel off layers):
1. For each layer offset from 0 to ceil(n / 2) - 1:
   - Top row: left to right (excluding the last column)
   - Right column: top to bottom (excluding the last row)
   - Bottom row: right to left (excluding the first column)
   - Left column: bottom to top (excluding the first row)
2. If n is odd, the center element is a layer of its own; add it last

Example 1:
Input: [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Explanation: Outer ring clockwise, then the center.

Example 2:
Input: [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation: Outer ring of 12 entries, then the inner 2 x 2 ring.
"""

from typing import List


class Solution:
    def matrix_in_spiral_order(self, square_matrix: List[List[int]]) -> List[int]:
        """
        Lists the entries of a square matrix in clockwise spiral order.

        Args:
            square_matrix: n x n 2D array

        Returns:
            The n^2 entries in spiral order

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement spiral ordering
        pass


def test_matrix_in_spiral_order():
    """Test cases for spiral ordering"""
    solution = Solution()

    # Test case 1: 3 x 3 (book example)
    m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution.matrix_in_spiral_order(m3) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print("✓ Test 1 passed: 3 x 3")

    # Test case 2: 4 x 4 (book example)
    m4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert solution.matrix_in_spiral_order(m4) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print("✓ Test 2 passed: 4 x 4")

    # Test case 3: 1 x 1
    assert solution.matrix_in_spiral_order([[7]]) == [7]
    print("✓ Test 3 passed: 1 x 1")

    # Test case 4: Empty matrix
    assert solution.matrix_in_spiral_order([]) == []
    print("✓ Test 4 passed: Empty matrix")

    # Test case 5: 2 x 2
    assert solution.matrix_in_spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    print("✓ Test 5 passed: 2 x 2")

    # Test case 6: 5 x 5 (odd size, multiple layers)
    m5 = [[5 * r + c + 1 for c in range(5)] for r in range(5)]
    expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6,
                7, 8, 9, 14, 19, 18, 17, 12, 13]
    assert solution.matrix_in_spiral_order(m5) == expected
    print("✓ Test 6 passed: 5 x 5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_matrix_in_spiral_order()
