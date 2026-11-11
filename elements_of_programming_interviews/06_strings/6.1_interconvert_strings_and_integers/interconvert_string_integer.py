"""
EPI 6.1 - Interconvert Strings and Integers

Problem:
Implement two functions: one that converts an integer to its decimal string
representation, and one that converts a decimal string to an integer.
Do not use built-in conversions such as int(), str() or repr().

Constraints:
- Integers may be negative
- Input strings contain an optional leading '-' or '+' followed by digits
- Use ord()/chr() arithmetic (e.g. ord('7') - ord('0') == 7)

How it works:
int_to_string:
1. Record the sign and work with abs(x)
2. Repeatedly take x % 10 as the next (least significant) digit, then x //= 10
3. Reverse the collected digits and prepend '-' if negative

string_to_int:
1. Skip a leading sign character, remembering if it was '-'
2. For each digit: result = result * 10 + digit value
3. Apply the sign

Example 1:
Input: int_to_string(-413)
Output: "-413"

Example 2:
Input: string_to_int("123")
Output: 123
"""


class Solution:
    def int_to_string(self, x: int) -> str:
        """
        Converts an integer to its decimal string representation.

        Args:
            x: Integer to convert

        Returns:
            Decimal string representation of x

        Time Complexity: O(d) where d is the number of digits
        Space Complexity: O(d)
        """
        # TODO: Implement int_to_string without str()
        pass

    def string_to_int(self, s: str) -> int:
        """
        Converts a decimal string to an integer.

        Args:
            s: String of digits with an optional leading sign

        Returns:
            Integer value of s

        Time Complexity: O(n) where n is len(s)
        Space Complexity: O(1)
        """
        # TODO: Implement string_to_int without int()
        pass


def test_interconvert():
    """Test cases for string/integer conversion"""
    solution = Solution()

    # Test case 1: Zero
    assert solution.int_to_string(0) == "0"
    assert solution.string_to_int("0") == 0
    print("✓ Test 1 passed: Zero")

    # Test case 2: Positive number
    assert solution.int_to_string(123) == "123"
    assert solution.string_to_int("123") == 123
    print("✓ Test 2 passed: Positive number")

    # Test case 3: Negative number
    assert solution.int_to_string(-413) == "-413"
    assert solution.string_to_int("-413") == -413
    print("✓ Test 3 passed: Negative number")

    # Test case 4: Explicit plus sign
    assert solution.string_to_int("+42") == 42
    print("✓ Test 4 passed: Explicit plus sign")

    # Test case 5: Large number round trip
    big = 9876543210123456789
    assert solution.int_to_string(big) == "9876543210123456789"
    assert solution.string_to_int(solution.int_to_string(-big)) == -big
    print("✓ Test 5 passed: Large number round trip")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_interconvert()
