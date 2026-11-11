"""
EPI 17.6 Extra Variant - Minimum Starting Fuel From Every City on the Loop
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the 17.6 running balance and its lowest point, computed for
every possible starting city at once.

Problem:
Same setup as the gasup problem: cities on a circular road, gallons[i] gas
at city i, distances[i] miles from city i to city i + 1 (the last city
wraps to city 0), mpg miles per gallon, unlimited tank. For every city s,
compute the minimum range, in miles, that the tank must already hold when
you start at s (before taking s's gas) so that you can drive the full loop
back to s, taking the gas at every city, without running out. Return the
list of these minimums, one per city.

Constraints:
- 1 <= n <= 10^5, 0 <= gallons[i] <= 10^4, 0 <= distances[i] <= 10^6
- 1 <= mpg <= 100
- O(n) time; running the one-way scan from every city (O(n^2)) is too slow

How it works (prefix balances, lowest point after each start):
1. P[0] = 0 and P[i + 1] = P[i] + gallons[i] * mpg - distances[i]
2. Starting at s, the balance on reaching the city at offset j is
   P[j] - P[s] for s < j <= n, and P[n] + P[j] - P[s] after wrapping
   (1 <= j <= s)
3. The answer for s is max(0, P[s] - m), where m is the smallest of
   min(P[s+1..n]) and P[n] + min(P[1..s])
4. Precompute suffix minimums of P[1..n] and prefix minimums, then fill in
   every answer in one pass
(A sliding-window minimum over a doubled array also works.)

Example 1:
Input: gallons = [2, 0, 2, 0], distances = [20, 20, 20, 20], mpg = 20
Output: [0, 20, 0, 20]
Explanation: From city 1 the first leg needs 20 miles with no gas there;
after that the loop pays for itself.

Example 2:
Input: gallons = [1, 1], distances = [30, 30], mpg = 20
Output: [20, 20]
Explanation: The loop is 20 miles short no matter where you start.
"""

from typing import List


class Solution:
    def min_start_range_each_city(
        self, gallons: List[int], distances: List[int], mpg: int
    ) -> List[int]:
        """
        Computes the minimum starting range for a full loop from each city.

        Args:
            gallons: Gas available at each city
            distances: Miles from each city to the next one (circular)
            mpg: Miles per gallon

        Returns:
            List where entry s is the minimum starting range from city s

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement prefix balances with prefix and suffix minimums
        pass


def simulate_min_start(s: int, gallons: List[int], distances: List[int], mpg: int) -> int:
    """Finds the deepest dip of the loop from city s by direct simulation."""
    n = len(gallons)
    balance, lowest = 0, 0
    for k in range(n):
        i = (s + k) % n
        balance += gallons[i] * mpg - distances[i]
        lowest = min(lowest, balance)
    return -lowest


def test_min_start_range_each_city():
    """Test cases for the minimum starting fuel from every city"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.min_start_range_each_city([2, 0, 2, 0], [20] * 4, 20) == [0, 20, 0, 20]
    print("✓ Test 1 passed: [2, 0, 2, 0] -> [0, 20, 0, 20]")

    # Test case 2: Example 2 (no ample city)
    assert solution.min_start_range_each_city([1, 1], [30, 30], 20) == [20, 20]
    print("✓ Test 2 passed: [1, 1] -> [20, 20]")

    # Test case 3: Single city
    assert solution.min_start_range_each_city([0], [35], 20) == [35]
    print("✓ Test 3 passed: single city -> [35]")

    # Test case 4: Book example; only city 3 needs nothing
    g4, d4 = [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]
    assert solution.min_start_range_each_city(g4, d4, 20) == [
        simulate_min_start(s, g4, d4, 20) for s in range(7)
    ]
    assert solution.min_start_range_each_city(g4, d4, 20)[3] == 0
    print("✓ Test 4 passed: book example")

    # Test case 5: Deficit far from the start
    assert solution.min_start_range_each_city([0, 0, 5], [10, 10, 10], 10) == [20, 10, 0]
    print("✓ Test 5 passed: [0, 0, 5] -> [20, 10, 0]")

    # Test case 6: Random small cases against simulation
    import random
    rng = random.Random(1760)
    for _ in range(300):
        n = rng.randint(1, 8)
        g = [rng.randint(0, 3) for _ in range(n)]
        d = [rng.randint(0, 60) for _ in range(n)]
        expected = [simulate_min_start(s, g, d, 20) for s in range(n)]
        assert solution.min_start_range_each_city(g, d, 20) == expected
    print("✓ Test 6 passed: 300 random cases match simulation")

    # Test case 7: Large input
    n = 100000
    g7 = [2 if i % 2 == 0 else 0 for i in range(n)]
    d7 = [20] * n
    r7 = solution.min_start_range_each_city(g7, d7, 20)
    assert r7 == [0 if i % 2 == 0 else 20 for i in range(n)]
    print("✓ Test 7 passed: 100000 cities")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_start_range_each_city()
