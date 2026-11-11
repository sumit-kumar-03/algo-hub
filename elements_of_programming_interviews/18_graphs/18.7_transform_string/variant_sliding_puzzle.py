"""
EPI 18.7 Extra Variant - Solve a 2x3 Sliding Puzzle
(Practice problem, not in the book. Difficulty: Medium)
Builds on: BFS over states encoded as strings; each move is a small local
change to the string, like changing one letter in a word ladder.

Problem:
A 2x3 board holds the tiles 1..5 and one blank (0). A move slides a tile
that is next to the blank (up, down, left or right) into the blank. Given
the starting board, return the minimum number of moves to reach the
solved board [[1, 2, 3], [4, 5, 0]], or -1 if it can never be solved.

Constraints:
- board is 2x3 and holds each of 0..5 exactly once
- Do not modify the caller's board
- Target: O(6! * 6) time, O(6!) space (only 720 possible states)

How it works (BFS over board strings):
1. Flatten the board to a 6-character string, e.g. "123450"
2. Precompute, for each index of the blank, the indexes it can swap with
   (index i is row i // 3, column i % 3)
3. BFS from the start string; each neighbor swaps the blank with one of
   those indexes
4. Return the distance when "123450" is popped, or -1 if BFS ends first
   (half of all boards are unsolvable)

Example 1:
Input: board = [[1, 2, 3], [4, 0, 5]]
Output: 1
Explanation: Slide 5 left into the blank.

Example 2:
Input: board = [[1, 2, 3], [5, 4, 0]]
Output: -1
Explanation: Swapping two tiles changes the permutation parity; no
sequence of slides can fix it.
"""

from itertools import permutations
from typing import List


class Solution:
    def sliding_puzzle(self, board: List[List[int]]) -> int:
        """
        Computes the fewest slides that solve a 2x3 puzzle.

        Args:
            board: 2x3 grid with tiles 1..5 and 0 for the blank

        Returns:
            Minimum number of moves, or -1 if the board is unsolvable

        Time Complexity: O(6! * 6)
        Space Complexity: O(6!)
        """
        # TODO: Implement BFS over board states
        pass


def test_sliding_puzzle():
    """Test cases for the 2x3 sliding puzzle"""
    solution = Solution()

    # Test case 1: Already solved
    assert solution.sliding_puzzle([[1, 2, 3], [4, 5, 0]]) == 0
    print("✓ Test 1 passed: Solved board = 0")

    # Test case 2: One move away
    assert solution.sliding_puzzle([[1, 2, 3], [4, 0, 5]]) == 1
    print("✓ Test 2 passed: One slide = 1")

    # Test case 3: Unsolvable (two tiles swapped)
    assert solution.sliding_puzzle([[1, 2, 3], [5, 4, 0]]) == -1
    print("✓ Test 3 passed: Swapped tiles = -1")

    # Test case 4: Medium scramble
    assert solution.sliding_puzzle([[4, 1, 2], [5, 0, 3]]) == 5
    print("✓ Test 4 passed: Scramble = 5")

    # Test case 5: Longer scramble
    assert solution.sliding_puzzle([[3, 2, 4], [1, 5, 0]]) == 14
    print("✓ Test 5 passed: Scramble = 14")

    # Test case 6: Exactly half of all 720 boards are solvable, input unchanged
    board = [[4, 1, 2], [5, 0, 3]]
    snapshot = [row[:] for row in board]
    solution.sliding_puzzle(board)
    assert board == snapshot
    solvable = 0
    for p in permutations(range(6)):
        b = [list(p[:3]), list(p[3:])]
        if solution.sliding_puzzle(b) >= 0:
            solvable += 1
    assert solvable == 360
    print("✓ Test 6 passed: 360 of 720 boards solvable, input unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_sliding_puzzle()
