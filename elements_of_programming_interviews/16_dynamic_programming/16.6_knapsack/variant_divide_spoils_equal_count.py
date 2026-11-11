"""
EPI 16.6 Variant - Divide the Spoils Fairly with Equal Item Counts

Problem:
Like divide-the-spoils-fairly, but each thief must also receive the same
number of items. Given an even number of item values, split them into two
groups of equal size so the difference between the groups' totals is as
small as possible, and return that difference.

Constraints:
- len(values) is even, 0 <= len(values) <= 100
- 0 <= values[i] <= 10^3
- O(n^2 * S) time where S is the sum of all values

How it works (subset-sum DP with an item count dimension):
1. reachable[c] = set of sums achievable with exactly c items
2. reachable[0] = {0}; for each value v, for c from n/2 down to 1:
   reachable[c] |= {s + v for s in reachable[c - 1]}
3. Return min(|S - 2s|) over s in reachable[n / 2]

Example 1:
Input: values = [1, 1, 1, 10]
Output: 9
Explanation: Without the count rule {1, 1, 1} vs {10} differs by 7, but
with two items each the best is {1, 10} vs {1, 1}.

Example 2:
Input: values = [1, 2, 3, 4]
Output: 0
Explanation: {1, 4} vs {2, 3}
"""

from typing import List


class Solution:
    def min_spoils_difference_equal_count(self, values: List[int]) -> int:
        """
        Computes the smallest value difference between two equal-size groups.

        Args:
            values: Value of each stolen item (even length)

        Returns:
            Minimum absolute difference between the two groups' totals

        Time Complexity: O(n^2 * S)
        Space Complexity: O(n * S)
        """
        # TODO: Implement subset-sum DP with an item count
        pass


CLOCK_VALUES = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]


def test_min_spoils_difference_equal_count():
    """Test cases for equal-count fair division"""
    solution = Solution()

    # Test case 1: Count constraint changes the answer
    assert solution.min_spoils_difference_equal_count([1, 1, 1, 10]) == 9
    print("✓ Test 1 passed: [1, 1, 1, 10] -> 9")

    # Test case 2: Perfect equal-size split
    assert solution.min_spoils_difference_equal_count([1, 2, 3, 4]) == 0
    print("✓ Test 2 passed: [1, 2, 3, 4] -> 0")

    # Test case 3: Two items
    assert solution.min_spoils_difference_equal_count([5, 8]) == 3
    print("✓ Test 3 passed: [5, 8] -> 3")

    # Test case 4: Six items
    assert solution.min_spoils_difference_equal_count([3, 1, 4, 1, 5, 9]) == 1
    print("✓ Test 4 passed: [3, 1, 4, 1, 5, 9] -> 1")

    # Test case 5: Clock store, eight clocks each
    assert solution.min_spoils_difference_equal_count(CLOCK_VALUES) == 1
    print("✓ Test 5 passed: clock store -> 1")

    # Test case 6: No items
    assert solution.min_spoils_difference_equal_count([]) == 0
    print("✓ Test 6 passed: [] -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_spoils_difference_equal_count()
