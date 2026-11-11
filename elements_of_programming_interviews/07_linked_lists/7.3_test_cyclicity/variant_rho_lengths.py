"""
EPI 7.3 Extra Variant - Tail and Cycle Length of an Iterated Function
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Fast and slow pointers on an implicit "list" where next(x) is
f(x), plus measuring the cycle and the path into it.

Problem:
Let f map the integers 0..m-1 to themselves, and consider the sequence
x0, f(x0), f(f(x0)), ... Because there are finitely many values, the
sequence eventually repeats and then loops forever, tracing the shape of
the Greek letter rho. Return the pair (mu, lam): mu is the index of the
first element that lies on the loop, and lam is the loop length. You may
only call f; storing the visited values is not allowed.

Constraints:
- 1 <= m <= 10^6, 0 <= x0 < m
- O(mu + lam) calls to f, O(1) extra space

How it works:
1. Move slow by one application of f and fast by two until they hold the
   same value
2. lam: keep fast fixed and step slow around the loop until it returns,
   counting the steps
3. mu: start one pointer at x0 and another lam steps ahead; move both one
   step at a time, counting steps until they hold the same value

Example 1:
Input: f(x) = (x * x + 1) % 10, x0 = 3
Output: (1, 6)
Explanation: The sequence is 3, 0, 1, 2, 5, 6, 7, 0, 1, ... The loop
0 -> 1 -> 2 -> 5 -> 6 -> 7 starts at index 1 and has length 6.

Example 2:
Input: f(x) = (x + 3) % 7, x0 = 0
Output: (0, 7)
Explanation: Adding 3 modulo 7 visits all seven values before repeating
"""

from typing import Callable, Tuple


class Solution:
    def rho_lengths(self, f: Callable[[int], int], x0: int) -> Tuple[int, int]:
        """
        Measures the tail length and the cycle length of x0, f(x0), ...

        Args:
            f: Function mapping 0..m-1 to 0..m-1
            x0: Starting value

        Returns:
            (mu, lam): index of the first value on the cycle, cycle length

        Time Complexity: O(mu + lam) calls to f
        Space Complexity: O(1)
        """
        # TODO: Implement tail and cycle length measurement
        pass


def test_rho_lengths():
    """Test cases for tail and cycle lengths"""
    solution = Solution()

    # Test case 1: Short tail into a longer loop
    assert solution.rho_lengths(lambda x: (x * x + 1) % 10, 3) == (1, 6)
    print("✓ Test 1 passed: x^2 + 1 mod 10 from 3 -> (1, 6)")

    # Test case 2: Pure cycle through every value
    assert solution.rho_lengths(lambda x: (x + 3) % 7, 0) == (0, 7)
    print("✓ Test 2 passed: x + 3 mod 7 -> (0, 7)")

    # Test case 3: Fixed point at the start
    assert solution.rho_lengths(lambda x: x, 5) == (0, 1)
    print("✓ Test 3 passed: Identity -> (0, 1)")

    # Test case 4: Long tail into a fixed point
    assert solution.rho_lengths(lambda x: max(x - 1, 0), 9) == (9, 1)
    print("✓ Test 4 passed: Countdown to a fixed point -> (9, 1)")

    # Test case 5: Table-driven function, tail of 3 into a loop of 2
    table = [1, 2, 3, 4, 3]  # 0 -> 1 -> 2 -> 3 -> 4 -> 3
    assert solution.rho_lengths(lambda x: table[x], 0) == (3, 2)
    print("✓ Test 5 passed: Table function -> (3, 2)")

    # Test case 6: Larger quadratic map, checked against a reference count
    m = 100003

    def f(x: int) -> int:
        return (x * x + 7) % m

    seen = {}
    x, i = 2, 0
    while x not in seen:
        seen[x] = i
        x, i = f(x), i + 1
    expected = (seen[x], i - seen[x])
    assert solution.rho_lengths(f, 2) == expected
    print("✓ Test 6 passed: x^2 + 7 mod 100003 from 2")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_rho_lengths()
