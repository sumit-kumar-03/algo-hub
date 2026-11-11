"""
EPI 11.4 Extra Variant - Valid Perfect Square
(Practice problem, not in the book. Difficulty: Easy)
Builds on: binary search over candidate roots, comparing mid * mid with the
target instead of calling a square-root function.

Problem:
Given an integer n, return True if n is the square of some integer and
False otherwise. Negative numbers are never perfect squares; 0 and 1 are.

Constraints:
- -10^18 <= n <= 10^18
- O(log n) time, O(1) space
- Do not use math.sqrt, math.isqrt, ** 0.5, or floating-point arithmetic
  (floats lose precision for large n)

How it works (search for an exact root):
1. Reject negative n
2. Binary search r in [0, n]: if r * r == n, return True; if r * r < n,
   search right; otherwise search left
3. If the interval empties without a hit, return False

Example 1:
Input: n = 144
Output: True

Example 2:
Input: n = 145
Output: False
"""


class Solution:
    def is_perfect_square(self, n: int) -> bool:
        """
        Checks whether n is the square of an integer.

        Args:
            n: Any integer

        Returns:
            True if n == r * r for some integer r

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement with binary search
        pass


def test_is_perfect_square():
    """Test cases for perfect square check"""
    solution = Solution()

    # Test case 1: Perfect square
    assert solution.is_perfect_square(144) is True
    print("✓ Test 1 passed: 144 is a perfect square")

    # Test case 2: Not a perfect square
    assert solution.is_perfect_square(145) is False
    assert solution.is_perfect_square(2) is False
    print("✓ Test 2 passed: 145 and 2 are not")

    # Test case 3: 0 and 1
    assert solution.is_perfect_square(0) is True
    assert solution.is_perfect_square(1) is True
    print("✓ Test 3 passed: 0 and 1")

    # Test case 4: Negative numbers
    assert solution.is_perfect_square(-4) is False
    assert solution.is_perfect_square(-1) is False
    print("✓ Test 4 passed: Negatives")

    # Test case 5: Small range checked exhaustively
    squares = {r * r for r in range(40)}
    assert all(solution.is_perfect_square(n) is (n in squares) for n in range(1500))
    print("✓ Test 5 passed: n = 0..1499")

    # Test case 6: Large values where floats would fail
    r = 999999999
    assert solution.is_perfect_square(r * r) is True
    assert solution.is_perfect_square(r * r + 1) is False
    assert solution.is_perfect_square(r * r - 1) is False
    assert solution.is_perfect_square(10 ** 18) is True
    print("✓ Test 6 passed: Values near 10^18")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_perfect_square()
