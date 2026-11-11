"""
EPI 16.2 Extra Variant - Count the Occurrences of a String as a Subsequence
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the 16.2 table over prefix pairs (i, j), switching from "fewest
edits" to "number of ways", where only deletions from s are allowed.

Problem:
Given strings s and t, count the number of ways to delete characters from
s so that what remains is exactly t. Two ways are different if they keep
a different set of positions of s. In other words, count the index
sequences i_1 < i_2 < ... < i_len(t) with s[i_k] == t[k] for every k.

Constraints:
- 0 <= len(s), len(t) <= 1000
- Comparison is case-sensitive
- O(len(s) * len(t)) time; O(len(t)) space is possible
- Answers can be large; return the exact integer

How it works (DP over prefixes):
1. W[i][j] = number of ways that s[:i] contains t[:j] as a subsequence
2. W[i][0] = 1 for every i (keep nothing); W[0][j] = 0 for j > 0
3. W[i][j] = W[i-1][j] (skip s[i-1])
             + W[i-1][j-1] if s[i-1] == t[j-1] (match it with t[j-1])
4. Return W[len(s)][len(t)]
Space saver: keep one row and update j from high to low.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: Any one of the three b's can be the one that is deleted.

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
"""

import math


class Solution:
    def count_subsequence_occurrences(self, s: str, t: str) -> int:
        """
        Counts the ways t appears as a subsequence of s.

        Args:
            s: Source string
            t: Pattern string

        Returns:
            Number of distinct index sequences of s that spell t

        Time Complexity: O(len(s) * len(t))
        Space Complexity: O(len(t)) with a rolling row
        """
        # TODO: Implement the prefix DP counting matches
        pass


def test_count_subsequence_occurrences():
    """Test cases for counting subsequence occurrences"""
    solution = Solution()

    # Test case 1: Examples from the statement
    assert solution.count_subsequence_occurrences("rabbbit", "rabbit") == 3
    assert solution.count_subsequence_occurrences("babgbag", "bag") == 5
    print("✓ Test 1 passed: rabbbit/rabbit -> 3, babgbag/bag -> 5")

    # Test case 2: Empty pattern appears exactly once
    assert solution.count_subsequence_occurrences("", "") == 1
    assert solution.count_subsequence_occurrences("abc", "") == 1
    print("✓ Test 2 passed: empty pattern -> 1")

    # Test case 3: Pattern longer than source, or missing letters
    assert solution.count_subsequence_occurrences("", "a") == 0
    assert solution.count_subsequence_occurrences("abc", "abcd") == 0
    assert solution.count_subsequence_occurrences("abc", "ca") == 0
    print("✓ Test 3 passed: impossible patterns -> 0")

    # Test case 4: Case-sensitive
    assert solution.count_subsequence_occurrences("aAa", "a") == 2
    print("✓ Test 4 passed: aAa/a -> 2")

    # Test case 5: Repeated letters give binomial coefficients
    assert solution.count_subsequence_occurrences("aaaaa", "aa") == 10
    print("✓ Test 5 passed: aaaaa/aa -> C(5, 2) = 10")

    # Test case 6: Identical strings
    assert solution.count_subsequence_occurrences("abcde", "abcde") == 1
    print("✓ Test 6 passed: identical -> 1")

    # Test case 7: Large answer
    r7 = solution.count_subsequence_occurrences("a" * 200, "a" * 100)
    assert r7 == math.comb(200, 100)
    print("✓ Test 7 passed: 200 a's choose 100 -> C(200, 100)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_subsequence_occurrences()
