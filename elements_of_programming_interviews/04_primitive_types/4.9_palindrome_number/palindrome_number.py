"""
EPI 4.9 - Check if a Decimal Integer Is a Palindrome

Problem:
Determine whether the decimal string representation of an integer reads
the same forwards and backwards. Negative numbers are never palindromes
because their string starts with '-'.

Constraints:
- x is any integer
- Aim for O(n) time and O(1) space, where n is the number of digits
  (i.e. do not build the decimal string)

How it works (compare outermost digits):
1. If x < 0, return False
2. Let n = number of digits; mask = 10^(n - 1)
3. While x is not 0:
   - Compare the leading digit (x // mask) with the trailing digit (x % 10)
   - If they differ, return False
   - Strip both digits: x = (x % mask) // 10; mask //= 100
4. Return True

Example 1:
Input: x = 2147447412
Output: True
Explanation: The digits read the same in both directions.

Example 2:
Input: x = 100
Output: False
Explanation: "100" reversed is "001".
"""


class Solution:
    def is_palindrome_number(self, x: int) -> bool:
        """
        Checks whether the decimal representation of x is a palindrome.

        Args:
            x: Any integer

        Returns:
            True if x's decimal string is a palindrome, False otherwise

        Time Complexity: O(n) where n is the number of digits
        Space Complexity: O(1)
        """
        # TODO: Implement palindrome check on the digits
        pass


def test_is_palindrome_number():
    """Test cases for palindrome number implementation"""
    solution = Solution()

    # Test case 1: Single digits are palindromes
    for x in (0, 1, 7):
        assert solution.is_palindrome_number(x) is True
    print("✓ Test 1 passed: 0, 1, 7 are palindromes")

    # Test case 2: Multi-digit palindromes
    for x in (11, 121, 333, 2147447412):
        assert solution.is_palindrome_number(x) is True
    print("✓ Test 2 passed: 11, 121, 333, 2147447412 are palindromes")

    # Test case 3: Negative numbers are never palindromes
    assert solution.is_palindrome_number(-1) is False
    assert solution.is_palindrome_number(-121) is False
    print("✓ Test 3 passed: -1, -121 are not palindromes")

    # Test case 4: Trailing zeros break symmetry
    assert solution.is_palindrome_number(100) is False
    assert solution.is_palindrome_number(10) is False
    print("✓ Test 4 passed: 100, 10 are not palindromes")

    # Test case 5: Non-palindromes
    assert solution.is_palindrome_number(12) is False
    assert solution.is_palindrome_number(2147483647) is False
    print("✓ Test 5 passed: 12, 2147483647 are not palindromes")

    # Test case 6: Inner zeros must also match
    assert solution.is_palindrome_number(1000021) is False
    assert solution.is_palindrome_number(1000001) is True
    print("✓ Test 6 passed: 1000021 is not, 1000001 is a palindrome")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_palindrome_number()
