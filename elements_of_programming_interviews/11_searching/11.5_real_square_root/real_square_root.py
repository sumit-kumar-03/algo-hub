"""
EPI 11.5 - Compute the Real Square Root

Problem:
Given a nonnegative floating-point number x, return its square root (to
floating-point tolerance) without calling a library square root.

Constraints:
- 0 <= x <= 10^100
- Do not use math.sqrt, ** 0.5, or pow
- O(log(x / tolerance)) iterations

How it works (binary search on reals):
1. Pick a bracket that surely contains the answer:
   - x < 1: [x, 1] (the root of a number below 1 is bigger than it)
   - x >= 1: [1, x]
2. Repeat until the bracket endpoints are close (math.isclose):
   - mid = (left + right) / 2
   - mid * mid > x: right = mid, else left = mid
3. Return left
(Watch out for x = 0, where a purely relative stopping test never ends.)

Example 1:
Input: x = 2.0
Output: 1.41421356...

Example 2:
Input: x = 0.25
Output: 0.5
Explanation: The root is larger than x, so [0, x] would not contain it.
"""

import math


class Solution:
    def square_root(self, x: float) -> float:
        """
        Computes the square root of a nonnegative float.

        Args:
            x: Nonnegative number

        Returns:
            sqrt(x) to within floating-point tolerance

        Time Complexity: O(log(x / tolerance))
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on a bracket around the root
        pass


def _ok(got: float, x: float) -> bool:
    return got is not None and math.isclose(got, math.sqrt(x), rel_tol=1e-7, abs_tol=1e-9)


def test_square_root():
    """Test cases for the real square root"""
    solution = Solution()

    # Test case 1: Irrational root
    assert _ok(solution.square_root(2.0), 2.0)
    print("✓ Test 1 passed: sqrt(2)")

    # Test case 2: Input below 1
    assert _ok(solution.square_root(0.25), 0.25)
    print("✓ Test 2 passed: sqrt(0.25) = 0.5")

    # Test case 3: Perfect square
    assert _ok(solution.square_root(144.0), 144.0)
    print("✓ Test 3 passed: sqrt(144) = 12")

    # Test case 4: Exactly 1 and 0
    assert _ok(solution.square_root(1.0), 1.0)
    assert _ok(solution.square_root(0.0), 0.0)
    print("✓ Test 4 passed: sqrt(1) and sqrt(0)")

    # Test case 5: Very small input
    assert _ok(solution.square_root(1e-6), 1e-6)
    print("✓ Test 5 passed: sqrt(1e-6)")

    # Test case 6: Very large input
    assert _ok(solution.square_root(1e30), 1e30)
    print("✓ Test 6 passed: sqrt(1e30)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_square_root()
