"""
EPI 16.2 Variant - Minimum Deletions to Make a Palindrome

Problem:
Given a string, return the fewest characters you must delete so that the
remaining characters (in their original order) read the same forward and
backward.

Constraints:
- 0 <= len(s) <= 1000
- O(n^2) time where n = len(s)

How it works (reduce to longest palindromic subsequence):
1. The characters you keep form a palindromic subsequence, so keep as many
   as possible
2. The longest palindromic subsequence of s equals the LCS of s and
   reversed(s) (or use P[i][j] over substrings s[i..j]:
   P[i][j] = P[i+1][j-1] + 2 if s[i] == s[j],
   else max(P[i+1][j], P[i][j-1]))
3. Answer = len(s) - longest palindromic subsequence length

Example 1:
Input: s = "abca"
Output: 1
Explanation: Delete 'b' (or 'c') to get "aca" (or "aba").

Example 2:
Input: s = "aebcbda"
Output: 2
Explanation: Delete 'e' and 'd' to get "abcba".
"""


class Solution:
    def min_deletions_to_palindrome(self, s: str) -> int:
        """
        Computes the minimum deletions needed to turn s into a palindrome.

        Args:
            s: Input string

        Returns:
            Minimum number of characters to delete

        Time Complexity: O(n^2)
        Space Complexity: O(n^2) (O(n) with rolling rows)
        """
        # TODO: Implement via longest palindromic subsequence
        pass


def test_min_deletions_to_palindrome():
    """Test cases for minimum deletions to palindrome"""
    solution = Solution()

    # Test case 1: Already a palindrome
    assert solution.min_deletions_to_palindrome("racecar") == 0
    print("✓ Test 1 passed: racecar -> 0")

    # Test case 2: One deletion
    assert solution.min_deletions_to_palindrome("abca") == 1
    print("✓ Test 2 passed: abca -> 1")

    # Test case 3: All distinct characters
    assert solution.min_deletions_to_palindrome("abcde") == 4
    print("✓ Test 3 passed: abcde -> 4")

    # Test case 4: Empty string
    assert solution.min_deletions_to_palindrome("") == 0
    print("✓ Test 4 passed: '' -> 0")

    # Test case 5: Interior deletions
    assert solution.min_deletions_to_palindrome("aebcbda") == 2
    print("✓ Test 5 passed: aebcbda -> 2")

    # Test case 6: Longer string
    assert solution.min_deletions_to_palindrome("geeksforgeeks") == 8
    print("✓ Test 6 passed: geeksforgeeks -> 8")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_deletions_to_palindrome()
