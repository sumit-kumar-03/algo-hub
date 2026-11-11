"""
EPI 16.2 Extra Variant - At Most One Edit Apart
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the three Levenshtein edits (insert, delete, substitute), but
for a distance threshold of 1 a single linear scan replaces the full table.

Problem:
Given two strings a and b, return whether their Levenshtein distance is at
most 1, that is, whether b can be obtained from a by inserting one
character, deleting one character, substituting one character, or doing
nothing at all.

Constraints:
- 0 <= len(a), len(b) <= 10^5
- Comparison is case-sensitive
- O(len(a) + len(b)) time and O(1) extra space (no DP table)

How it works (scan to the first mismatch):
1. If the lengths differ by more than 1, return False
2. Let a be the shorter (or equal-length) string. Walk both strings until
   the first mismatch at a[i] != b[j]
3. Equal lengths: the rest must match after skipping one character in each
   (a substitution). Lengths differ by 1: the rest must match after
   skipping one character of the longer string only (an insertion)
4. If no mismatch is found, the answer is True

Example 1:
Input: a = "pale", b = "ple"
Output: True
Explanation: Delete 'a'.

Example 2:
Input: a = "pale", b = "bake"
Output: False
Explanation: Two substitutions are needed.
"""


class Solution:
    def is_one_edit_away(self, a: str, b: str) -> bool:
        """
        Checks whether two strings are within Levenshtein distance 1.

        Args:
            a: First string
            b: Second string

        Returns:
            True if at most one edit turns a into b, False otherwise

        Time Complexity: O(len(a) + len(b))
        Space Complexity: O(1)
        """
        # TODO: Implement the single-pass mismatch check
        pass


def test_is_one_edit_away():
    """Test cases for one edit away"""
    solution = Solution()

    # Test case 1: Examples from the statement
    assert solution.is_one_edit_away("pale", "ple") is True
    assert solution.is_one_edit_away("pale", "bake") is False
    print("✓ Test 1 passed: pale/ple -> True, pale/bake -> False")

    # Test case 2: Identical and empty strings
    assert solution.is_one_edit_away("", "") is True
    assert solution.is_one_edit_away("abc", "abc") is True
    print("✓ Test 2 passed: identical strings -> True")

    # Test case 3: Insert into an empty string, and length gap of 2
    assert solution.is_one_edit_away("", "x") is True
    assert solution.is_one_edit_away("", "xy") is False
    print("✓ Test 3 passed: '' vs 'x' -> True, '' vs 'xy' -> False")

    # Test case 4: Edits at the very start and end
    assert solution.is_one_edit_away("abc", "zbc") is True
    assert solution.is_one_edit_away("abc", "abcd") is True
    assert solution.is_one_edit_away("abc", "xabc") is True
    print("✓ Test 4 passed: edits at the ends")

    # Test case 5: Same length but a swap needs two edits
    assert solution.is_one_edit_away("ab", "ba") is False
    print("✓ Test 5 passed: ab/ba -> False")

    # Test case 6: Insertion plus a later mismatch
    assert solution.is_one_edit_away("pale", "palse") is True
    assert solution.is_one_edit_away("pale", "pxlse") is False
    print("✓ Test 6 passed: palse -> True, pxlse -> False")

    # Test case 7: Long strings, case-sensitive
    long_a = "a" * 50000 + "b" + "a" * 50000
    assert solution.is_one_edit_away(long_a, "a" * 100001) is True
    assert solution.is_one_edit_away(long_a, "a" * 100000) is True
    assert solution.is_one_edit_away("A" + long_a[1:], "a" * 100001) is False
    print("✓ Test 7 passed: long strings")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_one_edit_away()
