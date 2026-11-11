"""
EPI 16.6 Variant - The Fractional Knapsack Problem

Problem:
Same as the knapsack problem, but the thief may take any fraction of an
item, earning that fraction of its value. Return the maximum total value
that fits within the capacity.

Constraints:
- 0 <= len(items) <= 10^5, 0 <= capacity <= 10^9
- Weights are positive integers; values are non-negative integers
- O(n log n) time

How it works (greedy, which is optimal here unlike 0/1 knapsack):
1. Sort items by value / weight, highest first
2. Take whole items while they fit
3. Take the fraction of the next item that fills the remaining capacity
4. Return the accumulated value (a float)

Example 1:
Input: items = [(10, 60), (20, 100), (30, 120)] as (weight, value),
       capacity = 50
Output: 240.0
Explanation: All of the first two items, then 20/30 of the third (80).

Example 2:
Input: items = [(10, 60)], capacity = 5
Output: 30.0
"""

from typing import List, Tuple

Item = Tuple[int, int]  # (weight, value)


class Solution:
    def fractional_knapsack(self, items: List[Item], capacity: int) -> float:
        """
        Computes the maximum value when items can be split.

        Args:
            items: List of (weight, value) pairs
            capacity: Maximum total weight

        Returns:
            Maximum achievable total value

        Time Complexity: O(n log n)
        Space Complexity: O(n) for the sorted order
        """
        # TODO: Implement greedy fractional knapsack
        pass


def close(a, b) -> bool:
    """Float comparison with a small tolerance."""
    return isinstance(a, (int, float)) and abs(a - b) < 1e-6


def test_fractional_knapsack():
    """Test cases for the fractional knapsack problem"""
    solution = Solution()

    # Test case 1: Classic example
    assert close(solution.fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50), 240.0)
    print("✓ Test 1 passed: classic instance -> 240.0")

    # Test case 2: Half of a single item
    assert close(solution.fractional_knapsack([(10, 60)], 5), 30.0)
    print("✓ Test 2 passed: half an item -> 30.0")

    # Test case 3: Everything fits
    assert close(solution.fractional_knapsack([(5, 10), (4, 40)], 100), 50.0)
    print("✓ Test 3 passed: everything fits -> 50.0")

    # Test case 4: Fraction beats the 0/1 answer (80)
    assert close(solution.fractional_knapsack([(5, 60), (3, 50), (4, 70), (2, 30)], 5), 260 / 3)
    print("✓ Test 4 passed: fractional beats 0/1 -> 86.67")

    # Test case 5: No items
    assert close(solution.fractional_knapsack([], 10), 0.0)
    print("✓ Test 5 passed: no items -> 0.0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fractional_knapsack()
