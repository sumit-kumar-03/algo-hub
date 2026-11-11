"""
EPI 4.7 - Compute x^y

Problem:
Given a floating-point number x and an integer y (which may be negative),
return x raised to the power y. Overflow and underflow can be ignored.
Do not use the built-in ** operator or math.pow.

Constraints:
- x is a float; y is any integer (negative y means 1 / x^|y|)
- x != 0 when y < 0
- Aim for O(log |y|) multiplications

How it works (repeated squaring):
1. If y < 0, replace x with 1 / x and y with -y
2. result = 1.0
3. While y is not 0:
   - If the lowest bit of y is 1, multiply result by x
   - Square x and shift y right by one bit
4. Return result

Example 1:
Input: x = 1.1, y = 21
Output: about 7.4002499
Explanation: Using squares of 1.1 takes far fewer than 20 multiplications.

Example 2:
Input: x = 2.0, y = -2
Output: 0.25
Explanation: 2^-2 = 1 / 4.
"""

import math


class Solution:
    def power(self, x: float, y: int) -> float:
        """
        Computes x raised to the integer power y.

        Args:
            x: Base, a floating-point number
            y: Integer exponent (may be negative or zero)

        Returns:
            x^y as a float

        Time Complexity: O(log |y|)
        Space Complexity: O(1)
        """
        # TODO: Implement x^y with repeated squaring
        pass


def test_power():
    """Test cases for x^y implementation"""
    solution = Solution()

    # Test case 1: Any base to the power 0 is 1
    assert math.isclose(solution.power(5.0, 0), 1.0)
    print("✓ Test 1 passed: 5.0^0 == 1.0")

    # Test case 2: Simple positive exponent
    assert math.isclose(solution.power(2.0, 10), 1024.0)
    print("✓ Test 2 passed: 2.0^10 == 1024.0")

    # Test case 3: Book example
    assert math.isclose(solution.power(1.1, 21), 1.1 ** 21, rel_tol=1e-12)
    print("✓ Test 3 passed: 1.1^21")

    # Test case 4: Negative exponent
    assert math.isclose(solution.power(2.0, -2), 0.25)
    print("✓ Test 4 passed: 2.0^-2 == 0.25")

    # Test case 5: Negative base with odd and even exponents
    assert math.isclose(solution.power(-3.0, 3), -27.0)
    assert math.isclose(solution.power(-3.0, 4), 81.0)
    print("✓ Test 5 passed: (-3.0)^3 == -27.0, (-3.0)^4 == 81.0")

    # Test case 6: Fractional base, large exponent
    assert math.isclose(solution.power(0.5, 30), 1 / (1 << 30))
    print("✓ Test 6 passed: 0.5^30 == 2^-30")

    # Test case 7: Base close to 1 with a large exponent
    expected = math.exp(10**7 * math.log1p(1e-7))
    assert math.isclose(solution.power(1.0000001, 10**7), expected, rel_tol=1e-6)
    print("✓ Test 7 passed: 1.0000001^(10^7) is about e")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_power()
