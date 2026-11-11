"""
EPI 4.1 Variant - Constant-Time Bit Tricks

Problem:
Using only bitwise operators, equality checks, and Boolean operators, write
O(1) expressions for each of the following:
1. Right-propagate the rightmost set bit of x, e.g. turn 0b01010000 into
   0b01011111 (every bit below the lowest set bit becomes 1).
2. Compute x mod a power of two, e.g. 77 mod 64 == 13.
3. Test whether x is a power of two (true for 1, 2, 4, 8, ...; false for
   everything else, including 0).

Constraints:
- 0 <= x < 2^64
- Each operation must run in O(1) time with no loops or arithmetic modulo

How it works:
1. x - 1 flips the lowest set bit and every 0 below it; OR it back into x
2. For a power of two p, the bits of p - 1 form a mask of the low bits
3. A power of two has exactly one set bit, so x & (x - 1) clears it to 0

Example 1:
Input: right_propagate_rightmost_set_bit(0b01010000)
Output: 0b01011111
Explanation: The four 0s below the lowest set bit become 1s.

Example 2:
Input: mod_power_of_two(77, 64)
Output: 13
Explanation: 77 = 64 + 13, which is the low 6 bits of 77.
"""


class Solution:
    def right_propagate_rightmost_set_bit(self, x: int) -> int:
        """
        Sets every bit below the lowest set bit of x.

        Args:
            x: Non-negative integer that fits in 64 bits

        Returns:
            x with all bits to the right of its lowest set bit turned on
            (0 is returned unchanged)

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement right propagation of the rightmost set bit
        pass

    def mod_power_of_two(self, x: int, power: int) -> int:
        """
        Computes x mod power, where power is a power of two.

        Args:
            x: Non-negative integer that fits in 64 bits
            power: A power of two (1, 2, 4, 8, ...)

        Returns:
            x mod power

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement x mod a power of two using a bit mask
        pass

    def is_power_of_two(self, x: int) -> bool:
        """
        Tests whether x is a power of two.

        Args:
            x: Non-negative integer that fits in 64 bits

        Returns:
            True if x is 1, 2, 4, 8, ...; False otherwise (including 0)

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement power-of-two check
        pass


def test_bit_tricks():
    """Test cases for the constant-time bit tricks"""
    solution = Solution()

    # Test case 1: Right-propagate example from the book
    assert solution.right_propagate_rightmost_set_bit(0b01010000) == 0b01011111
    print("✓ Test 1 passed: 0b01010000 -> 0b01011111")

    # Test case 2: Right-propagate edge cases
    assert solution.right_propagate_rightmost_set_bit(0b1) == 0b1
    assert solution.right_propagate_rightmost_set_bit(0) == 0
    assert solution.right_propagate_rightmost_set_bit(1 << 63) == (1 << 64) - 1
    print("✓ Test 2 passed: Right-propagate edge cases (1, 0, bit 63)")

    # Test case 3: Mod a power of two example from the book
    assert solution.mod_power_of_two(77, 64) == 13
    print("✓ Test 3 passed: 77 mod 64 == 13")

    # Test case 4: Mod edge cases
    assert solution.mod_power_of_two(64, 64) == 0
    assert solution.mod_power_of_two(5, 1) == 0
    assert solution.mod_power_of_two(1023, 512) == 511
    assert solution.mod_power_of_two(3, 8) == 3
    print("✓ Test 4 passed: Mod edge cases")

    # Test case 5: Powers of two
    for k in (0, 1, 2, 3, 10, 63):
        assert solution.is_power_of_two(1 << k) is True
    print("✓ Test 5 passed: 1, 2, 4, 8, 1024, 2^63 are powers of two")

    # Test case 6: Non-powers of two (including 0)
    for x in (0, 3, 6, 12, 100, (1 << 64) - 1):
        assert solution.is_power_of_two(x) is False
    print("✓ Test 6 passed: 0, 3, 6, 12, 100, 2^64 - 1 are not powers of two")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_bit_tricks()
