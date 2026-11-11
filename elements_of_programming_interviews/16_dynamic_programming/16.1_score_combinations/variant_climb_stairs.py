"""
EPI 16.1 Variant - Count the Ways to Climb Stairs

Problem:
You are climbing a staircase and can advance anywhere from 1 to k steps at
a time. Count the number of distinct ways to land exactly on step n.
Different orders of the same step sizes count as different ways.

Constraints:
- 0 <= n <= 10^4, 1 <= k <= n (k may exceed n; extra sizes are unusable)
- O(n * k) time (O(n) with a sliding window sum), O(n) space

How it works (bottom-up DP):
1. ways[0] = 1 (already at the bottom)
2. ways[i] = ways[i - 1] + ways[i - 2] + ... + ways[i - k] (skip negatives)
3. Return ways[n]

Example 1:
Input: n = 4, k = 2
Output: 5
Explanation: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2

Example 2:
Input: n = 4, k = 3
Output: 7
Explanation: The 5 ways above plus 1+3 and 3+1
"""


class Solution:
    def number_of_ways_to_top(self, n: int, k: int) -> int:
        """
        Counts the ways to climb exactly n stairs taking 1..k steps at a time.

        Args:
            n: Number of stairs
            k: Maximum number of stairs per move

        Returns:
            Number of distinct ordered ways to reach step n

        Time Complexity: O(n * k)
        Space Complexity: O(n)
        """
        # TODO: Implement stair climbing DP
        pass


def test_number_of_ways_to_top():
    """Test cases for climbing stairs"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.number_of_ways_to_top(4, 2) == 5
    print("✓ Test 1 passed: n=4, k=2 -> 5")

    # Test case 2: Larger step size
    assert solution.number_of_ways_to_top(4, 3) == 7
    print("✓ Test 2 passed: n=4, k=3 -> 7")

    # Test case 3: Only single steps allowed
    assert solution.number_of_ways_to_top(5, 1) == 1
    print("✓ Test 3 passed: n=5, k=1 -> 1")

    # Test case 4: Zero stairs
    assert solution.number_of_ways_to_top(0, 2) == 1
    print("✓ Test 4 passed: n=0 -> 1")

    # Test case 5: k larger than n
    assert solution.number_of_ways_to_top(1, 3) == 1
    print("✓ Test 5 passed: n=1, k=3 -> 1")

    # Test case 6: Fibonacci growth for k=2
    assert solution.number_of_ways_to_top(10, 2) == 89
    print("✓ Test 6 passed: n=10, k=2 -> 89")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_number_of_ways_to_top()
