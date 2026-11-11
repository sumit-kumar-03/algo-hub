"""
EPI 16.3 Variant - Maximum Fish on a Path (Fixed Corners)

Problem:
A fisherman crosses a rectangular sea from the top-left point to the
bottom-right point, moving only down or right. sea[i][j] is the value of the
fish at point (i, j), collected when he passes through it. Return the
maximum total value he can collect.

Constraints:
- 1 <= rows, cols <= 1000
- 0 <= sea[i][j] <= 10^6
- O(rows * cols) time

How it works (DP, best value to reach each cell):
1. best[0][0] = sea[0][0]
2. best[i][j] = sea[i][j] + max(best[i-1][j], best[i][j-1]) using only the
   neighbors that exist
3. Return best[rows-1][cols-1]

Example 1:
Input: sea = [[1, 3, 1],
              [1, 5, 1],
              [4, 2, 1]]
Output: 12
Explanation: 1 -> 3 -> 5 -> 2 -> 1

Example 2:
Input: sea = [[1, 2, 3]]
Output: 6
"""

from typing import List


class Solution:
    def max_fish(self, sea: List[List[int]]) -> int:
        """
        Computes the maximum fish value on a down/right path between corners.

        Args:
            sea: 2D array of fish values

        Returns:
            Maximum total value collected from top-left to bottom-right

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols) (O(cols) with a single row)
        """
        # TODO: Implement max-value path DP
        pass


def test_max_fish():
    """Test cases for the fisherman problem"""
    solution = Solution()

    # Test case 1: Standard grid
    assert solution.max_fish([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 12
    print("✓ Test 1 passed: 3x3 grid -> 12")

    # Test case 2: Single cell
    assert solution.max_fish([[7]]) == 7
    print("✓ Test 2 passed: single cell -> 7")

    # Test case 3: Single row
    assert solution.max_fish([[1, 2, 3]]) == 6
    print("✓ Test 3 passed: single row -> 6")

    # Test case 4: Can only reach one of two rich cells
    assert solution.max_fish([[0, 0, 9], [9, 0, 0], [0, 0, 0]]) == 9
    print("✓ Test 4 passed: two rich cells -> 9")

    # Test case 5: Tall grid
    assert solution.max_fish([[1, 2], [3, 4], [5, 6]]) == 15
    print("✓ Test 5 passed: 3x2 grid -> 15")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_fish()
