"""
EPI 5.18 Variant - Generate a Spiral Matrix

Problem:
Given a dimension d, build a d x d 2D array whose spiral order (clockwise,
starting at the top-left corner) is 1, 2, 3, ..., d^2.

Constraints:
- 0 <= d <= 1000 (d = 0 gives an empty list)
- Must run in O(d^2) time

How it works (walk the spiral and write values):
1. Start with a d x d grid of zeros at position (0, 0), heading right
2. For value from 1 to d^2:
   - Write value at the current cell
   - If the next cell in the current direction is outside the grid or
     already filled, turn clockwise (right -> down -> left -> up)
   - Step to the next cell

Example 1:
Input: d = 3
Output: [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
Explanation: Reading in spiral order gives 1 through 9.

Example 2:
Input: d = 2
Output: [[1, 2],
         [4, 3]]
Explanation: Right, down, left.
"""

from typing import List


class Solution:
    def generate_spiral_matrix(self, d: int) -> List[List[int]]:
        """
        Builds a d x d matrix whose spiral order is 1..d^2.

        Args:
            d: Dimension of the square matrix

        Returns:
            The d x d matrix (empty list if d == 0)

        Time Complexity: O(d^2)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement spiral matrix generation
        pass


def test_generate_spiral_matrix():
    """Test cases for spiral matrix generation"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.generate_spiral_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print("✓ Test 1 passed: d = 3")

    # Test case 2: d = 2
    assert solution.generate_spiral_matrix(2) == [[1, 2], [4, 3]]
    print("✓ Test 2 passed: d = 2")

    # Test case 3: d = 1 and d = 0
    assert solution.generate_spiral_matrix(1) == [[1]]
    assert solution.generate_spiral_matrix(0) == []
    print("✓ Test 3 passed: d = 1 and d = 0")

    # Test case 4: d = 4
    assert solution.generate_spiral_matrix(4) == [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    print("✓ Test 4 passed: d = 4")

    # Test case 5: d = 5
    assert solution.generate_spiral_matrix(5) == [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]
    print("✓ Test 5 passed: d = 5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_generate_spiral_matrix()
