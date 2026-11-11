"""
EPI 4.11 Variant - Check if Four Points Form a Rectangle

Problem:
Given four points in the plane, in any order, determine whether they are
the four vertices of a rectangle. The rectangle does not need to be
aligned with the axes (a rotated square counts). Degenerate inputs, such
as repeated points or points that all lie on one line, are not rectangles.

Constraints:
- Exactly 4 points with integer coordinates
- Must run in O(1) time

How it works (diagonals):
1. A quadrilateral is a rectangle iff its diagonals share a midpoint and
   have equal length
2. Try each way of pairing p0 with another point as a diagonal; the other
   two points form the second diagonal
3. Compare doubled midpoints (to stay in integers) and squared lengths;
   also require all four points to be distinct

Example 1:
Input: points = [(0, 0), (2, 0), (2, 1), (0, 1)]
Output: True
Explanation: An axis-aligned 2 x 1 rectangle.

Example 2:
Input: points = [(0, 0), (2, 0), (3, 1), (1, 1)]
Output: False
Explanation: This is a parallelogram; its diagonals have different lengths.
"""

from typing import List, Tuple


class Solution:
    def is_rectangle(self, points: List[Tuple[int, int]]) -> bool:
        """
        Checks whether four points are the vertices of a rectangle.

        Args:
            points: Four (x, y) integer points, in any order

        Returns:
            True if the points form a non-degenerate rectangle, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement four-point rectangle check
        pass


def test_is_rectangle():
    """Test cases for four-point rectangle check"""
    solution = Solution()

    # Test case 1: Axis-aligned rectangle in order
    assert solution.is_rectangle([(0, 0), (2, 0), (2, 1), (0, 1)]) is True
    print("✓ Test 1 passed: Axis-aligned rectangle")

    # Test case 2: Same rectangle with points shuffled
    assert solution.is_rectangle([(2, 1), (0, 0), (0, 1), (2, 0)]) is True
    print("✓ Test 2 passed: Shuffled vertex order")

    # Test case 3: Rotated rectangle
    assert solution.is_rectangle([(0, 0), (2, 2), (1, 3), (-1, 1)]) is True
    print("✓ Test 3 passed: Rotated rectangle")

    # Test case 4: Parallelogram is not a rectangle
    assert solution.is_rectangle([(0, 0), (2, 0), (3, 1), (1, 1)]) is False
    print("✓ Test 4 passed: Parallelogram -> False")

    # Test case 5: Rhombus (equal sides, unequal diagonals)
    assert solution.is_rectangle([(0, 1), (2, 0), (4, 1), (2, 2)]) is False
    print("✓ Test 5 passed: Rhombus -> False")

    # Test case 6: Degenerate inputs
    assert solution.is_rectangle([(0, 0), (0, 0), (1, 1), (1, 1)]) is False
    assert solution.is_rectangle([(0, 0), (1, 0), (2, 0), (3, 0)]) is False
    print("✓ Test 6 passed: Repeated / collinear points -> False")

    # Test case 7: Kite with a right angle but not a rectangle
    assert solution.is_rectangle([(0, 0), (1, 0), (2, 2), (0, 1)]) is False
    print("✓ Test 7 passed: Kite -> False")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_rectangle()
