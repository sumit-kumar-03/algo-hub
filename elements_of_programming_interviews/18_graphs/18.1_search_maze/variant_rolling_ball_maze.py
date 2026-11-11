"""
EPI 18.1 Extra Variant - Rolling Ball Maze
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Graph search over a maze, but the "neighbors" of a cell are now
the cells where a rolling ball comes to rest, not the adjacent cells.

Problem:
A maze is a 2D grid where 0 is open and 1 is a wall; everything outside the
grid also acts as a wall. A ball sits at start. In one roll you push the
ball up, down, left or right, and it keeps rolling in that direction until
the next cell would be a wall, then stops. The ball can only change
direction once it has stopped. Return the minimum number of rolls needed
for the ball to stop exactly on the exit cell, or -1 if that is
impossible. Rolling over the exit without stopping there does not count.

Constraints:
- 1 <= rows, cols <= 100
- start and exit are open cells within the grid
- Do not modify the caller's maze
- Target: O(rows * cols * (rows + cols)) time, O(rows * cols) space

How it works (BFS over resting positions):
1. BFS from start with 0 rolls; mark resting cells visited
2. For a popped cell, simulate each of the 4 rolls to find where it stops
3. If that stop cell is unvisited, mark it and enqueue it with rolls + 1
4. Return the roll count when the exit is popped, or -1 when the queue
   empties

Example 1:
Input: maze = [[0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 0, 0, 0]], start = (0, 4), exit = (1, 0)
Output: 3
Explanation: Roll left (stops at (0, 3) next to the wall), roll down
(stops at (1, 3) above the wall), roll left (stops at (1, 0)).

Example 2:
Input: maze = [[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]], start = (0, 0), exit = (1, 0)
Output: -1
Explanation: Rolling down from (0, 0) passes (1, 0) and stops at (2, 0);
no roll ever stops on (1, 0).
"""

from typing import List, Tuple

Coordinate = Tuple[int, int]


class Solution:
    def min_rolls(
        self, maze: List[List[int]], start: Coordinate, exit: Coordinate
    ) -> int:
        """
        Computes the fewest rolls that leave the ball resting on exit.

        Args:
            maze: Grid where 0 is open and 1 is a wall
            start: (row, col) where the ball starts at rest
            exit: (row, col) where the ball must stop

        Returns:
            Minimum number of rolls, or -1 if the ball can never stop there

        Time Complexity: O(rows * cols * (rows + cols))
        Space Complexity: O(rows * cols)
        """
        # TODO: Implement BFS over the cells where the ball can stop
        pass


def test_rolling_ball_maze():
    """Test cases for the rolling ball maze"""
    solution = Solution()

    # Test case 1: One roll straight to the corner
    assert solution.min_rolls([[0, 0, 0]], (0, 0), (0, 2)) == 1
    print("✓ Test 1 passed: One roll")

    # Test case 2: Ball rolls past the exit and can never stop on it
    ring = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert solution.min_rolls(ring, (0, 0), (1, 0)) == -1
    print("✓ Test 2 passed: Exit passed over but never a resting point = -1")

    # Test case 3: Start equals exit
    assert solution.min_rolls(ring, (0, 0), (0, 0)) == 0
    print("✓ Test 3 passed: Start equals exit = 0")

    # Test case 4: A wall makes a mid-corridor stop possible
    maze4 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    # (0, 0) -> down (2, 0) -> right (2, 2): 2 rolls
    assert solution.min_rolls(maze4, (0, 0), (2, 2)) == 2
    print("✓ Test 4 passed: Wall stops the ball mid-row = 2")

    # Test case 5: Fewest rolls, not fewest cells
    maze5 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    # e.g. (0, 4) -> left (0, 3) -> down (1, 3) -> left (1, 0) is 3 rolls
    assert solution.min_rolls(maze5, (0, 4), (1, 0)) == 3
    # The only way into row 4 is down column 2, which takes a detour
    assert solution.min_rolls(maze5, (0, 4), (4, 4)) == 7
    print("✓ Test 5 passed: Multi-roll routes")

    # Test case 6: Unreachable region and unchanged input
    maze6 = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
    ]
    snapshot = [row[:] for row in maze6]
    assert solution.min_rolls(maze6, (0, 0), (1, 3)) == -1
    assert maze6 == snapshot
    print("✓ Test 6 passed: Walled-off exit = -1, maze unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_rolling_ball_maze()
