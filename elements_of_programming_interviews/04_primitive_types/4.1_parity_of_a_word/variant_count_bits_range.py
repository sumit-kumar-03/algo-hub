"""
EPI 4.1 Extra Variant - Set-Bit Counts for Every Number up to n
(Practice problem, not in the book. Difficulty: Medium)
Builds on: x & (x - 1) drops the lowest set bit, so results for smaller
words can be reused (the same caching idea as the parity lookup table).

Problem:
Given a non-negative integer n, return a list counts of length n + 1
where counts[i] is the number of 1 bits in the binary form of i. Counting
each number from scratch costs O(n log n); do it in O(n) total by reusing
answers you already computed.

Constraints:
- 0 <= n <= 10^6
- O(n) time, O(1) extra space beyond the output
- Do not use bin(), format(), or int.bit_count()

How it works (reuse a smaller answer):
1. counts[0] = 0
2. For i from 1 to n: i & (i - 1) is i with its lowest set bit removed,
   which is smaller than i, so counts[i] = counts[i & (i - 1)] + 1
3. Return counts

Example 1:
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
Explanation: 0, 1, 10, 11, 100, 101 in binary.

Example 2:
Input: n = 0
Output: [0]
Explanation: Only the number 0, which has no set bits.
"""

from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        """
        Computes the number of set bits of every integer from 0 to n.

        Args:
            n: Largest number to include, n >= 0

        Returns:
            A list where entry i is the number of set bits in i

        Time Complexity: O(n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement set-bit counts for 0..n
        pass


def test_count_bits():
    """Test cases for set-bit counts over a range"""
    solution = Solution()

    # Test case 1: Only zero
    assert solution.count_bits(0) == [0]
    print("✓ Test 1 passed: n = 0 -> [0]")

    # Test case 2: Example 1
    assert solution.count_bits(5) == [0, 1, 1, 2, 1, 2]
    print("✓ Test 2 passed: n = 5 -> [0, 1, 1, 2, 1, 2]")

    # Test case 3: Up to a power of two
    assert solution.count_bits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]
    print("✓ Test 3 passed: n = 8")

    # Test case 4: Matches a direct count for every value up to 2000
    expected = [bin(i).count("1") for i in range(2001)]
    assert solution.count_bits(2000) == expected
    print("✓ Test 4 passed: n = 2000 matches a direct count")

    # Test case 5: Total over 0..2^10 - 1 is 10 * 2^9
    result = solution.count_bits(1023)
    assert len(result) == 1024 and sum(result) == 5120 and result[1023] == 10
    print("✓ Test 5 passed: n = 1023 sums to 5120")

    # Test case 6: Large n stays fast
    result = solution.count_bits(10**6)
    assert len(result) == 10**6 + 1
    assert result[10**6] == bin(10**6).count("1")
    assert result[(1 << 19) + (1 << 18) - 1] == 19
    print("✓ Test 6 passed: n = 10^6")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_bits()
