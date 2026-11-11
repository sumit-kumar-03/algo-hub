"""
EPI 4.7 Extra Variant - Modular Exponentiation
(Practice problem, not in the book. Difficulty: Easy)
Builds on: repeated squaring driven by the bits of the exponent.

Problem:
Given integers x, y and m, return x^y mod m as a value in [0, m - 1].
The exponent can be as large as 10^18, so multiplying x by itself y times
is far too slow, and computing x^y first and then taking the remainder
creates a gigantic number. Do not use the built-in pow() or the **
operator.

Constraints:
- x is any integer (it may be negative); 0 <= y <= 10^18; 1 <= m <= 10^18
- x^0 mod m is 1 mod m (which is 0 when m == 1)
- O(log y) multiplications, each on numbers smaller than m^2

How it works (repeated squaring, reducing as you go):
1. result = 1 % m, base = x % m (Python's % already gives a value in
   [0, m - 1] for a negative x)
2. While y > 0:
   - If y is odd, result = result * base % m
   - base = base * base % m, y >>= 1
3. Return result

Example 1:
Input: x = 2, y = 10, m = 1000
Output: 24
Explanation: 2^10 = 1024, and 1024 mod 1000 = 24.

Example 2:
Input: x = -2, y = 3, m = 5
Output: 2
Explanation: (-2)^3 = -8, and -8 mod 5 = 2.
"""


class Solution:
    def mod_power(self, x: int, y: int, m: int) -> int:
        """
        Computes x^y mod m with repeated squaring.

        Args:
            x: Base (any integer)
            y: Non-negative exponent
            m: Positive modulus

        Returns:
            x^y mod m, in the range [0, m - 1]

        Time Complexity: O(log y)
        Space Complexity: O(1)
        """
        # TODO: Implement modular exponentiation
        pass


def test_mod_power():
    """Test cases for modular exponentiation"""
    solution = Solution()
    MOD = 10**9 + 7

    # Test case 1: Example 1
    assert solution.mod_power(2, 10, 1000) == 24
    print("✓ Test 1 passed: 2^10 mod 1000 == 24")

    # Test case 2: Zero exponent, including modulus 1
    assert solution.mod_power(3, 0, 7) == 1
    assert solution.mod_power(3, 0, 1) == 0
    assert solution.mod_power(5, 3, 1) == 0
    print("✓ Test 2 passed: y = 0 and m = 1")

    # Test case 3: Negative base
    assert solution.mod_power(-2, 3, 5) == 2
    assert solution.mod_power(-2, 4, 5) == 1
    print("✓ Test 3 passed: Negative base")

    # Test case 4: Zero base
    assert solution.mod_power(0, 0, 13) == 1
    assert solution.mod_power(0, 5, 13) == 0
    print("✓ Test 4 passed: Zero base")

    # Test case 5: Huge exponent with a prime modulus
    assert solution.mod_power(2, 10**18, MOD) == pow(2, 10**18, MOD)
    assert solution.mod_power(123456789, 987654321, MOD) == pow(123456789, 987654321, MOD)
    print("✓ Test 5 passed: Huge exponents mod 10^9 + 7")

    # Test case 6: Huge modulus and base larger than the modulus
    m = 10**18 - 11
    assert solution.mod_power(10**20 + 3, 10**17 + 1, m) == pow(10**20 + 3, 10**17 + 1, m)
    print("✓ Test 6 passed: Modulus near 10^18")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_mod_power()
