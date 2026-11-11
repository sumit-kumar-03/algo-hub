"""
EPI 18.1 - Search a Maze

Problem:
A maze is a 2D grid where 0 is an open cell and 1 is a wall. Given a start
cell and an exit cell, return a path from start to exit as a list of
(row, col) coordinates, moving only up, down, left or right through open
cells. Return [] if no path exists. Any valid path is accepted; it does not
need to be the shortest.

Constraints:
- 1 <= rows, cols <= 500
- start and exit are open cells within the grid
- Do not modify the caller's maze (copy it, or track visited cells separately)

How it works (DFS with backtracking):
1. Mark the current cell visited and append it to the path
2. If it is the exit, return True
3. For each open, unvisited neighbor: if DFS(neighbor) succeeds, return True
4. Otherwise pop the cell from the path (backtrack) and return False
(BFS with parent pointers also works and gives the shortest path.)

Example 1:
Input: maze = [[0, 0, 0],
               [1, 1, 0],
               [0, 0, 0]], start = (0, 0), exit = (2, 0)
Output: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]

Example 2:
Input: maze = [[0, 1],
               [1, 0]], start = (0, 0), exit = (1, 1)
Output: []
"""

from typing import List, Tuple

Coordinate = Tuple[int, int]


class Solution:
    def search_maze(
        self, maze: List[List[int]], start: Coordinate, exit: Coordinate
    ) -> List[Coordinate]:
        """
        Finds a path through the maze from start to exit.

        Args:
            maze: Grid where 0 is open and 1 is a wall
            start: (row, col) of the starting cell
            exit: (row, col) of the exit cell

        Returns:
            List of coordinates from start to exit, or [] if unreachable

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols) for visited cells and the path
        """
        # TODO: Implement maze search with DFS (or BFS)
        pass


def is_valid_path(maze: List[List[int]], path, start: Coordinate, exit: Coordinate) -> bool:
    """Checks that path walks through open, adjacent cells from start to exit."""
    if not isinstance(path, list) or not path or path[0] != start or path[-1] != exit:
        return False
    for r, c in path:
        if not (0 <= r < len(maze) and 0 <= c < len(maze[0])) or maze[r][c] != 0:
            return False
    return all(
        abs(r1 - r2) + abs(c1 - c2) == 1
        for (r1, c1), (r2, c2) in zip(path, path[1:])
    )


def test_search_maze():
    """Test cases for maze search"""
    solution = Solution()

    # Test case 1: Winding path around a wall
    maze1 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    path1 = solution.search_maze([row[:] for row in maze1], (0, 0), (2, 0))
    assert is_valid_path(maze1, path1, (0, 0), (2, 0))
    print(f"✓ Test 1 passed: Winding path = {path1}")

    # Test case 2: Exit unreachable
    maze2 = [
        [0, 1],
        [1, 0],
    ]
    assert solution.search_maze([row[:] for row in maze2], (0, 0), (1, 1)) == []
    print("✓ Test 2 passed: No path returns []")

    # Test case 3: Start equals exit
    assert solution.search_maze([[0]], (0, 0), (0, 0)) == [(0, 0)]
    print("✓ Test 3 passed: Start equals exit")

    # Test case 4: Larger maze with dead ends
    maze4 = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]
    path4 = solution.search_maze([row[:] for row in maze4], (0, 0), (4, 4))
    assert is_valid_path(maze4, path4, (0, 0), (4, 4))
    print(f"✓ Test 4 passed: Larger maze path length = {len(path4)}")

    # Test case 5: Caller's maze is not modified
    maze5 = [[0, 0], [0, 0]]
    solution.search_maze(maze5, (0, 0), (1, 1))
    assert maze5 == [[0, 0], [0, 0]]
    print("✓ Test 5 passed: Input maze unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_search_maze()
