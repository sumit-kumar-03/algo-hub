"""
EPI 15.9 - Implement a Sudoku Solver

Problem:
Given a partially filled n x n Sudoku grid (n = 9 normally, or any perfect
square such as 4), fill in the empty cells (marked 0) so that every row,
every column, and every sqrt(n) x sqrt(n) box contains each of 1..n
exactly once. Solve the grid in place and return True, or return False
if no solution exists. Prefilled cells must not change.

Constraints:
- n is a perfect square (4 or 9 in the tests)
- The givens never repeat a value within a row, column, or box
- Generalized Sudoku is NP-complete, so backtracking is expected

How it works (backtracking with local checks):
1. Find the next empty cell (scan in a fixed order)
2. For each value 1..n, check only that cell's row, column, and box for a
   conflict (the rest of the grid is already consistent)
3. If the value fits, write it and recurse; if the recursion fails, reset
   the cell to 0 and try the next value
4. If no value fits, return False; if no empty cell is left, return True
Tip: keeping sets of used values per row, column, and box makes each
check O(1).

Example 1:
Input:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
Output: True, and the grid becomes
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
...  (a complete valid grid)

Example 2:
Input: a grid whose first row holds 1..8 in columns 1..8 and whose first
column holds a 9 lower down
Output: False
Explanation: The top-left cell can only be 9, but column 0 already has 9.
"""

from typing import List


class Solution:
    def solve_sudoku(self, grid: List[List[int]]) -> bool:
        """
        Solves a Sudoku grid in place.

        Args:
            grid: n x n grid with 0 for empty cells (n is a perfect square)

        Returns:
            True if the grid was solved (grid now holds the solution),
            False if no solution exists

        Time Complexity: Exponential in the number of empty cells (worst case)
        Space Complexity: O(n^2) for recursion depth and bookkeeping
        """
        # TODO: Implement backtracking Sudoku solver
        pass


def is_valid_solution(grid: List[List[int]], givens: List[List[int]]) -> bool:
    """True if grid is a complete valid Sudoku that agrees with the givens."""
    n = len(givens)
    box = int(round(n ** 0.5))
    full = set(range(1, n + 1))
    if len(grid) != n or any(len(row) != n for row in grid):
        return False
    for r in range(n):
        for c in range(n):
            if givens[r][c] != 0 and grid[r][c] != givens[r][c]:
                return False
    rows_ok = all(set(row) == full for row in grid)
    cols_ok = all({grid[r][c] for r in range(n)} == full for c in range(n))
    boxes_ok = all(
        {grid[br + i][bc + j] for i in range(box) for j in range(box)} == full
        for br in range(0, n, box)
        for bc in range(0, n, box)
    )
    return rows_ok and cols_ok and boxes_ok


def parse(rows: List[str]) -> List[List[int]]:
    """Turns strings like '53..7....' into a grid with 0 for '.'."""
    return [[0 if ch == "." else int(ch) for ch in row] for row in rows]


def test_solve_sudoku():
    """Test cases for the Sudoku solver"""
    solution = Solution()

    # Test case 1: Classic 9 x 9 puzzle from the example
    givens1 = parse([
        "53..7....", "6..195...", ".98....6.",
        "8...6...3", "4..8.3..1", "7...2...6",
        ".6....28.", "...419..5", "....8..79",
    ])
    grid1 = [row[:] for row in givens1]
    assert solution.solve_sudoku(grid1) is True
    assert is_valid_solution(grid1, givens1)
    print("✓ Test 1 passed: Classic puzzle solved")

    # Test case 2: Another 9 x 9 puzzle
    givens2 = parse([
        "..9748...", "7........", ".2.1.9...",
        "..7...24.", ".64.1.59.", ".98...3..",
        "...8.3.2.", "........6", "...2759..",
    ])
    grid2 = [row[:] for row in givens2]
    assert solution.solve_sudoku(grid2) is True
    assert is_valid_solution(grid2, givens2)
    print("✓ Test 2 passed: Second puzzle solved")

    # Test case 3: Already complete grid stays the same
    complete = parse([
        "534678912", "672195348", "198342567",
        "859761423", "426853791", "713924856",
        "961537284", "287419635", "345286179",
    ])
    grid3 = [row[:] for row in complete]
    assert solution.solve_sudoku(grid3) is True and grid3 == complete
    print("✓ Test 3 passed: Complete grid returns True unchanged")

    # Test case 4: 4 x 4 grid
    givens4 = [
        [1, 0, 0, 0],
        [0, 0, 3, 0],
        [0, 4, 0, 0],
        [0, 0, 0, 2],
    ]
    grid4 = [row[:] for row in givens4]
    assert solution.solve_sudoku(grid4) is True
    assert is_valid_solution(grid4, givens4)
    print("✓ Test 4 passed: 4 x 4 puzzle solved")

    # Test case 5: Empty 9 x 9 grid (any valid filling)
    givens5 = [[0] * 9 for _ in range(9)]
    grid5 = [row[:] for row in givens5]
    assert solution.solve_sudoku(grid5) is True
    assert is_valid_solution(grid5, givens5)
    print("✓ Test 5 passed: Empty grid filled")

    # Test case 6: Unsolvable puzzle (top-left cell has no legal value)
    givens6 = [[0] * 9 for _ in range(9)]
    givens6[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    givens6[4][0] = 9
    grid6 = [row[:] for row in givens6]
    assert solution.solve_sudoku(grid6) is False
    print("✓ Test 6 passed: Unsolvable puzzle returns False")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_solve_sudoku()
