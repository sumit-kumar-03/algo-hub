"""
EPI 15.2 Extra Variant - n-Queens on a Board With Holes
(Practice problem, not in the book. Difficulty: Medium)
Builds on: row-by-row backtracking with column and diagonal sets, plus an
extra per-square constraint that prunes candidate columns.

Problem:
Some squares of an n x n board are holes: a queen cannot stand on a hole.
Holes do not block attacks, so two queens on the same line still attack
each other even if a hole lies between them. Count the ways to place n
queens on non-hole squares so that no two share a row, a column, or a
diagonal. Holes are given as a list of (row, col) pairs (duplicates may
appear and should be treated as one hole).

Constraints:
- 1 <= n <= 10
- 0 <= len(holes) <= n * n, 0 <= row, col < n
- Backtracking with O(1) checks per candidate square

How it works (backtracking with a forbidden-square set):
1. Put the holes in a set (or one bitmask per row)
2. Place queens row by row; in row r skip column c if (r, c) is a hole or
   the column / either diagonal is already used
3. Count the placements that reach row n
Tip: if some row is entirely holes, the answer is 0 right away.

Example 1:
Input: n = 4, holes = [(0, 1)]
Output: 1
Explanation: Of the two 4-queens solutions, [1, 3, 0, 2] uses the hole,
so only [2, 0, 3, 1] remains.

Example 2:
Input: n = 4, holes = [(0, 1), (0, 2)]
Output: 0
"""

from typing import List, Tuple


class Solution:
    def count_queens_with_holes(self, n: int, holes: List[Tuple[int, int]]) -> int:
        """
        Counts nonattacking n-queens placements that avoid every hole.

        Args:
            n: Board size
            holes: (row, col) squares that cannot hold a queen

        Returns:
            Number of valid placements

        Time Complexity: O(n!) in the worst case
        Space Complexity: O(n + len(holes))
        """
        # TODO: Implement backtracking that skips hole squares
        pass


def test_count_queens_with_holes():
    """Test cases for n-Queens with holes"""
    solution = Solution()

    # Test case 1: No holes matches the classic counts
    assert solution.count_queens_with_holes(4, []) == 2
    assert solution.count_queens_with_holes(8, []) == 92
    print("✓ Test 1 passed: no holes -> 2 and 92")

    # Test case 2: Examples from the statement
    assert solution.count_queens_with_holes(4, [(0, 1)]) == 1
    assert solution.count_queens_with_holes(4, [(0, 1), (0, 2)]) == 0
    print("✓ Test 2 passed: n=4 examples -> 1 and 0")

    # Test case 3: 1 x 1 board with and without a hole
    assert solution.count_queens_with_holes(1, []) == 1
    assert solution.count_queens_with_holes(1, [(0, 0)]) == 0
    print("✓ Test 3 passed: 1 x 1 board")

    # Test case 4: Duplicate holes and a hole no solution uses
    assert solution.count_queens_with_holes(4, [(0, 0), (0, 0), (3, 3)]) == 2
    print("✓ Test 4 passed: duplicate and unused holes -> 2")

    # Test case 5: Holes on the main diagonal of an 8 x 8 board
    diag = [(i, i) for i in range(8)]
    assert solution.count_queens_with_holes(8, diag) == 28
    print("✓ Test 5 passed: n=8, main diagonal removed -> 28")

    # Test case 6: Both diagonals removed on a 6 x 6 board
    both = [(i, i) for i in range(6)] + [(i, 5 - i) for i in range(6)]
    assert solution.count_queens_with_holes(6, both) == 4
    print("✓ Test 6 passed: n=6, both diagonals removed -> 4")

    # Test case 7: A full row of holes
    assert solution.count_queens_with_holes(8, [(5, c) for c in range(8)]) == 0
    print("✓ Test 7 passed: full row of holes -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_queens_with_holes()
