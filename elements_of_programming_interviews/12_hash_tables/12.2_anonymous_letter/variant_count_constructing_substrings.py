"""
EPI 12.2 Extra Variant - Count Magazine Substrings That Can Build the Letter
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the "still needed" character-count table from the anonymous
letter check, combined with a two-pointer window over the magazine.

Problem:
You may only cut one contiguous piece out of the magazine. Count how many
nonempty substrings magazine[i:j] (0 <= i < j <= len(magazine)) contain
enough characters to assemble the letter, that is, every character occurs in
the substring at least as many times as in the letter. Characters are
case-sensitive. If the letter is empty, every nonempty substring works.

Constraints:
- 0 <= len(letter), len(magazine) <= 10^5
- Target: O(m + n) time, O(L) extra space where L is the number of distinct
  letter characters; checking every substring is O(n^2) or worse

How it works (two pointers with a need table):
1. Count the letter's characters into a "need" table and keep `missing`, the
   total number of characters still required
2. For each left end i, extend the right end j (never moving it backward)
   until the window magazine[i:j] supplies everything, i.e. missing == 0
3. If that happens, every substring magazine[i:j'] with j' >= j also works,
   so add len(magazine) - j + 1 to the answer
4. Before moving i forward, give back magazine[i] to the need table
5. Monotonicity: if magazine[i:j] works then so does magazine[i-1:j], so the
   minimal right end never decreases as i grows

Example 1:
Input: letter = "ab", magazine = "abab"
Output: 6
Explanation: The qualifying substrings are "ab", "aba", "abab", "ba",
"bab", and the final "ab".

Example 2:
Input: letter = "aa", magazine = "aba"
Output: 1
Explanation: Only the whole magazine "aba" contains two 'a's.
"""


class Solution:
    def count_constructing_substrings(self, letter: str, magazine: str) -> int:
        """
        Counts the substrings of magazine from which the letter can be built.

        Args:
            letter: Text of the letter
            magazine: Text of the magazine

        Returns:
            Number of nonempty substrings of magazine that cover the letter

        Time Complexity: O(m + n)
        Space Complexity: O(L) where L is the number of distinct letter characters
        """
        # TODO: Implement two-pointer counting of covering substrings
        pass


def test_count_constructing_substrings():
    """Test cases for counting covering substrings"""
    solution = Solution()

    # Test case 1: Example with overlapping windows
    assert solution.count_constructing_substrings("ab", "abab") == 6
    print("✓ Test 1 passed: 'ab' in 'abab' -> 6")

    # Test case 2: Duplicate letter characters
    assert solution.count_constructing_substrings("aa", "aba") == 1
    print("✓ Test 2 passed: 'aa' in 'aba' -> 1")

    # Test case 3: Impossible
    assert solution.count_constructing_substrings("abc", "aabb") == 0
    print("✓ Test 3 passed: Missing 'c' -> 0")

    # Test case 4: Empty letter counts every nonempty substring
    assert solution.count_constructing_substrings("", "abcd") == 10
    assert solution.count_constructing_substrings("", "") == 0
    print("✓ Test 4 passed: Empty letter -> n(n+1)/2")

    # Test case 5: Single-character letter
    #   substrings of "xax" containing 'a': "a", "xa", "ax", "xax"
    assert solution.count_constructing_substrings("a", "xax") == 4
    print("✓ Test 5 passed: 'a' in 'xax' -> 4")

    # Test case 6: Case sensitivity
    assert solution.count_constructing_substrings("A", "aaa") == 0
    print("✓ Test 6 passed: 'A' in 'aaa' -> 0")

    # Test case 7: Brute-force cross-check on fixed strings
    def brute(letter: str, magazine: str) -> int:
        need = {}
        for c in letter:
            need[c] = need.get(c, 0) + 1
        total = 0
        n = len(magazine)
        for i in range(n):
            for j in range(i + 1, n + 1):
                piece = magazine[i:j]
                if all(piece.count(c) >= k for c, k in need.items()):
                    total += 1
        return total

    cases = [("abc", "cabbacbcab"), ("aab", "abacabaab"), ("zz", "zazbzz"),
             ("ba", "aaaaab"), ("abcabc", "cbacbacbacba")]
    for letter, magazine in cases:
        assert solution.count_constructing_substrings(letter, magazine) == brute(letter, magazine)
    print("✓ Test 7 passed: Matches brute force on 5 mixed cases")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_constructing_substrings()
