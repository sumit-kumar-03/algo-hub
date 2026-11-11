"""
EPI 16.3 - Count the Number of Ways to Traverse a 2D Array

Problem:
Starting at the top-left cell of an n x m grid, you may only move right or
down. Count the number of distinct paths that end at the bottom-right cell.

Constraints:
- 1 <= n, m <= 1000 (Python integers handle the large results)
- O(n * m) time, O(min(n, m)) space achievable

How it works (DP, each cell is reached from above or from the left):
1. ways[i][j] = 1 when i == 0 or j == 0 (only one straight path)
2. ways[i][j] = ways[i-1][j] + ways[i][j-1] otherwise
3. Return ways[n-1][m-1]
(A single row updated in place is enough. Closed form:
C(n + m - 2, n - 1).)

Example 1:
Input: n = 5, m = 5
Output: 70

Example 2:
Input: n = 2, m = 2
Output: 2
Explanation: right-down or down-right
"""


class Solution:
    def number_of_ways(self, n: int, m: int) -> int:
        """
        Counts right/down paths from the top-left to the bottom-right cell.

        Args:
            n: Number of rows
            m: Number of columns

        Returns:
            Number of distinct paths

        Time Complexity: O(n * m)
        Space Complexity: O(n * m) (O(min(n, m)) with a single row)
        """
        # TODO: Implement grid path counting DP
        pass


def test_number_of_ways():
    """Test cases for counting grid paths"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.number_of_ways(5, 5) == 70
    print("✓ Test 1 passed: 5x5 -> 70")

    # Test case 2: Single cell
    assert solution.number_of_ways(1, 1) == 1
    print("✓ Test 2 passed: 1x1 -> 1")

    # Test case 3: Single row
    assert solution.number_of_ways(1, 7) == 1
    print("✓ Test 3 passed: 1x7 -> 1")

    # Test case 4: 2x2 grid
    assert solution.number_of_ways(2, 2) == 2
    print("✓ Test 4 passed: 2x2 -> 2")

    # Test case 5: Rectangular grid
    assert solution.number_of_ways(3, 7) == 28
    print("✓ Test 5 passed: 3x7 -> 28")

    # Test case 6: Larger grid
    assert solution.number_of_ways(10, 10) == 48620
    print("✓ Test 6 passed: 10x10 -> 48620")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_number_of_ways()
