"""
EPI 12.5 Extra Variant - Shortest Distance Between Two Given Words
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the single left-to-right scan that remembers the latest index of
each word and measures the gap at every new occurrence.

Problem:
Given a list of words and two query words word1 and word2, return the
smallest index distance |i - j| such that words[i] == word1 and
words[j] == word2 with i != j. The two query words may be the same word, in
which case you need two different occurrences of it. Return -1 if no valid
pair exists.

Constraints:
- 0 <= len(words) <= 10^5
- O(n) time, O(1) extra space (only the latest index of each query word is
  needed, not a table of every word)

How it works:
1. Keep last1 and last2, the latest indices where word1 and word2 appeared
   (initially None)
2. For each index i: if words[i] == word1, compare with last2 before
   updating last1; if it equals word2, compare with last1 before updating
   last2
3. When word1 == word2, a single "latest index" suffices: every new
   occurrence is compared with the previous one, exactly like nearest
   repeated entries restricted to one word
4. Return the best distance, or -1

Example 1:
Input: words = ["practice", "makes", "perfect", "coding", "makes"],
       word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: same words, word1 = "makes", word2 = "makes"
Output: 3
Explanation: "makes" occurs at indices 1 and 4.
"""

from typing import List


class Solution:
    def shortest_distance(self, words: List[str], word1: str, word2: str) -> int:
        """
        Finds the closest pair of positions holding word1 and word2.

        Args:
            words: List of words
            word1: First query word
            word2: Second query word (may equal word1)

        Returns:
            Smallest index distance between distinct positions, or -1 if none

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement shortest word distance
        pass


def test_shortest_distance():
    """Test cases for shortest distance between words"""
    solution = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]

    # Test case 1: Two different words
    assert solution.shortest_distance(words, "coding", "practice") == 3
    print("✓ Test 1 passed: 'coding' / 'practice' -> 3")

    # Test case 2: Closest pair uses a later occurrence
    assert solution.shortest_distance(words, "makes", "coding") == 1
    print("✓ Test 2 passed: 'makes' / 'coding' -> 1")

    # Test case 3: Same word twice
    assert solution.shortest_distance(words, "makes", "makes") == 3
    print("✓ Test 3 passed: 'makes' / 'makes' -> 3")

    # Test case 4: Same word occurring only once
    assert solution.shortest_distance(words, "coding", "coding") == -1
    print("✓ Test 4 passed: Single occurrence of same word -> -1")

    # Test case 5: A query word that never appears, and empty input
    assert solution.shortest_distance(words, "coding", "rest") == -1
    assert solution.shortest_distance([], "a", "b") == -1
    print("✓ Test 5 passed: Missing word -> -1")

    # Test case 6: Order of the query words doesn't matter
    w = ["a", "x", "b", "a", "y", "y", "b"]
    assert solution.shortest_distance(w, "a", "b") == 1
    assert solution.shortest_distance(w, "b", "a") == 1
    print("✓ Test 6 passed: Symmetric in word1/word2")

    # Test case 7: Same word, nearest pair is not the first pair
    w = ["z", "q", "q", "q", "z", "z"]
    assert solution.shortest_distance(w, "z", "z") == 1
    assert solution.shortest_distance(w, "q", "z") == 1
    print("✓ Test 7 passed: Same word with several occurrences")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shortest_distance()
