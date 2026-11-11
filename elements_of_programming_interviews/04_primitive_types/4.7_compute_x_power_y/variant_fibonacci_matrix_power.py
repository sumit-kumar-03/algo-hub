"""
EPI 4.7 Extra Variant - nth Fibonacci Number by Matrix Powers
(Practice problem, not in the book. Difficulty: Medium)
Builds on: repeated squaring, applied to 2 x 2 matrices instead of
numbers.

Problem:
The Fibonacci numbers are F(0) = 0, F(1) = 1, and F(n) = F(n - 1) +
F(n - 2). Given n (up to 10^18), return F(n) mod 1,000,000,007. A loop
of n additions is far too slow; reach the answer in O(log n) steps.

Constraints:
- 0 <= n <= 10^18
- O(log n) time, O(1) space
- Do not use the built-in pow() or the ** operator

How it works:
1. The step (F(k + 1), F(k)) -> (F(k + 2), F(k + 1)) is a multiplication
   by Q = [[1, 1], [1, 0]], so Q^n = [[F(n + 1), F(n)], [F(n), F(n - 1)]]
2. Compute Q^n with repeated squaring: start from the identity matrix and,
   for each bit of n, square the running power and multiply it into the
   result when the bit is 1. Reduce every entry mod 10^9 + 7
3. Return the top-right entry of Q^n

Example 1:
Input: n = 10
Output: 55
Explanation: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.

Example 2:
Input: n = 0
Output: 0
Explanation: Q^0 is the identity matrix, whose top-right entry is 0.
"""


class Solution:
    def fibonacci(self, n: int) -> int:
        """
        Computes the nth Fibonacci number mod 10^9 + 7.

        Args:
            n: Index of the Fibonacci number, n >= 0

        Returns:
            F(n) mod 1,000,000,007

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement Fibonacci with 2 x 2 matrix repeated squaring
        pass


def test_fibonacci():
    """Test cases for matrix-power Fibonacci"""
    solution = Solution()
    MOD = 10**9 + 7

    # Test case 1: Base cases
    assert solution.fibonacci(0) == 0
    assert solution.fibonacci(1) == 1
    assert solution.fibonacci(2) == 1
    print("✓ Test 1 passed: F(0), F(1), F(2)")

    # Test case 2: Example 1
    assert solution.fibonacci(10) == 55
    print("✓ Test 2 passed: F(10) == 55")

    # Test case 3: First 300 values match a simple loop
    a, b = 0, 1
    for i in range(300):
        assert solution.fibonacci(i) == a % MOD
        a, b = b, a + b
    print("✓ Test 3 passed: F(0)..F(299) match a loop")

    # Test case 4: Value just past the 64-bit range is reduced
    assert solution.fibonacci(100) == 354224848179261915075 % MOD
    print("✓ Test 4 passed: F(100) mod 10^9 + 7")

    # Test case 5: Fibonacci numbers mod 10^9 + 7 repeat with a period
    # that divides 2 * (10^9 + 8), so F wraps back to (0, 1) there
    period = 2 * (MOD + 1)
    assert solution.fibonacci(period) == 0
    assert solution.fibonacci(period + 1) == 1
    assert solution.fibonacci(period + 10) == 55
    print("✓ Test 5 passed: Periodicity mod 10^9 + 7")

    # Test case 6: Largest n is fast and consistent with the recurrence
    n = 10**18
    assert solution.fibonacci(n) == 209783453
    assert (solution.fibonacci(n - 1) + solution.fibonacci(n)) % MOD == solution.fibonacci(n + 1)
    print("✓ Test 6 passed: F(10^18 + 1) == F(10^18) + F(10^18 - 1)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fibonacci()
