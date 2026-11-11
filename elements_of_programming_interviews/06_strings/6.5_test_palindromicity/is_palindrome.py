"""
EPI 6.5 - Test Palindromicity

Problem:
A string counts as palindromic if, after discarding every character that
is not a letter or digit, it reads the same forward and backward when case
is ignored. Return whether a given string is palindromic.

Constraints:
- 0 <= len(s) <= 10^5
- Compare letters case-insensitively; ignore non-alphanumeric characters
- O(n) time, O(1) extra space (don't build a cleaned or reversed copy)

How it works:
1. Place index i at the start and j at the end
2. Move i forward and j backward past non-alphanumeric characters
3. Compare s[i] and s[j] ignoring case; return False on a mismatch
4. Step both indices inward and repeat until they cross; return True

Example 1:
Input: s = "A man, a plan, a canal, Panama."
Output: True
Explanation: The letters read "amanaplanacanalpanama" both ways

Example 2:
Input: s = "Ray a Ray"
Output: False
Explanation: "rayaray" reversed is "yarayar"
"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Tests whether s is a palindrome, ignoring case and non-alphanumerics.

        Args:
            s: Input string

        Returns:
            True if s is palindromic, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement two-index palindrome check
        pass


def test_is_palindrome():
    """Test cases for palindromicity"""
    solution = Solution()

    # Test case 1: Classic sentence palindrome
    assert solution.is_palindrome("A man, a plan, a canal, Panama.") is True
    print("✓ Test 1 passed: 'A man, a plan, a canal, Panama.' is palindromic")

    # Test case 2: Mixed case with punctuation
    assert solution.is_palindrome("Able was I, ere I saw Elba!") is True
    print("✓ Test 2 passed: 'Able was I, ere I saw Elba!' is palindromic")

    # Test case 3: Not a palindrome
    assert solution.is_palindrome("Ray a Ray") is False
    print("✓ Test 3 passed: 'Ray a Ray' is not palindromic")

    # Test case 4: Empty string
    assert solution.is_palindrome("") is True
    print("✓ Test 4 passed: Empty string is palindromic")

    # Test case 5: Only punctuation
    assert solution.is_palindrome(",.!? ") is True
    print("✓ Test 5 passed: No alphanumerics is palindromic")

    # Test case 6: Digits count as characters
    assert solution.is_palindrome("0P") is False
    assert solution.is_palindrome("1a2-B1?") is False
    assert solution.is_palindrome("12a-A21") is True
    print("✓ Test 6 passed: Digits are compared")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_palindrome()
