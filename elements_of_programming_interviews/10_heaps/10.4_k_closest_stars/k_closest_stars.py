"""
EPI 10.4 - Compute the k Closest Stars

Problem:
Earth sits at the origin (0, 0, 0) and each star is a point (x, y, z). There
are far too many stars to hold in memory, so they arrive as a stream. Return
the k stars that are closest to Earth (Euclidean distance).

Constraints:
- 0 <= k; the stream may contain fewer than k stars (then return all of them)
- Read the stream only once
- Use a max-heap of size k: O(n log k) time, O(k) extra space
- Any order of the returned stars is accepted; ties may be broken arbitrarily

How it works:
1. Keep a max-heap (keyed by distance) of the k closest stars seen so far
2. For each star, push it; if the heap now has k + 1 stars, pop the farthest
3. When the stream ends, the heap holds the answer

Example 1:
Input: stars = [(1, 0, 0), (5, 5, 5), (0, 2, 0), (0, 0, -3), (10, 0, 0)], k = 2
Output: [(1, 0, 0), (0, 2, 0)]   (in any order)
Explanation: Distances are 1, ~8.66, 2, 3, 10; the two smallest are 1 and 2.

Example 2:
Input: stars = [(3, 4, 0)], k = 5
Output: [(3, 4, 0)]
Explanation: Fewer than k stars, so all of them are returned.
"""

import math
from typing import Iterable, List, Tuple

Star = Tuple[float, float, float]


class Solution:
    def find_closest_k_stars(self, stars: Iterable[Star], k: int) -> List[Star]:
        """
        Finds the k stars closest to the origin.

        Args:
            stars: Iterable of (x, y, z) coordinates, read once
            k: Number of stars to return

        Returns:
            List of the min(k, n) closest stars, in any order

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # TODO: Implement with a bounded max-heap
        pass


def _dist(star: Star) -> float:
    return math.sqrt(star[0] ** 2 + star[1] ** 2 + star[2] ** 2)


def _check(stars: List[Star], k: int, result: List[Star]) -> bool:
    """Valid iff result is a sub-multiset of stars of the right size whose
    sorted distances match the k smallest distances."""
    if result is None or len(result) != min(k, len(stars)):
        return False
    pool = list(stars)
    for s in result:
        if s not in pool:
            return False
        pool.remove(s)
    expected = sorted(_dist(s) for s in stars)[:k]
    got = sorted(_dist(s) for s in result)
    return all(math.isclose(a, b) for a, b in zip(expected, got))


def test_find_closest_k_stars():
    """Test cases for the k closest stars"""
    solution = Solution()

    # Test case 1: Basic example
    stars1 = [(1, 0, 0), (5, 5, 5), (0, 2, 0), (0, 0, -3), (10, 0, 0)]
    result1 = solution.find_closest_k_stars(iter(stars1), 2)
    assert _check(stars1, 2, result1) is True
    print(f"✓ Test 1 passed: Two closest -> {result1}")

    # Test case 2: Fewer stars than k
    stars2 = [(3, 4, 0)]
    assert _check(stars2, 5, solution.find_closest_k_stars(iter(stars2), 5)) is True
    print("✓ Test 2 passed: Fewer stars than k")

    # Test case 3: k = 0
    assert solution.find_closest_k_stars(iter([(1, 1, 1)]), 0) == []
    print("✓ Test 3 passed: k = 0")

    # Test case 4: Ties in distance (any valid choice accepted)
    stars4 = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0)]
    result4 = solution.find_closest_k_stars(iter(stars4), 2)
    assert _check(stars4, 2, result4) is True
    print(f"✓ Test 4 passed: Ties -> {result4}")

    # Test case 5: Negative and fractional coordinates
    stars5 = [(-0.5, 0.5, 0.0), (-7, -7, -7), (0.1, -0.1, 0.1), (2, -2, 1), (0, 0, 0)]
    result5 = solution.find_closest_k_stars(iter(stars5), 3)
    assert _check(stars5, 3, result5) is True
    print(f"✓ Test 5 passed: Negative/fractional -> {result5}")

    # Test case 6: Larger deterministic stream from a generator
    stars6 = [((i * 37) % 101 - 50, (i * 53) % 97 - 48, (i * 11) % 89 - 44) for i in range(500)]
    result6 = solution.find_closest_k_stars((s for s in stars6), 10)
    assert _check(stars6, 10, result6) is True
    print("✓ Test 6 passed: 500-star generator, k = 10")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_closest_k_stars()
