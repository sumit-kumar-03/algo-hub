"""
EPI 12.2 - Is an Anonymous Letter Constructible?

Problem:
You are given the text of an anonymous letter and the text of a magazine.
Decide whether the letter can be assembled by cutting characters out of the
magazine. This is possible exactly when every character occurs in the
magazine at least as many times as it occurs in the letter.

Constraints:
- 0 <= len(letter), len(magazine) <= 10^5
- O(m + n) time, O(L) space where L is the number of distinct characters in
  the letter

How it works:
1. Build a hash table counting each character of the letter
2. Scan the magazine; for each character that is still needed, decrement its
   count and delete it from the table once the count reaches zero
3. If the table becomes empty, the letter is constructible (you can stop early)
4. Otherwise, after the scan, return whether the table is empty

Example 1:
Input: letter = "hello", magazine = "oh well, hello there"
Output: True

Example 2:
Input: letter = "aab", magazine = "abc"
Output: False
Explanation: The letter needs two 'a's but the magazine only has one.
"""


class Solution:
    def is_letter_constructible_from_magazine(self, letter: str, magazine: str) -> bool:
        """
        Checks whether the letter can be written using characters of the magazine.

        Args:
            letter: Text of the anonymous letter
            magazine: Text of the magazine

        Returns:
            True if each character's count in letter is at most its count in magazine

        Time Complexity: O(m + n)
        Space Complexity: O(L) where L is the number of distinct letter characters
        """
        # TODO: Implement anonymous letter check
        pass


def test_is_letter_constructible_from_magazine():
    """Test cases for anonymous letter check"""
    solution = Solution()

    # Test case 1: Constructible
    assert solution.is_letter_constructible_from_magazine("hello", "oh well, hello there") is True
    print("✓ Test 1 passed: 'hello' from a magazine containing it -> True")

    # Test case 2: Not enough copies of a character
    assert solution.is_letter_constructible_from_magazine("aab", "abc") is False
    print("✓ Test 2 passed: Missing second 'a' -> False")

    # Test case 3: Empty letter is always constructible
    assert solution.is_letter_constructible_from_magazine("", "anything") is True
    print("✓ Test 3 passed: Empty letter -> True")

    # Test case 4: Empty magazine, nonempty letter
    assert solution.is_letter_constructible_from_magazine("a", "") is False
    print("✓ Test 4 passed: Empty magazine -> False")

    # Test case 5: Case sensitive and spaces count as characters
    assert solution.is_letter_constructible_from_magazine("A b", "a b") is False
    print("✓ Test 5 passed: Case-sensitive check -> False")

    # Test case 6: Same characters, letter is a permutation of magazine
    assert solution.is_letter_constructible_from_magazine("listen", "silent") is True
    print("✓ Test 6 passed: Anagram -> True")

    # Test case 7: Character absent from magazine
    assert solution.is_letter_constructible_from_magazine("abcz", "abcabcabc") is False
    print("✓ Test 7 passed: 'z' missing -> False")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_letter_constructible_from_magazine()
