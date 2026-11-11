"""
EPI 4.1 Extra Variant - Find the Two Numbers That Appear Once
(Practice problem, not in the book. Difficulty: Medium)
Builds on: XOR-folding a group of words (as in the parity XOR approach)
and isolating the lowest set bit with x & ~(x - 1).

Problem:
You are given a list of integers in which exactly two distinct values
appear once and every other value appears exactly twice. Return the two
values that appear once, smaller one first.

Constraints:
- 2 <= len(A) <= 10^5, and len(A) is even
- Values may be negative
- O(n) time and O(1) extra space (no hash sets or sorting)

How it works:
1. XOR all entries: pairs cancel, leaving x = a ^ b where a and b are the
   two singles. Since a != b, x is not 0
2. Isolate one bit where a and b differ: low = x & -x (its lowest set bit)
3. XOR together only the entries that have this bit set: pairs still
   cancel, so the result is whichever of a and b has the bit. Call it a
4. b = x ^ a. Return them in ascending order

Example 1:
Input: A = [1, 2, 1, 3, 2, 5]
Output: [3, 5]
Explanation: 1 and 2 appear twice; 3 and 5 appear once.

Example 2:
Input: A = [-1, 0]
Output: [-1, 0]
Explanation: Both values appear once.
"""

from typing import List


class Solution:
    def two_single_numbers(self, A: List[int]) -> List[int]:
        """
        Finds the two values that appear exactly once.

        Args:
            A: Integers where two distinct values appear once and every
               other value appears exactly twice

        Returns:
            The two single values in ascending order

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement XOR split to find the two singles
        pass


def test_two_single_numbers():
    """Test cases for finding the two single numbers"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.two_single_numbers([1, 2, 1, 3, 2, 5]) == [3, 5]
    print("✓ Test 1 passed: [1, 2, 1, 3, 2, 5] -> [3, 5]")

    # Test case 2: Only the two singles
    assert solution.two_single_numbers([-1, 0]) == [-1, 0]
    assert solution.two_single_numbers([7, 4]) == [4, 7]
    print("✓ Test 2 passed: Two-element inputs")

    # Test case 3: Negative values
    assert solution.two_single_numbers([-5, 8, -5, -9, 8, 2]) == [-9, 2]
    print("✓ Test 3 passed: Negatives -> [-9, 2]")

    # Test case 4: Singles differ only in a high bit
    # Pairs: 3, 6, 1 << 40; singles: (1 << 40) | 6 and 0
    A = [1 << 40, 3, 3, (1 << 40) | 6, 6, 6, 1 << 40, 0]
    assert solution.two_single_numbers(A) == [0, (1 << 40) | 6]
    print("✓ Test 4 passed: Singles 0 and 2^40 + 6")

    # Test case 5: Singles that share most of their bits
    assert solution.two_single_numbers([12, 13, 100, 100, 99, 99]) == [12, 13]
    print("✓ Test 5 passed: [.., 12, 13, ..] -> [12, 13]")

    # Test case 6: Large input
    A = []
    for v in range(-50000, 50000, 2):
        A.append(v)
    A = A + A[::-1] + [123457, -77777]
    assert solution.two_single_numbers(A) == [-77777, 123457]
    print("✓ Test 6 passed: 100,002 entries")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_two_single_numbers()
