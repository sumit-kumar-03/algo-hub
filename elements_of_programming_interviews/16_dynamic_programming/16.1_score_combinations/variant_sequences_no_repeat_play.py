"""
EPI 16.1 Extra Variant - Score Sequences With No Play Repeated Back to Back
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the 16.1 DP over totals, extended with "which play came last"
as part of the state, plus a trick to keep the transition O(1).

Problem:
Each play scores one of the given distinct point values. Count the ordered
sequences of plays whose points add up exactly to final_score, with the
rule that the same play value is never used twice in a row. For example,
with plays [2, 3, 7], the sequence (2, 3, 2) is allowed but (2, 2, 3) is
not.

Constraints:
- 0 <= final_score <= 10^4
- 1 <= n <= 50 play types, all values positive and distinct
- O(s * n) time and O(s * n) space, where s is the final score
- Answers can be large; return the exact integer (Python ints are fine)

How it works (DP over (total, last play)):
1. end[t][i] = number of valid sequences with total t whose last play is
   play i; all[t] = sum over i of end[t][i]; all[0] = 1 (empty sequence)
2. To end at t with play i, the sequence before it totals t - p_i and must
   not end with play i:
   end[t][i] = all[t - p_i] - end[t - p_i][i]   (when p_i <= t)
3. The empty sequence has no last play, so end[0][i] = 0
4. Return all[final_score]

Example 1:
Input: final_score = 12, individual_play_scores = [2, 3, 7]
Output: 7
Explanation: (2, 3, 2, 3, 2) plus the 6 orderings of (2, 3, 7). Sequences
such as (2, 2, 2, 3, 3) or (3, 3, 3, 3) repeat a play back to back.

Example 2:
Input: final_score = 5, individual_play_scores = [1, 2]
Output: 1
Explanation: Only (2, 1, 2) works; (1, 2, 2), (2, 2, 1), and anything
with two 1s in a row are not allowed.
"""

from typing import List


class Solution:
    def num_sequences_no_repeat(self, final_score: int, individual_play_scores: List[int]) -> int:
        """
        Counts ordered play sequences reaching final_score with no play
        value used twice in a row.

        Args:
            final_score: Target score
            individual_play_scores: Distinct positive point values of a play

        Returns:
            Number of valid sequences

        Time Complexity: O(s * n)
        Space Complexity: O(s * n)
        """
        # TODO: Implement the (total, last play) DP
        pass


def test_num_sequences_no_repeat():
    """Test cases for score sequences with no back-to-back repeats"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.num_sequences_no_repeat(12, [2, 3, 7]) == 7
    print("✓ Test 1 passed: 12 with [2, 3, 7] -> 7")

    # Test case 2: Example 2
    assert solution.num_sequences_no_repeat(5, [1, 2]) == 1
    print("✓ Test 2 passed: 5 with [1, 2] -> 1")

    # Test case 3: Zero score counts the empty sequence
    assert solution.num_sequences_no_repeat(0, [5]) == 1
    print("✓ Test 3 passed: 0 -> 1")

    # Test case 4: A single play type can be used only once
    assert solution.num_sequences_no_repeat(4, [2]) == 0
    assert solution.num_sequences_no_repeat(2, [2]) == 1
    print("✓ Test 4 passed: single play type")

    # Test case 5: Unreachable score
    assert solution.num_sequences_no_repeat(1, [2, 3, 7]) == 0
    print("✓ Test 5 passed: 1 with [2, 3, 7] -> 0")

    # Test case 6: Small values checked against a brute force
    assert solution.num_sequences_no_repeat(10, [1, 2, 3]) == 27
    print("✓ Test 6 passed: 10 with [1, 2, 3] -> 27")

    # Test case 7: Large score (exact big integer, checked modulo a prime)
    r7 = solution.num_sequences_no_repeat(2000, [1, 2, 3, 5])
    assert r7 % (10 ** 9 + 7) == 115238266
    print("✓ Test 7 passed: 2000 with [1, 2, 3, 5]")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_num_sequences_no_repeat()
