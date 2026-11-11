"""
EPI 16.5 Variant - Enumerate All Occurrences of a Sequence in a 2D Array

Problem:
Given a grid and a non-empty pattern, return every walk through adjacent
cells (up, down, left, right) that spells the pattern without using any
cell more than once. Each walk is a list of (row, col) coordinates. The
order of the walks in the result does not matter.

Constraints:
- 1 <= rows, cols <= 6, 1 <= len(pattern) <= 10
- Output size can be exponential; backtracking is expected

How it works (backtracking DFS that records full paths):
1. For each start cell, dfs(i, j, k) with a current path
2. Stop if out of bounds, already on the path, or grid[i][j] != pattern[k]
3. Append (i, j); if k is the last offset, save a copy of the path,
   otherwise recurse into the four neighbors
4. Pop (i, j) before returning

Example 1:
Input: grid = [[1, 2, 3],
               [3, 4, 5],
               [5, 6, 7]], pattern = [1, 3, 4, 6]
Output: [[(0, 0), (1, 0), (1, 1), (2, 1)]]

Example 2:
Input: same grid, pattern = [5]
Output: [[(1, 2)], [(2, 0)]] (in any order)
"""

from typing import List, Tuple

Coordinate = Tuple[int, int]


class Solution:
    def find_all_pattern_paths(
        self, grid: List[List[int]], pattern: List[int]
    ) -> List[List[Coordinate]]:
        """
        Lists every non-revisiting walk that spells pattern.

        Args:
            grid: 2D array of integers
            pattern: Non-empty sequence of values to trace

        Returns:
            All walks, each as a list of (row, col) coordinates

        Time Complexity: O(rows * cols * 3^len(pattern)) worst case
        Space Complexity: O(len(pattern)) besides the output
        """
        # TODO: Implement enumeration of all pattern walks
        pass


def normalize(paths) -> List[List[Coordinate]]:
    """Sorts walks so results can be compared regardless of order."""
    return sorted([tuple(p) for p in path] for path in paths)


def test_find_all_pattern_paths():
    """Test cases for enumerating pattern walks"""
    solution = Solution()
    grid = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

    # Test case 1: Book example has exactly one walk
    assert normalize(solution.find_all_pattern_paths(grid, [1, 3, 4, 6])) == [
        [(0, 0), (1, 0), (1, 1), (2, 1)]
    ]
    print("✓ Test 1 passed: [1, 3, 4, 6] -> one walk")

    # Test case 2: Pattern absent
    assert solution.find_all_pattern_paths(grid, [1, 2, 3, 4]) == []
    print("✓ Test 2 passed: [1, 2, 3, 4] -> no walks")

    # Test case 3: Single value appearing twice
    assert normalize(solution.find_all_pattern_paths(grid, [5])) == [[(1, 2)], [(2, 0)]]
    print("✓ Test 3 passed: [5] -> two walks")

    # Test case 4: Two-step pattern with one placement
    assert normalize(solution.find_all_pattern_paths(grid, [3, 4])) == [[(1, 0), (1, 1)]]
    print("✓ Test 4 passed: [3, 4] -> one walk")

    # Test case 5: All-equal grid; 4 starts x 2 directions
    result = normalize(solution.find_all_pattern_paths([[1, 1], [1, 1]], [1, 1, 1]))
    expected = normalize([
        [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)],
        [(0, 1), (0, 0), (1, 0)], [(0, 1), (1, 1), (1, 0)],
        [(1, 0), (0, 0), (0, 1)], [(1, 0), (1, 1), (0, 1)],
        [(1, 1), (0, 1), (0, 0)], [(1, 1), (1, 0), (0, 0)],
    ])
    assert result == expected
    print("✓ Test 5 passed: 2x2 of 1s, [1, 1, 1] -> 8 walks")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_all_pattern_paths()
