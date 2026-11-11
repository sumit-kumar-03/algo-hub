"""
EPI 18.1 Extra Variant - Shortest Path Length in a Maze
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Searching a 2D grid maze; switching from DFS to BFS so the first
time the exit is reached is along a shortest path.

Problem:
A maze is a 2D grid where 0 is an open cell and 1 is a wall. You may move
one step up, down, left or right into an open cell. Given a start cell and
an exit cell, return the minimum number of moves needed to go from start
to exit, or -1 if the exit cannot be reached.

Constraints:
- 1 <= rows, cols <= 500
- start and exit are open cells within the grid
- Do not modify the caller's maze
- Target: O(rows * cols) time and space

How it works (BFS layer by layer):
1. Put start in a queue with distance 0 and mark it visited
2. Pop a cell; if it is the exit, return its distance
3. Push every open, unvisited neighbor with distance + 1
4. If the queue empties, return -1

Example 1:
Input: maze = [[0, 0, 0],
               [1, 1, 0],
               [0, 0, 0]], start = (0, 0), exit = (2, 0)
Output: 6
Explanation: The only route goes right, down the right column, then left.

Example 2:
Input: maze = [[0, 1],
               [1, 0]], start = (0, 0), exit = (1, 1)
Output: -1
Explanation: Diagonal moves are not allowed, so the exit is unreachable.
"""

from typing import List, Tuple

Coordinate = Tuple[int, int]


class Solution:
    def shortest_path_length(
        self, maze: List[List[int]], start: Coordinate, exit: Coordinate
    ) -> int:
        """
        Computes the fewest moves from start to exit.

        Args:
            maze: Grid where 0 is open and 1 is a wall
            start: (row, col) of the starting cell
            exit: (row, col) of the exit cell

        Returns:
            Minimum number of moves, or -1 if the exit is unreachable

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols)
        """
        # TODO: Implement BFS shortest path in a grid
        pass


def test_shortest_maze_path():
    """Test cases for shortest path length in a maze"""
    solution = Solution()

    # Test case 1: Winding corridor
    maze1 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    assert solution.shortest_path_length(maze1, (0, 0), (2, 0)) == 6
    print("✓ Test 1 passed: Winding corridor = 6")

    # Test case 2: Unreachable exit
    assert solution.shortest_path_length([[0, 1], [1, 0]], (0, 0), (1, 1)) == -1
    print("✓ Test 2 passed: Unreachable exit = -1")

    # Test case 3: Start equals exit
    assert solution.shortest_path_length([[0]], (0, 0), (0, 0)) == 0
    print("✓ Test 3 passed: Start equals exit = 0")

    # Test case 4: DFS-style long detour is not the answer
    maze4 = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    assert solution.shortest_path_length(maze4, (0, 0), (4, 4)) == 8
    print("✓ Test 4 passed: Two routes, shortest = 8")

    # Test case 5: Open grid equals Manhattan distance
    open_grid = [[0] * 7 for _ in range(5)]
    assert solution.shortest_path_length(open_grid, (0, 0), (4, 6)) == 10
    assert solution.shortest_path_length(open_grid, (4, 6), (2, 3)) == 5
    print("✓ Test 5 passed: Open grid matches Manhattan distance")

    # Test case 6: Large serpentine maze, input unchanged
    n = 41
    big = [[0] * n for _ in range(n)]
    for r in range(1, n, 2):
        for c in range(n):
            big[r][c] = 1
        gap = n - 1 if (r // 2) % 2 == 0 else 0
        big[r][gap] = 0
    snapshot = [row[:] for row in big]
    # 20 wall rows force a full sweep across each corridor row
    expected = 20 * (n - 1) + (n - 1)
    assert solution.shortest_path_length(big, (0, 0), (n - 1, 0)) == expected
    assert big == snapshot
    print(f"✓ Test 6 passed: 41x41 serpentine = {expected}, maze unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shortest_maze_path()
