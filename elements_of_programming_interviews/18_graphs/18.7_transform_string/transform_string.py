"""
EPI 18.7 - Transform One String to Another

Problem:
Given a dictionary D (a set of lowercase strings) and two strings s and t,
s produces t if there is a sequence of dictionary words starting with s and
ending with t in which each word differs from the previous one in exactly
one character (same length). Return the number of one-character steps in a
shortest such sequence, or -1 if s does not produce t.

Constraints:
- 1 <= len(D) <= 10^4, all strings lowercase, s is in D
- Do not modify the caller's dictionary
- O(d * L * 26) time where d = len(D) and L = word length

How it works (BFS over words):
1. Treat words as vertices; edges join words that differ in one position
2. BFS from s with distance 0, using a copy of D as the unvisited set
3. For each popped word, try every position and every letter 'a'..'z';
   if the candidate is still in the unvisited set, remove it and enqueue it
   with distance + 1
4. Return the distance when t is popped, or -1 when the queue empties

Example 1:
Input: D = {"bat", "cot", "dog", "dag", "dot", "cat"}, s = "cat", t = "dog"
Output: 3
Explanation: cat -> cot -> dot -> dog

Example 2:
Input: D = {"cat", "dog"}, s = "cat", t = "dog"
Output: -1
"""

from typing import Set


class Solution:
    def transform_string(self, dictionary: Set[str], s: str, t: str) -> int:
        """
        Computes the fewest one-letter steps that turn s into t.

        Args:
            dictionary: Set of allowed words
            s: Start word (in the dictionary)
            t: Target word

        Returns:
            Number of steps in a shortest production sequence, or -1

        Time Complexity: O(d * L * 26)
        Space Complexity: O(d)
        """
        # TODO: Implement BFS word ladder
        pass


def test_transform_string():
    """Test cases for transforming one string to another"""
    solution = Solution()
    book = {"bat", "cot", "dog", "dag", "dot", "cat"}

    # Test case 1: Book example
    assert solution.transform_string(set(book), "cat", "dog") == 3
    print("✓ Test 1 passed: cat -> dog = 3")

    # Test case 2: One step
    assert solution.transform_string(set(book), "cat", "bat") == 1
    print("✓ Test 2 passed: cat -> bat = 1")

    # Test case 3: Same word
    assert solution.transform_string(set(book), "cat", "cat") == 0
    print("✓ Test 3 passed: cat -> cat = 0")

    # Test case 4: Not connected
    assert solution.transform_string({"cat", "dog"}, "cat", "dog") == -1
    print("✓ Test 4 passed: cat -> dog unreachable = -1")

    # Test case 5: Classic word ladder
    ladder = {"hit", "hot", "dot", "dog", "cog", "lot", "log"}
    assert solution.transform_string(set(ladder), "hit", "cog") == 4
    print("✓ Test 5 passed: hit -> cog = 4")

    # Test case 6: Dictionary is left unchanged
    d6 = {"cat", "cot", "cog", "dog", "dot", "bat", "bot"}
    snapshot = set(d6)
    assert solution.transform_string(d6, "bat", "dog") == 3
    assert d6 == snapshot
    print("✓ Test 6 passed: bat -> dog = 3, dictionary unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_transform_string()
