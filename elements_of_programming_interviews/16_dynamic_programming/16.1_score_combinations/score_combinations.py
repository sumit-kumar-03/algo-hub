"""
EPI 16.1 - Count the Number of Score Combinations

Problem:
In a game, each play scores one of a fixed set of point values. Given a final
score and the list of possible play scores, count how many distinct
combinations of plays add up to the final score. Order does not matter:
2 + 3 and 3 + 2 are the same combination.

Constraints:
- 0 <= final_score <= 10^4
- 1 <= len(individual_play_scores) <= 50, all values positive and distinct
- O(s * n) time where s is the final score and n the number of play types

How it works (bottom-up DP, like the coin change problem):
1. combinations[0] = 1 (one way to make 0: no plays)
2. For each play score p (outer loop, so order is ignored):
   - For total from p to final_score:
     combinations[total] += combinations[total - p]
3. Return combinations[final_score]

Example 1:
Input: final_score = 12, individual_play_scores = [2, 3, 7]
Output: 4
Explanation: 2x6, 2x3 + 3x2, 3x4, 2 + 3 + 7

Example 2:
Input: final_score = 1, individual_play_scores = [2, 3, 7]
Output: 0
"""

from typing import List


class Solution:
    def num_combinations_for_final_score(
        self, final_score: int, individual_play_scores: List[int]
    ) -> int:
        """
        Counts combinations of plays that sum to final_score.

        Args:
            final_score: Target total score
            individual_play_scores: Distinct point values of a single play

        Returns:
            Number of unordered combinations that reach final_score

        Time Complexity: O(s * n)
        Space Complexity: O(s) with a 1D table (O(s * n) with a 2D table)
        """
        # TODO: Implement score combinations DP
        pass


def test_num_combinations_for_final_score():
    """Test cases for score combinations"""
    solution = Solution()
    plays = [2, 3, 7]

    # Test case 1: Book example
    assert solution.num_combinations_for_final_score(12, plays) == 4
    print("✓ Test 1 passed: score 12 -> 4 combinations")

    # Test case 2: Zero score has exactly one combination
    assert solution.num_combinations_for_final_score(0, plays) == 1
    print("✓ Test 2 passed: score 0 -> 1 combination")

    # Test case 3: Unreachable score
    assert solution.num_combinations_for_final_score(1, plays) == 0
    print("✓ Test 3 passed: score 1 -> 0 combinations")

    # Test case 4: Small score
    assert solution.num_combinations_for_final_score(6, plays) == 2
    print("✓ Test 4 passed: score 6 -> 2 combinations")

    # Test case 5: Order must not be counted twice
    assert solution.num_combinations_for_final_score(7, plays) == 2
    print("✓ Test 5 passed: score 7 -> 2 combinations")

    # Test case 6: Single play type
    assert solution.num_combinations_for_final_score(10, [5]) == 1
    print("✓ Test 6 passed: score 10 with [5] -> 1 combination")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_num_combinations_for_final_score()
