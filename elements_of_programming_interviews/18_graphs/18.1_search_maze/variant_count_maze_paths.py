"""
EPI 18.1 Extra Variant - Count All Simple Paths Through a Maze
(Practice problem, not in the book. Difficulty: Medium)
Builds on: DFS with backtracking from the maze search; instead of stopping
at the first path, undo each step and keep exploring to count every path.

Problem:
A maze is a 2D grid where 0 is an open cell and 1 is a wall. A simple path
moves one step up, down, left or right at a time through open cells and
never visits the same cell twice. Count the distinct simple paths from the
start cell to the exit cell. A path ends as soon as it reaches the exit.

Constraints:
- 1 <= rows * cols <= 16 (the count grows exponentially)
- start and exit are open cells within the grid
- Do not modify the caller's maze
- Target: exponential backtracking, O(rows * cols) extra space

How it works (DFS with backtracking):
1. Mark the current cell visited
2. If it is the exit, count 1, unmark it and return
3. Otherwise sum the counts from every open, unvisited neighbor
4. Unmark the cell before returning so other paths may use it

Example 1:
Input: maze = [[0, 0],
               [0, 0]], start = (0, 0), exit = (1, 1)
Output: 2
Explanation: Right-then-down, or down-then-right.

Example 2:
Input: maze = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]], start = (0, 0), exit = (2, 2)
Output: 12
Explanation: Besides the 6 monotone paths, 6 more wander through the
center or snake around the edges without revisiting a cell.
"""

from typing import List, Tuple

Coordinate = Tuple[int, int]


class Solution:
    def count_paths(
        self, maze: List[List[int]], start: Coordinate, exit: Coordinate
    ) -> int:
        """
        Counts simple paths from start to exit.

        Args:
            maze: Grid where 0 is open and 1 is a wall
            start: (row, col) of the starting cell
            exit: (row, col) of the exit cell

        Returns:
            Number of distinct simple paths from start to exit

        Time Complexity: Exponential in rows * cols (backtracking)
        Space Complexity: O(rows * cols) for visited cells and recursion
        """
        # TODO: Implement DFS backtracking that counts every path
        pass


def test_count_maze_paths():
    """Test cases for counting simple paths in a maze"""
    solution = Solution()

    # Test case 1: 2x2 open grid
    assert solution.count_paths([[0, 0], [0, 0]], (0, 0), (1, 1)) == 2
    print("✓ Test 1 passed: 2x2 open grid = 2")

    # Test case 2: 3x3 open grid, corner to corner
    open3 = [[0] * 3 for _ in range(3)]
    assert solution.count_paths(open3, (0, 0), (2, 2)) == 12
    print("✓ Test 2 passed: 3x3 open grid = 12")

    # Test case 3: 4x4 open grid, corner to corner, input unchanged
    open4 = [[0] * 4 for _ in range(4)]
    assert solution.count_paths(open4, (0, 0), (3, 3)) == 184
    assert open4 == [[0] * 4 for _ in range(4)]
    print("✓ Test 3 passed: 4x4 open grid = 184, maze unchanged")

    # Test case 4: Start equals exit
    assert solution.count_paths([[0, 0], [0, 0]], (1, 0), (1, 0)) == 1
    print("✓ Test 4 passed: Start equals exit = 1")

    # Test case 5: Unreachable exit
    assert solution.count_paths([[0, 1], [1, 0]], (0, 0), (1, 1)) == 0
    print("✓ Test 5 passed: Unreachable exit = 0")

    # Test case 6: Single corridor gives exactly one path
    corridor = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    assert solution.count_paths(corridor, (0, 0), (2, 0)) == 1
    print("✓ Test 6 passed: Single corridor = 1")

    # Test case 7: Walls around a 2x2 room with two doors
    room = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    # Around the ring, left or right: 2 ways
    assert solution.count_paths(room, (0, 0), (2, 3)) == 2
    # Middle cell of the top row to the bottom-left corner: 2 ways
    assert solution.count_paths(room, (0, 1), (2, 0)) == 2
    print("✓ Test 7 passed: Ring-shaped maze")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_maze_paths()
