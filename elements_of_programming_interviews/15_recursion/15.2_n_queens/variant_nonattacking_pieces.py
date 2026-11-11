"""
EPI 15.2 Variant - Place Nonattacking Knights, Bishops, Kings, or Rooks

Problem:
Given a chess piece type ("knight", "bishop", "king", or "rook"), a count,
and a board size n, place exactly `count` pieces of that type on an n x n
board so that no two attack each other. Return their (row, col) positions,
or an empty list if it cannot be done. The book's challenge is the 8 x 8
board: 32 knights, 14 bishops, 16 kings, or 8 rooks (the maximum for each).

Constraints:
- 1 <= n <= 8, 0 <= count <= n * n
- Any valid placement is accepted
- Attacks: rook = same row or column; bishop = same diagonal;
  king = adjacent including diagonals; knight = an (1, 2) or (2, 1) jump
- Tests use 7 x 7 for knights (25 pieces) to keep plain backtracking fast;
  32 knights on 8 x 8 is a good stretch goal

How it works (backtracking over squares):
1. Visit squares in row-major order; at each step choose the next square
   (after the last one used) that is not attacked by any placed piece
2. Place a piece there, recurse, and remove it if the recursion fails
3. Prune: if the number of remaining unattacked squares is smaller than
   the number of pieces still needed, give up on this branch
4. Succeed as soon as `count` pieces are placed

Example 1:
Input: piece = "rook", count = 8, n = 8
Output: 8 positions with distinct rows and columns,
e.g. [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]

Example 2:
Input: piece = "king", count = 5, n = 4
Output: []
Explanation: At most one king fits in each 2 x 2 block, so a 4 x 4 board
holds at most 4 nonattacking kings.
"""

from typing import List, Tuple


class Solution:
    def place_pieces(self, piece: str, count: int, n: int = 8) -> List[Tuple[int, int]]:
        """
        Places `count` mutually nonattacking pieces of one type on an n x n board.

        Args:
            piece: One of "knight", "bishop", "king", "rook"
            count: Number of pieces to place
            n: Board size

        Returns:
            List of (row, col) positions, or [] if no placement exists

        Time Complexity: Exponential in the worst case (backtracking)
        Space Complexity: O(n^2) for the board and recursion
        """
        # TODO: Implement backtracking placement with pruning
        pass


def attacks(piece: str, a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    """True if a piece of the given type on square a attacks square b."""
    dr, dc = abs(a[0] - b[0]), abs(a[1] - b[1])
    if piece == "rook":
        return dr == 0 or dc == 0
    if piece == "bishop":
        return dr == dc
    if piece == "king":
        return max(dr, dc) <= 1
    if piece == "knight":
        return {dr, dc} == {1, 2}
    raise ValueError(piece)


def is_valid(piece: str, count: int, n: int, positions: List[Tuple[int, int]]) -> bool:
    """Checks count, board bounds, distinctness, and that nothing attacks."""
    if len(positions) != count or len(set(positions)) != count:
        return False
    if any(not (0 <= r < n and 0 <= c < n) for r, c in positions):
        return False
    return all(
        not attacks(piece, positions[i], positions[j])
        for i in range(count)
        for j in range(i + 1, count)
    )


def test_place_pieces():
    """Test cases for nonattacking piece placement"""
    solution = Solution()

    # Test case 1: 8 rooks on 8 x 8
    result1 = solution.place_pieces("rook", 8, 8)
    assert is_valid("rook", 8, 8, result1)
    print("✓ Test 1 passed: 8 nonattacking rooks on 8 x 8")

    # Test case 2: 16 kings on 8 x 8
    result2 = solution.place_pieces("king", 16, 8)
    assert is_valid("king", 16, 8, result2)
    print("✓ Test 2 passed: 16 nonattacking kings on 8 x 8")

    # Test case 3: 14 bishops on 8 x 8
    result3 = solution.place_pieces("bishop", 14, 8)
    assert is_valid("bishop", 14, 8, result3)
    print("✓ Test 3 passed: 14 nonattacking bishops on 8 x 8")

    # Test case 4: 25 knights on 7 x 7
    result4 = solution.place_pieces("knight", 25, 7)
    assert is_valid("knight", 25, 7, result4)
    print("✓ Test 4 passed: 25 nonattacking knights on 7 x 7")

    # Test case 5: Impossible requests return []
    assert solution.place_pieces("king", 5, 4) == []
    assert solution.place_pieces("rook", 5, 4) == []
    print("✓ Test 5 passed: 5 kings or 5 rooks on 4 x 4 -> []")

    # Test case 6: Zero pieces is trivially possible
    assert solution.place_pieces("bishop", 0, 3) == []
    print("✓ Test 6 passed: 0 pieces -> []")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_place_pieces()
