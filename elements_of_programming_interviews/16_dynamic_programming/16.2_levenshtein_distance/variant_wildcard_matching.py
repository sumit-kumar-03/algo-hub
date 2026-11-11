"""
EPI 16.2 Extra Variant - Wildcard Pattern Matching
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the 16.2 DP over prefix pairs (i, j), where each cell looks at
its diagonal, upper, and left neighbors depending on the current symbols.

Problem:
A pattern is made of ordinary characters plus two wildcards:
- '?' matches exactly one character (any character)
- '*' matches any sequence of characters, including the empty sequence
Given a text s (no wildcards) and a pattern p, return whether p matches
the whole of s (not just part of it).

Constraints:
- 0 <= len(s), len(p) <= 2000
- s has no '?' or '*'; comparison is case-sensitive
- O(len(s) * len(p)) time; O(len(p)) space is possible

How it works (DP over prefixes):
1. M[i][j] = True if p[:j] matches s[:i]; M[0][0] = True
2. M[0][j] = True only while p[:j] is all '*'
3. For i, j >= 1:
   - p[j-1] == '*': M[i][j] = M[i][j-1]  ('*' matches nothing)
                             or M[i-1][j] ('*' absorbs s[i-1] too)
   - p[j-1] == '?' or p[j-1] == s[i-1]: M[i][j] = M[i-1][j-1]
   - otherwise False
4. Return M[len(s)][len(p)]
(A greedy two-pointer method with backtracking to the last '*' also works
in O(1) space, but the DP is the one to master here.)

Example 1:
Input: s = "adceb", p = "*a*b"
Output: True
Explanation: The first '*' matches "", 'a' matches 'a', the second '*'
matches "dce", and 'b' matches 'b'.

Example 2:
Input: s = "acdcb", p = "a*c?b"
Output: False
"""


class Solution:
    def is_wildcard_match(self, s: str, p: str) -> bool:
        """
        Checks whether pattern p (with '?' and '*') matches all of s.

        Args:
            s: Text to match
            p: Pattern with optional '?' and '*' wildcards

        Returns:
            True if p matches the whole of s, False otherwise

        Time Complexity: O(len(s) * len(p))
        Space Complexity: O(len(p)) with a rolling row
        """
        # TODO: Implement the prefix DP for wildcard matching
        pass


def test_is_wildcard_match():
    """Test cases for wildcard matching"""
    solution = Solution()

    # Test case 1: Examples from the statement
    assert solution.is_wildcard_match("adceb", "*a*b") is True
    assert solution.is_wildcard_match("acdcb", "a*c?b") is False
    print("✓ Test 1 passed: adceb/*a*b -> True, acdcb/a*c?b -> False")

    # Test case 2: Empty text
    assert solution.is_wildcard_match("", "") is True
    assert solution.is_wildcard_match("", "***") is True
    assert solution.is_wildcard_match("", "?") is False
    print("✓ Test 2 passed: empty text cases")

    # Test case 3: Pattern must cover the whole text
    assert solution.is_wildcard_match("aa", "a") is False
    assert solution.is_wildcard_match("aa", "*") is True
    assert solution.is_wildcard_match("cb", "?a") is False
    print("✓ Test 3 passed: whole-text matching")

    # Test case 4: '?' needs exactly one character
    assert solution.is_wildcard_match("abc", "a?c") is True
    assert solution.is_wildcard_match("ac", "a?c") is False
    print("✓ Test 4 passed: '?' matches exactly one character")

    # Test case 5: Case-sensitive literal characters
    assert solution.is_wildcard_match("Hello", "h*") is False
    assert solution.is_wildcard_match("Hello", "H*o") is True
    print("✓ Test 5 passed: case-sensitive")

    # Test case 6: '*' must sometimes absorb a matching character
    assert solution.is_wildcard_match("abcabczzzde", "*abc???de*") is True
    assert solution.is_wildcard_match("mississippi", "m??*ss*?i*pi") is False
    print("✓ Test 6 passed: tricky star placements")

    # Test case 7: Long inputs that punish exponential backtracking
    s7 = "a" * 2000
    assert solution.is_wildcard_match(s7, "*a" * 30 + "*b") is False
    assert solution.is_wildcard_match(s7, "*a" * 30 + "*") is True
    print("✓ Test 7 passed: long inputs")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_wildcard_match()
