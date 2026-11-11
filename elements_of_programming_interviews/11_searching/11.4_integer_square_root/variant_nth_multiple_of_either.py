"""
EPI 11.4 Extra Variant - nth Number Divisible by a or b
(Practice problem, not in the book. Difficulty: Medium)
Builds on: binary search over a range of integers using a monotone test,
where the test is a cheap counting formula instead of squaring.

Problem:
Given positive integers a and b, list the positive integers that are
divisible by a or by b (or both) in increasing order. Return the nth number
in this list (1-based).

Constraints:
- 1 <= n <= 10^12; 2 <= a, b <= 10^6
- O(log(n * min(a, b))) time, O(1) space; do not generate the list

How it works (binary search on the value):
1. count(x) = x // a + x // b - x // lcm(a, b) is how many listed numbers
   are <= x (inclusion-exclusion); it never decreases as x grows
2. The answer is the smallest x with count(x) >= n
3. Search x in [1, n * min(a, b)] (that many numbers certainly contain n
   multiples of min(a, b)); move right when count(mid) < n, otherwise left

Example 1:
Input: n = 4, a = 2, b = 3
Output: 6
Explanation: The list is 2, 3, 4, 6, 8, 9, ...; 6 is counted once.

Example 2:
Input: n = 5, a = 4, b = 6
Output: 16
Explanation: 4, 6, 8, 12, 16.
"""


class Solution:
    def nth_multiple(self, n: int, a: int, b: int) -> int:
        """
        Returns the nth positive integer divisible by a or b.

        Args:
            n: 1-based position
            a: First divisor
            b: Second divisor

        Returns:
            The nth number in the merged list of multiples

        Time Complexity: O(log(n * min(a, b)))
        Space Complexity: O(1)
        """
        # TODO: Implement binary search with inclusion-exclusion counting
        pass


def _slow(n: int, a: int, b: int) -> int:
    x = 0
    while n:
        x += 1
        if x % a == 0 or x % b == 0:
            n -= 1
    return x


def test_nth_multiple():
    """Test cases for nth number divisible by a or b"""
    solution = Solution()

    # Test case 1: Overlapping multiples counted once
    assert solution.nth_multiple(4, 2, 3) == 6
    print("✓ Test 1 passed: n = 4, a = 2, b = 3 -> 6")

    # Test case 2: Non-coprime divisors
    assert solution.nth_multiple(5, 4, 6) == 16
    print("✓ Test 2 passed: n = 5, a = 4, b = 6 -> 16")

    # Test case 3: n = 1 is the smaller divisor
    assert solution.nth_multiple(1, 7, 5) == 5
    print("✓ Test 3 passed: n = 1")

    # Test case 4: a == b, and b a multiple of a
    assert solution.nth_multiple(10, 3, 3) == 30
    assert solution.nth_multiple(10, 3, 9) == 30
    print("✓ Test 4 passed: Redundant divisor")

    # Test case 5: Small cases against direct counting
    for a in range(2, 8):
        for b in range(2, 8):
            for n in (1, 2, 7, 25):
                assert solution.nth_multiple(n, a, b) == _slow(n, a, b)
    print("✓ Test 5 passed: Small cases")

    # Test case 6: Huge n
    assert solution.nth_multiple(10 ** 12, 2, 3) == 1500000000000
    assert solution.nth_multiple(10 ** 12, 999983, 1000000) == 499995999964000000
    print("✓ Test 6 passed: n = 10^12")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_nth_multiple()
