"""
EPI 12.2 Extra Variant - Anonymous Letter with Blank Tiles
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the character-count hash table from the anonymous letter check,
extended to track a shortfall instead of stopping at the first miss.

Problem:
The magazine now contains some blank tiles, written as '?'. Each blank tile
can be cut out and used as any single character of the letter. Decide
whether the letter can be assembled from the magazine. The letter itself
never contains '?'. Characters are case-sensitive.

Constraints:
- 0 <= len(letter), len(magazine) <= 10^5
- letter does not contain '?'
- O(m + n) time, O(L) space where L is the number of distinct letter characters

How it works:
1. Count the characters of the letter in a hash table
2. Scan the magazine: count blank tiles separately; for any other character
   that the letter still needs, decrement its count
3. The total remaining need is the number of characters the magazine could
   not supply directly
4. The letter is constructible exactly when that shortfall is at most the
   number of blank tiles

Example 1:
Input: letter = "help", magazine = "he??"
Output: True
Explanation: 'h' and 'e' come from the magazine; the two blanks become 'l'
and 'p'.

Example 2:
Input: letter = "aaa", magazine = "a?b"
Output: False
Explanation: One 'a' and one blank cover two of the three 'a's; 'b' is useless.
"""


class Solution:
    def can_construct_with_blanks(self, letter: str, magazine: str) -> bool:
        """
        Checks whether the letter can be built when '?' tiles act as wildcards.

        Args:
            letter: Text of the letter (no '?' characters)
            magazine: Text of the magazine, where '?' is a blank tile

        Returns:
            True if the letter can be assembled, False otherwise

        Time Complexity: O(m + n)
        Space Complexity: O(L) where L is the number of distinct letter characters
        """
        # TODO: Implement constructibility check with wildcard tiles
        pass


def test_can_construct_with_blanks():
    """Test cases for anonymous letter with blank tiles"""
    solution = Solution()

    # Test case 1: Blanks fill exactly the missing characters
    assert solution.can_construct_with_blanks("help", "he??") is True
    print("✓ Test 1 passed: 'help' from 'he??' -> True")

    # Test case 2: Not enough blanks
    assert solution.can_construct_with_blanks("aaa", "a?b") is False
    print("✓ Test 2 passed: 'aaa' from 'a?b' -> False")

    # Test case 3: Only blanks
    assert solution.can_construct_with_blanks("xyz", "???") is True
    print("✓ Test 3 passed: 'xyz' from '???' -> True")

    # Test case 4: Empty letter is always constructible
    assert solution.can_construct_with_blanks("", "") is True
    print("✓ Test 4 passed: Empty letter -> True")

    # Test case 5: Extra copies of one character can't stand in for another
    assert solution.can_construct_with_blanks("ab", "aaaa?") is True
    assert solution.can_construct_with_blanks("abc", "aaaa?") is False
    print("✓ Test 5 passed: Surplus 'a's don't replace 'c'")

    # Test case 6: Case sensitivity, blank covers the uppercase letter
    assert solution.can_construct_with_blanks("Aa", "a?") is True
    assert solution.can_construct_with_blanks("AA", "a?") is False
    print("✓ Test 6 passed: Case-sensitive with blanks")

    # Test case 7: No blanks behaves like the original problem
    assert solution.can_construct_with_blanks("listen", "silent") is True
    assert solution.can_construct_with_blanks("hello", "helo") is False
    print("✓ Test 7 passed: No blanks -> original rule")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_can_construct_with_blanks()
