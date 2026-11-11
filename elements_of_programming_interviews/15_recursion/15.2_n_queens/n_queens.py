"""
EPI 15.2 - Generate All Nonattacking Placements of n-Queens

Problem:
Place n queens on an n x n chessboard so that no two share a row, a
column, or a diagonal. Return every such placement. Represent a placement
as a list of length n whose i-th entry is the column of the queen in row i.
Each placement must appear exactly once; the order of placements does not
matter.

Constraints:
- 1 <= n <= 10
- The number of placements grows super-exponentially with n

How it works (backtracking, one queen per row):
1. Place queens row by row, keeping the columns chosen so far
2. For the current row, try each column that does not clash with an
   earlier queen: same column, or |col difference| == |row difference|
3. When all n rows are filled, record a copy of the placement
4. Undo the choice and try the next column
Tip: sets of used columns and used diagonals (row - col, row + col) make
each check O(1).

Example 1:
Input: n = 4
Output: [[1, 3, 0, 2], [2, 0, 3, 1]]
Explanation: These are the only two ways to place four queens.

Example 2:
Input: n = 3
Output: []
Explanation: No nonattacking placement exists for n = 2 or n = 3.
"""

from typing import List


class Solution:
    def n_queens(self, n: int) -> List[List[int]]:
        """
        Returns all nonattacking placements of n queens on an n x n board.

        Args:
            n: Board size and number of queens

        Returns:
            List of placements; placement[i] is the column of the queen in row i

        Time Complexity: O(n!) in the worst case (bounded by the search tree)
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement backtracking over rows
        pass


def is_valid_placement(n: int, placement: List[int]) -> bool:
    """Checks that a placement has n queens and no two attack each other."""
    if len(placement) != n or any(not 0 <= c < n for c in placement):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if placement[i] == placement[j] or abs(placement[i] - placement[j]) == j - i:
                return False
    return True


def normalize(placements: List[List[int]]) -> List[tuple]:
    """Sorts placements so results can be compared regardless of order."""
    return sorted(tuple(p) for p in placements)


def test_n_queens():
    """Test cases for n-Queens"""
    solution = Solution()

    # Test case 1: n = 1
    assert normalize(solution.n_queens(1)) == [(0,)]
    print("✓ Test 1 passed: n=1 -> [[0]]")

    # Test case 2: n = 2 and n = 3 have no solutions
    assert solution.n_queens(2) == [] and solution.n_queens(3) == []
    print("✓ Test 2 passed: n=2 and n=3 -> []")

    # Test case 3: Book example
    assert normalize(solution.n_queens(4)) == [(1, 3, 0, 2), (2, 0, 3, 1)]
    print("✓ Test 3 passed: n=4 -> [[1, 3, 0, 2], [2, 0, 3, 1]]")

    # Test case 4: n = 6 has exactly 4 solutions
    result4 = solution.n_queens(6)
    assert len(set(map(tuple, result4))) == len(result4) == 4
    assert all(is_valid_placement(6, p) for p in result4)
    print("✓ Test 4 passed: n=6 -> 4 valid, distinct placements")

    # Test case 5: n = 8 has exactly 92 solutions
    result5 = solution.n_queens(8)
    assert len(set(map(tuple, result5))) == len(result5) == 92
    assert all(is_valid_placement(8, p) for p in result5)
    print("✓ Test 5 passed: n=8 -> 92 valid, distinct placements")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_n_queens()
