"""
EPI 12.2 Extra Variant - Minimum Number of Magazine Copies
(Practice problem, not in the book. Difficulty: Medium)
Builds on: comparing per-character counts of the letter against the
magazine, now turning the comparison into a ratio instead of a yes/no.

Problem:
You can buy as many identical copies of the magazine as you like. Return the
minimum number of copies you need to cut out every character of the letter.
Return 0 if the letter is empty, and -1 if the letter uses a character that
never appears in the magazine. Characters are case-sensitive.

Constraints:
- 0 <= len(letter), len(magazine) <= 10^5
- O(m + n) time, O(L + M) space for the two count tables

How it works:
1. Count the characters of both the letter and the magazine
2. For every character c in the letter, one copy supplies mag[c] of them, so
   you need ceil(letter[c] / mag[c]) copies to cover c; if mag[c] is 0, the
   answer is -1
3. The answer is the maximum of those per-character requirements

Example 1:
Input: letter = "banana", magazine = "abn"
Output: 3
Explanation: The letter needs three 'a's and each copy has only one.

Example 2:
Input: letter = "hello", magazine = "hole"
Output: 2
Explanation: Two 'l's are needed but each copy provides one.
"""


class Solution:
    def min_magazine_copies(self, letter: str, magazine: str) -> int:
        """
        Computes how many magazine copies are needed to build the letter.

        Args:
            letter: Text of the letter
            magazine: Text of a single magazine copy

        Returns:
            Minimum number of copies, 0 for an empty letter, or -1 if impossible

        Time Complexity: O(m + n)
        Space Complexity: O(L + M) for the character counts
        """
        # TODO: Implement minimum copies computation
        pass


def test_min_magazine_copies():
    """Test cases for minimum magazine copies"""
    solution = Solution()

    # Test case 1: Limited by the most demanding character
    assert solution.min_magazine_copies("banana", "abn") == 3
    print("✓ Test 1 passed: 'banana' from 'abn' -> 3")

    # Test case 2: Two copies needed for the double 'l'
    assert solution.min_magazine_copies("hello", "hole") == 2
    print("✓ Test 2 passed: 'hello' from 'hole' -> 2")

    # Test case 3: One copy is enough
    assert solution.min_magazine_copies("abc", "cbaxyz") == 1
    print("✓ Test 3 passed: 'abc' from 'cbaxyz' -> 1")

    # Test case 4: Character missing from the magazine
    assert solution.min_magazine_copies("abz", "aabb") == -1
    print("✓ Test 4 passed: Missing 'z' -> -1")

    # Test case 5: Empty letter needs no copies
    assert solution.min_magazine_copies("", "") == 0
    assert solution.min_magazine_copies("", "abc") == 0
    print("✓ Test 5 passed: Empty letter -> 0")

    # Test case 6: Ceiling division (5 'a's, 2 per copy -> 3 copies)
    assert solution.min_magazine_copies("aaaaa", "aab") == 3
    print("✓ Test 6 passed: 5 'a's with 2 per copy -> 3")

    # Test case 7: Case sensitivity and empty magazine
    assert solution.min_magazine_copies("A", "a") == -1
    assert solution.min_magazine_copies("a", "") == -1
    print("✓ Test 7 passed: Case-sensitive / empty magazine -> -1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_magazine_copies()
