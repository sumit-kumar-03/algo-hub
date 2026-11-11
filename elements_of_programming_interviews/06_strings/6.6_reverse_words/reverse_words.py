"""
EPI 6.6 - Reverse All the Words in a Sentence

Problem:
Given a sentence stored as an array of characters, with words separated by
blanks, rearrange it in place so the words appear in reverse order. The
letters inside each word keep their original order. Blanks are preserved:
the result is the mirror image of the input at the word level, so a blank
at position i ends up at position n - 1 - i.

Constraints:
- 0 <= len(s) <= 10^5
- Words are separated by ' ' characters
- O(n) time, O(1) extra space (modify s in place)

How it works:
1. Reverse the whole array; the words are now in the right order, but
   each word is spelled backward
2. Scan the array, find each maximal run of non-blank characters, and
   reverse that run in place

Example 1:
Input: s = list("Alice likes Bob")
Output: s == list("Bob likes Alice")

Example 2:
Input: s = list("ram is costly")
Output: s == list("costly is ram")
Explanation: Reversing everything gives "yltsoc si mar"; reversing each
word then gives "costly is ram"
"""

from typing import List


class Solution:
    def reverse_words(self, s: List[str]) -> None:
        """
        Reverses the order of words in s, in place.

        Args:
            s: Sentence as a list of single characters

        Returns:
            None; s is modified in place

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place word reversal
        pass


def run(solution: Solution, text: str) -> str:
    """Applies reverse_words to text and returns the resulting string."""
    chars = list(text)
    solution.reverse_words(chars)
    return "".join(chars)


def test_reverse_words():
    """Test cases for reversing words in a sentence"""
    solution = Solution()

    # Test case 1: Book example
    assert run(solution, "Alice likes Bob") == "Bob likes Alice"
    print("✓ Test 1 passed: 'Alice likes Bob' -> 'Bob likes Alice'")

    # Test case 2: Second book example
    assert run(solution, "ram is costly") == "costly is ram"
    print("✓ Test 2 passed: 'ram is costly' -> 'costly is ram'")

    # Test case 3: Single word
    assert run(solution, "hello") == "hello"
    print("✓ Test 3 passed: Single word unchanged")

    # Test case 4: Empty string
    assert run(solution, "") == ""
    print("✓ Test 4 passed: Empty string")

    # Test case 5: Single-character words
    assert run(solution, "a b c d") == "d c b a"
    print("✓ Test 5 passed: 'a b c d' -> 'd c b a'")

    # Test case 6: Blanks are mirrored, not collapsed
    assert run(solution, " leading") == "leading "
    assert run(solution, "ab  cde") == "cde  ab"
    print("✓ Test 6 passed: Extra blanks are preserved")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_words()
