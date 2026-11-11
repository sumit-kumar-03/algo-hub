"""
EPI 16.1 Extra Variant - Score Combinations With Limited Plays of Each Type
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the 16.1 combinations DP (one play type at a time, order
ignored), now with a cap on how many times each type may be used.

Problem:
Each play scores individual_play_scores[i] points and may be used at most
limits[i] times. Count the distinct combinations of plays (order does not
matter, so a combination is just how many of each type you use) whose
points add up exactly to final_score.

Constraints:
- 0 <= final_score <= 10^4
- 1 <= n <= 50 play types, values positive and distinct, 0 <= limits[i] <= 10^4
- O(s * sum(limits)) is acceptable; O(s * n) is possible with a sliding
  window sum, where s is the final score

How it works (DP one play type at a time):
1. ways[0] = 1, all other totals 0
2. For play type i with value p and limit c, build new_ways where
   new_ways[t] = ways[t] + ways[t - p] + ways[t - 2p] + ... + ways[t - c*p]
   (stop early at negative totals)
3. Replace ways with new_ways; after all types, return ways[final_score]
Faster: for each residue r mod p, new_ways along t = r, r + p, r + 2p, ...
is a running sum over a window of the last c + 1 values of ways.

Example 1:
Input: final_score = 12, individual_play_scores = [2, 3, 7], limits = [3, 2, 1]
Output: 2
Explanation: 2x3 + 3x2, and 2 + 3 + 7. (2x6 and 3x4 exceed the limits.)

Example 2:
Input: final_score = 5, individual_play_scores = [1, 2], limits = [1, 2]
Output: 1
Explanation: 1 + 2 + 2 is the only option.
"""

from typing import List


class Solution:
    def num_limited_combinations(
        self, final_score: int, individual_play_scores: List[int], limits: List[int]
    ) -> int:
        """
        Counts combinations that reach final_score with per-type limits.

        Args:
            final_score: Target score
            individual_play_scores: Distinct positive point values of a play
            limits: limits[i] is the most times play i may be used

        Returns:
            Number of combinations

        Time Complexity: O(s * n) with the sliding window (O(s * sum(limits))
        with the direct sum)
        Space Complexity: O(s)
        """
        # TODO: Implement the bounded combinations DP
        pass


def test_num_limited_combinations():
    """Test cases for limited-play score combinations"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.num_limited_combinations(12, [2, 3, 7], [3, 2, 1]) == 2
    print("✓ Test 1 passed: 12, [2, 3, 7], limits [3, 2, 1] -> 2")

    # Test case 2: Example 2
    assert solution.num_limited_combinations(5, [1, 2], [1, 2]) == 1
    print("✓ Test 2 passed: 5, [1, 2], limits [1, 2] -> 1")

    # Test case 3: Zero score has exactly one (empty) combination
    assert solution.num_limited_combinations(0, [2, 3], [0, 0]) == 1
    print("✓ Test 3 passed: 0 -> 1")

    # Test case 4: Limits large enough to match plain 16.1
    assert solution.num_limited_combinations(12, [2, 3, 7], [100, 100, 100]) == 4
    print("✓ Test 4 passed: huge limits -> 4 (same as 16.1)")

    # Test case 5: A zero limit removes a play type
    assert solution.num_limited_combinations(7, [7, 1], [0, 7]) == 1
    assert solution.num_limited_combinations(7, [7, 1], [0, 6]) == 0
    print("✓ Test 5 passed: zero limits")

    # Test case 6: Coins 1, 5, 10 with limits
    assert solution.num_limited_combinations(20, [1, 5, 10], [5, 3, 1]) == 3
    print("✓ Test 6 passed: 20, [1, 5, 10], limits [5, 3, 1] -> 3")

    # Test case 7: Large score with several types
    assert solution.num_limited_combinations(
        3000, [1, 2, 5, 10, 25], [100, 200, 100, 100, 50]
    ) == 76237
    print("✓ Test 7 passed: large score")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_num_limited_combinations()
