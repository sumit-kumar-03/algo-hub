"""
EPI 6.2 Extra Variant - Smallest Base of All Ones
(Practice problem, not in the book. Difficulty: Hard)
Builds on: The positional value formula sum(digit * base^i) behind base
conversion, used in reverse to search for the base.

Problem:
Given an integer n >= 3, find the smallest base k >= 2 in which n is
written using only the digit 1 (for example 13 is "111" in base 3). Such a
base always exists, because n is "11" in base n - 1. Return k.

Constraints:
- 3 <= n <= 10^18
- O(log^2 n) iterations of O(log n) arithmetic each; trying every base is
  far too slow

How it works:
1. If n is m ones in base k, then n = 1 + k + k^2 + ... + k^(m-1), so
   k^(m-1) < n and m is at most about log2(n) + 1
2. More ones means a smaller base, so try m from the largest possible
   value down to 3
3. For a fixed m the sum grows with k, so binary search k in [2, n^(1/(m-1))]
   for a sum exactly equal to n (stop summing once it passes n)
4. The first m with an exact match gives the answer; if none matches,
   the answer is n - 1 (two ones)

Example 1:
Input: n = 13
Output: 3
Explanation: 13 = 1 + 3 + 9 is "111" in base 3; it is "1101" in base 2

Example 2:
Input: n = 4681
Output: 8
Explanation: 4681 = 1 + 8 + 64 + 512 + 4096 is "11111" in base 8
"""


class Solution:
    def smallest_good_base(self, n: int) -> int:
        """
        Finds the smallest base in which n is written with only 1s.

        Args:
            n: Integer, 3 <= n <= 10^18

        Returns:
            The smallest base k >= 2 for which n is "11...1" in base k

        Time Complexity: O(log^3 n)
        Space Complexity: O(1)
        """
        # TODO: Implement smallest all-ones base search
        pass


def _digits(n: int, k: int):
    """Yields the base-k digits of n."""
    while n:
        yield n % k
        n //= k


def test_smallest_good_base():
    """Test cases for the smallest all-ones base"""
    solution = Solution()

    # Test case 1: Classic examples
    assert solution.smallest_good_base(13) == 3
    assert solution.smallest_good_base(4681) == 8
    print("✓ Test 1 passed: 13 -> 3, 4681 -> 8")

    # Test case 2: Smallest input and powers of two minus one
    assert solution.smallest_good_base(3) == 2
    assert solution.smallest_good_base(7) == 2
    assert solution.smallest_good_base(2**59 - 1) == 2
    print("✓ Test 2 passed: 2^m - 1 is all ones in base 2")

    # Test case 3: Only "11" works
    assert solution.smallest_good_base(6) == 5
    assert solution.smallest_good_base(10**18) == 10**18 - 1
    print("✓ Test 3 passed: Fallback to base n - 1")

    # Test case 4: Three ones in a larger base
    k = 10**9
    assert solution.smallest_good_base(1 + k + k * k) == k
    print("✓ Test 4 passed: 1 + k + k^2 with k = 10^9")

    # Test case 5: Several valid bases, smallest is returned
    assert solution.smallest_good_base(31) == 2  # 11111 base 2, 111 base 5
    assert solution.smallest_good_base(21) == 4
    print("✓ Test 5 passed: Smallest of several bases")

    # Test case 6: Brute-force agreement for small n
    for n in range(3, 400):
        expected = next(
            k for k in range(2, n)
            if all(d == 1 for d in _digits(n, k))
        )
        assert solution.smallest_good_base(n) == expected
    print("✓ Test 6 passed: Matches brute force for 3..399")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_smallest_good_base()
