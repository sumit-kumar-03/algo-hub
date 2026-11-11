"""
EPI 16.6 Variant - Can the Electoral College Tie?

Problem:
In a two-candidate presidential election, every state (and Washington,
D.C.) casts all of its electoral votes for one candidate. Given the number
of electors per state, determine whether the election can end in a tie,
i.e., whether the states can be split into two groups with equal elector
totals.

Constraints:
- 1 <= len(electors) <= 100, 1 <= electors[i] <= 100
- O(n * S) time where S is the total number of electors

How it works (subset-sum DP, the knapsack with value == weight):
1. If the total S is odd, a tie is impossible
2. reachable[s] = True if some set of states sums to s
3. Return reachable[S / 2]

Example 1:
Input: electors for the 50 states + D.C. as apportioned for 2012-2020
       (538 total)
Output: True
Explanation: 269-269 is achievable.

Example 2:
Input: electors = [3, 5]
Output: False
"""

from typing import List


class Solution:
    def is_tie_possible(self, electors: List[int]) -> bool:
        """
        Checks whether the states can split into two equal elector totals.

        Args:
            electors: Number of electors for each state

        Returns:
            True if a tie is possible, False otherwise

        Time Complexity: O(n * S)
        Space Complexity: O(S)
        """
        # TODO: Implement subset-sum tie check
        pass


# Electors per state + D.C., 2012-2020 apportionment (alphabetical, D.C. after DE).
ELECTORS_2012 = [
    9, 3, 11, 6, 55, 9, 7, 3, 3, 29, 16, 4, 4, 20, 11, 6, 6, 8, 8, 4, 10, 11, 16, 10, 6, 10,
    3, 5, 6, 4, 14, 5, 29, 15, 3, 18, 7, 7, 20, 4, 9, 3, 11, 38, 6, 3, 13, 12, 5, 10, 3,
]


def test_is_tie_possible():
    """Test cases for the electoral college tie problem"""
    solution = Solution()

    # Test case 1: Real electoral map (538 electors)
    assert solution.is_tie_possible(ELECTORS_2012) is True
    print("✓ Test 1 passed: 2012-2020 map -> tie possible")

    # Test case 2: Even total but no equal split
    assert solution.is_tie_possible([3, 5]) is False
    print("✓ Test 2 passed: [3, 5] -> no tie")

    # Test case 3: Odd total
    assert solution.is_tie_possible([3, 4]) is False
    print("✓ Test 3 passed: [3, 4] -> no tie (odd total)")

    # Test case 4: Simple tie
    assert solution.is_tie_possible([2, 3, 5]) is True
    print("✓ Test 4 passed: [2, 3, 5] -> tie")

    # Test case 5: One big state balanced by smaller ones
    assert solution.is_tie_possible([10, 4, 3, 3]) is True
    print("✓ Test 5 passed: [10, 4, 3, 3] -> tie")

    # Test case 6: Single state
    assert solution.is_tie_possible([6]) is False
    print("✓ Test 6 passed: [6] -> no tie")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_tie_possible()
