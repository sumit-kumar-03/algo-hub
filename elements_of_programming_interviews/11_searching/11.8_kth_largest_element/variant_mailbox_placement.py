"""
EPI 11.8 Variant - Optimal Mailbox Placement

Problem:
Several apartment buildings stand along a straight street. Each building has
a number of residents and a distance from the start of the street. Choose a
position for a single mailbox that minimizes the total walking distance of
all residents (sum over buildings of residents * |position - distance|).
Return any optimal position.

Constraints:
- 1 <= number of buildings <= 10^5
- residents >= 1, distances are nonnegative numbers
- Expected O(n) time (O(n log n) by sorting is acceptable as a first step)
- Several positions may be optimal; any one is accepted

How it works (weighted median):
1. The total cost only changes slope at building positions, and the slope
   flips from negative to nonnegative once at least half of all residents
   are at or to the left of the position
2. Find the building where the running resident count first reaches half of
   the total, i.e., the weighted median (sorting, or quickselect-style
   partitioning for expected O(n))
3. Return that building's distance

Example 1:
Input: buildings = [(1, 0.0), (1, 10.0), (5, 3.0)]   # (residents, distance)
Output: 3.0
Explanation: 5 of 7 residents live at 3.0, so the mailbox goes there.

Example 2:
Input: buildings = [(2, 1.0), (2, 9.0)]
Output: any position in [1.0, 9.0]
Explanation: Total cost is 16 for every point between the two buildings.
"""

import math
from typing import List, Tuple

Building = Tuple[int, float]  # (residents, distance from start of street)


class Solution:
    def place_mailbox(self, buildings: List[Building]) -> float:
        """
        Finds a mailbox position that minimizes total walking distance.

        Args:
            buildings: List of (residents, distance) pairs

        Returns:
            An optimal mailbox position

        Time Complexity: O(n) expected with selection, O(n log n) with sorting
        Space Complexity: O(1) extra with in-place selection
        """
        # TODO: Implement the weighted median
        pass


def _cost(buildings: List[Building], position: float) -> float:
    return sum(r * abs(position - d) for r, d in buildings)


def _is_optimal(buildings: List[Building], position: float) -> bool:
    if position is None:
        return False
    best = min(_cost(buildings, d) for _, d in buildings)  # optimum is at a building
    return math.isclose(_cost(buildings, position), best, rel_tol=1e-9, abs_tol=1e-9)


def test_place_mailbox():
    """Test cases for mailbox placement"""
    solution = Solution()

    # Test case 1: One dominant building
    b1 = [(1, 0.0), (1, 10.0), (5, 3.0)]
    p1 = solution.place_mailbox(b1)
    assert _is_optimal(b1, p1) is True
    print(f"✓ Test 1 passed: Dominant building -> {p1}")

    # Test case 2: Tie between two buildings
    b2 = [(2, 1.0), (2, 9.0)]
    assert _is_optimal(b2, solution.place_mailbox(b2)) is True
    print("✓ Test 2 passed: Tie")

    # Test case 3: Single building
    b3 = [(4, 7.5)]
    assert _is_optimal(b3, solution.place_mailbox(b3)) is True
    print("✓ Test 3 passed: Single building")

    # Test case 4: Equal residents (plain median), unsorted input
    b4 = [(1, 50.0), (1, 2.0), (1, 30.0), (1, 9.0), (1, 41.0)]
    assert _is_optimal(b4, solution.place_mailbox(b4)) is True
    print("✓ Test 4 passed: Unsorted, equal residents")

    # Test case 5: Weighted median far from the plain median
    b5 = [(1, 0.0), (1, 1.0), (1, 2.0), (1, 3.0), (10, 100.0)]
    p5 = solution.place_mailbox(b5)
    assert _is_optimal(b5, p5) is True
    print(f"✓ Test 5 passed: Heavy far building -> {p5}")

    # Test case 6: Larger deterministic input
    b6 = [((i * 13) % 9 + 1, float((i * 37) % 211)) for i in range(200)]
    assert _is_optimal(b6, solution.place_mailbox(b6)) is True
    print("✓ Test 6 passed: 200 buildings")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_place_mailbox()
