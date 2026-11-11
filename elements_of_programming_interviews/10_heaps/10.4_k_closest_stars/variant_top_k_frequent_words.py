"""
EPI 10.4 Extra Variant - Top k Frequent Words
(Practice problem, not in the book. Difficulty: Medium)
Builds on: a size-k heap that keeps the best candidates and evicts the
worst, here with a two-part ordering (count, then alphabetical).

Problem:
Given a list of words and an integer k, return the k most frequent distinct
words. Order the result from most to least frequent; words with the same
frequency are ordered alphabetically (lexicographically smaller first). If
there are fewer than k distinct words, return all of them in that order.

Constraints:
- 0 <= len(words) <= 10^5; words are lowercase letters
- 0 <= k
- O(n + d log k) time and O(d) space, where d is the number of distinct
  words (counting needs O(d); the heap itself stays at size k)

How it works (count, then keep the k best in a min-heap of "worst first"):
1. Count each word with a dictionary
2. The heap's top must be the weakest of the current k: lowest count, and
   among equal counts the alphabetically largest word. Since heapq is a
   min-heap on tuples, wrap the word in a small class whose comparison is
   reversed (or push (count, word) into a heap of size d and pop k times
   with key (-count, word))
3. After processing every distinct word, pop all entries and reverse

Example 1:
Input: words = ["a", "b", "a", "c", "b", "a"], k = 2
Output: ["a", "b"]
Explanation: "a" appears 3 times, "b" 2 times, "c" once.

Example 2:
Input: words = ["dog", "cat", "dog", "cat", "emu"], k = 2
Output: ["cat", "dog"]
Explanation: "cat" and "dog" both appear twice; "cat" comes first
alphabetically.
"""

from typing import List


class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        """
        Returns the k most frequent words, ties broken alphabetically.

        Args:
            words: List of lowercase words
            k: Number of words to return

        Returns:
            Up to k distinct words, most frequent first

        Time Complexity: O(n + d log k)
        Space Complexity: O(d)
        """
        # TODO: Implement with a counter and a size-k heap
        pass


def test_top_k_frequent():
    """Test cases for top k frequent words"""
    solution = Solution()

    # Test case 1: Distinct frequencies
    assert solution.top_k_frequent(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]
    print("✓ Test 1 passed: Distinct frequencies")

    # Test case 2: Frequency tie broken alphabetically
    assert solution.top_k_frequent(["dog", "cat", "dog", "cat", "emu"], 2) == ["cat", "dog"]
    print("✓ Test 2 passed: Alphabetical tie-break")

    # Test case 3: Tie at the cutoff
    words3 = ["x", "y", "z", "y", "x", "w"]
    assert solution.top_k_frequent(words3, 3) == ["x", "y", "w"]
    print("✓ Test 3 passed: Tie at the cutoff")

    # Test case 4: Empty input, k = 0, and k above the distinct count
    assert solution.top_k_frequent([], 3) == []
    assert solution.top_k_frequent(["a"], 0) == []
    assert solution.top_k_frequent(["b", "a", "b"], 10) == ["b", "a"]
    print("✓ Test 4 passed: Edge sizes")

    # Test case 5: Prefix words ("ab" sorts before "abc")
    words5 = ["abc", "ab", "abc", "ab", "a"]
    assert solution.top_k_frequent(words5, 2) == ["ab", "abc"]
    print("✓ Test 5 passed: Prefix words")

    # Test case 6: Larger deterministic input vs. full sort
    pool = ["w%d" % (i % 37) for i in range(0, 5000, 3)] + ["w%d" % (i % 11) for i in range(700)]
    counts = {}
    for w in pool:
        counts[w] = counts.get(w, 0) + 1
    expected = sorted(counts, key=lambda w: (-counts[w], w))[:12]
    assert solution.top_k_frequent(pool, 12) == expected
    print("✓ Test 6 passed: Larger input")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_top_k_frequent()
