"""
EPI 11.6 - Search in a 2D Sorted Array

Problem:
A 2D array is "sorted" if every row and every column is nondecreasing. Given
such an array and a number x, decide whether x appears in it.

Constraints:
- 0 <= m, n <= 10^3 (m rows, n columns)
- Must run in O(m + n) time, O(1) extra space
- Binary searching every row (O(m log n)) is not the target

How it works (start from the top-right corner):
1. row, col = 0, n - 1
2. While row < m and col >= 0:
   - A[row][col] == x: return True
   - A[row][col] < x: x is bigger than the whole row, so row += 1
   - A[row][col] > x: x is smaller than the whole column, so col -= 1
3. Return False (each step eliminates a row or a column)

Example 1:
Input: A = [[-1, 2, 4, 4, 6],
            [1, 5, 5, 9, 21],
            [3, 6, 6, 9, 22],
            [3, 6, 8, 10, 24],
            [6, 8, 9, 12, 25],
            [8, 10, 12, 13, 40]], x = 7
Output: False

Example 2:
Input: same A, x = 8
Output: True
"""

from typing import List


class Solution:
    def matrix_search(self, A: List[List[int]], x: int) -> bool:
        """
        Searches for x in a row- and column-sorted matrix.

        Args:
            A: Matrix whose rows and columns are nondecreasing
            x: Value to look for

        Returns:
            True if x is present, otherwise False

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement the staircase search from the top-right corner
        pass


def test_matrix_search():
    """Test cases for 2D sorted array search"""
    solution = Solution()
    A = [
        [-1, 2, 4, 4, 6],
        [1, 5, 5, 9, 21],
        [3, 6, 6, 9, 22],
        [3, 6, 8, 10, 24],
        [6, 8, 9, 12, 25],
        [8, 10, 12, 13, 40],
    ]

    # Test case 1: Absent value inside the range
    assert solution.matrix_search(A, 7) is False
    print("✓ Test 1 passed: 7 not present")

    # Test case 2: Present value
    assert solution.matrix_search(A, 8) is True
    print("✓ Test 2 passed: 8 present")

    # Test case 3: Corners
    assert solution.matrix_search(A, -1) is True
    assert solution.matrix_search(A, 40) is True
    assert solution.matrix_search(A, 6) is True
    assert solution.matrix_search(A, 8) is True
    print("✓ Test 3 passed: All four corners")

    # Test case 4: Out of range
    assert solution.matrix_search(A, -5) is False
    assert solution.matrix_search(A, 41) is False
    print("✓ Test 4 passed: Below min and above max")

    # Test case 5: Empty matrix
    assert solution.matrix_search([], 1) is False
    assert solution.matrix_search([[]], 1) is False
    print("✓ Test 5 passed: Empty matrix")

    # Test case 6: Every value from -2 to 41 against brute force
    present = {v for row in A for v in row}
    for x in range(-2, 42):
        assert solution.matrix_search(A, x) is (x in present)
    print("✓ Test 6 passed: Exhaustive check")

    # Test case 7: Single row and single column
    assert solution.matrix_search([[1, 3, 5]], 3) is True
    assert solution.matrix_search([[1], [3], [5]], 4) is False
    print("✓ Test 7 passed: Single row/column")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_matrix_search()
