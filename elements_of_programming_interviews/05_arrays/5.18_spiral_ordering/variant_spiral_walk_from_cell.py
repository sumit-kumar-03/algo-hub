"""
EPI 5.18 Extra Variant - Spiral Walk Outward from a Cell
(Practice problem, not in the book. Difficulty: Medium)
Builds on: walking a spiral with a direction vector that turns clockwise
(right, down, left, up), as in the spiral-order and spiral-pairs problems,
but growing outward instead of shrinking inward.

Problem:
A grid has `rows` rows and `cols` columns. You start at cell
(r_start, c_start) facing east (toward larger column numbers) and walk an
outward clockwise spiral: 1 step east, 1 step south, 2 steps west,
2 steps north, 3 steps east, 3 steps south, and so on. The walk may leave
the grid; it keeps going and may come back later. Return the cells of the
grid in the order they are first visited, as [row, column] pairs, until
every cell has been visited.

Constraints:
- 1 <= rows, cols <= 100; 0 <= r_start < rows; 0 <= c_start < cols
- O(max(rows, cols)^2) time (the spiral has to cover the whole grid)

How it works:
1. directions = east (0, 1), south (1, 0), west (0, -1), north (-1, 0)
2. Record the start cell. step_length = 1, d = 0
3. Repeat until rows * cols cells are recorded:
   - Walk step_length steps in direction d, recording each cell that lies
     inside the grid; then turn: d = (d + 1) % 4
   - Every two turns (after south and after north), step_length += 1

Example 1:
Input: rows = 1, cols = 4, r_start = 0, c_start = 0
Output: [[0, 0], [0, 1], [0, 2], [0, 3]]
Explanation: Only the eastward legs touch the single row.

Example 2:
Input: rows = 3, cols = 3, r_start = 1, c_start = 1
Output: [[1, 1], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0], [0, 1],
         [0, 2]]
Explanation: One ring around the center, starting east of it.
"""

from typing import List


class Solution:
    def spiral_walk(self, rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:
        """
        Lists grid cells in the order an outward spiral from a start cell visits them.

        Args:
            rows: Number of grid rows
            cols: Number of grid columns
            r_start: Starting row
            c_start: Starting column

        Returns:
            All rows * cols cells as [row, column] pairs in visit order

        Time Complexity: O(max(rows, cols)^2)
        Space Complexity: O(rows * cols) for the output
        """
        # TODO: Implement outward spiral walk
        pass


def test_spiral_walk():
    """Test cases for the outward spiral walk"""
    solution = Solution()

    # Test case 1: Single row from the left end
    assert solution.spiral_walk(1, 4, 0, 0) == [[0, 0], [0, 1], [0, 2], [0, 3]]
    print("✓ Test 1 passed: 1 x 4 from (0, 0)")

    # Test case 2: 3 x 3 from the center
    expected = [[1, 1], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]]
    assert solution.spiral_walk(3, 3, 1, 1) == expected
    print("✓ Test 2 passed: 3 x 3 from the center")

    # Test case 3: Single cell
    assert solution.spiral_walk(1, 1, 0, 0) == [[0, 0]]
    print("✓ Test 3 passed: 1 x 1")

    # Test case 4: Start in a corner of a rectangle (the walk leaves and re-enters)
    expected = [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4],
                [0, 5], [2, 2], [1, 2], [0, 2], [2, 1], [1, 1], [0, 1], [2, 0],
                [1, 0], [0, 0]]
    assert solution.spiral_walk(3, 6, 1, 4) == expected
    print("✓ Test 4 passed: 3 x 6 from (1, 4)")

    # Test case 5: Single column, starting at the bottom
    assert solution.spiral_walk(3, 1, 2, 0) == [[2, 0], [1, 0], [0, 0]]
    print("✓ Test 5 passed: 3 x 1 from the bottom")

    # Test case 6: Large grid from a corner covers every cell exactly once
    result = solution.spiral_walk(100, 100, 99, 99)
    assert len(result) == 10000
    assert len({(r, c) for r, c in result}) == 10000
    assert result[0] == [99, 99] and result[1] == [99, 98] and result[-1] == [0, 99]
    print("✓ Test 6 passed: 100 x 100 from the bottom-right corner")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_spiral_walk()
