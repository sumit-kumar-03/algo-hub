"""
EPI 15.2 Variant - Count the Nonattacking Placements of n-Queens

Problem:
Return how many ways there are to place n queens on an n x n chessboard so
that no two share a row, a column, or a diagonal. Only the count is
needed, so don't build the list of placements.

Constraints:
- 1 <= n <= 11
- Known counts for n = 1..10: 1, 0, 0, 2, 10, 4, 40, 92, 352, 724

How it works (backtracking that counts):
1. Place one queen per row, tracking used columns and both diagonal
   directions (row - col and row + col) in sets or bitmasks
2. When a queen is placed in the last row, add 1 to the count
3. Return the sum of the counts from every valid column choice
Tip: bitmasks for columns and diagonals make this very fast.

Example 1:
Input: n = 4
Output: 2

Example 2:
Input: n = 8
Output: 92
"""


class Solution:
    def count_n_queens(self, n: int) -> int:
        """
        Counts the nonattacking placements of n queens on an n x n board.

        Args:
            n: Board size and number of queens

        Returns:
            Number of nonattacking placements

        Time Complexity: O(n!) in the worst case (bounded by the search tree)
        Space Complexity: O(n) recursion depth
        """
        # TODO: Implement counting backtracking
        pass


def test_count_n_queens():
    """Test cases for counting n-Queens placements"""
    solution = Solution()

    # Test case 1: Trivial board
    assert solution.count_n_queens(1) == 1
    print("✓ Test 1 passed: n=1 -> 1")

    # Test case 2: Impossible boards
    assert solution.count_n_queens(2) == 0 and solution.count_n_queens(3) == 0
    print("✓ Test 2 passed: n=2 and n=3 -> 0")

    # Test case 3: Book example size
    assert solution.count_n_queens(4) == 2
    print("✓ Test 3 passed: n=4 -> 2")

    # Test case 4: n = 6 has fewer solutions than n = 5
    assert solution.count_n_queens(5) == 10 and solution.count_n_queens(6) == 4
    print("✓ Test 4 passed: n=5 -> 10, n=6 -> 4")

    # Test case 5: Standard chessboard
    assert solution.count_n_queens(8) == 92
    print("✓ Test 5 passed: n=8 -> 92")

    # Test case 6: n = 10
    assert solution.count_n_queens(10) == 724
    print("✓ Test 6 passed: n=10 -> 724")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_n_queens()
