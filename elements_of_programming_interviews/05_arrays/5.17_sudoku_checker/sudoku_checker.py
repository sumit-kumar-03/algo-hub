"""
EPI 5.17 - The Sudoku Checker Problem

Problem:
A Sudoku grid is n x n (normally 9 x 9) and is split into n square
sub-grids of size sqrt(n) x sqrt(n). A cell holds 0 if it is blank, or a
digit in [1, n]. Given a partially filled grid, decide whether it breaks
any Sudoku rule: no digit may repeat within a row, a column, or a
sub-grid. Blank cells are ignored. (You only check for conflicts; you do
not need to decide whether the puzzle can be completed.)

Constraints:
- n is a perfect square (4, 9, 16, ...); grid entries are in [0, n]
- Aim for O(n^2) time and O(n) extra space

How it works:
1. For each row, collect its non-zero entries and check for a repeat
   (e.g. with a set or a boolean array of size n + 1)
2. Do the same for each column
3. For each of the n sub-grids (blocks of size s = sqrt(n)), do the same
4. Return False on the first repeat, otherwise True

Example 1:
Input: the classic partially filled 9 x 9 puzzle (see Test 1)
Output: True
Explanation: No row, column, or 3 x 3 block repeats a digit.

Example 2:
Input: the same puzzle with a second 5 placed in the first row
Output: False
Explanation: The first row now contains two 5s.
"""

from typing import List


class Solution:
    def is_valid_sudoku(self, partial_assignment: List[List[int]]) -> bool:
        """
        Checks a partially filled Sudoku grid for rule violations.

        Args:
            partial_assignment: n x n grid; 0 means blank, otherwise a digit in [1, n]

        Returns:
            True if no row, column, or sub-grid repeats a digit, False otherwise

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        # TODO: Implement the Sudoku checker
        pass


PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

SOLVED = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def test_is_valid_sudoku():
    """Test cases for the Sudoku checker"""
    solution = Solution()

    # Test case 1: Valid partial assignment
    assert solution.is_valid_sudoku([row[:] for row in PUZZLE]) is True
    print("✓ Test 1 passed: Classic partial puzzle is valid")

    # Test case 2: Fully solved grid
    assert solution.is_valid_sudoku([row[:] for row in SOLVED]) is True
    print("✓ Test 2 passed: Solved grid is valid")

    # Test case 3: Duplicate in a row
    grid = [row[:] for row in PUZZLE]
    grid[0][8] = 5
    assert solution.is_valid_sudoku(grid) is False
    print("✓ Test 3 passed: Duplicate 5 in row 0 -> False")

    # Test case 4: Duplicate in a column only
    grid = [row[:] for row in PUZZLE]
    grid[8][0] = 4  # column 0 already has a 4 in row 4; row 8 and its block are clean
    assert solution.is_valid_sudoku(grid) is False
    print("✓ Test 4 passed: Duplicate 4 in column 0 -> False")

    # Test case 5: Duplicate in a 3 x 3 block only (different rows and columns)
    grid = [[0] * 9 for _ in range(9)]
    grid[3][3] = 4
    grid[5][4] = 4
    assert solution.is_valid_sudoku(grid) is False
    print("✓ Test 5 passed: Duplicate 4 in the center block -> False")

    # Test case 6: Empty 9 x 9 grid
    assert solution.is_valid_sudoku([[0] * 9 for _ in range(9)]) is True
    print("✓ Test 6 passed: Empty grid is valid")

    # Test case 7: 4 x 4 grids with 2 x 2 blocks
    valid4 = [[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 1, 2], [0, 0, 3, 4]]
    invalid4 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert solution.is_valid_sudoku(valid4) is True
    assert solution.is_valid_sudoku(invalid4) is False
    print("✓ Test 7 passed: 4 x 4 grids (valid and block conflict)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_valid_sudoku()
