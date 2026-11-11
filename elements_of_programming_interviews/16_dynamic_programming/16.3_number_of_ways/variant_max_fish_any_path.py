"""
EPI 16.3 Variant - Maximum Fish on a Path (Any Start and End)

Problem:
Same as the fisherman variant, but now the fisherman may start and stop at
any point of the sea, still moving only down or right. Fish values can be
negative. Return the maximum total value of a non-empty down/right path.

Constraints:
- 1 <= rows, cols <= 1000
- -10^6 <= sea[i][j] <= 10^6
- The path must contain at least one cell
- O(rows * cols) time

How it works (Kadane's idea on a grid):
1. best[i][j] = best total of a path that ends at (i, j)
2. best[i][j] = sea[i][j] + max(0, best[i-1][j], best[i][j-1]); the 0 means
   "start fresh here"
3. Return the maximum best[i][j] over all cells

Example 1:
Input: sea = [[1, -5, 2],
              [-1, 4, 3],
              [-10, 1, -2]]
Output: 7
Explanation: Start at 4, move right to 3.

Example 2:
Input: sea = [[-3, -1],
              [-2, -4]]
Output: -1
Explanation: Every value is negative, so take the single best cell.
"""

from typing import List


class Solution:
    def max_fish_any_path(self, sea: List[List[int]]) -> int:
        """
        Computes the best down/right path value with free start and end.

        Args:
            sea: 2D array of fish values (may be negative)

        Returns:
            Maximum total of any non-empty down/right path

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols) (O(cols) with a single row)
        """
        # TODO: Implement max-value path with free endpoints
        pass


def test_max_fish_any_path():
    """Test cases for the free-endpoint fisherman problem"""
    solution = Solution()

    # Test case 1: Mixed values
    assert solution.max_fish_any_path([[1, -5, 2], [-1, 4, 3], [-10, 1, -2]]) == 7
    print("✓ Test 1 passed: mixed grid -> 7")

    # Test case 2: All negative
    assert solution.max_fish_any_path([[-3, -1], [-2, -4]]) == -1
    print("✓ Test 2 passed: all negative -> -1")

    # Test case 3: Single cell
    assert solution.max_fish_any_path([[5]]) == 5
    print("✓ Test 3 passed: single cell -> 5")

    # Test case 4: All positive behaves like the corner-to-corner version
    assert solution.max_fish_any_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 12
    print("✓ Test 4 passed: all positive -> 12")

    # Test case 5: Skip the negative start
    assert solution.max_fish_any_path([[2, -9, 4], [-9, -9, 5]]) == 9
    print("✓ Test 5 passed: start mid-grid -> 9")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_fish_any_path()
