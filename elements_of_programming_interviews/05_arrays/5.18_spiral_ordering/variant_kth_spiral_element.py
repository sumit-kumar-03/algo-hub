"""
EPI 5.18 Variant - kth Element in Spiral Order

Problem:
Given a non-empty m x n 2D array and an index k (0-based), return the
element at position k of its clockwise spiral order (starting at the
top-left corner), without generating the whole spiral.

Constraints:
- 1 <= m, n <= 10^4; 0 <= k < m * n
- Aim for O(1) time (an O(min(m, n)) layer-by-layer skip is a good first
  step)

How it works (skip whole layers, then index into one ring):
1. Layer L (0-based) is a ring of size (m - 2L) x (n - 2L) holding
   2 * ((m - 2L) + (n - 2L)) - 4 elements (or all of them if it is a
   single row or column)
2. The number of elements in the first L layers is a quadratic in L, so
   the layer containing k can be found in O(1) by solving it (or by
   skipping layers one at a time)
3. Inside that ring, compute the offset t = k - (elements before it) and
   decide whether t falls on the top, right, bottom, or left side; turn
   that into a (row, column) index

Example 1:
Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], k = 5
Output: 12
Explanation: Spiral order is 1, 2, 3, 4, 8, 12, ... and index 5 is 12.

Example 2:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 8
Output: 5
Explanation: The center is the last (index 8) element.
"""

from typing import List


class Solution:
    def kth_in_spiral(self, matrix: List[List[int]], k: int) -> int:
        """
        Returns the element at index k of the spiral order.

        Args:
            matrix: Non-empty m x n 2D array
            k: 0-based position in spiral order, 0 <= k < m * n

        Returns:
            The element at spiral position k

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement direct lookup of the kth spiral element
        pass


def make_matrix(m: int, n: int) -> List[List[int]]:
    """Builds an m x n matrix holding 1..m*n in row-major order."""
    return [[n * i + j + 1 for j in range(n)] for i in range(m)]


def check_all(solution: "Solution", m: int, n: int, expected: List[int]) -> bool:
    """Checks every k of an m x n row-major matrix against the expected spiral."""
    matrix = make_matrix(m, n)
    return all(solution.kth_in_spiral(matrix, k) == v for k, v in enumerate(expected))


def test_kth_in_spiral():
    """Test cases for the kth element in spiral order"""
    solution = Solution()

    # Test case 1: Single lookups from the examples
    assert solution.kth_in_spiral(make_matrix(3, 4), 5) == 12
    assert solution.kth_in_spiral(make_matrix(3, 3), 8) == 5
    print("✓ Test 1 passed: Example lookups")

    # Test case 2: Every k of a 4 x 4 matrix
    assert check_all(solution, 4, 4, [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
    print("✓ Test 2 passed: All k for 4 x 4")

    # Test case 3: Every k of wide and tall matrices
    assert check_all(solution, 3, 4, [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    assert check_all(solution, 4, 3, [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8])
    print("✓ Test 3 passed: All k for 3 x 4 and 4 x 3")

    # Test case 4: Single row, single column, single element
    assert check_all(solution, 1, 5, [1, 2, 3, 4, 5])
    assert check_all(solution, 5, 1, [1, 2, 3, 4, 5])
    assert solution.kth_in_spiral([[42]], 0) == 42
    print("✓ Test 4 passed: 1 x 5, 5 x 1, 1 x 1")

    # Test case 5: Every k of a 6 x 5 matrix (three layers)
    assert check_all(solution, 6, 5, [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 29, 28, 27, 26, 21, 16,
                                      11, 6, 7, 8, 9, 14, 19, 24, 23, 22, 17, 12, 13, 18])
    print("✓ Test 5 passed: All k for 6 x 5")

    # Test case 6: Every k of a 7 x 4 matrix (inner layer is a column)
    assert check_all(solution, 7, 4, [1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 27, 26, 25, 21, 17, 13,
                                      9, 5, 6, 7, 11, 15, 19, 23, 22, 18, 14, 10])
    print("✓ Test 6 passed: All k for 7 x 4")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_in_spiral()
