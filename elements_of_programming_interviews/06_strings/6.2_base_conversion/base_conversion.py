"""
EPI 6.2 - Base Conversion

Problem:
Given a string representing an integer in base b1, return the string that
represents the same integer in base b2. Digits above 9 are written with the
uppercase letters "A" (10) through "F" (15).

Constraints:
- 2 <= b1, b2 <= 16
- The input may have a leading '-' for negative numbers
- Input digits use 0-9 and uppercase A-F
- O(n * (1 + log_b2(b1))) time where n is the length of the input

How it works:
1. Record the sign and skip a leading '-'
2. Convert the base-b1 string to an integer: value = value * b1 + digit
3. Convert the integer to base b2 by repeatedly taking value % b2 as the
   next (least significant) digit and dividing value by b2
4. Handle zero explicitly, reverse the digits, and prepend '-' if needed

Example 1:
Input: num_as_string = "615", b1 = 7, b2 = 13
Output: "1A7"
Explanation: 6*7^2 + 1*7 + 5 = 306 = 1*13^2 + 10*13 + 7

Example 2:
Input: num_as_string = "-255", b1 = 10, b2 = 16
Output: "-FF"
Explanation: 255 = 15*16 + 15, and the sign is preserved
"""


class Solution:
    def convert_base(self, num_as_string: str, b1: int, b2: int) -> str:
        """
        Converts a number written in base b1 into base b2.

        Args:
            num_as_string: Integer written in base b1 (optional leading '-')
            b1: Base of the input string (2 to 16)
            b2: Base of the output string (2 to 16)

        Returns:
            The same integer written in base b2, using uppercase A-F

        Time Complexity: O(n * (1 + log_b2(b1))) where n is len(num_as_string)
        Space Complexity: O(n * (1 + log_b2(b1))) for the output
        """
        # TODO: Implement base conversion
        pass


def test_convert_base():
    """Test cases for base conversion"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.convert_base("615", 7, 13) == "1A7"
    print("✓ Test 1 passed: '615' base 7 -> '1A7' base 13")

    # Test case 2: Zero
    assert solution.convert_base("0", 10, 2) == "0"
    print("✓ Test 2 passed: Zero stays '0'")

    # Test case 3: Negative number
    assert solution.convert_base("-255", 10, 16) == "-FF"
    print("✓ Test 3 passed: '-255' base 10 -> '-FF' base 16")

    # Test case 4: Hex to binary
    assert solution.convert_base("FF", 16, 2) == "11111111"
    print("✓ Test 4 passed: 'FF' base 16 -> '11111111' base 2")

    # Test case 5: Binary to decimal
    assert solution.convert_base("1010", 2, 10) == "10"
    print("✓ Test 5 passed: '1010' base 2 -> '10' base 10")

    # Test case 6: Round trip back to the original base
    assert solution.convert_base("-1A7", 13, 7) == "-615"
    print("✓ Test 6 passed: '-1A7' base 13 -> '-615' base 7")

    # Test case 7: Same base leaves the number unchanged
    assert solution.convert_base("12345", 10, 10) == "12345"
    print("✓ Test 7 passed: Same base is a no-op")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_convert_base()
