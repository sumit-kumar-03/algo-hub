"""
EPI 16.3 Variant - Count Paths in a 2D Array with Obstacles

Problem:
Same as 16.3, but some cells are blocked. The grid is given as a Boolean
2D array where True marks an obstacle. Count the right/down paths from the
top-left cell to the bottom-right cell that never step on an obstacle.

Constraints:
- 1 <= rows, cols <= 1000
- If the start or end cell is blocked, the answer is 0
- O(rows * cols) time

How it works (DP with blocked cells forced to zero):
1. ways[i][j] = 0 if obstacles[i][j]
2. ways[0][0] = 1 if the start is open
3. Otherwise ways[i][j] = ways[i-1][j] + ways[i][j-1] (missing neighbors
   count as 0)
4. Return ways[rows-1][cols-1]

Example 1:
Input: obstacles = [[F, F, F],
                    [F, T, F],
                    [F, F, F]]
Output: 2
Explanation: Go around the center either along the top-right or the bottom-left.

Example 2:
Input: obstacles = [[F, T],
                    [T, F]]
Output: 0
"""

from typing import List


class Solution:
    def number_of_ways_with_obstacles(self, obstacles: List[List[bool]]) -> int:
        """
        Counts right/down paths that avoid obstacles.

        Args:
            obstacles: Grid where True marks a blocked cell

        Returns:
            Number of obstacle-free paths from top-left to bottom-right

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols) (O(cols) with a single row)
        """
        # TODO: Implement path counting with obstacles
        pass


def test_number_of_ways_with_obstacles():
    """Test cases for grid paths with obstacles"""
    solution = Solution()
    F, T = False, True

    # Test case 1: Blocked center
    assert solution.number_of_ways_with_obstacles([[F, F, F], [F, T, F], [F, F, F]]) == 2
    print("✓ Test 1 passed: blocked center -> 2")

    # Test case 2: No obstacles matches 16.3
    assert solution.number_of_ways_with_obstacles([[F] * 5 for _ in range(5)]) == 70
    print("✓ Test 2 passed: open 5x5 -> 70")

    # Test case 3: Blocked start
    assert solution.number_of_ways_with_obstacles([[T, F], [F, F]]) == 0
    print("✓ Test 3 passed: blocked start -> 0")

    # Test case 4: Walled off
    assert solution.number_of_ways_with_obstacles([[F, T], [T, F]]) == 0
    print("✓ Test 4 passed: walled off -> 0")

    # Test case 5: Several obstacles
    grid = [
        [F, F, F, F],
        [F, T, F, F],
        [F, F, F, T],
        [T, F, F, F],
    ]
    assert solution.number_of_ways_with_obstacles(grid) == 3
    print("✓ Test 5 passed: 4x4 with obstacles -> 3")

    # Test case 6: Single open cell
    assert solution.number_of_ways_with_obstacles([[F]]) == 1
    print("✓ Test 6 passed: single open cell -> 1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_number_of_ways_with_obstacles()
