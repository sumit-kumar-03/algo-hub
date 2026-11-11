"""
EPI 4.8 - Reverse Digits

Problem:
Given an integer, return the integer formed by writing its decimal digits
in reverse order. The sign is kept: reversing -314 gives -413.

Constraints:
- x is any integer (positive, negative, or zero)
- Trailing zeros of the input disappear (reverse of 120 is 21)
- Aim for O(n) time where n is the number of digits, without converting
  to a string

How it works:
1. Remember the sign and work with |x|
2. result = 0; while the remaining value is not 0:
   - result = result * 10 + (remaining % 10)
   - remaining //= 10
3. Reapply the sign to result

Example 1:
Input: x = 42
Output: 24
Explanation: The digits 4, 2 read backwards are 2, 4.

Example 2:
Input: x = -314
Output: -413
Explanation: The sign stays; the digits 3, 1, 4 become 4, 1, 3.
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the decimal digits of an integer.

        Args:
            x: Any integer

        Returns:
            The integer whose digits are those of x in reverse, with x's sign

        Time Complexity: O(n) where n is the number of digits
        Space Complexity: O(1)
        """
        # TODO: Implement digit reversal
        pass


def test_reverse():
    """Test cases for reverse digits implementation"""
    solution = Solution()

    # Test case 1: Book example, positive
    assert solution.reverse(42) == 24
    print("✓ Test 1 passed: reverse(42) == 24")

    # Test case 2: Book example, negative
    assert solution.reverse(-314) == -413
    print("✓ Test 2 passed: reverse(-314) == -413")

    # Test case 3: Zero
    assert solution.reverse(0) == 0
    print("✓ Test 3 passed: reverse(0) == 0")

    # Test case 4: Single digit
    assert solution.reverse(7) == 7
    assert solution.reverse(-7) == -7
    print("✓ Test 4 passed: Single digits are unchanged")

    # Test case 5: Trailing zeros vanish
    assert solution.reverse(1200) == 21
    print("✓ Test 5 passed: reverse(1200) == 21")

    # Test case 6: Larger number
    assert solution.reverse(1132) == 2311
    assert solution.reverse(-1000000003) == -3000000001
    print("✓ Test 6 passed: reverse(1132) == 2311, reverse(-1000000003) == -3000000001")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse()
