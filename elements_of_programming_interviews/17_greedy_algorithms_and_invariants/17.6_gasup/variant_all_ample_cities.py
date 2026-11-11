"""
EPI 17.6 Extra Variant - Find Every Ample City
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the 17.6 running fuel balance, now asking for every city whose
balance is a low point of the whole circular route, not just one of them.

Problem:
Same setup as the gasup problem: cities on a circular road, gallons[i] gas
at city i, distances[i] miles from city i to city i + 1 (the last city
wraps to city 0), mpg miles per gallon, unlimited tank. A city is ample if
you can start there with an empty tank, take its gas, and drive the whole
loop back to it (taking the gas at every city) without running out. The
total gas is not guaranteed to cover the loop. Return the indices of all
ample cities in increasing order (an empty list if there are none).

Constraints:
- 1 <= n <= 10^5, 0 <= gallons[i] <= 10^4, 0 <= distances[i] <= 10^6
- 1 <= mpg <= 100
- O(n) time; simulating from every city (O(n^2)) is too slow

How it works (prefix balances plus prefix and suffix minimums):
1. P[0] = 0 and P[i + 1] = P[i] + gallons[i] * mpg - distances[i]; P[i] is
   the balance on arrival at city i when starting from city 0, and
   P[n] = total surplus of the loop
2. Starting at city s, the balance on reaching a later city j (s < j <= n)
   is P[j] - P[s]; after wrapping, on reaching city j (1 <= j <= s) it is
   P[n] + P[j] - P[s] (j = s means arriving back at the start)
3. So s is ample iff P[s] <= min(P[s+1..n]) and P[s] <= P[n] + min(P[1..s])
   (the second condition is empty for s = 0)
4. Precompute suffix minimums of P and prefix minimums, then test each s

Example 1:
Input: gallons = [2, 0, 2, 0], distances = [20, 20, 20, 20], mpg = 20
Output: [0, 2]
Explanation: From city 0 or city 2 you always arrive with enough gas;
starting at city 1 or 3 you run out on the very first leg.

Example 2:
Input: gallons = [1, 1], distances = [30, 30], mpg = 20
Output: []
Explanation: The loop is 60 miles but there are only 40 miles of gas.
"""

from typing import List


class Solution:
    def all_ample_cities(self, gallons: List[int], distances: List[int], mpg: int) -> List[int]:
        """
        Finds every city from which the full loop can be driven.

        Args:
            gallons: Gas available at each city
            distances: Miles from each city to the next one (circular)
            mpg: Miles per gallon

        Returns:
            Sorted list of ample city indices

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement prefix balances with prefix and suffix minimums
        pass


def is_ample(city: int, gallons: List[int], distances: List[int], mpg: int) -> bool:
    """Simulates the loop starting at city with an empty tank."""
    n = len(gallons)
    tank = 0
    for k in range(n):
        i = (city + k) % n
        tank += gallons[i] * mpg - distances[i]
        if tank < 0:
            return False
    return True


def test_all_ample_cities():
    """Test cases for finding every ample city"""
    solution = Solution()

    # Test case 1: Book example has a single ample city
    g1, d1 = [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]
    assert solution.all_ample_cities(g1, d1, 20) == [3]
    print("✓ Test 1 passed: book example -> [3]")

    # Test case 2: Example 1 (two ample cities)
    assert solution.all_ample_cities([2, 0, 2, 0], [20, 20, 20, 20], 20) == [0, 2]
    print("✓ Test 2 passed: [2, 0, 2, 0] -> [0, 2]")

    # Test case 3: Example 2 (not enough gas overall)
    assert solution.all_ample_cities([1, 1], [30, 30], 20) == []
    print("✓ Test 3 passed: [1, 1] -> []")

    # Test case 4: Single city
    assert solution.all_ample_cities([5], [100], 20) == [0]
    assert solution.all_ample_cities([4], [100], 20) == []
    print("✓ Test 4 passed: single city")

    # Test case 5: Surplus everywhere makes every city ample
    assert solution.all_ample_cities([3, 3, 3], [10, 20, 30], 20) == [0, 1, 2]
    print("✓ Test 5 passed: surplus everywhere -> [0, 1, 2]")

    # Test case 6: Random small cases against simulation
    import random
    rng = random.Random(176)
    for _ in range(300):
        n = rng.randint(1, 8)
        g = [rng.randint(0, 3) for _ in range(n)]
        d = [rng.randint(0, 60) for _ in range(n)]
        expected = [c for c in range(n) if is_ample(c, g, d, 20)]
        assert solution.all_ample_cities(g, d, 20) == expected
    print("✓ Test 6 passed: 300 random cases match simulation")

    # Test case 7: Large input with ample cities at every third index
    n = 99999
    g7 = [3 if i % 3 == 0 else 0 for i in range(n)]
    d7 = [20] * n
    assert solution.all_ample_cities(g7, d7, 20) == list(range(0, n, 3))
    print("✓ Test 7 passed: 99999 cities -> every third city")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_all_ample_cities()
