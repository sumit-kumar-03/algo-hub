"""
EPI 17.6 Extra Variant - Minimum Starting Fuel for a One-Way Trip
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the 17.6 running fuel balance, where the lowest point of the
running total decides everything.

Problem:
Cities 0, 1, ..., n - 1 lie along a straight road, and a destination lies
beyond the last city. City i has gallons[i] gallons of gas, and the next
stop (city i + 1, or the destination for the last city) is distances[i]
miles away. The car gets mpg miles per gallon and has an unlimited tank.
You start at city 0 and take all the gas at every city you reach. Return
the minimum range, in miles, that the tank must already hold before you
fill up at city 0 so that you never run out of gas before the destination.
(Running exactly to empty when arriving somewhere is fine.)

Constraints:
- 1 <= n <= 10^5, 0 <= gallons[i] <= 10^4, 0 <= distances[i] <= 10^6
- 1 <= mpg <= 100
- O(n) time, O(1) extra space

How it works (track the lowest running balance):
1. balance = 0; lowest = 0
2. For each city i in order: balance += gallons[i] * mpg - distances[i]
   (the range left on arrival at the next stop); lowest = min(lowest, balance)
3. The tank must make up for the deepest dip: return -lowest

Example 1:
Input: gallons = [1, 3, 0], distances = [30, 40, 50], mpg = 20
Output: 40
Explanation: The running balances on arrival at each stop are -10, 10,
and -40. The deepest dip is -40, so the tank must start with 40 miles.

Example 2:
Input: gallons = [5, 5], distances = [50, 50], mpg = 20
Output: 0
Explanation: Plenty of gas everywhere.
"""

from typing import List


class Solution:
    def min_initial_range(self, gallons: List[int], distances: List[int], mpg: int) -> int:
        """
        Returns the minimum starting range needed to reach the destination.

        Args:
            gallons: Gas available at each city
            distances: Miles from each city to the next stop
            mpg: Miles per gallon

        Returns:
            Minimum starting range in miles (0 if none is needed)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement the lowest running balance scan
        pass


def test_min_initial_range():
    """Test cases for the minimum starting fuel"""
    solution = Solution()

    # Test case 1: Example 1 (deepest dip at the end)
    assert solution.min_initial_range([1, 3, 0], [30, 40, 50], 20) == 40
    print("✓ Test 1 passed: [1, 3, 0] -> 40")

    # Test case 2: Example 2 (no extra fuel needed)
    assert solution.min_initial_range([5, 5], [50, 50], 20) == 0
    print("✓ Test 2 passed: [5, 5] -> 0")

    # Test case 3: Single city
    assert solution.min_initial_range([0], [25], 20) == 25
    assert solution.min_initial_range([2], [25], 20) == 0
    print("✓ Test 3 passed: single city")

    # Test case 4: Running exactly to empty is fine
    assert solution.min_initial_range([1, 1, 1], [20, 20, 20], 20) == 0
    print("✓ Test 4 passed: exact fuel -> 0")

    # Test case 5: Deepest dip in the middle, recovery afterwards
    assert solution.min_initial_range([0, 0, 10, 0], [10, 15, 5, 10], 20) == 25
    print("✓ Test 5 passed: dip in the middle -> 25")

    # Test case 6: Zero-length legs and mpg = 1
    assert solution.min_initial_range([0, 3, 0, 0], [0, 5, 0, 1], 1) == 3
    print("✓ Test 6 passed: zero-length legs -> 3")

    # Test case 7: Long road
    n = 100000
    g7 = [1] * n
    d7 = [21] * n  # each leg loses 1 mile of range
    assert solution.min_initial_range(g7, d7, 20) == n
    print("✓ Test 7 passed: 100000 cities -> 100000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_initial_range()
