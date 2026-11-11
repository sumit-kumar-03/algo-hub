"""
EPI 4.11 - Rectangle Intersection

Problem:
Each rectangle has sides parallel to the X and Y axes and is described by
its lower-left corner (x, y), its width, and its height. Determine whether
two such rectangles intersect and, if they do, return the rectangle formed
by their intersection. Boundaries count as part of a rectangle, so two
rectangles that only share an edge or a corner do intersect (the result
then has zero width and/or zero height).

Constraints:
- width >= 0 and height >= 0
- Coordinates are integers
- Must run in O(1) time

How it works (treat X and Y independently):
1. The rectangles intersect iff their X intervals overlap and their Y
   intervals overlap:
   R1.x <= R2.x + R2.width and R2.x <= R1.x + R1.width (and same for Y)
2. If they do, the intersection spans
   [max(left edges), min(right edges)] x [max(bottom edges), min(top edges)]
3. Otherwise return None

Example 1:
Input: R1 = (0, 0, 4, 4), R2 = (2, 2, 4, 4)
Output: Rectangle(x=2, y=2, width=2, height=2)
Explanation: The overlap is the square from (2, 2) to (4, 4).

Example 2:
Input: R1 = (0, 0, 1, 1), R2 = (2, 2, 1, 1)
Output: None
Explanation: The X intervals [0, 1] and [2, 3] do not overlap.
"""

from typing import NamedTuple, Optional


class Rectangle(NamedTuple):
    x: int
    y: int
    width: int
    height: int


class Solution:
    def intersect_rectangle(self, r1: Rectangle, r2: Rectangle) -> Optional[Rectangle]:
        """
        Computes the intersection of two XY-aligned rectangles.

        Args:
            r1: First rectangle (lower-left corner, width, height)
            r2: Second rectangle

        Returns:
            The intersection as a Rectangle, or None if they do not intersect

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement rectangle intersection
        pass


def test_intersect_rectangle():
    """Test cases for rectangle intersection implementation"""
    solution = Solution()

    # Test case 1: Partial overlap
    result = solution.intersect_rectangle(Rectangle(0, 0, 4, 4), Rectangle(2, 2, 4, 4))
    assert result == Rectangle(2, 2, 2, 2)
    print(f"✓ Test 1 passed: Partial overlap -> {result}")

    # Test case 2: Disjoint rectangles
    assert solution.intersect_rectangle(Rectangle(0, 0, 1, 1), Rectangle(2, 2, 1, 1)) is None
    print("✓ Test 2 passed: Disjoint rectangles -> None")

    # Test case 3: One rectangle contains the other
    result = solution.intersect_rectangle(Rectangle(0, 0, 10, 10), Rectangle(3, 4, 2, 1))
    assert result == Rectangle(3, 4, 2, 1)
    print(f"✓ Test 3 passed: Containment -> {result}")

    # Test case 4: Shared corner only (boundary counts)
    result = solution.intersect_rectangle(Rectangle(0, 0, 2, 2), Rectangle(2, 2, 3, 3))
    assert result == Rectangle(2, 2, 0, 0)
    print(f"✓ Test 4 passed: Shared corner -> {result}")

    # Test case 5: Shared edge only
    result = solution.intersect_rectangle(Rectangle(0, 0, 2, 3), Rectangle(2, 1, 4, 4))
    assert result == Rectangle(2, 1, 0, 2)
    print(f"✓ Test 5 passed: Shared edge -> {result}")

    # Test case 6: Cross shape
    result = solution.intersect_rectangle(Rectangle(0, 2, 6, 2), Rectangle(2, 0, 2, 6))
    assert result == Rectangle(2, 2, 2, 2)
    print(f"✓ Test 6 passed: Cross shape -> {result}")

    # Test case 7: X intervals overlap but Y intervals do not
    assert solution.intersect_rectangle(Rectangle(0, 0, 5, 1), Rectangle(1, 3, 2, 2)) is None
    print("✓ Test 7 passed: Overlap only in X -> None")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_intersect_rectangle()
