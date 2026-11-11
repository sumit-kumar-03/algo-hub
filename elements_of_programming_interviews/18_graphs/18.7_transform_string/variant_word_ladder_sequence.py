"""
EPI 18.7 Extra Variant - Return the Shortest Word Ladder Itself
(Practice problem, not in the book. Difficulty: Easy)
Builds on: BFS over dictionary words; record a parent pointer for each
word so the shortest production sequence can be rebuilt, not just counted.

Problem:
Given a dictionary D (a set of lowercase words) and two words s and t,
find a shortest sequence of dictionary words that starts with s, ends with
t, and in which each word differs from the previous one in exactly one
position (all words have the same length). Return the sequence as a list
of words, or [] if no sequence exists. If several shortest sequences
exist, any one of them is accepted.

Constraints:
- 1 <= len(D) <= 10^4, s is in D, all words lowercase and equal length
- Do not modify the caller's dictionary
- Target: O(d * L * 26) time, O(d) space (d = len(D), L = word length)

How it works (BFS with parent pointers):
1. BFS from s; keep parent[word] = the word it was discovered from
2. For each popped word, try every position and every letter; an unseen
   dictionary word gets its parent recorded and is enqueued
3. When t is discovered, follow parent pointers from t back to s and
   reverse the list
4. If BFS finishes without reaching t, return []

Example 1:
Input: D = {"bat", "cot", "dog", "dag", "dot", "cat"}, s = "cat", t = "dog"
Output: ["cat", "cot", "dot", "dog"]
Explanation: Each step changes one letter; no 2-step sequence exists.

Example 2:
Input: D = {"cat", "dog"}, s = "cat", t = "dog"
Output: []
"""

from typing import List, Set


class Solution:
    def ladder(self, dictionary: Set[str], s: str, t: str) -> List[str]:
        """
        Finds a shortest production sequence from s to t.

        Args:
            dictionary: Set of allowed words
            s: Start word (in the dictionary)
            t: Target word

        Returns:
            Words from s to t inclusive, or [] if t cannot be produced

        Time Complexity: O(d * L * 26)
        Space Complexity: O(d)
        """
        # TODO: Implement BFS with parent pointers
        pass


def is_valid_ladder(seq, dictionary: Set[str], s: str, t: str, steps: int) -> bool:
    """Checks the ladder is in D, links s to t, changes one letter per step."""
    if not isinstance(seq, list) or len(seq) != steps + 1:
        return False
    if seq[0] != s or seq[-1] != t or any(w not in dictionary for w in seq):
        return False
    return all(
        len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1
        for a, b in zip(seq, seq[1:])
    )


def test_word_ladder_sequence():
    """Test cases for returning a shortest word ladder"""
    solution = Solution()
    book = {"bat", "cot", "dog", "dag", "dot", "cat"}

    # Test case 1: Book dictionary
    seq = solution.ladder(set(book), "cat", "dog")
    assert is_valid_ladder(seq, book, "cat", "dog", 3)
    print(f"✓ Test 1 passed: {seq}")

    # Test case 2: Same word
    assert solution.ladder(set(book), "cat", "cat") == ["cat"]
    print("✓ Test 2 passed: s == t gives [s]")

    # Test case 3: Unreachable, and t not in the dictionary
    assert solution.ladder({"cat", "dog"}, "cat", "dog") == []
    assert solution.ladder(set(book), "cat", "cog") == []
    print("✓ Test 3 passed: Unreachable target = []")

    # Test case 4: Classic ladder with two equally short answers
    words = {"hit", "hot", "dot", "dog", "cog", "lot", "log"}
    seq = solution.ladder(set(words), "hit", "cog")
    assert is_valid_ladder(seq, words, "hit", "cog", 4)
    print(f"✓ Test 4 passed: {seq}")

    # Test case 5: Shortcut exists alongside a long chain
    chain = {"aaaa", "baaa", "bbaa", "bbba", "bbbb", "abbb", "aabb", "aaab"}
    seq = solution.ladder(set(chain), "aaaa", "aabb")
    assert is_valid_ladder(seq, chain, "aaaa", "aabb", 2)
    print(f"✓ Test 5 passed: {seq}")

    # Test case 6: Dictionary unchanged
    d6 = {"cold", "cord", "card", "ward", "warm", "word", "worm", "wore"}
    snapshot = set(d6)
    seq = solution.ladder(d6, "cold", "warm")
    assert is_valid_ladder(seq, snapshot, "cold", "warm", 4)
    assert d6 == snapshot
    print(f"✓ Test 6 passed: {seq}, dictionary unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_word_ladder_sequence()
