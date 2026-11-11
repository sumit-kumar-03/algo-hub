"""
EPI 16.1 Variant - Count Scoring Sequences for a Two-Team Final Score

Problem:
The final score of a game is given as (s, s'): Team 1 scored s points and
Team 2 scored s' points. Each play is made by one team and is worth one of
the given point values. Count the number of distinct scoring sequences
(ordered lists of (team, points) plays) that end at exactly (s, s').

Constraints:
- 0 <= s, s' <= 200
- 1 <= len(individual_play_scores) <= 10, all values positive and distinct
- O(s * s' * n) time and O(s * s') space

How it works (2D DP over the running score):
1. ways[0][0] = 1
2. ways[a][b] = sum over plays p of ways[a - p][b] (Team 1 made the last
   play) + ways[a][b - p] (Team 2 made the last play), skipping negatives
3. Return ways[s][s']
(Equivalently: for each pair of per-team sequences, count the ways to
interleave them.)

Example 1:
Input: team1_score = 6, team2_score = 3, individual_play_scores = [2, 3, 7]
Output: 7
Explanation: Team 1 can score (2, 2, 2) or (3, 3), Team 2 scores (3).
Interleaving gives 4 + 3 = 7 sequences, e.g. T1 3, T2 3, T1 3.

Example 2:
Input: team1_score = 2, team2_score = 2, individual_play_scores = [2, 3, 7]
Output: 2
Explanation: T1 2 then T2 2, or T2 2 then T1 2.
"""

from typing import List


class Solution:
    def num_scoring_sequences(
        self, team1_score: int, team2_score: int, individual_play_scores: List[int]
    ) -> int:
        """
        Counts scoring sequences that produce the final score (team1, team2).

        Args:
            team1_score: Final score of Team 1
            team2_score: Final score of Team 2
            individual_play_scores: Distinct point values of a single play

        Returns:
            Number of distinct ordered (team, points) sequences

        Time Complexity: O(s * s' * n)
        Space Complexity: O(s * s')
        """
        # TODO: Implement two-team scoring sequence DP
        pass


def test_num_scoring_sequences():
    """Test cases for two-team scoring sequences"""
    solution = Solution()
    plays = [2, 3, 7]

    # Test case 1: Book example
    assert solution.num_scoring_sequences(6, 3, plays) == 7
    print("✓ Test 1 passed: (6, 3) -> 7 sequences")

    # Test case 2: 0-0 has only the empty sequence
    assert solution.num_scoring_sequences(0, 0, plays) == 1
    print("✓ Test 2 passed: (0, 0) -> 1 sequence")

    # Test case 3: One side unreachable
    assert solution.num_scoring_sequences(1, 3, plays) == 0
    print("✓ Test 3 passed: (1, 3) -> 0 sequences")

    # Test case 4: Which team scores first matters
    assert solution.num_scoring_sequences(2, 2, plays) == 2
    print("✓ Test 4 passed: (2, 2) -> 2 sequences")

    # Test case 5: Only one team scored
    assert solution.num_scoring_sequences(3, 0, plays) == 1
    print("✓ Test 5 passed: (3, 0) -> 1 sequence")

    # Test case 6: Three interleavings of (2, 2) with (3)
    assert solution.num_scoring_sequences(4, 3, plays) == 3
    print("✓ Test 6 passed: (4, 3) -> 3 sequences")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_num_scoring_sequences()
