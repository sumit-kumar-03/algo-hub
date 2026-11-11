"""
EPI 5.18 Variant - Spiral Ordering of an m x n 2D Array

Problem:
Given an m x n 2D array (not necessarily square), return its entries in
clockwise spiral order, starting at the top-left corner.

Constraints:
- 0 <= m, n <= 1000 (an empty matrix gives an empty list)
- Must run in O(m * n) time

How it works (shrinking boundaries):
1. Keep top, bottom, left, right boundaries
2. While top <= bottom and left <= right:
   - Read the top row left to right; then the right column downward
   - If top < bottom, read the bottom row right to left
   - If left < right, read the left column upward
   - Move every boundary one step inward
3. The two guards stop a single remaining row or column from being read
   twice

Example 1:
Input: [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
Explanation: The last layer is the single row [6, 7].

Example 2:
Input: [[1], [2], [3]]
Output: [1, 2, 3]
Explanation: A single column is read top to bottom.
"""

from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Lists the entries of an m x n matrix in clockwise spiral order.

        Args:
            matrix: m x n 2D array

        Returns:
            The m * n entries in spiral order

        Time Complexity: O(m * n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement spiral ordering for rectangular matrices
        pass


def make_matrix(m: int, n: int) -> List[List[int]]:
    """Builds an m x n matrix holding 1..m*n in row-major order."""
    return [[n * i + j + 1 for j in range(n)] for i in range(m)]


def test_spiral_order():
    """Test cases for rectangular spiral ordering"""
    solution = Solution()

    # Test case 1: Wide matrix (3 x 4)
    assert solution.spiral_order(make_matrix(3, 4)) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print("✓ Test 1 passed: 3 x 4")

    # Test case 2: Tall matrix (4 x 3)
    assert solution.spiral_order(make_matrix(4, 3)) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    print("✓ Test 2 passed: 4 x 3")

    # Test case 3: Single row and single column
    assert solution.spiral_order(make_matrix(1, 4)) == [1, 2, 3, 4]
    assert solution.spiral_order([[1], [2], [3]]) == [1, 2, 3]
    print("✓ Test 3 passed: 1 x 4 and 3 x 1")

    # Test case 4: Two rows
    assert solution.spiral_order(make_matrix(2, 3)) == [1, 2, 3, 6, 5, 4]
    print("✓ Test 4 passed: 2 x 3")

    # Test case 5: Empty matrix
    assert solution.spiral_order([]) == []
    print("✓ Test 5 passed: Empty matrix")

    # Test case 6: Larger tall matrix (6 x 5)
    expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 29, 28, 27, 26, 21, 16, 11, 6,
                7, 8, 9, 14, 19, 24, 23, 22, 17, 12, 13, 18]
    assert solution.spiral_order(make_matrix(6, 5)) == expected
    print("✓ Test 6 passed: 6 x 5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_spiral_order()
