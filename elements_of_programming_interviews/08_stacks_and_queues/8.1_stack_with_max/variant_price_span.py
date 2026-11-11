"""
EPI 8.1 Extra Variant - Online Price Span
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Keeping aggregated information on a stack so a query about
everything below the top is answered without rescanning it.

Problem:
Prices of a stock arrive one day at a time. For each new price, report its
span: the number of consecutive days, ending today and going backward,
on which the price was less than or equal to today's price (today counts,
so the span is at least 1). Implement a class whose next(price) method
records the price and returns its span.

Constraints:
- 1 <= price <= 10^5, up to 10^5 calls
- Amortized O(1) time per call, O(n) space

How it works:
1. Keep a stack of (price, span) pairs whose prices strictly decrease
   from bottom to top
2. For a new price p, start with span = 1; while the top price is <= p,
   pop it and add its span (those days are all covered by p)
3. Push (p, span) and return span
4. Each price is pushed and popped at most once, giving amortized O(1)

Example:
next(100) -> 1, next(80) -> 1, next(60) -> 1, next(70) -> 2,
next(60) -> 1, next(75) -> 4, next(85) -> 6
"""

from typing import List, Tuple


class PriceSpanner:
    def __init__(self) -> None:
        # TODO: Choose the internal storage
        pass

    def next(self, price: int) -> int:
        """
        Records today's price and returns its span.

        Args:
            price: Today's price

        Returns:
            Number of consecutive days up to today with price <= today's

        Time Complexity: Amortized O(1)
        Space Complexity: O(n) overall
        """
        # TODO: Implement span computation
        pass


def test_price_spanner():
    """Test cases for online price spans"""

    # Test case 1: Classic sequence
    s = PriceSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    assert [s.next(p) for p in prices] == [1, 1, 1, 2, 1, 4, 6]
    print("✓ Test 1 passed: Classic example")

    # Test case 2: Single day
    assert PriceSpanner().next(42) == 1
    print("✓ Test 2 passed: First day has span 1")

    # Test case 3: Strictly increasing prices cover every earlier day
    s = PriceSpanner()
    assert [s.next(p) for p in range(1, 7)] == [1, 2, 3, 4, 5, 6]
    print("✓ Test 3 passed: Increasing prices")

    # Test case 4: Strictly decreasing prices
    s = PriceSpanner()
    assert [s.next(p) for p in (9, 7, 5, 3)] == [1, 1, 1, 1]
    print("✓ Test 4 passed: Decreasing prices")

    # Test case 5: Equal prices count toward the span
    s = PriceSpanner()
    assert [s.next(p) for p in (5, 5, 5, 4, 5)] == [1, 2, 3, 1, 5]
    print("✓ Test 5 passed: Ties are included")

    # Test case 6: Randomized comparison with a direct scan
    import random

    rng = random.Random(9)
    s = PriceSpanner()
    history: List[int] = []
    for _ in range(2000):
        p = rng.randint(1, 30)
        history.append(p)
        span = 0
        while span < len(history) and history[-1 - span] <= p:
            span += 1
        assert s.next(p) == span
    print("✓ Test 6 passed: Matches a direct scan")

    # Test case 7: Long increasing run is fast
    s = PriceSpanner()
    for p in range(1, 100001):
        last = s.next(p)
    assert last == 100000
    print("✓ Test 7 passed: 10^5 increasing prices")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_price_spanner()
