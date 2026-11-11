"""
EPI 16.12 Variant - Maximum Ascending Subset of Points

Problem:
A sequence of points in the plane is ascending if each point is strictly
above and strictly to the right of the previous one. Given a set of points,
return a largest subset that can be arranged as an ascending sequence,
listed in ascending order. Any largest answer is accepted.

Constraints:
- 0 <= len(points) <= 10^4, integer coordinates
- O(n^2) time (O(n log n) with sorting plus a strict LIS)

How it works (sort, then longest increasing subsequence):
1. Sort points by x ascending (break ties by y descending if you use the
   O(n log n) LIS, so two points with the same x cannot both be chosen)
2. Find a longest chain where both x and y strictly increase, using the
   LIS DP with predecessor links
3. Rebuild the chain

Example 1:
Input: points = [(0, 0), (1, 1), (2, 2), (1, 3), (3, 1)]
Output: [(0, 0), (1, 1), (2, 2)]

Example 2:
Input: points = [(1, 1), (1, 2), (2, 1)]
Output: [(1, 1)] (any single point)
Explanation: No pair is strictly above and to the right of the other.
"""

from typing import List, Tuple

Point = Tuple[int, int]


class Solution:
    def max_ascending_points(self, points: List[Point]) -> List[Point]:
        """
        Finds a largest ascending chain of points.

        Args:
            points: Points as (x, y) pairs

        Returns:
            Points of a largest ascending chain, in ascending order

        Time Complexity: O(n^2) (O(n log n) possible)
        Space Complexity: O(n)
        """
        # TODO: Implement maximum ascending point chain
        pass


def is_valid_chain(chain, points: List[Point], expected_length: int) -> bool:
    """Checks the chain uses input points, strictly ascends, and is optimal."""
    if not isinstance(chain, list) or len(chain) != expected_length:
        return False
    remaining = list(points)
    for p in chain:
        if tuple(p) not in remaining:
            return False
        remaining.remove(tuple(p))
    return all(a[0] < b[0] and a[1] < b[1] for a, b in zip(chain, chain[1:]))


def test_max_ascending_points():
    """Test cases for maximum ascending subset of points"""
    solution = Solution()

    cases = [
        ([(0, 0), (1, 1), (2, 2), (1, 3), (3, 1)], 3),
        ([(1, 1), (1, 2), (2, 1)], 1),
        ([(0, 5), (1, 1), (2, 2), (3, 0), (4, 3), (5, 4), (6, 1)], 4),
        ([(5, 5)], 1),
        ([], 0),
    ]
    for n, (points, expected) in enumerate(cases, 1):
        result = solution.max_ascending_points(list(points))
        assert is_valid_chain(result, points, expected)
        print(f"✓ Test {n} passed: {len(points)} points -> chain of {expected}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_ascending_points()
