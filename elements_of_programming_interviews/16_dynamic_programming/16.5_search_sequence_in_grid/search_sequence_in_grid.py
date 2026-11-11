"""
EPI 16.5 - Search for a Sequence in a 2D Array

Problem:
Given a 2D grid of integers and a 1D pattern, decide whether the pattern
occurs in the grid: you can start at some cell and walk through adjacent
cells (up, down, left, right) so the visited values spell out the pattern in
order. A cell may be visited more than once.

Constraints:
- 1 <= rows, cols <= 100, 0 <= len(pattern) <= 100
- An empty pattern always occurs
- O(rows * cols * len(pattern)) time

How it works (memoized DFS over (row, col, offset)):
1. match(i, j, k) = True if pattern[k:] can be traced starting at (i, j)
2. If k == len(pattern): True
3. If (i, j) is outside the grid or grid[i][j] != pattern[k]: False
4. Otherwise: any of match(neighbor, k + 1) for the four neighbors
5. Cache failures (or all results) by (i, j, k); try every start cell

Example 1:
Input: grid = [[1, 2, 3],
               [3, 4, 5],
               [5, 6, 7]], pattern = [1, 3, 4, 6]
Output: True
Explanation: (0, 0) -> (1, 0) -> (1, 1) -> (2, 1)

Example 2:
Input: same grid, pattern = [1, 2, 3, 4]
Output: False
"""

from typing import List


class Solution:
    def is_pattern_contained_in_grid(
        self, grid: List[List[int]], pattern: List[int]
    ) -> bool:
        """
        Checks whether pattern can be traced through adjacent grid cells.

        Args:
            grid: 2D array of integers
            pattern: Sequence of values to trace

        Returns:
            True if the pattern occurs in the grid, False otherwise

        Time Complexity: O(rows * cols * len(pattern))
        Space Complexity: O(rows * cols * len(pattern)) for the cache
        """
        # TODO: Implement memoized grid pattern search
        pass


def test_is_pattern_contained_in_grid():
    """Test cases for searching a sequence in a 2D array"""
    solution = Solution()
    grid = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

    # Test case 1: Book example (present)
    assert solution.is_pattern_contained_in_grid(grid, [1, 3, 4, 6]) is True
    print("✓ Test 1 passed: [1, 3, 4, 6] found")

    # Test case 2: Book example (absent)
    assert solution.is_pattern_contained_in_grid(grid, [1, 2, 3, 4]) is False
    print("✓ Test 2 passed: [1, 2, 3, 4] not found")

    # Test case 3: Revisiting cells is allowed
    assert solution.is_pattern_contained_in_grid(grid, [4, 5, 4, 5]) is True
    print("✓ Test 3 passed: [4, 5, 4, 5] found by revisiting")

    # Test case 4: Back and forth across the top row
    assert solution.is_pattern_contained_in_grid(grid, [1, 2, 1, 2, 1]) is True
    print("✓ Test 4 passed: [1, 2, 1, 2, 1] found")

    # Test case 5: Single value present / absent
    assert solution.is_pattern_contained_in_grid(grid, [7]) is True
    assert solution.is_pattern_contained_in_grid(grid, [8]) is False
    print("✓ Test 5 passed: single values")

    # Test case 6: Empty pattern
    assert solution.is_pattern_contained_in_grid(grid, []) is True
    print("✓ Test 6 passed: empty pattern found")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_pattern_contained_in_grid()
