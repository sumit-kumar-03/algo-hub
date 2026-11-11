"""
EPI 12.2 Extra Variant - First Unique Character in a String
(Practice problem, not in the book. Difficulty: Easy)
Builds on: counting characters in a hash table, then making a second pass
that consults the counts (the same count-then-check idea as the letter test).

Problem:
Given a string s, return the index of the first character that occurs
exactly once in s. If every character repeats (or s is empty), return -1.
Characters are case-sensitive, and spaces and punctuation count as ordinary
characters.

Constraints:
- 0 <= len(s) <= 10^5
- O(n) time, O(c) space where c is the number of distinct characters

How it works:
1. First pass: count how many times each character occurs
2. Second pass: return the first index whose character has count 1
3. If no such index exists, return -1

Example 1:
Input: s = "anonymous"
Output: 0
Explanation: 'a' occurs once and is the first character.

Example 2:
Input: s = "aabbccd"
Output: 6
Explanation: 'a', 'b', and 'c' each appear twice; 'd' is the only unique
character.
"""


class Solution:
    def first_unique_char(self, s: str) -> int:
        """
        Finds the index of the first character that appears exactly once.

        Args:
            s: Input string

        Returns:
            Index of the first non-repeating character, or -1 if none exists

        Time Complexity: O(n)
        Space Complexity: O(c) where c is the number of distinct characters
        """
        # TODO: Implement first unique character search
        pass


def test_first_unique_char():
    """Test cases for first unique character"""
    solution = Solution()

    # Test case 1: First character is unique
    assert solution.first_unique_char("anonymous") == 0
    print("✓ Test 1 passed: 'anonymous' -> 0")

    # Test case 2: Unique character at the very end
    assert solution.first_unique_char("aabbccd") == 6
    print("✓ Test 2 passed: 'aabbccd' -> 6")

    # Test case 3: Every character repeats
    assert solution.first_unique_char("aabbcc") == -1
    print("✓ Test 3 passed: 'aabbcc' -> -1")

    # Test case 4: Empty string
    assert solution.first_unique_char("") == -1
    print("✓ Test 4 passed: Empty string -> -1")

    # Test case 5: Single character
    assert solution.first_unique_char("z") == 0
    print("✓ Test 5 passed: 'z' -> 0")

    # Test case 6: Case sensitivity ('A' and 'a' are different)
    assert solution.first_unique_char("aAa") == 1
    print("✓ Test 6 passed: 'aAa' -> 1")

    # Test case 7: Unique character in the middle, later repeats
    assert solution.first_unique_char("abcab") == 2
    print("✓ Test 7 passed: 'abcab' -> 2")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_first_unique_char()
