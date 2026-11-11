"""
EPI 5.6 Extra Variant - Stock Trading with a Cooldown Day
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the one-pass idea of carrying the best "position so far"
(like the cheapest buy price) forward instead of trying all pairs.

Problem:
Given daily stock prices, you may complete as many buy/sell transactions
as you like, but you can hold at most one share at a time, and after you
sell you must skip the next day entirely (no buying on the day right after
a sale). Return the maximum total profit. Doing nothing is allowed.

Constraints:
- 0 <= len(prices) <= 10^5; prices[i] >= 0
- Must run in O(n) time and O(1) extra space

How it works (three states carried day by day):
1. hold = best profit while holding a share, sold = best profit if we
   sold today, rest = best profit while holding nothing and free to buy
2. Start: hold = -infinity, sold = -infinity, rest = 0
3. For each price p (use the previous day's values on the right):
   - new_hold = max(hold, rest - p)
   - new_sold = hold + p
   - new_rest = max(rest, sold)  (yesterday's sale makes today a rest day)
4. Return max(sold, rest)

Example 1:
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Explanation: Buy at 1, sell at 2, cool down on day 2, buy at 0, sell at 2.

Example 2:
Input: prices = [1, 4, 2, 7]
Output: 6
Explanation: Buy at 1 and sell at 7. Selling at 4 would force a rest on
the day priced 2, leaving only 3 + 0.
"""

from typing import List


class Solution:
    def max_profit_with_cooldown(self, prices: List[int]) -> int:
        """
        Computes the best profit with unlimited trades and a one-day cooldown.

        Args:
            prices: Daily prices

        Returns:
            Maximum achievable total profit (0 if no trade helps)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement trading with cooldown
        pass


def test_max_profit_with_cooldown():
    """Test cases for trading with a cooldown day"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.max_profit_with_cooldown([1, 2, 3, 0, 2]) == 3
    print("✓ Test 1 passed: [1, 2, 3, 0, 2] -> 3")

    # Test case 2: Example 2 (cooldown changes the best plan)
    assert solution.max_profit_with_cooldown([1, 4, 2, 7]) == 6
    print("✓ Test 2 passed: [1, 4, 2, 7] -> 6")

    # Test case 3: Empty, single day, falling prices
    assert solution.max_profit_with_cooldown([]) == 0
    assert solution.max_profit_with_cooldown([5]) == 0
    assert solution.max_profit_with_cooldown([5, 4, 3, 2, 1]) == 0
    print("✓ Test 3 passed: Empty, single day, falling prices")

    # Test case 4: Rising prices: one long trade
    assert solution.max_profit_with_cooldown([1, 2, 3, 4, 5]) == 4
    print("✓ Test 4 passed: Rising prices -> 4")

    # Test case 5: Gaps that allow back-to-back trades
    assert solution.max_profit_with_cooldown([1, 5, 5, 1, 5]) == 8
    assert solution.max_profit_with_cooldown([1, 5, 1, 5]) == 4
    print("✓ Test 5 passed: Cooldown allows / blocks a second trade")

    # Test case 6: Long repeating pattern
    prices = [1, 6, 0, 0] * 25000
    assert solution.max_profit_with_cooldown(prices) == 5 + 6 * 24999
    print("✓ Test 6 passed: 100,000 days")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_profit_with_cooldown()
