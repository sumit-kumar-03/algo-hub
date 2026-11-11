"""
EPI 16.6 Variant - Divide the Spoils Fairly

Problem:
Two thieves want to split their stolen items into two groups so that the
difference between the total values of the groups is as small as possible.
Every item goes to exactly one thief. Return that minimum difference.

Constraints:
- 0 <= len(values) <= 200, 0 <= values[i] <= 10^4
- O(n * S) time where S is the sum of all values

How it works (subset-sum DP):
1. reachable[s] = True if some subset of items sums to exactly s
2. Start with reachable[0] = True; for each value v, for s from S down to v:
   reachable[s] |= reachable[s - v]
3. The best split puts a subset with sum s as close to S / 2 as possible
4. Return min(|S - 2s|) over reachable s

Example 1:
Input: values of the 16 clocks in the book's clock store (total $2359)
Output: 1
Explanation: e.g. clocks A, G, J, M, O, P ($1179) vs the rest ($1180).
An even split is impossible because the total is odd.

Example 2:
Input: values = [1, 6, 11, 5]
Output: 1
Explanation: {1, 5, 6} = 12 vs {11} = 11
"""

from typing import List


class Solution:
    def min_spoils_difference(self, values: List[int]) -> int:
        """
        Computes the smallest possible value difference between two groups.

        Args:
            values: Value of each stolen item

        Returns:
            Minimum absolute difference between the two groups' totals

        Time Complexity: O(n * S)
        Space Complexity: O(S)
        """
        # TODO: Implement subset-sum based fair split
        pass


CLOCK_VALUES = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]


def test_min_spoils_difference():
    """Test cases for dividing the spoils fairly"""
    solution = Solution()

    # Test case 1: Book clock store example
    assert solution.min_spoils_difference(CLOCK_VALUES) == 1
    print("✓ Test 1 passed: clock store -> 1")

    # Test case 2: Small instance
    assert solution.min_spoils_difference([1, 6, 11, 5]) == 1
    print("✓ Test 2 passed: [1, 6, 11, 5] -> 1")

    # Test case 3: Perfect split exists
    assert solution.min_spoils_difference([3, 1, 4, 2, 2]) == 0
    print("✓ Test 3 passed: [3, 1, 4, 2, 2] -> 0")

    # Test case 4: One dominant item
    assert solution.min_spoils_difference([1, 2, 3, 9]) == 3
    print("✓ Test 4 passed: [1, 2, 3, 9] -> 3")

    # Test case 5: Single item
    assert solution.min_spoils_difference([10]) == 10
    print("✓ Test 5 passed: [10] -> 10")

    # Test case 6: No items
    assert solution.min_spoils_difference([]) == 0
    print("✓ Test 6 passed: [] -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_spoils_difference()
