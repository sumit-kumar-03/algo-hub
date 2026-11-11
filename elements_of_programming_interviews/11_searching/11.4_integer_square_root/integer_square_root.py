"""
EPI 11.4 - Compute the Integer Square Root

Problem:
Given a nonnegative integer k, return the largest integer whose square is at
most k (i.e., floor(sqrt(k))).

Constraints:
- 0 <= k <= 2^62
- Must run in O(log k) time
- Do not use math.sqrt, math.isqrt, or ** 0.5

How it works (binary search over candidate roots):
1. Search the interval [0, k]
2. mid = (left + right) // 2:
   - mid * mid <= k: mid and everything below it are too small or exact,
     so left = mid + 1
   - Otherwise: right = mid - 1
3. When the interval is empty, left - 1 is the answer

Example 1:
Input: k = 16
Output: 4

Example 2:
Input: k = 300
Output: 17
Explanation: 17^2 = 289 <= 300 and 18^2 = 324 > 300.
"""


class Solution:
    def square_root(self, k: int) -> int:
        """
        Computes floor(sqrt(k)) for a nonnegative integer.

        Args:
            k: Nonnegative integer

        Returns:
            Largest integer r with r * r <= k

        Time Complexity: O(log k)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on [0, k]
        pass


def test_square_root():
    """Test cases for the integer square root"""
    solution = Solution()

    # Test case 1: Perfect square
    assert solution.square_root(16) == 4
    print("✓ Test 1 passed: sqrt(16) = 4")

    # Test case 2: Non-square
    assert solution.square_root(300) == 17
    print("✓ Test 2 passed: isqrt(300) = 17")

    # Test case 3: Zero and one (corner cases)
    assert solution.square_root(0) == 0
    assert solution.square_root(1) == 1
    print("✓ Test 3 passed: 0 and 1")

    # Test case 4: Small values
    assert [solution.square_root(k) for k in range(2, 10)] == [1, 1, 2, 2, 2, 2, 2, 3]
    print("✓ Test 4 passed: k = 2..9")

    # Test case 5: Book walkthrough values
    assert solution.square_root(21) == 4
    assert solution.square_root(25) == 5
    print("✓ Test 5 passed: 21 -> 4, 25 -> 5")

    # Test case 6: Large values around a perfect square
    big = 3037000499
    assert solution.square_root(big * big) == big
    assert solution.square_root(big * big - 1) == big - 1
    assert solution.square_root(2 ** 62) == 2 ** 31
    print("✓ Test 6 passed: Large values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_square_root()
