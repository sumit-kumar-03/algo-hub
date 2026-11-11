"""
EPI 5.18 Variant - Last Element in Spiral Order

Problem:
Given a non-empty m x n 2D array, return the element that comes last in
its clockwise spiral order (starting at the top-left corner), in O(1)
time, i.e. without walking the spiral.

Constraints:
- 1 <= m, n <= 10^4
- Must run in O(1) time

How it works (find the innermost layer):
1. Let s = min(m, n) and layer = (s - 1) // 2; after peeling `layer`
   rings, the remaining block has size (m - 2*layer) x (n - 2*layer)
2. That innermost block is a single row, a single column, or a 2-row /
   2-column ring
3. Work out which case applies (compare m and n, and whether s is odd or
   even) and index the corresponding end cell directly:
   - s odd, m <= n: the middle row is read left to right, so the last
     element is at the right end of that row
   - s odd, m > n: the middle column is read top to bottom
   - s even: the last ring ends one row below its top-left corner

Example 1:
Input: [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
Output: 7
Explanation: Spiral order is 1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7.

Example 2:
Input: [[1, 2], [3, 4]]
Output: 3
Explanation: Spiral order is 1, 2, 4, 3.
"""

from typing import List


class Solution:
    def last_in_spiral(self, matrix: List[List[int]]) -> int:
        """
        Returns the last element of the spiral order in constant time.

        Args:
            matrix: Non-empty m x n 2D array

        Returns:
            The element visited last in clockwise spiral order

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement O(1) lookup of the last spiral element
        pass


def make_matrix(m: int, n: int) -> List[List[int]]:
    """Builds an m x n matrix holding 1..m*n in row-major order."""
    return [[n * i + j + 1 for j in range(n)] for i in range(m)]


def test_last_in_spiral():
    """Test cases for the last element in spiral order"""
    solution = Solution()

    # Test case 1: Wide and tall 3 x 4 / 4 x 3
    assert solution.last_in_spiral(make_matrix(3, 4)) == 7
    assert solution.last_in_spiral(make_matrix(4, 3)) == 8
    print("✓ Test 1 passed: 3 x 4 -> 7, 4 x 3 -> 8")

    # Test case 2: Odd and even squares
    assert solution.last_in_spiral(make_matrix(3, 3)) == 5
    assert solution.last_in_spiral(make_matrix(4, 4)) == 10
    assert solution.last_in_spiral(make_matrix(2, 2)) == 3
    print("✓ Test 2 passed: 3 x 3 -> 5, 4 x 4 -> 10, 2 x 2 -> 3")

    # Test case 3: Single element, row, and column
    assert solution.last_in_spiral([[9]]) == 9
    assert solution.last_in_spiral(make_matrix(1, 4)) == 4
    assert solution.last_in_spiral(make_matrix(4, 1)) == 4
    print("✓ Test 3 passed: 1 x 1, 1 x 4, 4 x 1")

    # Test case 4: Two rows
    assert solution.last_in_spiral(make_matrix(2, 3)) == 4
    print("✓ Test 4 passed: 2 x 3 -> 4")

    # Test case 5: Larger shapes
    assert solution.last_in_spiral(make_matrix(5, 3)) == 11
    assert solution.last_in_spiral(make_matrix(3, 6)) == 11
    assert solution.last_in_spiral(make_matrix(6, 5)) == 18
    assert solution.last_in_spiral(make_matrix(7, 4)) == 10
    print("✓ Test 5 passed: 5 x 3, 3 x 6, 6 x 5, 7 x 4")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_last_in_spiral()
