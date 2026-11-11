"""
EPI 16.7 - The Bedbathandbeyond.com Problem

Problem:
Given a dictionary (a set of words) and a name such as a domain name,
decide whether the name can be split into a sequence of dictionary words
written back to back. Words may be reused. If a split exists, return the
words in order; otherwise return []. When several splits exist, any one of
them is accepted.

Constraints:
- 1 <= len(name) <= 10^4
- Dictionary lookups are O(1) (hash set)
- O(n^2) dictionary lookups (O(n * W) if you only try word lengths up to
  the longest word length W)

How it works (DP over prefixes):
1. last_length[i] = length of the final word in some valid split of
   name[:i], or -1 if name[:i] cannot be split
2. name[:i] is splittable if name[:i] is a word, or some shorter splittable
   prefix name[:j] is followed by the word name[j:i]
3. If name[:n] is splittable, walk back through last_length to rebuild the
   words, then reverse them

Example 1:
Input: name = "bedbathandbeyond",
       dictionary = {"bed", "bath", "and", "beyond", "bat", "hand"}
Output: ["bed", "bath", "and", "beyond"]
Explanation: ["bed", "bat", "hand", "beyond"] is equally valid.

Example 2:
Input: name = "amanaplanacanal", dictionary = {"a", "man", "plan", "canal"}
Output: ["a", "man", "a", "plan", "a", "canal"]
"""

from typing import List, Set


class Solution:
    def decompose_into_dictionary_words(self, name: str, dictionary: Set[str]) -> List[str]:
        """
        Splits name into dictionary words, if possible.

        Args:
            name: The string to split
            dictionary: Set of valid words

        Returns:
            Words whose concatenation is name, or [] if no split exists

        Time Complexity: O(n^2) substring lookups
        Space Complexity: O(n)
        """
        # TODO: Implement word break DP with reconstruction
        pass


def is_valid_decomposition(words, name: str, dictionary: Set[str]) -> bool:
    """Checks that words are all in the dictionary and concatenate to name."""
    return (
        isinstance(words, list)
        and len(words) > 0
        and all(w in dictionary for w in words)
        and "".join(words) == name
    )


def test_decompose_into_dictionary_words():
    """Test cases for the bedbathandbeyond.com problem"""
    solution = Solution()

    # Test case 1: Book example with two valid splits
    d1 = {"bed", "bath", "and", "beyond", "bat", "hand"}
    r1 = solution.decompose_into_dictionary_words("bedbathandbeyond", d1)
    assert is_valid_decomposition(r1, "bedbathandbeyond", d1)
    print(f"✓ Test 1 passed: bedbathandbeyond -> {r1}")

    # Test case 2: Repeated words
    d2 = {"a", "man", "plan", "canal"}
    r2 = solution.decompose_into_dictionary_words("amanaplanacanal", d2)
    assert r2 == ["a", "man", "a", "plan", "a", "canal"]
    print(f"✓ Test 2 passed: amanaplanacanal -> {r2}")

    # Test case 3: No valid split
    d3 = {"cats", "dog", "sand", "and", "cat"}
    assert solution.decompose_into_dictionary_words("catsandog", d3) == []
    print("✓ Test 3 passed: catsandog -> []")

    # Test case 4: Greedy longest-first would fail
    d4 = {"aaaa", "aaa"}
    r4 = solution.decompose_into_dictionary_words("aaaaaaa", d4)
    assert is_valid_decomposition(r4, "aaaaaaa", d4)
    print(f"✓ Test 4 passed: aaaaaaa -> {r4}")

    # Test case 5: Whole name is one word
    assert solution.decompose_into_dictionary_words("xyz", {"xyz"}) == ["xyz"]
    print("✓ Test 5 passed: xyz -> ['xyz']")

    # Test case 6: Exponentially many partial splits, but no full split
    d6 = {"a", "b", "ab"}
    assert solution.decompose_into_dictionary_words("ab" * 30 + "c", d6) == []
    print("✓ Test 6 passed: (ab)^30 c -> [] quickly")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_decompose_into_dictionary_words()
