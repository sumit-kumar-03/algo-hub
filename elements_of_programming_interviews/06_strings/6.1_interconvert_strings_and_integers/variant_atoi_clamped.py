"""
EPI 6.1 Extra Variant - Forgiving String to 32-Bit Integer
(Practice problem, not in the book. Difficulty: Medium)
Builds on: string_to_int's "result = result * 10 + digit" loop, plus
input cleanup and overflow handling.

Problem:
Convert a messy string to a 32-bit signed integer the way a forgiving
parser would:
1. Skip any leading space characters (' ')
2. Read an optional '+' or '-' sign
3. Read as many digits as possible; stop at the first non-digit and
   ignore the rest of the string
4. If no digits were read, the result is 0
5. If the value falls outside [-2^31, 2^31 - 1], clamp it to the nearest
   end of that range
Do not use int(), float(), or str.isdigit(); compare characters and use
ord() arithmetic.

Constraints:
- 0 <= len(s) <= 10^4; s may contain letters, spaces, signs, dots
- O(n) time; the running value must never grow far beyond 2^31 (stop or
  clamp as soon as it overflows, even if thousands of digits follow)

How it works:
1. i = 0; advance past spaces
2. If s[i] is '+' or '-', record the sign and advance
3. While s[i] is between '0' and '9': result = result * 10 + digit; if
   result already exceeds 2^31 (or 2^31 - 1 for a positive sign), return
   the clamped limit right away
4. Return sign * result

Example 1:
Input: s = "   -42 apples"
Output: -42
Explanation: Spaces skipped, sign read, digits stop at ' '.

Example 2:
Input: s = "91283472332"
Output: 2147483647
Explanation: The value is too large and clamps to 2^31 - 1.
"""


class Solution:
    def my_atoi(self, s: str) -> int:
        """
        Parses a leading integer from s, clamped to 32-bit signed range.

        Args:
            s: Input string

        Returns:
            The parsed integer, or 0 if s has no leading number

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement forgiving string-to-integer parsing
        pass


def test_my_atoi():
    """Test cases for forgiving 32-bit parsing"""
    solution = Solution()
    INT_MAX, INT_MIN = 2**31 - 1, -(2**31)

    # Test case 1: Plain numbers and signs
    assert solution.my_atoi("42") == 42
    assert solution.my_atoi("+7") == 7
    assert solution.my_atoi("-0") == 0
    print("✓ Test 1 passed: '42', '+7', '-0'")

    # Test case 2: Leading spaces and trailing garbage
    assert solution.my_atoi("   -42 apples") == -42
    assert solution.my_atoi("4193 with words") == 4193
    assert solution.my_atoi("3.99") == 3
    print("✓ Test 2 passed: Spaces and trailing text")

    # Test case 3: No digits at the start
    assert solution.my_atoi("") == 0
    assert solution.my_atoi("   ") == 0
    assert solution.my_atoi("words 987") == 0
    assert solution.my_atoi("+-12") == 0
    assert solution.my_atoi("- 5") == 0
    print("✓ Test 3 passed: No leading number -> 0")

    # Test case 4: Leading zeros
    assert solution.my_atoi("  0000000000012345678") == 12345678
    print("✓ Test 4 passed: Leading zeros")

    # Test case 5: Exact limits and clamping
    assert solution.my_atoi("2147483647") == INT_MAX
    assert solution.my_atoi("-2147483648") == INT_MIN
    assert solution.my_atoi("2147483648") == INT_MAX
    assert solution.my_atoi("-2147483649") == INT_MIN
    assert solution.my_atoi("91283472332") == INT_MAX
    print("✓ Test 5 passed: Limits and clamping")

    # Test case 6: Very long digit string clamps
    assert solution.my_atoi("-" + "9" * 10000) == INT_MIN
    assert solution.my_atoi("1" * 9999 + "x") == INT_MAX
    print("✓ Test 6 passed: 10,000-digit inputs clamp")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_my_atoi()
