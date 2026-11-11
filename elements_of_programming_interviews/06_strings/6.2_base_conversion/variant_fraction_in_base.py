"""
EPI 6.2 Extra Variant - Fraction in Base b
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Digit-by-digit base conversion (here applied to the fractional
part by repeated multiplication).

Problem:
Given a fraction numerator / denominator and a base b, return the value
written in base b. Use the digits 0-9 and uppercase A-F. The integer part
is written as usual. If there is a fractional part, add a '.' followed by
its digits; if the fractional digits eventually repeat forever, wrap the
repeating block in parentheses. Prefix '-' for negative values. Never
write a trailing '.', and write zero as "0".

Constraints:
- -10^9 <= numerator <= 10^9, 1 <= |denominator| <= 10^6
- 2 <= b <= 16
- O(|denominator|) time beyond writing the integer part

How it works:
1. Work with absolute values and record the sign
2. Write the integer part abs(numerator) // abs(denominator) in base b
3. For the fractional part keep the remainder r; each step multiplies r
   by b, emits r // denominator as the next digit and keeps
   r % denominator
4. Remember the output position where each remainder first appeared; when
   a remainder repeats, the digits since that position form the cycle

Example 1:
Input: numerator = 1, denominator = 6, b = 10
Output: "0.1(6)"

Example 2:
Input: numerator = 1, denominator = 10, b = 2
Output: "0.0(0011)"
Explanation: One tenth has no finite binary expansion
"""


class Solution:
    def fraction_to_base(self, numerator: int, denominator: int, b: int) -> str:
        """
        Writes numerator / denominator in base b, marking any repeating block.

        Args:
            numerator: Numerator of the fraction
            denominator: Nonzero denominator of the fraction
            b: Output base (2 to 16)

        Returns:
            The base-b expansion, e.g. "-0.1(6)"

        Time Complexity: O(log_b(|numerator|) + |denominator|)
        Space Complexity: O(|denominator|) for the remainder positions
        """
        # TODO: Implement fraction to base-b expansion
        pass


def test_fraction_to_base():
    """Test cases for fractions in base b"""
    solution = Solution()

    # Test case 1: Whole numbers and zero have no '.'
    assert solution.fraction_to_base(4, 2, 10) == "2"
    assert solution.fraction_to_base(0, 7, 10) == "0"
    assert solution.fraction_to_base(255, 1, 16) == "FF"
    print("✓ Test 1 passed: Whole numbers and zero")

    # Test case 2: Terminating expansions
    assert solution.fraction_to_base(1, 2, 10) == "0.5"
    assert solution.fraction_to_base(5, 2, 2) == "10.1"
    assert solution.fraction_to_base(255, 16, 16) == "F.F"
    print("✓ Test 2 passed: Terminating expansions")

    # Test case 3: Pure repeating expansion
    assert solution.fraction_to_base(1, 3, 10) == "0.(3)"
    assert solution.fraction_to_base(1, 7, 10) == "0.(142857)"
    print("✓ Test 3 passed: Pure repeating expansions")

    # Test case 4: Terminates in one base, repeats in another
    assert solution.fraction_to_base(1, 3, 3) == "0.1"
    assert solution.fraction_to_base(1, 10, 2) == "0.0(0011)"
    print("✓ Test 4 passed: The base decides whether it repeats")

    # Test case 5: Negative values from either sign
    assert solution.fraction_to_base(-1, 6, 10) == "-0.1(6)"
    assert solution.fraction_to_base(7, -4, 10) == "-1.75"
    assert solution.fraction_to_base(-3, -4, 10) == "0.75"
    print("✓ Test 5 passed: Signs handled")

    # Test case 6: Hex digits in a repeating block
    assert solution.fraction_to_base(1, 17, 16) == "0.(0F)"
    assert solution.fraction_to_base(22, 7, 16) == "3.(249)"
    print("✓ Test 6 passed: Hex repeating blocks")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fraction_to_base()
