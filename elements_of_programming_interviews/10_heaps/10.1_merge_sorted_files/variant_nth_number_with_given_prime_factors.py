"""
EPI 10.1 Extra Variant - nth Number Built from Given Primes
(Practice problem, not in the book. Difficulty: Medium)
Builds on: merging several sorted sequences with a min-heap, where the
sequences are generated on the fly from the output itself.

Problem:
Given a list of distinct primes and an integer n, consider the increasing
sequence of positive integers whose prime factors all belong to the list.
The number 1 (no prime factors) is the first member. Return the nth member.

Constraints:
- 1 <= len(primes) <= 100, primes are distinct and given in ascending order
- 1 <= n <= 10^5
- O(n log p) time and O(n + p) space, where p = len(primes)
- The same number can be produced in several ways (2 * 3 = 3 * 2); it must
  be counted once

How it works (merge p sorted streams that feed on the output):
1. Keep the output list seq = [1]; for each prime q there is a stream
   q * seq[0], q * seq[1], ... which is sorted because seq is sorted
2. A min-heap holds the next value of every stream as
   (value, prime index, position in seq)
3. Repeatedly pop the smallest value; append it to seq if it differs from
   the last appended value; advance that stream's position and push its next
   value
4. Stop when seq has n numbers

Example 1:
Input: primes = [2, 3, 5], n = 10
Output: 12
Explanation: The sequence starts 1, 2, 3, 4, 5, 6, 8, 9, 10, 12.

Example 2:
Input: primes = [2, 7, 13, 19], n = 12
Output: 32
Explanation: 1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32.
"""

from typing import List


class Solution:
    def nth_number(self, primes: List[int], n: int) -> int:
        """
        Returns the nth positive integer whose prime factors are all in primes.

        Args:
            primes: Distinct primes in ascending order
            n: 1-based position in the sequence

        Returns:
            The nth member of the sequence

        Time Complexity: O(n log p)
        Space Complexity: O(n + p)
        """
        # TODO: Implement with a min-heap of p streams
        pass


def test_nth_number():
    """Test cases for numbers built from given primes"""
    solution = Solution()

    # Test case 1: n = 1 is always 1
    assert solution.nth_number([2, 3, 5], 1) == 1
    assert solution.nth_number([7], 1) == 1
    print("✓ Test 1 passed: First member is 1")

    # Test case 2: Primes 2, 3, 5
    expected2 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16]
    assert [solution.nth_number([2, 3, 5], n) for n in range(1, 13)] == expected2
    print("✓ Test 2 passed: First 12 members for [2, 3, 5]")

    # Test case 3: Four primes
    assert solution.nth_number([2, 7, 13, 19], 12) == 32
    print("✓ Test 3 passed: [2, 7, 13, 19], n = 12 -> 32")

    # Test case 4: Single prime gives powers of it
    assert solution.nth_number([3], 6) == 243
    print("✓ Test 4 passed: Powers of 3")

    # Test case 5: Many duplicates generated (2*3*5 in six orders)
    assert solution.nth_number([2, 3, 5], 1500) == 859963392
    print("✓ Test 5 passed: n = 1500 for [2, 3, 5]")

    # Test case 6: Larger primes and a large n
    assert solution.nth_number([2, 3, 5, 7], 5000) == 797343750
    print("✓ Test 6 passed: n = 5000 for [2, 3, 5, 7]")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_nth_number()
