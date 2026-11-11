"""
EPI 16.5 Variant - Search for a Sequence Without Revisiting Cells

Problem:
Same as 16.5, but each grid cell may be used at most once in the walk.
Return whether the pattern can be traced through adjacent cells (up, down,
left, right) without reusing a cell.

Constraints:
- 1 <= rows, cols <= 10, 0 <= len(pattern) <= 15
- An empty pattern always occurs
- Memoizing on (cell, offset) is no longer valid because the set of used
  cells matters; backtracking is exponential in the worst case

How it works (backtracking DFS):
1. For each start cell, run dfs(i, j, k)
2. Fail if (i, j) is out of bounds, already used, or grid[i][j] != pattern[k]
3. If k is the last offset, succeed
4. Mark (i, j) used, try the four neighbors with k + 1, then unmark

Example 1:
Input: grid = [[1, 2, 3],
               [3, 4, 5],
               [5, 6, 7]], pattern = [1, 3, 4, 6]
Output: True

Example 2:
Input: same grid, pattern = [4, 5, 4, 5]
Output: False
Explanation: It needs to reuse (1, 1) and (1, 2).
"""

from typing import List


class Solution:
    def is_pattern_contained_without_revisit(
        self, grid: List[List[int]], pattern: List[int]
    ) -> bool:
        """
        Checks whether pattern can be traced using each cell at most once.

        Args:
            grid: 2D array of integers
            pattern: Sequence of values to trace

        Returns:
            True if the pattern occurs without reusing cells, False otherwise

        Time Complexity: O(rows * cols * 3^len(pattern)) worst case
        Space Complexity: O(len(pattern)) recursion depth plus the used set
        """
        # TODO: Implement backtracking search without revisits
        pass


def test_is_pattern_contained_without_revisit():
    """Test cases for sequence search without revisiting"""
    solution = Solution()
    grid = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

    # Test case 1: Book example still works
    assert solution.is_pattern_contained_without_revisit(grid, [1, 3, 4, 6]) is True
    print("✓ Test 1 passed: [1, 3, 4, 6] found")

    # Test case 2: Needs revisiting, so not allowed
    assert solution.is_pattern_contained_without_revisit(grid, [4, 5, 4, 5]) is False
    print("✓ Test 2 passed: [4, 5, 4, 5] not found")

    # Test case 3: Bouncing back is a revisit
    assert solution.is_pattern_contained_without_revisit(grid, [1, 2, 1]) is False
    print("✓ Test 3 passed: [1, 2, 1] not found")

    # Test case 4: Long snake through distinct cells
    assert solution.is_pattern_contained_without_revisit(grid, [1, 2, 3, 5, 7, 6, 5, 3, 4]) is True
    print("✓ Test 4 passed: snake through all 9 cells found")

    # Test case 5: Equal values, enough cells
    assert solution.is_pattern_contained_without_revisit([[1, 1], [1, 1]], [1, 1, 1, 1]) is True
    print("✓ Test 5 passed: four 1s in a 2x2 grid")

    # Test case 6: Equal values, too few cells
    assert solution.is_pattern_contained_without_revisit([[1, 1], [1, 1]], [1, 1, 1, 1, 1]) is False
    print("✓ Test 6 passed: five 1s do not fit in a 2x2 grid")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_pattern_contained_without_revisit()
