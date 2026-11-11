"""
EPI 16.1 Variant - Count the Number of Score Sequences

Problem:
Same setup as 16.1, but now order matters: count the number of ordered
sequences of plays whose points add up to the final score. For example,
2 + 3 + 7 and 7 + 3 + 2 are different sequences.

Constraints:
- 0 <= final_score <= 10^4
- 1 <= len(individual_play_scores) <= 50, all values positive and distinct
- O(s * n) time and O(s) space, where s is the final score and n the number
  of play types

How it works (bottom-up DP, order-sensitive):
1. sequences[0] = 1 (the empty sequence)
2. For each total from 1 to final_score (outer loop over totals, so the
   last play can be any play type):
   sequences[total] = sum of sequences[total - p] for each play p <= total
3. Return sequences[final_score]
(Swapping the loop order from 16.1 is exactly what turns combinations into
sequences.)

Example 1:
Input: final_score = 12, individual_play_scores = [2, 3, 7]
Output: 18
Explanation: e.g. (2, 2, 2, 3, 3), (2, 3, 2, 2, 3), (2, 3, 7), (7, 3, 2), ...

Example 2:
Input: final_score = 5, individual_play_scores = [2, 3, 7]
Output: 2
Explanation: (2, 3) and (3, 2)
"""

from typing import List


class Solution:
    def num_sequences_for_final_score(
        self, final_score: int, individual_play_scores: List[int]
    ) -> int:
        """
        Counts ordered sequences of plays that sum to final_score.

        Args:
            final_score: Target total score
            individual_play_scores: Distinct point values of a single play

        Returns:
            Number of ordered play sequences that reach final_score

        Time Complexity: O(s * n)
        Space Complexity: O(s)
        """
        # TODO: Implement score sequences DP
        pass


def test_num_sequences_for_final_score():
    """Test cases for score sequences"""
    solution = Solution()
    plays = [2, 3, 7]

    # Test case 1: Book example
    assert solution.num_sequences_for_final_score(12, plays) == 18
    print("✓ Test 1 passed: score 12 -> 18 sequences")

    # Test case 2: Zero score has exactly one (empty) sequence
    assert solution.num_sequences_for_final_score(0, plays) == 1
    print("✓ Test 2 passed: score 0 -> 1 sequence")

    # Test case 3: Unreachable score
    assert solution.num_sequences_for_final_score(1, plays) == 0
    print("✓ Test 3 passed: score 1 -> 0 sequences")

    # Test case 4: Order matters
    assert solution.num_sequences_for_final_score(5, plays) == 2
    print("✓ Test 4 passed: score 5 -> 2 sequences")

    # Test case 5: Score 9
    assert solution.num_sequences_for_final_score(9, plays) == 7
    print("✓ Test 5 passed: score 9 -> 7 sequences")

    # Test case 6: Plays of 1 and 2 give Fibonacci numbers
    assert solution.num_sequences_for_final_score(10, [1, 2]) == 89
    print("✓ Test 6 passed: score 10 with [1, 2] -> 89 sequences")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_num_sequences_for_final_score()
