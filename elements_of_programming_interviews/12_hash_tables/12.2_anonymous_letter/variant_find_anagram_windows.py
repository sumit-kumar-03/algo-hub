"""
EPI 12.2 Extra Variant - Find All Anagram Windows
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the character-count hash table from the anonymous letter check,
maintained incrementally over a sliding window instead of a whole magazine.

Problem:
Given a text and a pattern, return the start indices (in increasing order)
of every substring of text that has length len(pattern) and is a
rearrangement of pattern, meaning it uses exactly the same characters with
the same counts. Characters are case-sensitive. An empty pattern has no
windows, so return [] in that case.

Constraints:
- 0 <= len(pattern), len(text) <= 10^5
- O(n) time (n = len(text)), O(c) space where c is the number of distinct
  characters; recounting every window from scratch is too slow

How it works (sliding window of counts):
1. Count the pattern's characters into a "need" table and track how many
   distinct characters still have a nonzero balance
2. Slide a window of length len(pattern) over text: when a character enters
   the window, decrement its balance; when one leaves, increment it, updating
   the number of nonzero balances as each balance crosses zero
3. Whenever no balance is nonzero, the window is an anagram; record its start

Example 1:
Input: text = "cbaebabacd", pattern = "abc"
Output: [0, 6]
Explanation: "cba" starts at 0 and "bac" starts at 6.

Example 2:
Input: text = "abab", pattern = "ab"
Output: [0, 1, 2]
Explanation: "ab", "ba", and "ab" are all rearrangements of "ab".
"""

from typing import List


class Solution:
    def find_anagram_windows(self, text: str, pattern: str) -> List[int]:
        """
        Finds the start of every window of text that is a permutation of pattern.

        Args:
            text: The string to scan
            pattern: The string whose rearrangements are sought

        Returns:
            Sorted list of start indices of matching windows

        Time Complexity: O(n) where n = len(text)
        Space Complexity: O(c) where c is the number of distinct characters
        """
        # TODO: Implement sliding-window anagram search
        pass


def test_find_anagram_windows():
    """Test cases for anagram windows"""
    solution = Solution()

    # Test case 1: Two matching windows
    assert solution.find_anagram_windows("cbaebabacd", "abc") == [0, 6]
    print("✓ Test 1 passed: 'cbaebabacd', 'abc' -> [0, 6]")

    # Test case 2: Overlapping matches
    assert solution.find_anagram_windows("abab", "ab") == [0, 1, 2]
    print("✓ Test 2 passed: 'abab', 'ab' -> [0, 1, 2]")

    # Test case 3: Pattern longer than text
    assert solution.find_anagram_windows("ab", "abc") == []
    print("✓ Test 3 passed: Pattern longer than text -> []")

    # Test case 4: Empty pattern and empty text
    assert solution.find_anagram_windows("abc", "") == []
    assert solution.find_anagram_windows("", "a") == []
    print("✓ Test 4 passed: Empty inputs -> []")

    # Test case 5: Duplicate characters in the pattern must match counts
    assert solution.find_anagram_windows("aabaa", "aab") == [0, 1, 2]
    assert solution.find_anagram_windows("abbba", "aab") == []
    print("✓ Test 5 passed: Counts matter, not just character sets")

    # Test case 6: Case sensitivity
    assert solution.find_anagram_windows("aAbBa", "ab") == []
    assert solution.find_anagram_windows("aAbBa", "aB") == [3]
    print("✓ Test 6 passed: Case-sensitive matching")

    # Test case 7: Every window matches
    assert solution.find_anagram_windows("aaaa", "a") == [0, 1, 2, 3]
    print("✓ Test 7 passed: 'aaaa', 'a' -> [0, 1, 2, 3]")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_anagram_windows()
