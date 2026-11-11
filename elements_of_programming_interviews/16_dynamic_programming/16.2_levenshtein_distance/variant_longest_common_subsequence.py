"""
EPI 16.2 Variant - Longest Common Subsequence

Problem:
Given two strings a and b, return a longest string that is a subsequence of
both (characters keep their relative order but need not be adjacent). If
several longest common subsequences exist, any one of them is accepted.

Constraints:
- 0 <= len(a), len(b) <= 1000
- Comparison is case-sensitive
- O(len(a) * len(b)) time and space

How it works (DP over prefixes, then backtrack):
1. L[i][j] = LCS length of a[:i] and b[:j]; L[0][*] = L[*][0] = 0
2. If a[i-1] == b[j-1]: L[i][j] = L[i-1][j-1] + 1
   Otherwise: L[i][j] = max(L[i-1][j], L[i][j-1])
3. Walk back from (len(a), len(b)): on a match take the character and move
   diagonally, otherwise move toward the larger neighbor
4. Reverse the collected characters

Example 1:
Input: a = "Carthorse", b = "Orchestra"
Output: "rhs" (length 3; "rtr" is equally valid)

Example 2:
Input: a = "abcde", b = "ace"
Output: "ace"
"""


class Solution:
    def longest_common_subsequence(self, a: str, b: str) -> str:
        """
        Finds a longest common subsequence of a and b.

        Args:
            a: First string
            b: Second string

        Returns:
            One longest string that is a subsequence of both a and b

        Time Complexity: O(len(a) * len(b))
        Space Complexity: O(len(a) * len(b))
        """
        # TODO: Implement LCS with reconstruction
        pass


def is_subsequence(sub: str, s: str) -> bool:
    """Checks that sub appears in s in order (not necessarily contiguously)."""
    it = iter(s)
    return all(ch in it for ch in sub)


def is_valid_lcs(result, a: str, b: str, expected_length: int) -> bool:
    """Checks that result is a common subsequence of the optimal length."""
    return (
        isinstance(result, str)
        and len(result) == expected_length
        and is_subsequence(result, a)
        and is_subsequence(result, b)
    )


def test_longest_common_subsequence():
    """Test cases for longest common subsequence"""
    solution = Solution()

    # Test case 1: Book example (several answers of length 3)
    result = solution.longest_common_subsequence("Carthorse", "Orchestra")
    assert is_valid_lcs(result, "Carthorse", "Orchestra", 3)
    print(f"✓ Test 1 passed: Carthorse/Orchestra -> '{result}'")

    # Test case 2: Classic example with multiple answers of length 4
    result = solution.longest_common_subsequence("ABCBDAB", "BDCABA")
    assert is_valid_lcs(result, "ABCBDAB", "BDCABA", 4)
    print(f"✓ Test 2 passed: ABCBDAB/BDCABA -> '{result}'")

    # Test case 3: Unique answer
    assert solution.longest_common_subsequence("abcde", "ace") == "ace"
    print("✓ Test 3 passed: abcde/ace -> 'ace'")

    # Test case 4: Nothing in common
    assert solution.longest_common_subsequence("abc", "def") == ""
    print("✓ Test 4 passed: abc/def -> ''")

    # Test case 5: Empty input
    assert solution.longest_common_subsequence("", "abc") == ""
    print("✓ Test 5 passed: ''/abc -> ''")

    # Test case 6: Identical strings
    assert solution.longest_common_subsequence("same", "same") == "same"
    print("✓ Test 6 passed: same/same -> 'same'")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_common_subsequence()
