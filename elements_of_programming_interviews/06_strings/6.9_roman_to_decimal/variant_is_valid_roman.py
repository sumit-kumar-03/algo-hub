"""
EPI 6.9 Variant - Validate a Roman Number String

Problem:
Given a string, decide whether it is a valid Roman number string under the
simplified rules of EPI 6.9:
- Only the symbols I, V, X, L, C, D, M may appear, and the string is
  nonempty
- Whenever a symbol is immediately followed by a symbol of larger value,
  the pair must be one of the six allowed exceptions:
      IV, IX, XL, XC, CD, CM
- Exceptions may not be back to back: a symbol can't be the larger half of
  one exception and the smaller half of the next (e.g. "IXC" is invalid)
Any other adjacent pair must be in nonincreasing order of value.

Constraints:
- 0 <= len(s) <= 100
- O(n) time, O(1) extra space

How it works:
1. Reject an empty string or any character outside the symbol table
2. Scan adjacent pairs (s[i], s[i + 1])
3. If value(s[i]) < value(s[i + 1]): the pair must be one of the six
   exceptions, and the previous pair (s[i - 1], s[i]) must not also have
   been increasing
4. Return True if no rule is broken

Example 1:
Input: s = "LIX"
Output: True
Explanation: L >= I, and IX is an allowed exception

Example 2:
Input: s = "IC"
Output: False
Explanation: I may only precede V and X
"""


class Solution:
    def is_valid_roman(self, s: str) -> bool:
        """
        Checks whether s is a valid Roman number string.

        Args:
            s: Candidate string

        Returns:
            True if s follows the simplified Roman rules, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Roman string validation
        pass


def test_is_valid_roman():
    """Test cases for Roman string validation"""
    solution = Solution()

    # Test case 1: Valid ways to write 59
    assert solution.is_valid_roman("LIX") is True
    assert solution.is_valid_roman("LVIII") is True
    assert solution.is_valid_roman("XXXXXIIIIIIIII") is True
    print("✓ Test 1 passed: Valid representations of 59")

    # Test case 2: Standard numerals with several exceptions
    assert solution.is_valid_roman("MCMXCIV") is True
    assert solution.is_valid_roman("MMMCMXCIX") is True
    print("✓ Test 2 passed: 'MCMXCIV' and 'MMMCMXCIX' are valid")

    # Test case 3: Disallowed smaller-before-larger pairs
    assert solution.is_valid_roman("IC") is False
    assert solution.is_valid_roman("VX") is False
    assert solution.is_valid_roman("XM") is False
    print("✓ Test 3 passed: 'IC', 'VX', 'XM' are invalid")

    # Test case 4: Back-to-back exceptions
    assert solution.is_valid_roman("IXC") is False
    assert solution.is_valid_roman("XCM") is False
    print("✓ Test 4 passed: 'IXC' and 'XCM' are invalid")

    # Test case 5: Increasing pair that is not an exception
    assert solution.is_valid_roman("CDM") is False
    print("✓ Test 5 passed: 'CDM' is invalid")

    # Test case 6: Bad characters or empty input
    assert solution.is_valid_roman("") is False
    assert solution.is_valid_roman("XIZ") is False
    assert solution.is_valid_roman("xiv") is False
    print("✓ Test 6 passed: Empty or unknown symbols are invalid")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_valid_roman()
