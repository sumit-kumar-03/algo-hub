"""
EPI 11.5 Variant - Divide Without Division

Problem:
Given two positive floating-point numbers x and y, compute x / y to within a
relative tolerance without using the division operator (/, //) or any library
functions such as log and exp. Addition and multiplication are allowed
(multiplying by 0.5 to halve is fine).

Constraints:
- 1e-6 <= x, y <= 1e6
- Result must be within a relative error of about 1e-9 of x / y
- O(log(1 / tolerance)) iterations after bracketing

How it works (binary search on the quotient):
1. Find a bracket [lo, hi] with lo * y <= x <= hi * y, e.g. start with
   [0, 1] and double hi until hi * y >= x
2. Repeat until hi - lo is tiny relative to hi:
   - mid = (lo + hi) * 0.5
   - mid * y > x: hi = mid, else lo = mid
3. Return lo (or mid)

Example 1:
Input: x = 1.0, y = 3.0
Output: 0.3333333333...

Example 2:
Input: x = 10.0, y = 0.5
Output: 20.0
"""

import math


class Solution:
    def divide(self, x: float, y: float) -> float:
        """
        Computes x / y using only addition and multiplication.

        Args:
            x: Positive dividend
            y: Positive divisor

        Returns:
            x / y to within a relative tolerance of about 1e-9

        Time Complexity: O(log(x / y) + log(1 / tolerance))
        Space Complexity: O(1)
        """
        # TODO: Implement binary search for q with q * y close to x
        pass


def _ok(got: float, x: float, y: float) -> bool:
    return got is not None and math.isclose(got, x / y, rel_tol=1e-6)


def test_divide():
    """Test cases for division without the division operator"""
    solution = Solution()

    # Test case 1: Repeating decimal
    assert _ok(solution.divide(1.0, 3.0), 1.0, 3.0)
    print("✓ Test 1 passed: 1 / 3")

    # Test case 2: Divisor below 1
    assert _ok(solution.divide(10.0, 0.5), 10.0, 0.5)
    print("✓ Test 2 passed: 10 / 0.5 = 20")

    # Test case 3: Equal operands
    assert _ok(solution.divide(7.25, 7.25), 7.25, 7.25)
    print("✓ Test 3 passed: x / x = 1")

    # Test case 4: Large quotient
    assert _ok(solution.divide(1e6, 1e-6), 1e6, 1e-6)
    print("✓ Test 4 passed: 1e6 / 1e-6")

    # Test case 5: Tiny quotient
    assert _ok(solution.divide(1e-6, 1e6), 1e-6, 1e6)
    print("✓ Test 5 passed: 1e-6 / 1e6")

    # Test case 6: Arbitrary values
    assert _ok(solution.divide(123.456, 7.89), 123.456, 7.89)
    print("✓ Test 6 passed: 123.456 / 7.89")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_divide()
