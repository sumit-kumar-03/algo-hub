"""
EPI 11.1 Variant - Prefix Search in Sorted Strings

Problem:
Given an array of strings sorted in lexicographic order and a string p,
decide whether p is a prefix of at least one string in the array.

Constraints:
- 0 <= len(words) <= 10^5
- words is sorted lexicographically
- O(m log n) time, where m = len(p); do not scan every word
- The empty string is a prefix of any string (but there must be a string)

How it works:
1. Binary search for the first word that is >= p (strings starting with p
   sort immediately at or after p itself)
2. p is a prefix of some word iff that word exists and starts with p

Example 1:
Input: words = ["apple", "banana", "band", "cat"], p = "ban"
Output: True

Example 2:
Input: words = ["apple", "banana", "band", "cat"], p = "bat"
Output: False
"""

from typing import List


class Solution:
    def is_prefix_of_any(self, words: List[str], p: str) -> bool:
        """
        Tests whether p is a prefix of some word in a sorted list.

        Args:
            words: Lexicographically sorted strings
            p: Candidate prefix

        Returns:
            True if some word starts with p, otherwise False

        Time Complexity: O(m log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search for the first word >= p
        pass


def test_is_prefix_of_any():
    """Test cases for prefix search"""
    solution = Solution()
    words = ["apple", "banana", "band", "cat"]

    # Test case 1: Prefix of two words
    assert solution.is_prefix_of_any(words, "ban") is True
    print("✓ Test 1 passed: 'ban' is a prefix")

    # Test case 2: Not a prefix
    assert solution.is_prefix_of_any(words, "bat") is False
    print("✓ Test 2 passed: 'bat' is not a prefix")

    # Test case 3: Full word counts as its own prefix
    assert solution.is_prefix_of_any(words, "cat") is True
    print("✓ Test 3 passed: Whole word")

    # Test case 4: Longer than any match
    assert solution.is_prefix_of_any(words, "cats") is False
    print("✓ Test 4 passed: Longer than the word")

    # Test case 5: Empty list
    assert solution.is_prefix_of_any([], "a") is False
    print("✓ Test 5 passed: Empty list")

    # Test case 6: Prefix of the first word only
    assert solution.is_prefix_of_any(words, "a") is True
    print("✓ Test 6 passed: First word")

    # Test case 7: Sorts before everything
    assert solution.is_prefix_of_any(words, "aa") is False
    print("✓ Test 7 passed: Sorts before all words")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_prefix_of_any()
