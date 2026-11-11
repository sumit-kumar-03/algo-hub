"""
EPI 6.2 Extra Variant - Palindrome in Base b
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Peeling off base-b digits with value % b and value // b.

Problem:
Given a nonnegative integer n and a base b, decide whether the base-b
representation of n (without leading zeros) reads the same forward and
backward. Do it arithmetically, without building a string or a list of
digits.

Constraints:
- 0 <= n <= 10^18
- 2 <= b <= 16
- O(log_b(n)) time, O(1) extra space

How it works:
1. Build the base-b reversal of n: repeatedly take the last digit
   n % b, append it to reversed_value (reversed_value * b + digit), and
   drop it from n with n // b
2. n is a base-b palindrome exactly when its reversal equals n

Example 1:
Input: n = 585, b = 2
Output: True
Explanation: 585 is 1001001001 in binary, which is a palindrome

Example 2:
Input: n = 6, b = 2
Output: False
Explanation: 6 is 110 in binary; reversed it is 011
"""


class Solution:
    def is_palindrome_in_base(self, n: int, b: int) -> bool:
        """
        Checks whether n written in base b is a palindrome.

        Args:
            n: Nonnegative integer to test
            b: Base (2 to 16)

        Returns:
            True if the base-b digits of n form a palindrome, else False

        Time Complexity: O(log_b(n))
        Space Complexity: O(1)
        """
        # TODO: Implement the base-b palindrome check
        pass


def test_is_palindrome_in_base():
    """Test cases for palindrome in base b"""
    solution = Solution()

    # Test case 1: Zero and single digits are palindromes
    assert solution.is_palindrome_in_base(0, 2) is True
    assert solution.is_palindrome_in_base(9, 10) is True
    print("✓ Test 1 passed: Zero and single digits")

    # Test case 2: Binary palindrome and non-palindrome
    assert solution.is_palindrome_in_base(5, 2) is True
    assert solution.is_palindrome_in_base(6, 2) is False
    print("✓ Test 2 passed: 101 is a palindrome, 110 is not")

    # Test case 3: Palindrome in two bases at once
    assert solution.is_palindrome_in_base(585, 2) is True
    assert solution.is_palindrome_in_base(585, 10) is True
    print("✓ Test 3 passed: 585 is a palindrome in base 2 and base 10")

    # Test case 4: Trailing zero breaks the palindrome
    assert solution.is_palindrome_in_base(16, 16) is False
    assert solution.is_palindrome_in_base(10, 10) is False
    print("✓ Test 4 passed: Trailing zero means not a palindrome")

    # Test case 5: Depends on the base
    assert solution.is_palindrome_in_base(10, 3) is True  # 101
    assert solution.is_palindrome_in_base(10, 2) is False  # 1010
    assert solution.is_palindrome_in_base(255, 16) is True  # FF
    print("✓ Test 5 passed: Answer depends on the base")

    # Test case 6: Large value
    assert solution.is_palindrome_in_base(2**60 + 1, 2) is True
    assert solution.is_palindrome_in_base(2**60 + 2, 2) is False
    print("✓ Test 6 passed: 61-bit values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_palindrome_in_base()
