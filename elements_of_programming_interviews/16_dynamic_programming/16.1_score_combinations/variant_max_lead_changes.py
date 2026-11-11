"""
EPI 16.1 Variant - Maximum Number of Lead Changes

Problem:
The final score of a game is (s, s'): Team 1 scored s points and Team 2
scored s' points, with every play worth one of the given point values.
Over all scoring sequences that end at (s, s'), find the maximum number of
times the lead could have changed. Return -1 if (s, s') is unreachable.

Definitions used here:
- After each play, the team that is strictly ahead holds the lead.
- A lead change happens when a team takes the lead while the other team
  held the most recent lead. Ties do not reset who held the lead last, and
  the very first lead of the game is not a change.

Constraints:
- 0 <= s, s' <= 100
- 1 <= len(individual_play_scores) <= 10, all values positive and distinct
- O(s * s' * n) time and O(s * s') space

How it works (DP over states (a, b, last_leader)):
1. best(a, b, leader) = most lead changes possible from running score
   (a, b), where leader is who held the most recent lead (or nobody)
2. Try each play by each team, update the leader, add 1 if it flipped
3. Memoize; unreachable completions are -1
4. Answer is best(0, 0, nobody)

Example 1:
Input: team1_score = 10, team2_score = 6, individual_play_scores = [2, 3, 7]
Output: 5
Explanation: The book shows a sequence with 4 changes. One with 5:
T2 2 (0-2), T1 3 (3-2), T2 2 (3-4), T1 2 (5-4), T2 2 (5-6), T1 2 (7-6),
T1 3 (10-6).

Example 2:
Input: team1_score = 6, team2_score = 0, individual_play_scores = [2, 3, 7]
Output: 0
Explanation: Team 2 never scores, so Team 1 leads throughout.
"""

from typing import List


class Solution:
    def max_lead_changes(
        self, team1_score: int, team2_score: int, individual_play_scores: List[int]
    ) -> int:
        """
        Computes the maximum number of lead changes for a final score.

        Args:
            team1_score: Final score of Team 1
            team2_score: Final score of Team 2
            individual_play_scores: Distinct point values of a single play

        Returns:
            Maximum number of lead changes, or -1 if the score is unreachable

        Time Complexity: O(s * s' * n)
        Space Complexity: O(s * s')
        """
        # TODO: Implement max lead changes DP
        pass


def test_max_lead_changes():
    """Test cases for maximum lead changes"""
    solution = Solution()
    plays = [2, 3, 7]

    # Test case 1: Book setup (10, 6)
    assert solution.max_lead_changes(10, 6, plays) == 5
    print("✓ Test 1 passed: (10, 6) -> 5 lead changes")

    # Test case 2: No scoring at all
    assert solution.max_lead_changes(0, 0, plays) == 0
    print("✓ Test 2 passed: (0, 0) -> 0 lead changes")

    # Test case 3: One-sided game
    assert solution.max_lead_changes(6, 0, plays) == 0
    print("✓ Test 3 passed: (6, 0) -> 0 lead changes")

    # Test case 4: Single comeback
    assert solution.max_lead_changes(2, 3, plays) == 1
    print("✓ Test 4 passed: (2, 3) -> 1 lead change")

    # Test case 5: Unreachable score
    assert solution.max_lead_changes(1, 2, plays) == -1
    print("✓ Test 5 passed: (1, 2) -> -1 (unreachable)")

    # Test case 6: Tie game; a tie does not count as a change
    assert solution.max_lead_changes(3, 3, plays) == 0
    print("✓ Test 6 passed: (3, 3) -> 0 lead changes")

    # Test case 7: Tie game with room for back-and-forth
    assert solution.max_lead_changes(7, 7, plays) == 4
    print("✓ Test 7 passed: (7, 7) -> 4 lead changes")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_lead_changes()
