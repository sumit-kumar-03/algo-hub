"""
EPI 16.6 - The Knapsack Problem

Problem:
A thief can carry at most `capacity` units of weight. Each item has an
integer weight and an integer value, and each item can be taken at most
once (0/1 knapsack). Return the largest total value of a subset of items
whose total weight fits within the capacity. Greedy choices (by value or by
value-to-weight ratio) do not always give the optimum.

Constraints:
- 0 <= len(items) <= 1000, 0 <= capacity <= 10^4
- Weights are positive integers; values are non-negative integers
- O(n * capacity) time

How it works (DP over items and capacities):
1. V[i][w] = best value using the first i items with capacity w
2. V[0][w] = 0
3. V[i][w] = max(V[i-1][w],                         (skip item i)
                 V[i-1][w - weight_i] + value_i)    (take it, if it fits)
4. Return V[n][capacity]
(A single row iterated from high to low capacity uses O(capacity) space.)

Example 1:
Input: the 16 clocks of the book's clock store, capacity = 130
Output: 695
Explanation: Clocks H ($155, 25 oz), J ($320, 65 oz), and O ($220, 40 oz).
The greedy ratio choice only reaches $669.

Example 2:
Input: items = [(5, 60), (3, 50), (4, 70), (2, 30)] as (weight, value),
       capacity = 5
Output: 80
Explanation: Take the items with weights 3 and 2.
"""

from typing import List, Tuple

Item = Tuple[int, int]  # (weight, value)


class Solution:
    def optimum_subject_to_capacity(self, items: List[Item], capacity: int) -> int:
        """
        Computes the maximum value of items that fit in the knapsack.

        Args:
            items: List of (weight, value) pairs
            capacity: Maximum total weight

        Returns:
            Maximum achievable total value

        Time Complexity: O(n * capacity)
        Space Complexity: O(n * capacity) (O(capacity) with one row)
        """
        # TODO: Implement 0/1 knapsack DP
        pass


CLOCKS = [  # (weight in oz, value in $), clocks A through P from the book
    (20, 65), (8, 35), (60, 245), (55, 195), (40, 65), (70, 150), (85, 275), (25, 155),
    (30, 120), (65, 320), (75, 75), (10, 40), (95, 200), (50, 100), (40, 220), (10, 99),
]


def test_optimum_subject_to_capacity():
    """Test cases for the knapsack problem"""
    solution = Solution()

    # Test case 1: Book clock store example
    assert solution.optimum_subject_to_capacity(CLOCKS, 130) == 695
    print("✓ Test 1 passed: clock store, capacity 130 -> 695")

    # Test case 2: Greedy by value/weight fails here
    assert solution.optimum_subject_to_capacity([(5, 60), (3, 50), (4, 70), (2, 30)], 5) == 80
    print("✓ Test 2 passed: small instance -> 80")

    # Test case 3: No items
    assert solution.optimum_subject_to_capacity([], 10) == 0
    print("✓ Test 3 passed: no items -> 0")

    # Test case 4: Nothing fits
    assert solution.optimum_subject_to_capacity([(5, 10)], 4) == 0
    print("✓ Test 4 passed: nothing fits -> 0")

    # Test case 5: Classic instance
    assert solution.optimum_subject_to_capacity([(1, 1), (2, 6), (5, 18), (6, 22), (7, 28)], 11) == 40
    print("✓ Test 5 passed: classic instance -> 40")

    # Test case 6: Zero capacity
    assert solution.optimum_subject_to_capacity(CLOCKS, 0) == 0
    print("✓ Test 6 passed: zero capacity -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_optimum_subject_to_capacity()
