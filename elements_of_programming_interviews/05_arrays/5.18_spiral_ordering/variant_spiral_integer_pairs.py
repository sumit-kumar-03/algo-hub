"""
EPI 5.18 Variant - Enumerate Integer Pairs in Spiral Order

Problem:
Starting from (0, 0) and then (1, 0), list the first n integer points
(a, b) of the plane in spiral order. The path winds outward around the
origin: from (1, 0) it goes down, left, up, and right, growing by one
ring each time.

Constraints:
- 0 <= n <= 10^5
- Must run in O(n) time

How it works (segments of lengths 1, 1, 2, 2, 3, 3, ...):
1. Start at (0, 0); the directions cycle through
   right (+1, 0), down (0, -1), left (-1, 0), up (0, +1)
2. Walk 1 step right, 1 down, 2 left, 2 up, 3 right, 3 down, ...
   (each length is used for two consecutive directions)
3. Record every point visited until n points have been collected

Example 1:
Input: n = 10
Output: [(0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1),
         (0, 1), (1, 1), (2, 1)]
Explanation: The first ring around the origin, then the start of the next.

Example 2:
Input: n = 1
Output: [(0, 0)]
Explanation: Only the origin.
"""

from typing import List, Tuple


class Solution:
    def spiral_pairs(self, n: int) -> List[Tuple[int, int]]:
        """
        Lists the first n integer points of the plane in spiral order.

        Args:
            n: Number of points to produce

        Returns:
            List of n (a, b) tuples starting with (0, 0), (1, 0)

        Time Complexity: O(n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement spiral enumeration of integer pairs
        pass


def test_spiral_pairs():
    """Test cases for spiral enumeration of integer pairs"""
    solution = Solution()
    book = [(0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (2, 1)]

    # Test case 1: Book example
    assert solution.spiral_pairs(10) == book
    print("✓ Test 1 passed: n = 10 matches the book")

    # Test case 2: Small n
    assert solution.spiral_pairs(0) == []
    assert solution.spiral_pairs(1) == [(0, 0)]
    assert solution.spiral_pairs(2) == [(0, 0), (1, 0)]
    print("✓ Test 2 passed: n = 0, 1, 2")

    # Test case 3: First 25 points fill the 5 x 5 square around the origin
    pts = solution.spiral_pairs(26)
    assert pts[:10] == book
    assert set(pts[:25]) == {(a, b) for a in range(-2, 3) for b in range(-2, 3)}
    print("✓ Test 3 passed: First 25 points cover [-2, 2] x [-2, 2]")

    # Test case 4: Ring boundaries
    assert pts[24] == (2, 2) and pts[25] == (3, 2)
    print("✓ Test 4 passed: Ring 2 ends at (2, 2); ring 3 starts at (3, 2)")

    # Test case 5: Consecutive points are neighbors and all points are distinct
    many = solution.spiral_pairs(500)
    assert len(many) == 500 and len(set(many)) == 500
    assert all(abs(a1 - a2) + abs(b1 - b2) == 1 for (a1, b1), (a2, b2) in zip(many, many[1:]))
    print("✓ Test 5 passed: 500 distinct points, each one step from the previous")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_spiral_pairs()
