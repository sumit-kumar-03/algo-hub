"""
EPI 4.11 Variant - Intersection of Rectangles Not Aligned with the Axes

Problem:
Two rectangles are given by their four vertices listed in order around
the boundary (clockwise or counterclockwise). The rectangles may be
rotated arbitrarily. Determine whether they intersect. Boundaries count:
rectangles that only touch at an edge or corner do intersect, and so do
rectangles where one lies entirely inside the other.

Constraints:
- Each rectangle is a list of 4 integer (x, y) vertices in boundary order
- Rectangles are non-degenerate (positive area)
- Must run in O(1) time

How it works (separating axis theorem):
1. Two convex polygons are disjoint iff some edge normal of one of them is
   a separating axis
2. For each edge of both rectangles, take its normal (-dy, dx) as an axis
3. Project all 8 vertices onto the axis (dot product) and get the
   [min, max] interval of each rectangle
4. If the intervals do not overlap on some axis, return False; if they
   overlap (or touch) on every axis, return True

Example 1:
Input: r1 = [(0, 0), (2, 0), (2, 2), (0, 2)]
       r2 = [(3, 1), (5, 3), (3, 5), (1, 3)]
Output: True
Explanation: An edge of the diamond r2 passes through the corner (2, 2)
of the square r1, so they touch.

Example 2:
Input: r1 = [(0, 0), (2, 0), (2, 2), (0, 2)]
       r2 = [(4, 1), (6, 3), (4, 5), (2, 3)]
Output: False
Explanation: A diagonal axis separates the two shapes even though their
bounding boxes overlap.
"""

from typing import List, Tuple

Point = Tuple[int, int]


class Solution:
    def rectangles_intersect(self, r1: List[Point], r2: List[Point]) -> bool:
        """
        Checks whether two arbitrarily rotated rectangles intersect.

        Args:
            r1: Four vertices of the first rectangle, in boundary order
            r2: Four vertices of the second rectangle, in boundary order

        Returns:
            True if the rectangles share at least one point, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement rotated rectangle intersection test
        pass


def test_rectangles_intersect():
    """Test cases for rotated rectangle intersection"""
    solution = Solution()
    square = [(0, 0), (2, 0), (2, 2), (0, 2)]

    # Test case 1: Overlapping axis-aligned rectangles
    assert solution.rectangles_intersect(square, [(1, 1), (3, 1), (3, 3), (1, 3)]) is True
    print("✓ Test 1 passed: Overlapping axis-aligned rectangles")

    # Test case 2: Diamond edge touching the square's corner
    diamond = [(3, 1), (5, 3), (3, 5), (1, 3)]
    assert solution.rectangles_intersect(square, diamond) is True
    print("✓ Test 2 passed: Touching at a corner counts")

    # Test case 3: Bounding boxes overlap but shapes do not
    shifted = [(x + 1, y) for x, y in diamond]
    assert solution.rectangles_intersect(square, shifted) is False
    print("✓ Test 3 passed: Separated by a diagonal axis")

    # Test case 4: Rotated rectangle fully inside another
    big = [(-10, -10), (10, -10), (10, 10), (-10, 10)]
    small_rotated = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    assert solution.rectangles_intersect(big, small_rotated) is True
    assert solution.rectangles_intersect(small_rotated, big) is True
    print("✓ Test 4 passed: Containment in both argument orders")

    # Test case 5: Far apart rotated rectangles
    a = [(0, 0), (2, 2), (1, 3), (-1, 1)]
    b = [(10, 0), (12, 2), (11, 3), (9, 1)]
    assert solution.rectangles_intersect(a, b) is False
    print("✓ Test 5 passed: Far apart -> False")

    # Test case 6: Cross of two rotated rectangles (no vertex inside the other)
    c1 = [(-4, -3), (-3, -4), (4, 3), (3, 4)]
    c2 = [(-4, 3), (3, -4), (4, -3), (-3, 4)]
    assert solution.rectangles_intersect(c1, c2) is True
    print("✓ Test 6 passed: X-shaped crossing")

    # Test case 7: Clockwise vertex order also works
    assert solution.rectangles_intersect(list(reversed(square)), list(reversed(shifted))) is False
    assert solution.rectangles_intersect(list(reversed(square)), list(reversed(diamond))) is True
    print("✓ Test 7 passed: Clockwise vertex order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_rectangles_intersect()
