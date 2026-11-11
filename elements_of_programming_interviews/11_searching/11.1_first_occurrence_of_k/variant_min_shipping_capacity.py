"""
EPI 11.1 Extra Variant - Minimum Truck Capacity to Ship on Time
(Practice problem, not in the book. Difficulty: Medium)
Builds on: binary search for the FIRST position where a condition holds;
here the "array" is the range of possible capacities and the condition is
"this capacity is enough", which is monotone.

Problem:
Packages must be shipped in the given order, one truckload per day. Package
i weighs weights[i]. Each day the truck is loaded with the next packages in
order as long as the total stays within its capacity; packages cannot be
split or reordered. Return the smallest integer capacity that ships all
packages within the given number of days.

Constraints:
- 1 <= len(weights) <= 5 * 10^4; 1 <= weights[i] <= 500
- 1 <= days <= len(weights)
- O(n log(sum(weights))) time, O(1) extra space

How it works (binary search on the answer):
1. The capacity must be at least max(weights) and never needs to exceed
   sum(weights)
2. feasible(c): greedily fill each day up to c and count the days used;
   feasible(c) is True iff the count <= days. If c works, every larger c
   works too
3. Binary search [max(weights), sum(weights)] for the first c with
   feasible(c) True, exactly like searching for the first occurrence

Example 1:
Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
Output: 15
Explanation: [1..5], [6, 7], [8], [9], [10] fit in capacity 15; 14 needs
6 days.

Example 2:
Input: weights = [3, 2, 2, 4, 1, 4], days = 3
Output: 6
Explanation: [3, 2], [2, 4], [1, 4].
"""

from typing import List


class Solution:
    def min_capacity(self, weights: List[int], days: int) -> int:
        """
        Returns the least truck capacity that ships everything in time.

        Args:
            weights: Package weights, in shipping order
            days: Number of days available

        Returns:
            The minimum feasible integer capacity

        Time Complexity: O(n log(sum(weights)))
        Space Complexity: O(1)
        """
        # TODO: Implement binary search over capacities
        pass


def test_min_capacity():
    """Test cases for minimum shipping capacity"""
    solution = Solution()

    # Test case 1: Classic example
    assert solution.min_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    print("✓ Test 1 passed: 1..10 in 5 days -> 15")

    # Test case 2: Three days
    assert solution.min_capacity([3, 2, 2, 4, 1, 4], 3) == 6
    print("✓ Test 2 passed: 3 days -> 6")

    # Test case 3: One day needs the total weight
    assert solution.min_capacity([1, 2, 3, 1, 1], 1) == 8
    print("✓ Test 3 passed: One day")

    # Test case 4: One day per package needs the heaviest one
    assert solution.min_capacity([5, 1, 9, 2], 4) == 9
    print("✓ Test 4 passed: One package per day")

    # Test case 5: Single package
    assert solution.min_capacity([42], 1) == 42
    print("✓ Test 5 passed: Single package")

    # Test case 6: Order matters (sorting would give a different answer)
    assert solution.min_capacity([1, 2, 3, 1, 1], 4) == 3
    assert solution.min_capacity([10, 1, 1, 1, 10], 2) == 12
    print("✓ Test 6 passed: Order matters")

    # Test case 7: Larger input with many equal weights
    weights7 = [500] * 10000 + [1] * 5000
    assert solution.min_capacity(weights7, 7) == 715000
    print("✓ Test 7 passed: 15,000 packages")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_capacity()
