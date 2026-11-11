"""
EPI 11.4 Extra Variant - Integer kth Root
(Practice problem, not in the book. Difficulty: Medium)
Builds on: binary search for the largest candidate whose power does not
exceed the target, generalized from squares to any exponent.

Problem:
Given a nonnegative integer n and an integer k >= 1, return the largest
integer r such that r^k <= n (that is, floor of the kth root of n).

Constraints:
- 0 <= n <= 10^30; 1 <= k <= 100
- O(k * log n) multiplications; do not use floating point, ** with a
  fractional exponent, or math functions
- Computing mid^k for a large mid can create huge numbers; stop
  multiplying as soon as the partial product exceeds n

How it works:
1. Search r in [0, n] (or a tighter upper bound such as
   2^(bit_length(n) // k + 1))
2. power_at_most(mid, k, n): multiply mid by itself k times, returning False
   as soon as the product exceeds n
3. Keep the largest mid for which power_at_most is True

Example 1:
Input: n = 1000, k = 3
Output: 10

Example 2:
Input: n = 80, k = 4
Output: 2
Explanation: 2^4 = 16 <= 80 and 3^4 = 81 > 80.
"""


class Solution:
    def kth_root(self, n: int, k: int) -> int:
        """
        Computes floor(n ** (1 / k)) exactly for integers.

        Args:
            n: Nonnegative integer
            k: Root degree (k >= 1)

        Returns:
            Largest integer r with r ** k <= n

        Time Complexity: O(k log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search with an early-exit power check
        pass


def test_kth_root():
    """Test cases for the integer kth root"""
    solution = Solution()

    # Test case 1: Perfect cube
    assert solution.kth_root(1000, 3) == 10
    print("✓ Test 1 passed: cbrt(1000) = 10")

    # Test case 2: Just below a perfect power
    assert solution.kth_root(80, 4) == 2
    assert solution.kth_root(81, 4) == 3
    print("✓ Test 2 passed: 80 and 81 with k = 4")

    # Test case 3: k = 1 returns n itself, k = 2 is the square root
    assert solution.kth_root(12345, 1) == 12345
    assert solution.kth_root(300, 2) == 17
    print("✓ Test 3 passed: k = 1 and k = 2")

    # Test case 4: n = 0 and n = 1, any k
    assert solution.kth_root(0, 5) == 0
    assert solution.kth_root(1, 50) == 1
    print("✓ Test 4 passed: n = 0 and n = 1")

    # Test case 5: Large k makes the root small
    assert solution.kth_root(2 ** 100, 100) == 2
    assert solution.kth_root(2 ** 100 - 1, 100) == 1
    assert solution.kth_root(10 ** 30, 97) == 2
    print("✓ Test 5 passed: Large k")

    # Test case 6: Huge n where floats lose precision
    r = 10 ** 10 - 7
    assert solution.kth_root(r ** 3, 3) == r
    assert solution.kth_root(r ** 3 - 1, 3) == r - 1
    assert solution.kth_root(10 ** 30, 2) == 10 ** 15
    print("✓ Test 6 passed: n near 10^30")

    # Test case 7: Small values exhaustively
    for k in range(1, 6):
        for n in range(300):
            r = 0
            while (r + 1) ** k <= n:
                r += 1
            assert solution.kth_root(n, k) == r
    print("✓ Test 7 passed: n = 0..299, k = 1..5")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_root()
