"""
EPI 16.1 Extra Variant - Fewest Plays to Reach a Score
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the 1D DP over totals from 16.1, switching the combine step from
"add the counts" to "take the minimum".

Problem:
Each play in a game scores one of the given point values, and any play can
be repeated as often as you like. Given a final score, return the smallest
number of plays whose points add up exactly to it, or -1 if the score
cannot be reached.

Constraints:
- 0 <= final_score <= 10^4
- 1 <= len(individual_play_scores) <= 50, all values positive and distinct
- O(s * n) time and O(s) space, where s is the final score and n the number
  of play types

How it works (bottom-up DP over totals):
1. fewest[0] = 0; every other total starts at infinity
2. For each total from 1 to final_score:
   fewest[total] = 1 + min(fewest[total - p]) over plays p <= total
3. Return fewest[final_score], or -1 if it is still infinity
Note: always grabbing the biggest play first (greedy) does not work.

Example 1:
Input: final_score = 12, individual_play_scores = [2, 3, 7]
Output: 3
Explanation: 2 + 3 + 7.

Example 2:
Input: final_score = 6, individual_play_scores = [1, 3, 4]
Output: 2
Explanation: 3 + 3. Greedy would take 4 + 1 + 1 (three plays).
"""

from typing import List


class Solution:
    def min_plays_for_score(self, final_score: int, individual_play_scores: List[int]) -> int:
        """
        Returns the fewest plays that add up exactly to final_score.

        Args:
            final_score: Target score
            individual_play_scores: Distinct positive point values of a play

        Returns:
            Minimum number of plays, or -1 if the score is unreachable

        Time Complexity: O(s * n)
        Space Complexity: O(s)
        """
        # TODO: Implement the min-over-last-play DP
        pass


def test_min_plays_for_score():
    """Test cases for the fewest plays to reach a score"""
    solution = Solution()

    # Test case 1: Book plays
    assert solution.min_plays_for_score(12, [2, 3, 7]) == 3
    print("✓ Test 1 passed: 12 with [2, 3, 7] -> 3")

    # Test case 2: Greedy trap
    assert solution.min_plays_for_score(6, [1, 3, 4]) == 2
    print("✓ Test 2 passed: 6 with [1, 3, 4] -> 2")

    # Test case 3: Zero score needs zero plays
    assert solution.min_plays_for_score(0, [2, 3, 7]) == 0
    print("✓ Test 3 passed: 0 -> 0")

    # Test case 4: Unreachable scores
    assert solution.min_plays_for_score(1, [2, 3, 7]) == -1
    assert solution.min_plays_for_score(7, [2, 4]) == -1
    print("✓ Test 4 passed: unreachable -> -1")

    # Test case 5: Another greedy trap with larger values
    assert solution.min_plays_for_score(11, [1, 5, 6, 9]) == 2
    print("✓ Test 5 passed: 11 with [1, 5, 6, 9] -> 2")

    # Test case 6: Single play type
    assert solution.min_plays_for_score(21, [7]) == 3
    print("✓ Test 6 passed: 21 with [7] -> 3")

    # Test case 7: Large score
    assert solution.min_plays_for_score(10000, [3, 7, 405, 436]) == 24
    print("✓ Test 7 passed: 10000 with [3, 7, 405, 436] -> 24")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_plays_for_score()
