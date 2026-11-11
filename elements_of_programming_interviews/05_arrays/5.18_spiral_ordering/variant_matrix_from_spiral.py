"""
EPI 5.18 Variant - Build a Matrix from Its Spiral Order

Problem:
Given a sequence P whose length is n^2 for some integer n, build the
n x n 2D array A whose clockwise spiral order (starting at the top-left
corner) is exactly P.

Constraints:
- len(P) == n^2 for some integer n >= 0 (empty P gives an empty list)
- Must run in O(n^2) time

How it works (walk the spiral and place P's values):
1. n = integer square root of len(P); create an n x n grid
2. Walk the spiral path (right, down, left, up, shrinking each layer)
3. Write P[0], P[1], ... into the cells in the order they are visited

Example 1:
Input: P = [1, 2, 3, 6, 9, 8, 7, 4, 5]
Output: [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
Explanation: This is the inverse of computing the spiral order.

Example 2:
Input: P = [5, 1, 4, 2]
Output: [[5, 1],
         [2, 4]]
Explanation: 5 and 1 go across the top, 4 down the right, 2 back left.
"""

from typing import List


class Solution:
    def matrix_from_spiral(self, P: List[int]) -> List[List[int]]:
        """
        Builds the square matrix whose spiral order is P.

        Args:
            P: Sequence of length n^2

        Returns:
            The n x n matrix with spiral order P (empty list if P is empty)

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement matrix construction from a spiral sequence
        pass


def test_matrix_from_spiral():
    """Test cases for building a matrix from its spiral order"""
    solution = Solution()

    # Test case 1: 3 x 3 (inverse of the book example)
    assert solution.matrix_from_spiral([1, 2, 3, 6, 9, 8, 7, 4, 5]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("✓ Test 1 passed: 3 x 3")

    # Test case 2: 2 x 2
    assert solution.matrix_from_spiral([5, 1, 4, 2]) == [[5, 1], [2, 4]]
    print("✓ Test 2 passed: 2 x 2")

    # Test case 3: 1 x 1 and empty
    assert solution.matrix_from_spiral([42]) == [[42]]
    assert solution.matrix_from_spiral([]) == []
    print("✓ Test 3 passed: 1 x 1 and empty")

    # Test case 4: 4 x 4 (inverse of the book example)
    P = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    expected = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert solution.matrix_from_spiral(P) == expected
    print("✓ Test 4 passed: 4 x 4")

    # Test case 5: Sequence 1..9 gives the generated spiral matrix
    assert solution.matrix_from_spiral(list(range(1, 10))) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print("✓ Test 5 passed: 1..9 -> spiral matrix")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_matrix_from_spiral()
