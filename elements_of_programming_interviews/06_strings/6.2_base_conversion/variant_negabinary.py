"""
EPI 6.2 Extra Variant - Convert to Base -2
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Repeated division by the target base, collecting remainders.

Problem:
In base -2 (negabinary) every digit is 0 or 1, and the digit at position i
is worth (-2)^i. Every integer, positive or negative, has exactly one
negabinary representation and needs no sign. Given an integer n, return its
negabinary representation as a string of '0's and '1's with no leading
zeros ("0" for zero).

Constraints:
- -10^9 <= n <= 10^9
- O(log |n|) time

How it works:
1. The remainder must be 0 or 1, so take digit = n & 1 (works for
   negative n as well)
2. Remove that digit and divide by the base: n = (n - digit) // -2;
   the subtraction makes the division exact
3. Repeat until n is 0, then reverse the collected digits
4. Return "0" if no digits were produced

Example 1:
Input: n = 2
Output: "110"
Explanation: (-2)^2 + (-2)^1 = 4 - 2 = 2

Example 2:
Input: n = -1
Output: "11"
Explanation: (-2)^1 + (-2)^0 = -2 + 1 = -1
"""


class Solution:
    def to_negabinary(self, n: int) -> str:
        """
        Writes n in base -2.

        Args:
            n: Any integer

        Returns:
            The base -2 digits of n, most significant first

        Time Complexity: O(log |n|)
        Space Complexity: O(log |n|) for the output
        """
        # TODO: Implement conversion to base -2
        pass


def negabinary_value(digits: str) -> int:
    """Evaluates a string of base -2 digits."""
    value = 0
    for d in digits:
        value = value * -2 + int(d)
    return value


def test_to_negabinary():
    """Test cases for converting to base -2"""
    solution = Solution()

    # Test case 1: Zero
    assert solution.to_negabinary(0) == "0"
    print("✓ Test 1 passed: 0 -> '0'")

    # Test case 2: Small positives
    assert solution.to_negabinary(1) == "1"
    assert solution.to_negabinary(2) == "110"
    assert solution.to_negabinary(3) == "111"
    assert solution.to_negabinary(4) == "100"
    print("✓ Test 2 passed: 1, 2, 3, 4")

    # Test case 3: Small negatives need no sign
    assert solution.to_negabinary(-1) == "11"
    assert solution.to_negabinary(-2) == "10"
    assert solution.to_negabinary(-3) == "1101"
    print("✓ Test 3 passed: -1, -2, -3")

    # Test case 4: Larger value
    assert solution.to_negabinary(6) == "11010"
    print("✓ Test 4 passed: 6 -> '11010'")

    # Test case 5: Round trip over a range, no leading zeros
    for n in range(-300, 301):
        digits = solution.to_negabinary(n)
        assert set(digits) <= {"0", "1"}
        assert digits == "0" or digits[0] == "1"
        assert negabinary_value(digits) == n
    print("✓ Test 5 passed: Round trip for -300..300")

    # Test case 6: Extremes
    for n in (10**9, -(10**9)):
        assert negabinary_value(solution.to_negabinary(n)) == n
    print("✓ Test 6 passed: +/- 10^9")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_to_negabinary()
