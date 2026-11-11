"""
EPI 17.6 Extra Variant - Fewest Refueling Stops to Reach a Destination
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the 17.6 fuel-balance reasoning, turned into a greedy with an
invariant: only refuel when forced, and then use the biggest station
already passed.

Problem:
A car drives along a straight road from mile 0 to a destination at mile
target. It starts with start_fuel units of fuel and burns one unit per
mile; its tank has no capacity limit. Gas stations are given as
(position, fuel) pairs, sorted by position, with 0 < position < target.
When the car stops at a station it takes all of that station's fuel. Arriving
somewhere with exactly zero fuel is fine. Return the fewest stops needed
to reach the destination, or -1 if it cannot be reached.

Constraints:
- 1 <= target, start_fuel <= 10^9
- 0 <= len(stations) <= 10^5, positions strictly increasing in (0, target)
- 1 <= fuel at a station <= 10^9
- O(n log n) time with a heap

How it works (greedy with a max-heap of passed stations):
1. Drive as far as the current fuel allows. Every station passed on the way
   is a stop you could have made: push its fuel onto a max-heap
2. If you cannot reach the next station (or the destination), "retroactively"
   stop at the passed station with the most fuel: pop the heap, add that
   fuel, and count one stop. If the heap is empty, return -1
3. Repeat until the destination is within reach
Invariant: after k pops, the reach is the farthest possible with k stops.

Example 1:
Input: target = 100, start_fuel = 10,
       stations = [(10, 60), (20, 30), (30, 30), (60, 40)]
Output: 2
Explanation: Stop at mile 10 (fuel 60, reach 70), then at mile 60
(fuel 40, reach 110).

Example 2:
Input: target = 100, start_fuel = 1, stations = [(10, 100)]
Output: -1
Explanation: The car cannot even reach the first station.
"""

from typing import List, Tuple


class Solution:
    def min_refuel_stops(
        self, target: int, start_fuel: int, stations: List[Tuple[int, int]]
    ) -> int:
        """
        Returns the fewest stops needed to reach target, or -1.

        Args:
            target: Destination mile marker
            start_fuel: Initial fuel (one unit per mile)
            stations: (position, fuel) pairs sorted by position

        Returns:
            Minimum number of stops, or -1 if the destination is unreachable

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement the max-heap greedy
        pass


def test_min_refuel_stops():
    """Test cases for the fewest refueling stops"""
    solution = Solution()

    # Test case 1: No stops needed
    assert solution.min_refuel_stops(1, 1, []) == 0
    assert solution.min_refuel_stops(100, 150, [(10, 60), (50, 20)]) == 0
    print("✓ Test 1 passed: enough fuel at the start -> 0")

    # Test case 2: Unreachable first station
    assert solution.min_refuel_stops(100, 1, [(10, 100)]) == -1
    print("✓ Test 2 passed: cannot reach any station -> -1")

    # Test case 3: Example 1
    stations3 = [(10, 60), (20, 30), (30, 30), (60, 40)]
    assert solution.min_refuel_stops(100, 10, stations3) == 2
    print("✓ Test 3 passed: example 1 -> 2")

    # Test case 4: Greedy "nearest first" is wrong; biggest passed station wins
    stations4 = [(10, 10), (20, 5), (30, 100)]
    assert solution.min_refuel_stops(100, 30, stations4) == 1
    print("✓ Test 4 passed: skip small stations -> 1")

    # Test case 5: Arriving with exactly zero fuel is allowed
    assert solution.min_refuel_stops(100, 50, [(50, 50)]) == 1
    assert solution.min_refuel_stops(100, 50, [(50, 49)]) == -1
    print("✓ Test 5 passed: exact-zero arrivals")

    # Test case 6: Must use every station
    stations6 = [(i, 1) for i in range(1, 10)]
    assert solution.min_refuel_stops(10, 1, stations6) == 9
    print("✓ Test 6 passed: every station needed -> 9")

    # Test case 7: Large input
    n = 100000
    stations7 = [(i, 1 if i % 1000 else 1000) for i in range(1, n + 1)]
    assert solution.min_refuel_stops(n + 1, 1000, stations7) == 100
    print("✓ Test 7 passed: 100000 stations -> 100")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_refuel_stops()
