"""
EPI 5.18 Extra Variant - Rotate Every Ring of a Matrix
(Practice problem, not in the book. Difficulty: Hard)
Builds on: listing one layer (ring) of a 2D array in clockwise order, and
writing values back along the same path.

Problem:
An m x n 2D array is made of concentric rings: the outer boundary, the
boundary of what is left inside it, and so on. Rotate every ring
clockwise by k positions in place: each entry moves k steps forward along
its own ring in clockwise order (rightward along the top, down the right
side, leftward along the bottom, up the left side). Rings move
independently, and k can be huge, so reduce it modulo each ring's length.
A layer that is only one row or one column thick (or a single cell) is
not a loop, so leave it unchanged.

Constraints:
- 0 <= m, n <= 300; 0 <= k <= 10^18
- O(m * n) time; O(m + n) extra space (one ring at a time)

How it works:
1. For each layer t while both dimensions of the remaining block are
   at least 2 (top = t, bottom = m - 1 - t, left = t, right = n - 1 - t):
   - Collect the ring's cell coordinates in clockwise order starting at
     (top, left): top row, right column, bottom row reversed, left column
     reversed, skipping corners already listed
   - L = number of cells, s = k mod L; read the values along the path
   - Write value i to cell (i + s) mod L
2. Stop when the remaining block is empty, one row, or one column thick

Example 1:
Input: matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]], k = 1
Output: [[5, 1, 2, 3],
         [9, 10, 6, 4],
         [13, 11, 7, 8],
         [14, 15, 16, 12]]
Explanation: The outer 12 entries and the inner 4 each move one step
clockwise.

Example 2:
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]], k = 2
Output: [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
Explanation: Two steps on the 8-cell outer ring; the center stays put
(for a 3 x 3 this matches a quarter-turn rotation).
"""

from typing import List


class Solution:
    def rotate_rings(self, matrix: List[List[int]], k: int) -> None:
        """
        Rotates every ring of the matrix clockwise by k positions, in place.

        Args:
            matrix: m x n 2D array (modified in place)
            k: Number of positions each entry moves along its ring

        Returns:
            None (matrix is modified in place)

        Time Complexity: O(m * n)
        Space Complexity: O(m + n)
        """
        # TODO: Implement ring rotation
        pass


def make_matrix(m: int, n: int) -> List[List[int]]:
    """Builds an m x n matrix holding 1..m*n in row-major order."""
    return [[n * i + j + 1 for j in range(n)] for i in range(m)]


def test_rotate_rings():
    """Test cases for rotating matrix rings"""
    solution = Solution()

    # Test case 1: Example 1 (4 x 4, k = 1)
    M1 = make_matrix(4, 4)
    solution.rotate_rings(M1, 1)
    assert M1 == [[5, 1, 2, 3], [9, 10, 6, 4], [13, 11, 7, 8], [14, 15, 16, 12]]
    print("✓ Test 1 passed: 4 x 4, k = 1")

    # Test case 2: Example 2 (3 x 3, k = 2)
    M2 = make_matrix(3, 3)
    solution.rotate_rings(M2, 2)
    assert M2 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print("✓ Test 2 passed: 3 x 3, k = 2")

    # Test case 3: Rectangle whose inner layer is a single row (stays put)
    M3 = make_matrix(3, 5)
    solution.rotate_rings(M3, 3)
    assert M3 == [[12, 11, 6, 1, 2], [13, 7, 8, 9, 3], [14, 15, 10, 5, 4]]
    print("✓ Test 3 passed: 3 x 5, k = 3")

    # Test case 4: Degenerate shapes are unchanged
    M4 = make_matrix(1, 5)
    solution.rotate_rings(M4, 7)
    assert M4 == make_matrix(1, 5)
    M5 = make_matrix(4, 1)
    solution.rotate_rings(M5, 2)
    assert M5 == make_matrix(4, 1)
    M6: List[List[int]] = []
    solution.rotate_rings(M6, 5)
    assert M6 == []
    print("✓ Test 4 passed: 1 x 5, 4 x 1, empty")

    # Test case 5: k = 0 and k equal to a multiple of every ring length
    M7 = make_matrix(6, 6)  # rings of 20, 12 and 4 cells
    solution.rotate_rings(M7, 0)
    assert M7 == make_matrix(6, 6)
    solution.rotate_rings(M7, 60 * 10**15)
    assert M7 == make_matrix(6, 6)
    print("✓ Test 5 passed: k = 0 and k a multiple of 60 on 6 x 6")

    # Test case 6: Huge k reduces per ring (outer ring 12, inner ring 4)
    M8 = make_matrix(4, 4)
    solution.rotate_rings(M8, 10**18 + 1)  # 5 steps on the outer ring, 1 on the inner
    assert M8 == [[15, 14, 13, 9], [16, 10, 6, 5], [12, 11, 7, 1], [8, 4, 3, 2]]
    print("✓ Test 6 passed: 4 x 4, k = 10^18 + 1")

    # Test case 7: Tall rectangle (5 x 2)
    M9 = make_matrix(5, 2)
    solution.rotate_rings(M9, 1)
    assert M9 == [[3, 1], [5, 2], [7, 4], [9, 6], [10, 8]]
    print("✓ Test 7 passed: 5 x 2, k = 1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_rotate_rings()
