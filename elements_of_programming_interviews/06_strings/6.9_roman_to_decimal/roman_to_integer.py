"""
EPI 6.9 - Convert from Roman to Decimal

Problem:
Roman numerals use the symbols I=1, V=5, X=10, L=50, C=100, D=500 and
M=1000. Under the simplified rules used here, a valid Roman string lists
symbols in nonincreasing order of value, except that these six pairs may
appear with the smaller symbol directly before the larger one:
    IV, IX, XL, XC, CD, CM
Two such exceptions may not overlap (e.g. "IXC" is invalid). The value of
a valid string is the sum of its symbols, where each exception pair
contributes (larger - smaller). Given a valid Roman string, return its
integer value.

Constraints:
- 1 <= len(s) <= 100
- s is guaranteed to be valid
- O(n) time, O(1) extra space

How it works:
1. Start with the value of the last symbol
2. Walk from the second-to-last symbol to the first
3. If the current symbol is smaller than the one after it, subtract its
   value; otherwise add it

Example 1:
Input: s = "LIX"
Output: 59
Explanation: L = 50, IX = 9

Example 2:
Input: s = "XXXXXIIIIIIIII"
Output: 59
Explanation: Five X's plus nine I's (valid, though not the shortest form)
"""


class Solution:
    def roman_to_integer(self, s: str) -> int:
        """
        Converts a valid Roman number string to an integer.

        Args:
            s: Valid Roman number string

        Returns:
            The integer value of s

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Roman to integer conversion
        pass


def test_roman_to_integer():
    """Test cases for Roman to decimal conversion"""
    solution = Solution()

    # Test case 1: Single symbols
    assert solution.roman_to_integer("I") == 1
    assert solution.roman_to_integer("M") == 1000
    print("✓ Test 1 passed: Single symbols")

    # Test case 2: Three ways to write 59
    assert solution.roman_to_integer("LIX") == 59
    assert solution.roman_to_integer("LVIIII") == 59
    assert solution.roman_to_integer("XXXXXIIIIIIIII") == 59
    print("✓ Test 2 passed: 'LIX', 'LVIIII', 'XXXXXIIIIIIIII' -> 59")

    # Test case 3: Subtractive pairs
    assert solution.roman_to_integer("IV") == 4
    assert solution.roman_to_integer("XC") == 90
    assert solution.roman_to_integer("CM") == 900
    print("✓ Test 3 passed: Subtractive pairs")

    # Test case 4: Mixed numeral
    assert solution.roman_to_integer("MCMXCIV") == 1994
    print("✓ Test 4 passed: 'MCMXCIV' -> 1994")

    # Test case 5: Largest standard numeral
    assert solution.roman_to_integer("MMMCMXCIX") == 3999
    print("✓ Test 5 passed: 'MMMCMXCIX' -> 3999")

    # Test case 6: No subtractive pairs
    assert solution.roman_to_integer("MDCLXVI") == 1666
    print("✓ Test 6 passed: 'MDCLXVI' -> 1666")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_roman_to_integer()
