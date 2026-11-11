"""
EPI 5.2 Variant - Add Two Binary Strings

Problem:
Given two strings s and t made of '0' and '1' characters, each encoding a
non-negative binary number, return a new bit string that encodes their
sum. Do not convert the strings to built-in integers.

Constraints:
- 1 <= len(s), len(t) <= 10^5
- Inputs have no leading zeros unless the number is "0"
- The result must have no leading zeros unless it is "0"
- Must run in O(max(len(s), len(t))) time

How it works (add from the right with a carry):
1. Point i and j at the last characters of s and t; carry = 0
2. While i >= 0 or j >= 0 or carry:
   - total = carry + bit at i (if any) + bit at j (if any)
   - Record total % 2 as the next result bit; carry = total // 2
   - Move i and j one position left
3. Reverse the collected bits and join them into a string

Example 1:
Input: s = "1011", t = "110"
Output: "10001"
Explanation: 11 + 6 = 17.

Example 2:
Input: s = "0", t = "0"
Output: "0"
Explanation: 0 + 0 = 0.
"""


class Solution:
    def add_binary(self, s: str, t: str) -> str:
        """
        Adds two binary numbers given as bit strings.

        Args:
            s: Bit string of the first number
            t: Bit string of the second number

        Returns:
            Bit string of s + t without leading zeros

        Time Complexity: O(max(m, n))
        Space Complexity: O(max(m, n)) for the result
        """
        # TODO: Implement binary string addition
        pass


def test_add_binary():
    """Test cases for binary string addition"""
    solution = Solution()

    # Test case 1: Different lengths with carries
    assert solution.add_binary("1011", "110") == "10001"
    print("✓ Test 1 passed: 1011 + 110 == 10001")

    # Test case 2: Zeros
    assert solution.add_binary("0", "0") == "0"
    print("✓ Test 2 passed: 0 + 0 == 0")

    # Test case 3: Adding zero
    assert solution.add_binary("101", "0") == "101"
    assert solution.add_binary("0", "101") == "101"
    print("✓ Test 3 passed: Adding 0 on either side")

    # Test case 4: Carry ripples to a new leading bit
    assert solution.add_binary("1111", "1") == "10000"
    print("✓ Test 4 passed: 1111 + 1 == 10000")

    # Test case 5: No carries
    assert solution.add_binary("1010", "101") == "1111"
    print("✓ Test 5 passed: 1010 + 101 == 1111")

    # Test case 6: Long inputs
    assert solution.add_binary("1" * 100, "1") == "1" + "0" * 100
    print("✓ Test 6 passed: (2^100 - 1) + 1 == 2^100")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_add_binary()
