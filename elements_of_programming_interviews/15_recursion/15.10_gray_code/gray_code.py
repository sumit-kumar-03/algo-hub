"""
EPI 15.10 - Compute a Gray Code

Problem:
An n-bit Gray code is an ordering of all integers 0 .. 2^n - 1 in which
the binary forms of any two neighbors differ in exactly one bit, including
the wraparound pair (last and first). Given n, return any n-bit Gray code.

Constraints:
- 0 <= n <= 16
- The result has exactly 2^n entries, all distinct
- Target: O(2^n) time

How it works (reflect and prefix):
1. The 0-bit Gray code is [0]
2. Given an (n-1)-bit code G, the n-bit code is G followed by G in reverse
   order with bit n-1 set on every reversed entry
3. Inside each half neighbors still differ in one bit; at the seam the two
   entries are equal except for bit n-1; and the wraparound pair (first of
   G, first of G with bit n-1 set) also differs only in bit n-1
Alternative: entry i is i ^ (i >> 1).

Example 1:
Input: n = 2
Output: [0, 1, 3, 2]
Explanation: 00, 01, 11, 10; each step (and 10 -> 00) flips one bit.

Example 2:
Input: n = 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
Explanation: [0, 4, 5, 7, 6, 2, 3, 1] is also a valid 3-bit Gray code.
"""

from typing import List


class Solution:
    def gray_code(self, num_bits: int) -> List[int]:
        """
        Returns an n-bit Gray code.

        Args:
            num_bits: Number of bits n

        Returns:
            A list of all 2^n integers where cyclic neighbors differ in one bit

        Time Complexity: O(2^n)
        Space Complexity: O(2^n) for the output
        """
        # TODO: Implement Gray code generation
        pass


def is_gray_code(num_bits: int, code: List[int]) -> bool:
    """Checks length, distinctness, range, and the one-bit (cyclic) property."""
    size = 1 << num_bits
    if len(code) != size or set(code) != set(range(size)):
        return False
    if size == 1:
        return True
    for i in range(size):
        diff = code[i] ^ code[(i + 1) % size]
        if diff == 0 or diff & (diff - 1):
            return False
    return True


def test_gray_code():
    """Test cases for Gray code generation"""
    solution = Solution()

    # Test case 1: Zero bits
    assert solution.gray_code(0) == [0]
    print("✓ Test 1 passed: n=0 -> [0]")

    # Test case 2: One bit
    assert sorted(solution.gray_code(1)) == [0, 1]
    print("✓ Test 2 passed: n=1 -> [0, 1] in some order")

    # Test case 3: Two bits
    result3 = solution.gray_code(2)
    assert is_gray_code(2, result3)
    print(f"✓ Test 3 passed: n=2 -> {result3}")

    # Test case 4: Three bits
    result4 = solution.gray_code(3)
    assert is_gray_code(3, result4)
    print(f"✓ Test 4 passed: n=3 -> {result4}")

    # Test case 5: Four through twelve bits
    for n in range(4, 13):
        assert is_gray_code(n, solution.gray_code(n))
    print("✓ Test 5 passed: n=4..12 are valid Gray codes")

    # Test case 6: Sixteen bits (65536 entries)
    assert is_gray_code(16, solution.gray_code(16))
    print("✓ Test 6 passed: n=16 is a valid Gray code")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_gray_code()
