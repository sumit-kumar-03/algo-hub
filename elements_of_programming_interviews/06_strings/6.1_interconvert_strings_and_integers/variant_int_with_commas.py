"""
EPI 6.1 Extra Variant - Integer to String with Thousands Separators
(Practice problem, not in the book. Difficulty: Easy)
Builds on: producing decimal digits from least to most significant with
x % 10 and x // 10, then reversing.

Problem:
Given an integer x, return its decimal representation with a comma
between every group of three digits, counting from the right, e.g.
1234567 -> "1,234,567". Negative numbers get a leading '-'. Do not use
str(), repr(), format(), f-strings, or any other built-in number
formatting; build the digits yourself with chr()/ord() arithmetic.

Constraints:
- -10^18 <= x <= 10^18
- O(d) time where d is the number of digits

How it works:
1. Handle 0 directly. Record the sign and work with abs(x)
2. Peel digits with x % 10 and x //= 10, appending
   chr(ord('0') + digit); after every third digit, if more digits remain,
   append ','
3. Append '-' if negative, reverse the collected characters, and join

Example 1:
Input: x = 1234567
Output: "1,234,567"

Example 2:
Input: x = -1000
Output: "-1,000"
"""


class Solution:
    def format_with_commas(self, x: int) -> str:
        """
        Converts an integer to a decimal string with thousands separators.

        Args:
            x: Integer to format

        Returns:
            The decimal representation with commas every three digits

        Time Complexity: O(d) where d is the number of digits
        Space Complexity: O(d)
        """
        # TODO: Implement integer formatting with commas
        pass


def test_format_with_commas():
    """Test cases for thousands-separator formatting"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.format_with_commas(1234567) == "1,234,567"
    print("✓ Test 1 passed: 1234567 -> '1,234,567'")

    # Test case 2: Zero and short numbers need no comma
    assert solution.format_with_commas(0) == "0"
    assert solution.format_with_commas(7) == "7"
    assert solution.format_with_commas(999) == "999"
    print("✓ Test 2 passed: 0, 7, 999")

    # Test case 3: Exact group boundaries
    assert solution.format_with_commas(1000) == "1,000"
    assert solution.format_with_commas(100000) == "100,000"
    assert solution.format_with_commas(999999) == "999,999"
    print("✓ Test 3 passed: 1000, 100000, 999999")

    # Test case 4: Negative numbers
    assert solution.format_with_commas(-1000) == "-1,000"
    assert solution.format_with_commas(-5) == "-5"
    assert solution.format_with_commas(-12345) == "-12,345"
    print("✓ Test 4 passed: Negative numbers")

    # Test case 5: Zeros inside groups are kept
    assert solution.format_with_commas(1000001) == "1,000,001"
    assert solution.format_with_commas(10020030) == "10,020,030"
    print("✓ Test 5 passed: Inner zeros")

    # Test case 6: Extremes
    assert solution.format_with_commas(10**18) == "1,000,000,000,000,000,000"
    assert solution.format_with_commas(-(10**18) + 1) == "-999,999,999,999,999,999"
    print("✓ Test 6 passed: +/- 10^18")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_format_with_commas()
