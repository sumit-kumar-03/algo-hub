"""
EPI 15.2 Variant - Minimum Queens That Cover an n x n Board

Problem:
Find the smallest set of queens to place on an n x n chessboard so that
every square that is not occupied by a queen is attacked by at least one
queen. (Queens may attack each other.) Return the positions of such a
minimum set as (row, col) pairs; any minimum set is accepted.

Constraints:
- 1 <= n <= 6 (the search space explodes quickly)
- Known minimum sizes for n = 1..8: 1, 1, 1, 2, 3, 3, 4, 5

How it works (iterative deepening + backtracking):
1. For k = 1, 2, 3, ..., try to choose k squares that cover the board
2. Choose squares in increasing index order (to avoid revisiting the same
   set in a different order) and recurse
3. Prune: find the first square that is not yet covered; at least one
   queen must be placed on a square that attacks or occupies it, so only
   branch on those squares
4. The first k that succeeds is the minimum; return that placement

Example 1:
Input: n = 3
Output: [(1, 1)]
Explanation: A queen in the center attacks all 8 other squares.

Example 2:
Input: n = 4
Output: [(0, 0), (2, 2)]
Explanation: No single queen covers a 4 x 4 board, but two can. Other
covering pairs, such as [(1, 0), (1, 3)], are also accepted.
"""

from typing import List, Tuple


class Solution:
    def min_dominating_queens(self, n: int) -> List[Tuple[int, int]]:
        """
        Finds a minimum set of queens that attack or occupy every square.

        Args:
            n: Board size

        Returns:
            List of (row, col) positions of a minimum covering set of queens

        Time Complexity: Exponential in n (combinatorial search)
        Space Complexity: O(n^2) for coverage bookkeeping
        """
        # TODO: Implement iterative deepening search for a covering set
        pass


MIN_QUEENS = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 3}


def covers_board(n: int, queens: List[Tuple[int, int]]) -> bool:
    """True if every square is occupied or attacked by some queen."""
    if any(not (0 <= r < n and 0 <= c < n) for r, c in queens):
        return False
    for r in range(n):
        for c in range(n):
            if not any(
                r == qr or c == qc or abs(r - qr) == abs(c - qc) for qr, qc in queens
            ):
                return False
    return True


def test_min_dominating_queens():
    """Test cases for minimum queen domination"""
    solution = Solution()

    # Test case 1: 1 x 1 board
    result1 = solution.min_dominating_queens(1)
    assert result1 == [(0, 0)]
    print("✓ Test 1 passed: n=1 -> [(0, 0)]")

    # Test case 2: 3 x 3 board needs one queen (the center)
    result2 = solution.min_dominating_queens(3)
    assert result2 == [(1, 1)]
    print("✓ Test 2 passed: n=3 -> [(1, 1)]")

    # Test case 3: 2 x 2 and 4 x 4 boards
    for n in (2, 4):
        result = solution.min_dominating_queens(n)
        assert len(set(result)) == len(result) == MIN_QUEENS[n] and covers_board(n, result)
    print("✓ Test 3 passed: n=2 -> 1 queen, n=4 -> 2 queens")

    # Test case 4: 5 x 5 board needs three queens
    result4 = solution.min_dominating_queens(5)
    assert len(set(result4)) == len(result4) == 3 and covers_board(5, result4)
    print(f"✓ Test 4 passed: n=5 -> {result4}")

    # Test case 5: 6 x 6 board also needs only three queens
    result5 = solution.min_dominating_queens(6)
    assert len(set(result5)) == len(result5) == 3 and covers_board(6, result5)
    print(f"✓ Test 5 passed: n=6 -> {result5}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_dominating_queens()
