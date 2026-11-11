"""
EPI 18.3 - Compute Enclosed Regions

Problem:
A 2D array holds 'W' (white) and 'B' (black) entries. A white entry is
enclosed if there is no path of white entries (moving up, down, left, or
right) from it to the boundary of the array. Replace every enclosed 'W'
with 'B', modifying the array in place.

Constraints:
- 0 <= rows, cols <= 1000
- O(rows * cols) time

How it works (solve the complement: find whites that can escape):
1. Seed a queue with every boundary cell
2. BFS: when a dequeued cell is an in-bounds 'W', mark it as escaping
   (e.g. temporarily set it to 'T') and enqueue its four neighbors
3. Finally, turn every remaining 'W' into 'B' and every 'T' back into 'W'

Example 1:
Input: board = [['B', 'B', 'B', 'B'],
                ['W', 'B', 'W', 'B'],
                ['B', 'W', 'W', 'B'],
                ['B', 'B', 'B', 'B']]
Output: board = [['B', 'B', 'B', 'B'],
                 ['W', 'B', 'B', 'B'],
                 ['B', 'B', 'B', 'B'],
                 ['B', 'B', 'B', 'B']]
Explanation: Three of the four whites are enclosed; (1, 0) touches the edge.

Example 2:
Input: board = [['W', 'W'],
                ['W', 'W']]
Output: unchanged (every white is on the boundary)
"""

from typing import List


class Solution:
    def fill_surrounded_regions(self, board: List[List[str]]) -> None:
        """
        Replaces enclosed 'W' entries with 'B', in place.

        Args:
            board: 2D array of 'W' and 'B' (modified in place)

        Returns:
            None

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols) for the queue
        """
        # TODO: Implement boundary BFS for enclosed regions
        pass


def to_board(rows: List[str]) -> List[List[str]]:
    """Builds a mutable board from strings like 'BWB'."""
    return [list(r) for r in rows]


def test_fill_surrounded_regions():
    """Test cases for enclosed regions"""
    solution = Solution()

    # Test case 1: Book example
    b1 = to_board(["BBBB", "WBWB", "BWWB", "BBBB"])
    solution.fill_surrounded_regions(b1)
    assert b1 == to_board(["BBBB", "WBBB", "BBBB", "BBBB"])
    print("✓ Test 1 passed: book example")

    # Test case 2: All white boundary cells stay
    b2 = to_board(["WW", "WW"])
    solution.fill_surrounded_regions(b2)
    assert b2 == to_board(["WW", "WW"])
    print("✓ Test 2 passed: all-boundary whites unchanged")

    # Test case 3: Single enclosed white
    b3 = to_board(["BBB", "BWB", "BBB"])
    solution.fill_surrounded_regions(b3)
    assert b3 == to_board(["BBB", "BBB", "BBB"])
    print("✓ Test 3 passed: single enclosed white filled")

    # Test case 4: Winding escape path to the boundary
    b4 = to_board(["BBBBB", "BWWWB", "BWBWB", "BWBBB", "BWBBB"])
    solution.fill_surrounded_regions(b4)
    assert b4 == to_board(["BBBBB", "BWWWB", "BWBWB", "BWBBB", "BWBBB"])
    print("✓ Test 4 passed: winding path escapes")

    # Test case 5: Enclosed and escaping regions together
    b5 = to_board(["BBBBBB", "BWWBWB", "BWWBBW", "BBBBWW", "WBBBBB"])
    solution.fill_surrounded_regions(b5)
    assert b5 == to_board(["BBBBBB", "BBBBBB", "BBBBBW", "BBBBWW", "WBBBBB"])
    print("✓ Test 5 passed: mixed regions")

    # Test case 6: Empty board
    b6 = []
    solution.fill_surrounded_regions(b6)
    assert b6 == []
    print("✓ Test 6 passed: empty board")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fill_surrounded_regions()
