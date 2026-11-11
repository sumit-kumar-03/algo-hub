"""
EPI 6.1 Extra Variant - Fraction to Decimal String
(Practice problem, not in the book. Difficulty: Hard)
Builds on: generating decimal digits one at a time with % and //, here
continued past the decimal point by long division.

Problem:
Given integers numerator and denominator (denominator != 0), return the
exact value of numerator / denominator as a decimal string. If the
fractional part repeats forever, put the repeating block in parentheses,
e.g. 1/6 -> "0.1(6)". Omit the decimal point when the result is an
integer, and never write "-0". Do not use str(), float(), the decimal or
fractions modules, or any built-in formatting; build every digit with
chr()/ord() arithmetic.

Constraints:
- -2^31 <= numerator, denominator <= 2^31 - 1; denominator != 0
- O(denominator) time and space in the worst case (a fraction with
  denominator d has at most d - 1 distinct remainders)

How it works (long division with remainder memory):
1. Decide the sign (negative iff exactly one input is negative and the
   numerator is not 0); continue with absolute values n and d
2. Integer part: n // d, converted digit by digit; r = n % d
3. If r == 0, done. Otherwise add '.', and repeat:
   - If r was seen before at output position p, insert '(' at p and
     append ')': the digits since p repeat forever
   - Remember r -> current position; r *= 10; append digit r // d;
     r %= d; stop if r == 0

Example 1:
Input: numerator = 4, denominator = 333
Output: "0.(012)"
Explanation: 4/333 = 0.012012012...

Example 2:
Input: numerator = -50, denominator = 8
Output: "-6.25"
"""


class Solution:
    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        """
        Writes a fraction as a decimal string with repeating digits in parentheses.

        Args:
            numerator: Integer numerator
            denominator: Nonzero integer denominator

        Returns:
            The exact decimal expansion, e.g. "0.1(6)" or "-6.25"

        Time Complexity: O(d) where d = |denominator|
        Space Complexity: O(d)
        """
        # TODO: Implement fraction to decimal conversion
        pass


def test_fraction_to_decimal():
    """Test cases for fraction to decimal"""
    solution = Solution()

    # Test case 1: Integers and terminating decimals
    assert solution.fraction_to_decimal(2, 1) == "2"
    assert solution.fraction_to_decimal(1, 2) == "0.5"
    assert solution.fraction_to_decimal(-50, 8) == "-6.25"
    print("✓ Test 1 passed: 2/1, 1/2, -50/8")

    # Test case 2: Pure repeating decimals
    assert solution.fraction_to_decimal(1, 3) == "0.(3)"
    assert solution.fraction_to_decimal(4, 333) == "0.(012)"
    assert solution.fraction_to_decimal(1, 7) == "0.(142857)"
    print("✓ Test 2 passed: 1/3, 4/333, 1/7")

    # Test case 3: Repeating block after a non-repeating prefix
    assert solution.fraction_to_decimal(1, 6) == "0.1(6)"
    assert solution.fraction_to_decimal(22, 7) == "3.(142857)"
    assert solution.fraction_to_decimal(1, 90) == "0.0(1)"
    print("✓ Test 3 passed: 1/6, 22/7, 1/90")

    # Test case 4: Signs and zero
    assert solution.fraction_to_decimal(0, -5) == "0"
    assert solution.fraction_to_decimal(-1, -3) == "0.(3)"
    assert solution.fraction_to_decimal(7, -12) == "-0.58(3)"
    print("✓ Test 4 passed: Signs and zero")

    # Test case 5: 32-bit extremes
    assert solution.fraction_to_decimal(-2147483648, -1) == "2147483648"
    assert solution.fraction_to_decimal(-1, -2147483648) == "0.0000000004656612873077392578125"
    assert solution.fraction_to_decimal(2147483647, 1) == "2147483647"
    print("✓ Test 5 passed: 32-bit extremes")

    # Test case 6: Long repeating block
    result = solution.fraction_to_decimal(1, 9967)  # 1/9967 repeats with period 9966
    assert result.startswith("0.(0001003310926055") and result.endswith(")")
    assert len(result) == len("0.()") + 9966
    print("✓ Test 6 passed: 1/9967 has a 9966-digit repeating block")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fraction_to_decimal()
