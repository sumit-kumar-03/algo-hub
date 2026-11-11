"""
EPI 5.6 - Buy and Sell a Stock Once

Problem:
Given an array of daily stock prices, return the maximum profit from
buying one share on some day and selling it on the same or a later day.
If no profit is possible, return 0 (you are not required to trade).

Constraints:
- 0 <= len(prices) <= 10^5
- prices[i] >= 0
- Must run in O(n) time and O(1) extra space

How it works (track the cheapest price so far):
1. min_price = infinity, max_profit = 0
2. For each price:
   - max_profit = max(max_profit, price - min_price)
   - min_price = min(min_price, price)
3. Return max_profit

Example 1:
Input: prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
Output: 30
Explanation: Buy at 260 and sell at 290. Neither is the overall minimum
or maximum price.

Example 2:
Input: prices = [5, 4, 3, 2]
Output: 0
Explanation: Prices only fall, so it is best not to trade.
"""

from typing import List


class Solution:
    def buy_and_sell_stock_once(self, prices: List[float]) -> float:
        """
        Computes the maximum profit from a single buy and a later sell.

        Args:
            prices: Daily stock prices

        Returns:
            Maximum achievable profit (0 if no profitable trade exists)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement single-trade max profit
        pass


def test_buy_and_sell_stock_once():
    """Test cases for buy and sell stock once"""
    solution = Solution()

    # Test case 1: Book example
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    assert solution.buy_and_sell_stock_once(prices) == 30
    print("✓ Test 1 passed: Book example -> 30")

    # Test case 2: Falling prices
    assert solution.buy_and_sell_stock_once([5, 4, 3, 2]) == 0
    print("✓ Test 2 passed: Falling prices -> 0")

    # Test case 3: Empty and single-day inputs
    assert solution.buy_and_sell_stock_once([]) == 0
    assert solution.buy_and_sell_stock_once([7]) == 0
    print("✓ Test 3 passed: Empty / single day -> 0")

    # Test case 4: Rising prices
    assert solution.buy_and_sell_stock_once([1, 2, 3, 4, 5]) == 4
    print("✓ Test 4 passed: Rising prices -> 4")

    # Test case 5: Global max comes before global min
    assert solution.buy_and_sell_stock_once([9, 11, 8, 5, 7, 10]) == 5
    print("✓ Test 5 passed: [9, 11, 8, 5, 7, 10] -> 5")

    # Test case 6: Float prices
    result = solution.buy_and_sell_stock_once([2.5, 1.25, 3.75, 3.0])
    assert abs(result - 2.5) < 1e-9
    print("✓ Test 6 passed: Float prices -> 2.5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_buy_and_sell_stock_once()
