"""
EPI 6.1 Extra Variant - Compare Two Integer Strings Without Converting
(Practice problem, not in the book. Difficulty: Medium)
Builds on: reading a decimal string as sign + digits, where the value of
each digit depends on its position.

Problem:
Given two strings a and b, each holding a decimal integer with an
optional leading '+' or '-' and possibly leading zeros, return -1 if
a < b, 0 if they are equal, and 1 if a > b. The numbers can have up to
10^5 digits, so do not convert them with int() or build their values;
compare them as strings. Note that "-0", "+0" and "000" are all zero.

Constraints:
- 1 <= number of digits in each string <= 10^5
- Each string matches: optional sign, then one or more digits
- O(len(a) + len(b)) time, O(1) extra space (index into the strings
  instead of copying them)

How it works:
1. For each string, find where its digits start (after the sign) and skip
   leading zeros; what is left is the magnitude (empty means zero, and
   zero has no sign)
2. If the signs differ, the positive one (or the zero vs a negative) is
   larger
3. Same sign: the magnitude with more digits is larger; with equal
   lengths, the first differing digit decides
4. For two negatives, flip the magnitude result

Example 1:
Input: a = "-0045", b = "-123"
Output: 1
Explanation: -45 > -123.

Example 2:
Input: a = "+000", b = "-0"
Output: 0
Explanation: Both are zero.
"""


class Solution:
    def compare_numbers(self, a: str, b: str) -> int:
        """
        Compares two decimal integer strings by value.

        Args:
            a: Integer string with optional sign and leading zeros
            b: Integer string with optional sign and leading zeros

        Returns:
            -1 if a < b, 0 if a == b, 1 if a > b

        Time Complexity: O(len(a) + len(b))
        Space Complexity: O(1)
        """
        # TODO: Implement numeric string comparison
        pass


def test_compare_numbers():
    """Test cases for comparing integer strings"""
    solution = Solution()

    # Test case 1: Simple comparisons
    assert solution.compare_numbers("12", "13") == -1
    assert solution.compare_numbers("13", "12") == 1
    assert solution.compare_numbers("99", "99") == 0
    print("✓ Test 1 passed: Simple comparisons")

    # Test case 2: Length decides (not alphabetical order)
    assert solution.compare_numbers("9", "10") == -1
    assert solution.compare_numbers("100", "99") == 1
    print("✓ Test 2 passed: '9' < '10', '100' > '99'")

    # Test case 3: Leading zeros and plus signs
    assert solution.compare_numbers("000123", "123") == 0
    assert solution.compare_numbers("+0099", "100") == -1
    print("✓ Test 3 passed: Leading zeros and '+'")

    # Test case 4: The many spellings of zero
    assert solution.compare_numbers("+000", "-0") == 0
    assert solution.compare_numbers("-0", "0") == 0
    assert solution.compare_numbers("-000", "-1") == 1
    print("✓ Test 4 passed: Zero with signs")

    # Test case 5: Negative numbers
    assert solution.compare_numbers("-0045", "-123") == 1
    assert solution.compare_numbers("-5", "3") == -1
    assert solution.compare_numbers("-12", "-12") == 0
    assert solution.compare_numbers("-130", "-129") == -1
    print("✓ Test 5 passed: Negative numbers")

    # Test case 6: Very long numbers that differ in the last digit
    big = "7" * 99999
    assert solution.compare_numbers(big + "1", big + "2") == -1
    assert solution.compare_numbers("-" + big + "1", "-" + big + "2") == 1
    assert solution.compare_numbers("0" * 50000 + big, big) == 0
    print("✓ Test 6 passed: 100,000-digit numbers")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compare_numbers()
