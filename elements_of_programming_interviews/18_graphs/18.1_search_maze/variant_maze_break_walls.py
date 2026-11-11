"""
EPI 18.1 Extra Variant - Shortest Maze Path Breaking at Most k Walls
(Practice problem, not in the book. Difficulty: Medium)
Builds on: BFS through a grid maze, extended so each search state also
records how many walls have been broken so far.

Problem:
A maze is a 2D grid where 0 is an open cell and 1 is a wall. You move one
step up, down, left or right per move. You carry a hammer that can smash
at most k walls in total: stepping onto a wall cell smashes it and uses
one of your k breaks (the cell then counts as part of your path). Return
the minimum number of moves from start to exit, or -1 if the exit cannot
be reached even with k breaks.

Constraints:
- 1 <= rows, cols <= 40
- 0 <= k <= rows * cols
- start and exit are open cells within the grid
- Do not modify the caller's maze
- Target: O(rows * cols * (k + 1)) time and space

How it works (BFS over (cell, breaks used) states):
1. A state is (row, col, used); the start state is (start, 0)
2. BFS from the start state; moving onto a wall increments used
3. Skip moves that would make used > k, and states already seen
4. The first time any state at the exit is popped, its distance is the
   answer (BFS pops states in order of distance)
5. Return -1 when the queue empties

Example 1:
Input: maze = [[0, 1, 0],
               [0, 1, 0],
               [0, 1, 0]], start = (0, 0), exit = (0, 2), k = 1
Output: 2
Explanation: Break the wall at (0, 1) and walk straight across.

Example 2:
Input: same maze, k = 0
Output: -1
Explanation: The middle column is solid, so without breaking a wall the
right side is unreachable.
"""

from typing import List, Tuple

Coordinate = Tuple[int, int]


class Solution:
    def shortest_path_breaking_walls(
        self,
        maze: List[List[int]],
        start: Coordinate,
        exit: Coordinate,
        k: int,
    ) -> int:
        """
        Computes the fewest moves from start to exit breaking <= k walls.

        Args:
            maze: Grid where 0 is open and 1 is a wall
            start: (row, col) of the starting cell
            exit: (row, col) of the exit cell
            k: Maximum number of walls that may be broken

        Returns:
            Minimum number of moves, or -1 if the exit is unreachable

        Time Complexity: O(rows * cols * (k + 1))
        Space Complexity: O(rows * cols * (k + 1))
        """
        # TODO: Implement BFS over (cell, walls broken) states
        pass


def test_maze_break_walls():
    """Test cases for shortest path breaking at most k walls"""
    solution = Solution()
    solid_middle = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]

    # Test case 1: One break opens a shortcut
    assert solution.shortest_path_breaking_walls(solid_middle, (0, 0), (0, 2), 1) == 2
    print("✓ Test 1 passed: One break, 2 moves")

    # Test case 2: No breaks allowed
    assert solution.shortest_path_breaking_walls(solid_middle, (0, 0), (0, 2), 0) == -1
    print("✓ Test 2 passed: k = 0 with a solid wall = -1")

    # Test case 3: k = 0 behaves like plain BFS
    maze3 = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    assert solution.shortest_path_breaking_walls(maze3, (0, 0), (2, 0), 0) == 6
    print("✓ Test 3 passed: k = 0 equals plain shortest path = 6")

    # Test case 4: More breaks keep shortening the path
    maze4 = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
    ]
    results = [
        solution.shortest_path_breaking_walls(maze4, (0, 0), (0, 4), k)
        for k in range(4)
    ]
    assert results == [10, 4, 4, 4]
    print(f"✓ Test 4 passed: k = 0..3 gives {results}")

    # Test case 5: Breaks are a budget across the whole path
    layers = [
        [0, 1, 0, 1, 0, 1, 0],
    ]
    assert solution.shortest_path_breaking_walls(layers, (0, 0), (0, 6), 2) == -1
    assert solution.shortest_path_breaking_walls(layers, (0, 0), (0, 6), 3) == 6
    print("✓ Test 5 passed: Three walls in a row need k = 3")

    # Test case 6: Start equals exit, input unchanged
    snapshot = [row[:] for row in maze4]
    assert solution.shortest_path_breaking_walls(maze4, (3, 2), (3, 2), 5) == 0
    assert maze4 == snapshot
    print("✓ Test 6 passed: Start equals exit = 0, maze unchanged")

    # Test case 7: A larger maze where a fixed budget matters
    n = 21
    big = [[0] * n for _ in range(n)]
    for r in range(1, n, 2):
        for c in range(n):
            big[r][c] = 1
        big[r][n - 1 if (r // 2) % 2 == 0 else 0] = 0
    # Smash straight down column 0 through all 10 wall rows
    assert solution.shortest_path_breaking_walls(big, (0, 0), (n - 1, 0), 10) == 20
    # With no breaks, every corridor must be walked end to end
    assert solution.shortest_path_breaking_walls(big, (0, 0), (n - 1, 0), 0) == 220
    print("✓ Test 7 passed: 21x21 serpentine with k = 10 and k = 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_maze_break_walls()
