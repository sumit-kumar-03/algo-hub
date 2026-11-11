"""
EPI 6.2 Extra Variant - Balanced Ternary
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Repeated division by the target base, collecting remainders.

Problem:
Balanced ternary is base 3 with the digits -1, 0 and 1 instead of 0, 1 and
2. Write the digit -1 as 'T', 0 as '0' and 1 as '1'. The digit at position
i is worth 3^i times its value, and every integer (including negatives) has
exactly one representation, with no sign needed. Given an integer n, return
its balanced ternary string with no leading zeros ("0" for zero).

Constraints:
- -10^12 <= n <= 10^12
- O(log |n|) time

How it works:
1. Take the ordinary remainder r = n % 3 (0, 1 or 2)
2. Remainders 0 and 1 are valid digits: emit them and set n = (n - r) // 3
3. Remainder 2 is out of range: emit 'T' (that is, -1) and carry one into
   the next position, n = (n + 1) // 3
4. Repeat until n is 0, then reverse the collected digits

Example 1:
Input: n = 5
Output: "1TT"
Explanation: 9 - 3 - 1 = 5

Example 2:
Input: n = -5
Output: "T11"
Explanation: -9 + 3 + 1 = -5
"""


class Solution:
    def to_balanced_ternary(self, n: int) -> str:
        """
        Writes n in balanced ternary using the digits 'T', '0' and '1'.

        Args:
            n: Any integer

        Returns:
            The balanced ternary digits of n, most significant first

        Time Complexity: O(log |n|)
        Space Complexity: O(log |n|) for the output
        """
        # TODO: Implement conversion to balanced ternary
        pass


def balanced_ternary_value(digits: str) -> int:
    """Evaluates a balanced ternary string."""
    value = 0
    for d in digits:
        value = value * 3 + {"T": -1, "0": 0, "1": 1}[d]
    return value


def test_to_balanced_ternary():
    """Test cases for balanced ternary conversion"""
    solution = Solution()

    # Test case 1: Zero and one
    assert solution.to_balanced_ternary(0) == "0"
    assert solution.to_balanced_ternary(1) == "1"
    print("✓ Test 1 passed: 0 and 1")

    # Test case 2: A carry is needed for remainder 2
    assert solution.to_balanced_ternary(2) == "1T"
    assert solution.to_balanced_ternary(3) == "10"
    assert solution.to_balanced_ternary(5) == "1TT"
    assert solution.to_balanced_ternary(8) == "10T"
    print("✓ Test 2 passed: 2, 3, 5, 8")

    # Test case 3: Negatives are digit-wise mirror images
    assert solution.to_balanced_ternary(-1) == "T"
    assert solution.to_balanced_ternary(-5) == "T11"
    print("✓ Test 3 passed: -1 and -5")

    # Test case 4: Powers of three
    assert solution.to_balanced_ternary(81) == "10000"
    assert solution.to_balanced_ternary(-27) == "T000"
    print("✓ Test 4 passed: Powers of three")

    # Test case 5: Round trip over a range, no leading zeros
    for n in range(-500, 501):
        digits = solution.to_balanced_ternary(n)
        assert digits == "0" or digits[0] != "0"
        assert balanced_ternary_value(digits) == n
    print("✓ Test 5 passed: Round trip for -500..500")

    # Test case 6: Extremes
    for n in (10**12, -(10**12)):
        assert balanced_ternary_value(solution.to_balanced_ternary(n)) == n
    print("✓ Test 6 passed: +/- 10^12")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_to_balanced_ternary()
