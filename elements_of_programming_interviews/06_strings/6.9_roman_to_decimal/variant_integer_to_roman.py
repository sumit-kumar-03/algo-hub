"""
EPI 6.9 Variant - Shortest Roman Number String

Problem:
Given a positive integer n, return a shortest valid Roman number string
that represents n under the rules of EPI 6.9 (symbols in nonincreasing
order, with the six exceptions IV, IX, XL, XC, CD, CM allowed).

Constraints:
- 1 <= n <= 10^4 (values of 4000 and above simply repeat M)
- O(n / 1000 + 1) time, i.e. proportional to the output length

How it works:
1. List the symbols and exception pairs from largest to smallest value:
   M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10,
   IX=9, V=5, IV=4, I=1
2. Greedily take the largest entry that fits, subtract it from n, and
   append its symbols, until n reaches 0

Example 1:
Input: n = 59
Output: "LIX"
Explanation: "LVIIII" and "XXXXXIIIIIIIII" are also valid, but longer

Example 2:
Input: n = 1994
Output: "MCMXCIV"
Explanation: M + CM + XC + IV = 1000 + 900 + 90 + 4
"""


class Solution:
    def integer_to_roman(self, n: int) -> str:
        """
        Converts a positive integer to its shortest valid Roman string.

        Args:
            n: Positive integer

        Returns:
            A shortest valid Roman number string with value n

        Time Complexity: O(length of the output)
        Space Complexity: O(length of the output)
        """
        # TODO: Implement greedy integer to Roman conversion
        pass


def test_integer_to_roman():
    """Test cases for integer to Roman conversion"""
    solution = Solution()

    # Test case 1: Single symbols
    assert solution.integer_to_roman(1) == "I"
    assert solution.integer_to_roman(500) == "D"
    print("✓ Test 1 passed: 1 -> 'I', 500 -> 'D'")

    # Test case 2: Book example
    assert solution.integer_to_roman(59) == "LIX"
    print("✓ Test 2 passed: 59 -> 'LIX'")

    # Test case 3: Exception pairs
    assert solution.integer_to_roman(4) == "IV"
    assert solution.integer_to_roman(9) == "IX"
    assert solution.integer_to_roman(40) == "XL"
    assert solution.integer_to_roman(400) == "CD"
    print("✓ Test 3 passed: 4, 9, 40, 400")

    # Test case 4: Several exceptions combined
    assert solution.integer_to_roman(1994) == "MCMXCIV"
    print("✓ Test 4 passed: 1994 -> 'MCMXCIV'")

    # Test case 5: Large values
    assert solution.integer_to_roman(3999) == "MMMCMXCIX"
    assert solution.integer_to_roman(3888) == "MMMDCCCLXXXVIII"
    print("✓ Test 5 passed: 3999 and 3888")

    # Test case 6: Values without exceptions
    assert solution.integer_to_roman(1666) == "MDCLXVI"
    assert solution.integer_to_roman(3) == "III"
    print("✓ Test 6 passed: 1666 and 3")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_integer_to_roman()
