"""
EPI 12.1 - Test for Palindromic Permutations

Problem:
Given a string, determine whether its letters can be rearranged to form a
palindrome. For example, "edified" can be rearranged to "deified".

Constraints:
- 0 <= len(s) <= 10^5
- O(n) time using a hash table of character counts

How it works:
1. Count how many times each character appears
2. A palindrome can have at most one character with an odd count
   (the middle character of an odd-length palindrome)
3. Return True if the number of odd counts is <= 1

Example 1:
Input: s = "edified"
Output: True
Explanation: "deified" is a palindrome.

Example 2:
Input: s = "abc"
Output: False
Explanation: Three characters each appear an odd number of times.
"""


class Solution:
    def can_form_palindrome(self, s: str) -> bool:
        """
        Checks whether some permutation of s is a palindrome.

        Args:
            s: Input string

        Returns:
            True if the characters of s can form a palindrome

        Time Complexity: O(n)
        Space Complexity: O(c) where c is the number of distinct characters
        """
        # TODO: Implement palindromic permutation check
        pass


def test_can_form_palindrome():
    """Test cases for palindromic permutation check"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.can_form_palindrome("edified") is True
    print("✓ Test 1 passed: 'edified' -> True")

    # Test case 2: Already a palindrome
    assert solution.can_form_palindrome("level") is True
    print("✓ Test 2 passed: 'level' -> True")

    # Test case 3: All distinct characters
    assert solution.can_form_palindrome("abc") is False
    print("✓ Test 3 passed: 'abc' -> False")

    # Test case 4: Empty string
    assert solution.can_form_palindrome("") is True
    print("✓ Test 4 passed: Empty string -> True")

    # Test case 5: Single character
    assert solution.can_form_palindrome("a") is True
    print("✓ Test 5 passed: Single character -> True")

    # Test case 6: Two odd counts
    assert solution.can_form_palindrome("aabbcd") is False
    print("✓ Test 6 passed: 'aabbcd' -> False")

    # Test case 7: Even length, all counts even
    assert solution.can_form_palindrome("abab") is True
    print("✓ Test 7 passed: 'abab' -> True")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_can_form_palindrome()
