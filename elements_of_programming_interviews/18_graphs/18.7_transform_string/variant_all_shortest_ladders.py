"""
EPI 18.7 Extra Variant - All Shortest Word Ladders
(Practice problem, not in the book. Difficulty: Hard)
Builds on: BFS over dictionary words, now keeping every BFS parent of a
word (not just the first) and backtracking through that DAG to list every
shortest production sequence.

Problem:
Given a dictionary D (a set of lowercase words, all the same length) and
two words s and t, return every shortest sequence of dictionary words that
starts at s, ends at t, and changes exactly one letter per step. Return
the sequences sorted in lexicographic order (compare them as lists of
words). If t cannot be produced from s, return [].

Constraints:
- 1 <= len(D) <= 5000, s is in D, all words lowercase and equal length
- Do not modify the caller's dictionary
- The output itself can be exponentially large; the search should still
  avoid exploring words that cannot lie on a shortest sequence
- Target: O(d * L * 26) for BFS plus O(total output size) to enumerate

How it works (layered BFS + DFS over the parent DAG):
1. BFS from s one whole layer at a time; record dist[word]
2. For a word w in the current layer and a neighbor v: if v is unseen,
   set dist[v] = dist[w] + 1; if dist[v] == dist[w] + 1, add w to
   parents[v] (a word can have several parents in the previous layer)
3. Stop after the layer that contains t
4. DFS backward from t through parents to s, building each path, then
   reverse each path and sort the results

Example 1:
Input: D = {"hit", "hot", "dot", "dog", "cog", "lot", "log"},
       s = "hit", t = "cog"
Output: [["hit", "hot", "dot", "dog", "cog"],
         ["hit", "hot", "lot", "log", "cog"]]

Example 2:
Input: D = {"hit", "hot", "dot", "dog", "lot", "log"}, s = "hit", t = "cog"
Output: []
Explanation: "cog" is not in the dictionary.
"""

from itertools import product
from typing import List, Set


class Solution:
    def all_shortest_ladders(
        self, dictionary: Set[str], s: str, t: str
    ) -> List[List[str]]:
        """
        Lists every shortest production sequence from s to t.

        Args:
            dictionary: Set of allowed words
            s: Start word (in the dictionary)
            t: Target word

        Returns:
            All shortest sequences, sorted lexicographically, or []

        Time Complexity: O(d * L * 26 + total output size)
        Space Complexity: O(d * L + total output size)
        """
        # TODO: Implement layered BFS with multiple parents, then backtrack
        pass


def test_all_shortest_ladders():
    """Test cases for listing all shortest word ladders"""
    solution = Solution()

    # Test case 1: Classic example with two shortest ladders
    words = {"hit", "hot", "dot", "dog", "cog", "lot", "log"}
    assert solution.all_shortest_ladders(set(words), "hit", "cog") == [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"],
    ]
    print("✓ Test 1 passed: Two shortest ladders")

    # Test case 2: Target missing or unreachable
    assert solution.all_shortest_ladders(words - {"cog"}, "hit", "cog") == []
    assert solution.all_shortest_ladders({"cat", "dog"}, "cat", "dog") == []
    print("✓ Test 2 passed: No ladder = []")

    # Test case 3: s == t
    assert solution.all_shortest_ladders(set(words), "hot", "hot") == [["hot"]]
    print("✓ Test 3 passed: s == t gives [[s]]")

    # Test case 4: Longer routes must be excluded
    d4 = {"aa", "ab", "bb", "ba", "ca", "cb"}
    assert solution.all_shortest_ladders(set(d4), "aa", "bb") == [
        ["aa", "ab", "bb"],
        ["aa", "ba", "bb"],
    ]
    print("✓ Test 4 passed: Only the 2-step ladders, not detours via c")

    # Test case 5: Every route through a 3-bit cube (3! = 6 ladders)
    cube = {"".join(bits) for bits in product("xy", repeat=3)}
    result = solution.all_shortest_ladders(set(cube), "xxx", "yyy")
    assert len(result) == 6
    assert result == sorted(result)
    assert all(len(p) == 4 and p[0] == "xxx" and p[-1] == "yyy" for p in result)
    assert len({tuple(p) for p in result}) == 6
    print("✓ Test 5 passed: 6 ladders across a 3-bit cube, sorted")

    # Test case 6: Count explodes with length, dictionary unchanged
    hyper = {"".join(bits) for bits in product("xy", repeat=5)}
    snapshot = set(hyper)
    result = solution.all_shortest_ladders(hyper, "xxxxx", "yyyyy")
    assert len(result) == 120  # 5! orders to flip the 5 letters
    assert hyper == snapshot
    print("✓ Test 6 passed: 120 ladders across a 5-bit cube, dictionary unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_all_shortest_ladders()
