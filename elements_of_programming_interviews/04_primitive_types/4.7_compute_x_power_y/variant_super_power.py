"""
EPI 4.7 Extra Variant - Power with an Exponent Given as Digits
(Practice problem, not in the book. Difficulty: Medium)
Builds on: repeated squaring, but driven by decimal digits of the exponent
instead of its binary bits.

Problem:
Given an integer a, a modulus m, and a very large non-negative exponent
written as a list of decimal digits (most significant digit first), return
a^exponent mod m. The exponent can have thousands of digits, so you
cannot turn it into a machine-size number or walk its binary bits
directly. Do not use the built-in pow() or the ** operator, and do not
convert the digit list into a single integer.

Constraints:
- a >= 0; 1 <= m <= 10^9
- 1 <= len(digits) <= 10^4, each entry in 0..9, no leading zeros unless
  the exponent is exactly [0]
- a^0 is 1 mod m (which is 0 when m == 1)
- O(len(digits)) modular multiplications (each digit costs O(1) work)

How it works (Horner's rule on the exponent):
1. If the exponent so far is e, appending digit d gives 10 * e + d, so
   a^(10e + d) = (a^e)^10 * a^d
2. result = 1 % m. For each digit d:
   result = power(result, 10) * power(a, d) mod m, where power() is a
   small repeated-squaring helper for exponents 0..10
3. Return result

Example 1:
Input: a = 2, digits = [1, 0], m = 1337
Output: 1024
Explanation: 2^10 = 1024, which is already below 1337.

Example 2:
Input: a = 2, digits = [3], m = 1337
Output: 8
Explanation: 2^3 = 8.
"""

from typing import List


class Solution:
    def super_power(self, a: int, digits: List[int], m: int) -> int:
        """
        Computes a raised to a digit-list exponent, modulo m.

        Args:
            a: Non-negative base
            digits: Exponent as decimal digits, most significant first
            m: Positive modulus

        Returns:
            a^exponent mod m, in the range [0, m - 1]

        Time Complexity: O(len(digits))
        Space Complexity: O(1)
        """
        # TODO: Implement exponentiation by a digit-list exponent
        pass


def test_super_power():
    """Test cases for digit-list exponentiation"""
    solution = Solution()

    # Test case 1: Examples
    assert solution.super_power(2, [1, 0], 1337) == 1024
    assert solution.super_power(2, [3], 1337) == 8
    print("✓ Test 1 passed: 2^10 and 2^3 mod 1337")

    # Test case 2: Zero exponent and modulus 1
    assert solution.super_power(9, [0], 1000) == 1
    assert solution.super_power(9, [5, 2], 1) == 0
    print("✓ Test 2 passed: Exponent 0 and m = 1")

    # Test case 3: Base 0 and base 1
    assert solution.super_power(0, [1, 2, 3], 97) == 0
    assert solution.super_power(1, [9, 9, 9, 9], 97) == 1
    print("✓ Test 3 passed: Base 0 and base 1")

    # Test case 4: Base larger than the modulus
    assert solution.super_power(2147483647, [2, 0, 0], 1337) == pow(2147483647, 200, 1337)
    print("✓ Test 4 passed: Large base")

    # Test case 5: Exponent with many digits
    digits = [(7 * i + 3) % 10 for i in range(1000)]
    digits[0] = 4
    e = 0
    for d in digits:
        e = e * 10 + d
    assert solution.super_power(78267, digits, 10**9 + 7) == pow(78267, e, 10**9 + 7)
    print("✓ Test 5 passed: 1000-digit exponent")

    # Test case 6: Composite modulus and exponent with zeros inside
    digits = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert solution.super_power(12, digits, 10**9) == pow(12, 10**18 + 1, 10**9)
    print("✓ Test 6 passed: 12^(10^18 + 1) mod 10^9")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_super_power()
