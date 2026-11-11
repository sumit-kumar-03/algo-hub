"""
EPI 4.1 - Computing the Parity of a Word

Problem:
The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0. Write a function that computes the parity of a
non-negative 64-bit integer.

Constraints:
- 0 <= x < 2^64
- Aim for better than O(n) where n is the word size (e.g. drop the lowest
  set bit with x & (x - 1), or XOR-fold the word in halves for O(log n))

How it works (x & (x - 1) approach):
1. Start with result = 0
2. While x is not 0:
   - Flip result (result ^= 1)
   - Drop the lowest set bit: x &= x - 1
3. Return result

Example 1:
Input: x = 0b1011
Output: 1
Explanation: Three bits are set, which is odd.

Example 2:
Input: x = 0b10001000
Output: 0
Explanation: Two bits are set, which is even.
"""


class Solution:
    def parity(self, x: int) -> int:
        """
        Computes the parity of a 64-bit word.

        Args:
            x: Non-negative integer that fits in 64 bits

        Returns:
            1 if the number of set bits is odd, 0 otherwise

        Time Complexity: O(k) where k is the number of set bits (O(log n) with XOR folding)
        Space Complexity: O(1)
        """
        # TODO: Implement parity
        pass


def test_parity():
    """Test cases for parity implementation"""
    solution = Solution()

    # Test case 1: Zero has no set bits
    assert solution.parity(0) == 0
    print("✓ Test 1 passed: parity(0) == 0")

    # Test case 2: Single set bit
    assert solution.parity(1) == 1
    print("✓ Test 2 passed: parity(1) == 1")

    # Test case 3: Odd number of set bits
    assert solution.parity(0b1011) == 1
    print("✓ Test 3 passed: parity(0b1011) == 1")

    # Test case 4: Even number of set bits
    assert solution.parity(0b10001000) == 0
    print("✓ Test 4 passed: parity(0b10001000) == 0")

    # Test case 5: Highest bit of a 64-bit word
    assert solution.parity(1 << 63) == 1
    print("✓ Test 5 passed: Only bit 63 set")

    # Test case 6: All 64 bits set
    assert solution.parity((1 << 64) - 1) == 0
    print("✓ Test 6 passed: All 64 bits set")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_parity()
