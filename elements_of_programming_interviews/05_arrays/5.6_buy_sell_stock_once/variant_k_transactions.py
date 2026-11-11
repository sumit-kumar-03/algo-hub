"""
EPI 5.6 Extra Variant - Buy and Sell a Stock at Most k Times
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the single-pass "best balance after buying" idea from the main
problem, stacked into k layers (each layer's buy is funded by the profit
of the layer before it).

Problem:
Given daily stock prices and an integer k, return the maximum profit from
at most k buy/sell transactions. You can hold at most one share at a
time, so each sale must happen before the next purchase; selling and
buying again on the same day is allowed. Doing nothing is allowed.

Constraints:
- 0 <= len(prices) <= 10^4; prices[i] >= 0; 0 <= k <= 10^9
- O(n * min(k, n)) time and O(min(k, n)) extra space
- When k >= n // 2 the limit never binds: handle that case in O(n) by
  taking every upward move, so a huge k does not blow up the run time

How it works (k layers of the one-trade scan):
1. If k >= n // 2, return the sum of max(0, prices[i] - prices[i - 1])
2. buy[t] = best balance after the t-th buy, sell[t] = best balance after
   the t-th sale, for t = 1..k; buy[t] = -infinity, sell[t] = 0 at start
3. For each price p, for t from 1 to k:
   - buy[t] = max(buy[t], sell[t - 1] - p)   (sell[0] = 0)
   - sell[t] = max(sell[t], buy[t] + p)
4. Return sell[k]

Example 1:
Input: prices = [3, 2, 6, 5, 0, 3], k = 2
Output: 7
Explanation: Buy at 2, sell at 6 (+4); buy at 0, sell at 3 (+3).

Example 2:
Input: prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], k = 1
Output: 8
Explanation: With one trade, buy at 1 and sell at 9.
"""

from typing import List


class Solution:
    def max_profit_k_transactions(self, prices: List[int], k: int) -> int:
        """
        Computes the best profit using at most k transactions.

        Args:
            prices: Daily prices
            k: Maximum number of buy/sell transactions

        Returns:
            Maximum achievable total profit (0 if no trade helps)

        Time Complexity: O(n * min(k, n))
        Space Complexity: O(min(k, n))
        """
        # TODO: Implement at-most-k-transactions profit
        pass


def best_profit_brute(prices: List[int], k: int) -> int:
    """Slow reference: try every buy/sell pair recursively."""
    n = len(prices)

    def go(start: int, left: int) -> int:
        if left == 0:
            return 0
        best = 0
        for i in range(start, n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    best = max(best, prices[j] - prices[i] + go(j, left - 1))
        return best

    return go(0, k)


def test_max_profit_k_transactions():
    """Test cases for at most k transactions"""
    solution = Solution()

    # Test case 1: Examples
    assert solution.max_profit_k_transactions([3, 2, 6, 5, 0, 3], 2) == 7
    assert solution.max_profit_k_transactions([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 1) == 8
    print("✓ Test 1 passed: Examples")

    # Test case 2: Same prices with more transactions allowed
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    assert solution.max_profit_k_transactions(prices, 2) == 13
    assert solution.max_profit_k_transactions(prices, 3) == 15
    assert solution.max_profit_k_transactions(prices, 4) == 15
    print("✓ Test 2 passed: k = 2, 3, 4 -> 13, 15, 15")

    # Test case 3: k = 0, empty prices, falling prices
    assert solution.max_profit_k_transactions([1, 5], 0) == 0
    assert solution.max_profit_k_transactions([], 3) == 0
    assert solution.max_profit_k_transactions([9, 7, 4, 1], 2) == 0
    print("✓ Test 3 passed: k = 0, empty, falling prices")

    # Test case 4: Matches brute force on small arrays
    for seed in range(60):
        small = [(seed * 7 + i * i * 13 + i * 5) % 11 for i in range(7)]
        for k in range(0, 4):
            assert solution.max_profit_k_transactions(small, k) == best_profit_brute(small, k)
    print("✓ Test 4 passed: Matches brute force on 60 small arrays")

    # Test case 5: Huge k must not be slow
    prices = [i % 3 for i in range(10000)]  # 0, 1, 2, 0, 1, 2, ...
    expected = 2 * (10000 // 3)
    assert solution.max_profit_k_transactions(prices, 10**9) == expected
    print("✓ Test 5 passed: k = 10^9 on 10,000 days")

    # Test case 6: Moderate k on a long series
    prices = [0, 10] * 5000
    assert solution.max_profit_k_transactions(prices, 50) == 500
    print("✓ Test 6 passed: k = 50 on 10,000 days")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_profit_k_transactions()
