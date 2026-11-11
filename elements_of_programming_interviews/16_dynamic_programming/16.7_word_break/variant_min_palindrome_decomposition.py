"""
EPI 16.7 Variant - Minimum Palindromic Decomposition

Problem:
A palindromic decomposition of a string splits it into pieces that are all
palindromes. Every string has one (single characters), so the question is
how few pieces are needed. Return a palindromic decomposition of s that
uses the minimum number of pieces. Any minimum decomposition is accepted.

Constraints:
- 1 <= len(s) <= 2000
- O(n^2) time with a precomputed palindrome table

How it works (DP over prefixes):
1. Precompute is_pal[i][j] for every substring (expand around centers or
   is_pal[i][j] = s[i] == s[j] and is_pal[i+1][j-1])
2. cuts[i] = fewest pieces for s[:i]; cuts[0] = 0
3. cuts[i] = min(cuts[j] + 1) over j < i with s[j:i] a palindrome; remember
   the best j
4. Walk back from n through the stored j values to rebuild the pieces

Example 1:
Input: s = "0204451881"
Output: ["020", "44", "5", "1881"]

Example 2:
Input: s = "abc"
Output: ["a", "b", "c"]
"""

from typing import List


class Solution:
    def min_palindrome_decomposition(self, s: str) -> List[str]:
        """
        Splits s into the fewest palindromic pieces.

        Args:
            s: Input string

        Returns:
            Palindromic pieces, in order, whose concatenation is s

        Time Complexity: O(n^2)
        Space Complexity: O(n^2) for the palindrome table
        """
        # TODO: Implement minimum palindromic decomposition DP
        pass


def is_valid_decomposition(pieces, s: str, expected_count: int) -> bool:
    """Checks pieces are palindromes, rebuild s, and have the optimal count."""
    return (
        isinstance(pieces, list)
        and len(pieces) == expected_count
        and "".join(pieces) == s
        and all(p and p == p[::-1] for p in pieces)
    )


def test_min_palindrome_decomposition():
    """Test cases for minimum palindromic decomposition"""
    solution = Solution()

    # Test case 1: Book example
    r1 = solution.min_palindrome_decomposition("0204451881")
    assert r1 == ["020", "44", "5", "1881"]
    print(f"✓ Test 1 passed: 0204451881 -> {r1}")

    # Test case 2: Whole string is a palindrome
    assert solution.min_palindrome_decomposition("racecar") == ["racecar"]
    print("✓ Test 2 passed: racecar -> ['racecar']")

    # Test case 3: No palindromes longer than 1
    assert solution.min_palindrome_decomposition("abc") == ["a", "b", "c"]
    print("✓ Test 3 passed: abc -> ['a', 'b', 'c']")

    # Test case 4: Two pieces
    assert solution.min_palindrome_decomposition("aab") == ["aa", "b"]
    print("✓ Test 4 passed: aab -> ['aa', 'b']")

    # Test case 5: Single character
    assert solution.min_palindrome_decomposition("a") == ["a"]
    print("✓ Test 5 passed: a -> ['a']")

    # Test case 6: Optimal split uses 2 pieces
    r6 = solution.min_palindrome_decomposition("abacdc")
    assert is_valid_decomposition(r6, "abacdc", 2)
    print(f"✓ Test 6 passed: abacdc -> {r6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_palindrome_decomposition()
