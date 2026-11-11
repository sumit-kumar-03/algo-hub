"""
EPI 4.1 Extra Variant - Next Larger Number with the Same Number of Set Bits
(Practice problem, not in the book. Difficulty: Hard)
Builds on: isolating the lowest set bit (x & -x) and reasoning about how
adding it ripples through a block of 1s.

Problem:
Given a positive integer x, return the smallest integer y > x that has
exactly as many 1 bits as x. For example, after 0b0111 comes 0b1011. Use
a constant number of arithmetic and bitwise operations, with no loop over
the bits and no search over candidate numbers.

Constraints:
- 1 <= x < 2^64 (the answer may need one bit more than x)
- O(1) operations, O(1) space
- Do not use bin(), format(), or int.bit_count()

How it works:
1. low = x & -x isolates the lowest set bit
2. ripple = x + low turns the lowest block of 1s into 0s and carries a 1
   into the next higher position
3. ones = ripple ^ x marks the bits that changed (the block plus the
   carry bit). Shift it right so that only (block size - 1) 1s remain at
   the bottom: ones = (ones >> 2) // low
4. Return ripple | ones

Example 1:
Input: x = 0b0110 (6)
Output: 0b1001 (9)
Explanation: 7 has three bits and 8 has one; 9 is the first with two.

Example 2:
Input: x = 0b1111 (15)
Output: 0b10111 (23)
Explanation: The four 1s move up: the top one shifts left, the rest drop
back to the lowest positions.
"""


class Solution:
    def next_same_popcount(self, x: int) -> int:
        """
        Finds the smallest larger integer with the same number of set bits.

        Args:
            x: Positive integer that fits in 64 bits

        Returns:
            The smallest y > x with the same number of 1 bits as x

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement next number with the same popcount
        pass


def test_next_same_popcount():
    """Test cases for next number with the same popcount"""
    solution = Solution()

    # Test case 1: A single set bit moves up one place
    assert solution.next_same_popcount(1) == 2
    assert solution.next_same_popcount(8) == 16
    print("✓ Test 1 passed: 1 -> 2, 8 -> 16")

    # Test case 2: Examples
    assert solution.next_same_popcount(0b0110) == 0b1001
    assert solution.next_same_popcount(0b1111) == 0b10111
    print("✓ Test 2 passed: 6 -> 9, 15 -> 23")

    # Test case 3: Low block of 1s with higher bits set
    assert solution.next_same_popcount(0b0111) == 0b1011
    assert solution.next_same_popcount(0b10011100) == 0b10100011
    print("✓ Test 3 passed: 0b0111 -> 0b1011, 0b10011100 -> 0b10100011")

    # Test case 4: Matches a brute-force search for all small x
    for x in range(1, 3000):
        y = x + 1
        while bin(y).count("1") != bin(x).count("1"):
            y += 1
        assert solution.next_same_popcount(x) == y
    print("✓ Test 4 passed: Matches brute force for 1..2999")

    # Test case 5: Top bit of a 64-bit word
    assert solution.next_same_popcount(1 << 63) == 1 << 64
    assert solution.next_same_popcount((1 << 64) - 1) == (1 << 64) | ((1 << 63) - 1)
    print("✓ Test 5 passed: Answers that need a 65th bit")

    # Test case 6: Large word with scattered bits
    x = 0b1011 << 50 | 0b110
    assert solution.next_same_popcount(x) == (0b1011 << 50) | 0b1001
    print("✓ Test 6 passed: Large word with scattered bits")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_next_same_popcount()
