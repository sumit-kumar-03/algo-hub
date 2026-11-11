"""
EPI 17.6 Variant - The Gasup Problem Without a Guaranteed Ample City

Problem:
Same setup as the gasup problem, but the total gas is no longer guaranteed
to match the loop length, so an ample city may not exist. Return the index
of an ample city, or -1 if there is none. If several cities are ample, any
of them is accepted.

Constraints:
- 1 <= n <= 10^5
- O(n) time, O(1) space

How it works:
1. If sum(gallons) * mpg < sum(distances), no city can work: return -1
2. Otherwise run the same "lowest running fuel" scan as 17.6; the city at
   the minimum is ample (extra gas only helps)
3. (Optionally confirm by simulating once from that city)

Example 1:
Input: gallons = [50, 20, 5, 30, 25, 10, 10],
       distances = [900, 600, 200, 400, 600, 200, 100], mpg = 20
Output: 3

Example 2:
Input: gallons = [1, 1], distances = [30, 30], mpg = 20
Output: -1
Explanation: 40 miles of gas for a 60-mile loop.
"""

from typing import List


class Solution:
    def find_ample_city_if_exists(
        self, gallons: List[int], distances: List[int], mpg: int = 20
    ) -> int:
        """
        Finds an ample city, or reports that none exists.

        Args:
            gallons: Gas available at each city
            distances: Miles from each city to the next one
            mpg: Miles per gallon of the car

        Returns:
            Index of an ample city, or -1 if there is none

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement ample city search without the existence guarantee
        pass


def is_ample(city, gallons: List[int], distances: List[int], mpg: int) -> bool:
    """Simulates the loop starting at city with an empty tank."""
    n = len(gallons)
    if not isinstance(city, int) or not 0 <= city < n:
        return False
    tank = 0
    for k in range(n):
        i = (city + k) % n
        tank += gallons[i] * mpg - distances[i]
        if tank < 0:
            return False
    return True


def test_find_ample_city_if_exists():
    """Test cases for gasup without an existence guarantee"""
    solution = Solution()

    # Test case 1: Book example still works
    g1, d1 = [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]
    assert solution.find_ample_city_if_exists(g1, d1, 20) == 3
    print("✓ Test 1 passed: book example -> city 3")

    # Test case 2: Not enough gas overall
    assert solution.find_ample_city_if_exists([1, 1], [30, 30], 20) == -1
    print("✓ Test 2 passed: not enough gas -> -1")

    # Test case 3: Surplus gas, several ample cities
    g3, d3 = [5, 5, 5], [20, 20, 20]
    r3 = solution.find_ample_city_if_exists(g3, d3, 20)
    assert is_ample(r3, g3, d3, 20)
    print(f"✓ Test 3 passed: surplus gas, returned {r3}")

    # Test case 4: Surplus gas, only one ample city
    g4, d4 = [0, 0, 4], [10, 10, 10]
    assert solution.find_ample_city_if_exists(g4, d4, 10) == 2
    print("✓ Test 4 passed: only city 2 is ample")

    # Test case 5: Single city that cannot make it
    assert solution.find_ample_city_if_exists([1], [100], 20) == -1
    print("✓ Test 5 passed: single city short on gas -> -1")

    # Test case 6: Total just short by one mile
    assert solution.find_ample_city_if_exists([3, 1, 1], [1, 2, 3], 1) == -1
    print("✓ Test 6 passed: one mile short -> -1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_ample_city_if_exists()
