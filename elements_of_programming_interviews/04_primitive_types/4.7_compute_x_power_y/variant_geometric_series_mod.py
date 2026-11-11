"""
EPI 4.7 Extra Variant - Geometric Series Modulo m
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the halving recursion behind repeated squaring
(x^(2k) = (x^k)^2), applied to a sum of powers.

Problem:
Given integers x, n and m, return (1 + x + x^2 + ... + x^(n - 1)) mod m,
the sum of the first n powers of x. The usual closed form
(x^n - 1) / (x - 1) needs a division, which does not work modulo an
arbitrary m (m need not be prime, and x - 1 may share factors with m).
Use only additions and multiplications, in O(log n) steps.

Constraints:
- x >= 0; 0 <= n <= 10^18; 1 <= m <= 10^18
- An empty sum (n == 0) is 0
- O(log n) time
- Do not use the built-in pow() or the ** operator, and do not divide by
  x - 1

How it works (halve the number of terms):
Let S(n) = 1 + x + ... + x^(n - 1) and P(n) = x^n, both mod m.
1. S(0) = 0, P(0) = 1 % m
2. If n is even, the second half of the terms is the first half times
   x^(n/2): S(n) = S(n/2) * (1 + P(n/2)) and P(n) = P(n/2)^2
3. If n is odd, peel off the last term: S(n) = S(n - 1) + P(n - 1) and
   P(n) = P(n - 1) * x
4. Reduce mod m at every step and return S(n)

Example 1:
Input: x = 2, n = 4, m = 100
Output: 15
Explanation: 1 + 2 + 4 + 8 = 15.

Example 2:
Input: x = 3, n = 5, m = 7
Output: 2
Explanation: 1 + 3 + 9 + 27 + 81 = 121, and 121 mod 7 = 2.
"""


class Solution:
    def geometric_sum(self, x: int, n: int, m: int) -> int:
        """
        Computes 1 + x + ... + x^(n - 1) modulo m without division.

        Args:
            x: Non-negative ratio of the series
            n: Number of terms, n >= 0
            m: Positive modulus (not necessarily prime)

        Returns:
            The sum of the first n powers of x, mod m

        Time Complexity: O(log n)
        Space Complexity: O(log n) recursive, O(1) iterative
        """
        # TODO: Implement the geometric sum with halving
        pass


def test_geometric_sum():
    """Test cases for the modular geometric series"""
    solution = Solution()

    # Test case 1: Examples
    assert solution.geometric_sum(2, 4, 100) == 15
    assert solution.geometric_sum(3, 5, 7) == 2
    print("✓ Test 1 passed: Examples")

    # Test case 2: Empty sum and modulus 1
    assert solution.geometric_sum(5, 0, 13) == 0
    assert solution.geometric_sum(5, 10, 1) == 0
    print("✓ Test 2 passed: n = 0 and m = 1")

    # Test case 3: Ratios 0 and 1 (where the closed form breaks)
    assert solution.geometric_sum(0, 1, 10) == 1
    assert solution.geometric_sum(0, 10**18, 10) == 1
    assert solution.geometric_sum(1, 10**18, 10**9 + 7) == 10**18 % (10**9 + 7)
    print("✓ Test 3 passed: x = 0 and x = 1")

    # Test case 4: Matches brute force on small inputs
    for x in range(0, 8):
        for n in range(0, 25):
            for m in (1, 2, 6, 9, 10, 12, 97):
                assert solution.geometric_sum(x, n, m) == sum(x**i for i in range(n)) % m
    print("✓ Test 4 passed: Matches brute force for small x, n, m")

    # Test case 5: Modulus shares a factor with x - 1
    m = 10**9
    n = 10**12
    expected = (pow(3, n, 2 * m) - 1) // 2 % m  # (3^n - 1) / 2, computed exactly mod m
    assert solution.geometric_sum(3, n, m) == expected
    print("✓ Test 5 passed: x = 3, n = 10^12, m = 10^9")

    # Test case 6: Large modulus, sum fits exactly
    assert solution.geometric_sum(2, 60, 10**18) == ((1 << 60) - 1) % 10**18
    assert solution.geometric_sum(10, 18, 10**18) == 111111111111111111
    print("✓ Test 6 passed: Large modulus")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_geometric_sum()
