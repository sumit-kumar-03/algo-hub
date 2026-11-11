"""
EPI 17.6 - The Gasup Problem

Problem:
Cities lie on a circular road. City i has gallons[i] gallons of gas
available and is distances[i] miles from the next city (city i + 1, with
the last city wrapping to city 0). The car gets mpg miles per gallon and
has an unlimited tank. In total there is exactly enough gas to drive the
full loop once. A city is ample if you can start there with an empty tank,
fill up, and drive around the whole loop (refueling at every city) without
running out. Return the index of an ample city.

Constraints:
- 1 <= n <= 10^5
- sum(gallons) * mpg == sum(distances), and an ample city exists
- O(n) time, O(1) space

How it works (start where the running fuel is lowest):
1. Pretend to start at city 0 with plenty of gas and track the remaining
   miles of range when arriving at each city:
   remaining += gallons[i - 1] * mpg - distances[i - 1]
2. The city where this running total is smallest is ample: starting there,
   the tank never dips below what it held at that low point, which is 0
3. Return that city's index (city 0 if the minimum is at the start)

Example 1:
Input: gallons = [50, 20, 5, 30, 25, 10, 10],
       distances = [900, 600, 200, 400, 600, 200, 100], mpg = 20
Output: 3
Explanation: City D (index 3) in the book's figure; the loop is 3000 miles.

Example 2:
Input: gallons = [3, 1, 1], distances = [1, 2, 2], mpg = 1
Output: 0
"""

from typing import List


class Solution:
    def find_ample_city(self, gallons: List[int], distances: List[int], mpg: int = 20) -> int:
        """
        Finds a city from which the full loop can be completed.

        Args:
            gallons: Gas available at each city
            distances: Miles from each city to the next one
            mpg: Miles per gallon of the car

        Returns:
            Index of an ample city

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement ample city search
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


def test_find_ample_city():
    """Test cases for the gasup problem"""
    solution = Solution()

    # Test case 1: Book example
    g1, d1 = [50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100]
    assert solution.find_ample_city(g1, d1, 20) == 3
    print("✓ Test 1 passed: book example -> city 3")

    # Test case 2: Single city
    assert solution.find_ample_city([5], [100], 20) == 0
    print("✓ Test 2 passed: single city -> 0")

    # Test case 3: Ample city in the middle
    g3, d3 = [1, 2, 3, 4, 5], [60, 80, 100, 20, 40]
    assert solution.find_ample_city(g3, d3, 20) == 3
    print("✓ Test 3 passed: [1, 2, 3, 4, 5] -> city 3")

    # Test case 4: First city has no gas
    assert solution.find_ample_city([0, 10], [100, 100], 20) == 1
    print("✓ Test 4 passed: empty first city -> city 1")

    # Test case 5: Ample city is the start
    assert solution.find_ample_city([3, 1, 1], [1, 2, 2], 1) == 0
    print("✓ Test 5 passed: [3, 1, 1] -> city 0")

    # Test case 6: Result is verified by simulation (ties allowed)
    g6, d6 = [2, 0, 2, 0], [20, 20, 20, 20]
    r6 = solution.find_ample_city(g6, d6, 20)
    assert is_ample(r6, g6, d6, 20)
    print(f"✓ Test 6 passed: two ample cities, returned {r6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_ample_city()
