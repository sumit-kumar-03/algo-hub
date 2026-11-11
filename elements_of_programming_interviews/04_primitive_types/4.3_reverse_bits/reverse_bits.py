"""
EPI 4.3 - Reverse Bits

Problem:
Given a 64-bit unsigned integer, return the 64-bit unsigned integer whose
bits are those of the input in reverse order: bit i of the input becomes
bit 63 - i of the output.

Constraints:
- 0 <= x < 2^64
- For repeated calls, aim for O(n / L) per call using a precomputed lookup
  table of reversed L-bit chunks (e.g. L = 16), where n = 64

How it works (lookup table approach):
1. Precompute rev[y] = bit-reversal of y for every 16-bit value y
2. Split x into four 16-bit chunks y3 y2 y1 y0 (y3 most significant)
3. The result is rev[y0] rev[y1] rev[y2] rev[y3], with rev[y0] placed in
   the most significant 16 bits

Example 1:
Input: x = 0b1110000000000001 (a 16-bit pattern in the low bits)
Output: 0b1000000000000111 << 48
Explanation: The low 16 bits, reversed, land in the high 16 bits of the
64-bit result.

Example 2:
Input: x = 1
Output: 1 << 63
Explanation: Bit 0 moves to bit 63.
"""


class Solution:
    def reverse_bits(self, x: int) -> int:
        """
        Reverses the bits of a 64-bit unsigned integer.

        Args:
            x: Non-negative integer that fits in 64 bits

        Returns:
            The 64-bit integer whose bits are those of x in reverse order

        Time Complexity: O(n / L) with an L-bit lookup table (O(n) bit by bit)
        Space Complexity: O(2^L) for the lookup table
        """
        # TODO: Implement bit reversal
        pass


def test_reverse_bits():
    """Test cases for reverse bits implementation"""
    solution = Solution()

    # Test case 1: Zero stays zero
    assert solution.reverse_bits(0) == 0
    print("✓ Test 1 passed: reverse_bits(0) == 0")

    # Test case 2: Lowest bit moves to the highest bit
    assert solution.reverse_bits(1) == 1 << 63
    print("✓ Test 2 passed: Bit 0 -> bit 63")

    # Test case 3: Highest bit moves to the lowest bit
    assert solution.reverse_bits(1 << 63) == 1
    print("✓ Test 3 passed: Bit 63 -> bit 0")

    # Test case 4: Book example in the low 16 bits
    assert solution.reverse_bits(0b1110000000000001) == 0b1000000000000111 << 48
    print("✓ Test 4 passed: 0b1110000000000001 reversed into the high bits")

    # Test case 5: All 64 bits set
    assert solution.reverse_bits((1 << 64) - 1) == (1 << 64) - 1
    print("✓ Test 5 passed: All ones is its own reverse")

    # Test case 6: Mixed pattern across chunk boundaries
    x = 0x0123456789ABCDEF
    assert solution.reverse_bits(x) == 0xF7B3D591E6A2C480
    print("✓ Test 6 passed: 0x0123456789ABCDEF -> 0xF7B3D591E6A2C480")

    # Test case 7: Reversing twice gives back the input
    y = 0xDEADBEEF00C0FFEE
    assert solution.reverse_bits(solution.reverse_bits(y)) == y
    print("✓ Test 7 passed: Reversal is its own inverse")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_bits()
