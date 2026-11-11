"""
EPI 4.1 Extra Variant - Hamming Distance Between Two Words
(Practice problem, not in the book. Difficulty: Easy)
Builds on: counting set bits by repeatedly dropping the lowest set bit
with x & (x - 1).

Problem:
The Hamming distance between two 64-bit words is the number of bit
positions in which they differ. Given two non-negative integers x and y
that fit in 64 bits, return their Hamming distance. Do not convert the
numbers to strings (no bin(), format(), or int.bit_count()).

Constraints:
- 0 <= x, y < 2^64
- O(k) time where k is the number of differing bits, O(1) space

How it works:
1. diff = x ^ y has a 1 exactly where x and y differ
2. Count the set bits of diff: while diff is not 0, drop its lowest set
   bit with diff &= diff - 1 and add 1 to the count
3. Return the count

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation: 0b001 and 0b100 differ in bit 0 and bit 2.

Example 2:
Input: x = 0b1011, y = 0b1001
Output: 1
Explanation: Only bit 1 differs.
"""


class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        """
        Counts the bit positions in which x and y differ.

        Args:
            x: Non-negative integer that fits in 64 bits
            y: Non-negative integer that fits in 64 bits

        Returns:
            The number of differing bit positions

        Time Complexity: O(k) where k is the number of differing bits
        Space Complexity: O(1)
        """
        # TODO: Implement Hamming distance
        pass


def test_hamming_distance():
    """Test cases for Hamming distance"""
    solution = Solution()

    # Test case 1: Identical words
    assert solution.hamming_distance(0, 0) == 0
    assert solution.hamming_distance(123456789, 123456789) == 0
    print("✓ Test 1 passed: Identical words -> 0")

    # Test case 2: Example 1
    assert solution.hamming_distance(1, 4) == 2
    print("✓ Test 2 passed: (1, 4) -> 2")

    # Test case 3: Example 2
    assert solution.hamming_distance(0b1011, 0b1001) == 1
    print("✓ Test 3 passed: (0b1011, 0b1001) -> 1")

    # Test case 4: Every bit differs
    assert solution.hamming_distance(0, (1 << 64) - 1) == 64
    print("✓ Test 4 passed: 0 vs all 64 bits set -> 64")

    # Test case 5: Alternating patterns differ everywhere
    assert solution.hamming_distance(0xAAAAAAAAAAAAAAAA, 0x5555555555555555) == 64
    print("✓ Test 5 passed: 0xAA...AA vs 0x55...55 -> 64")

    # Test case 6: Highest bit only
    assert solution.hamming_distance(1 << 63, 0) == 1
    assert solution.hamming_distance((1 << 63) | 1, 1) == 1
    print("✓ Test 6 passed: Only bit 63 differs -> 1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_hamming_distance()
