"""
EPI 11.4 Extra Variant - Complete Rows of a Coin Staircase
(Practice problem, not in the book. Difficulty: Medium)
Builds on: binary search for the largest integer whose image under a
monotone function is at most a target (11.4 uses r -> r * r).

Problem:
You have n coins and build a staircase: row 1 holds 1 coin, row 2 holds 2
coins, row i holds i coins, filling rows in order until you run out. The
last row may be incomplete. Return the number of complete rows.

Constraints:
- 0 <= n <= 10^18
- O(log n) time, O(1) space
- Do not use floating point (the closed-form formula with a square root is
  inexact for large n)

How it works (binary search on the row count):
1. r complete rows need r * (r + 1) // 2 coins, which grows with r
2. Search r in [0, n] for the largest value with r * (r + 1) // 2 <= n
3. Same loop shape as the integer square root: if mid works, move left up,
   otherwise move right down

Example 1:
Input: n = 8
Output: 3
Explanation: Rows of 1, 2, 3 use 6 coins; row 4 would need 4 more but only
2 are left.

Example 2:
Input: n = 10
Output: 4
Explanation: 1 + 2 + 3 + 4 = 10 exactly.
"""


class Solution:
    def complete_rows(self, n: int) -> int:
        """
        Returns the number of complete staircase rows built from n coins.

        Args:
            n: Number of coins (n >= 0)

        Returns:
            Largest r with r * (r + 1) / 2 <= n

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement with binary search
        pass


def test_complete_rows():
    """Test cases for coin staircase rows"""
    solution = Solution()

    # Test case 1: Incomplete last row
    assert solution.complete_rows(8) == 3
    print("✓ Test 1 passed: 8 coins -> 3 rows")

    # Test case 2: Exact triangular number
    assert solution.complete_rows(10) == 4
    print("✓ Test 2 passed: 10 coins -> 4 rows")

    # Test case 3: Zero, one, and two coins
    assert solution.complete_rows(0) == 0
    assert solution.complete_rows(1) == 1
    assert solution.complete_rows(2) == 1
    print("✓ Test 3 passed: 0, 1, 2 coins")

    # Test case 4: Small values exhaustively
    expected = []
    for n in range(200):
        r = 0
        while (r + 1) * (r + 2) // 2 <= n:
            r += 1
        expected.append(r)
    assert [solution.complete_rows(n) for n in range(200)] == expected
    print("✓ Test 4 passed: n = 0..199")

    # Test case 5: One coin short of the next row
    r = 10 ** 6
    t = r * (r + 1) // 2
    assert solution.complete_rows(t) == r
    assert solution.complete_rows(t - 1) == r - 1
    print("✓ Test 5 passed: Around a triangular number")

    # Test case 6: Very large n (floats would be off)
    r = 1414213562
    t = r * (r + 1) // 2
    assert solution.complete_rows(t + r) == r
    assert solution.complete_rows(t + r + 1) == r + 1
    assert solution.complete_rows(10 ** 18) == 1414213561
    print("✓ Test 6 passed: n near 10^18")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_complete_rows()
