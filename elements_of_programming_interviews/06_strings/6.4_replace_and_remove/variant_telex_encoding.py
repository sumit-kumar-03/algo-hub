"""
EPI 6.4 Variant - Telex Encoding

Problem:
You are given an array of characters (letters, digits, blanks and
punctuation) and an integer size giving the number of meaningful entries.
Produce its telex encoding in place: letters, digits and blanks stay as
they are, while punctuation is spelled out, one character per array entry:
    '.' -> "DOT"
    ',' -> "COMMA"
    '?' -> "QUESTION MARK"
    '!' -> "EXCLAMATION MARK"
Return the number of valid entries in the result. The array is guaranteed
to have enough room for the encoded result.

Constraints:
- 0 <= size <= len(s)
- len(s) is large enough to hold the encoded result
- O(n) time, O(1) extra space (the replacement table is constant size)

How it works:
1. Forward pass: compute the final length by adding the length of each
   replacement (or 1 for an unchanged character)
2. Backward pass: walk from the last original character to the front,
   writing from the final end of the array backward; write the spelled-out
   word (last letter first) for punctuation and copy everything else
3. Return the final length

Example 1:
Input: size = 3, s = ['H', 'i', '!', ...spare slots]
Output: 18, s[:18] == list("HiEXCLAMATION MARK")

Example 2:
Input: size = 4, s = ['a', '.', 'b', ',', ...spare slots]
Output: 10, s[:10] == list("aDOTbCOMMA")
"""

from typing import List


class Solution:
    def telex_encode(self, size: int, s: List[str]) -> int:
        """
        Spells out punctuation in the first size entries of s, in place.

        Args:
            size: Number of leading entries of s to encode
            s: Character array with enough room for the result

        Returns:
            Number of valid entries in s after encoding

        Time Complexity: O(n) where n is the length of the result
        Space Complexity: O(1)
        """
        # TODO: Implement in-place telex encoding
        pass


def make_buffer(text: str, extra: int) -> List[str]:
    """Builds a character array holding text followed by extra empty slots."""
    return list(text) + [""] * extra


def test_telex_encode():
    """Test cases for telex encoding"""
    solution = Solution()

    # Test case 1: Exclamation mark at the end
    s1 = make_buffer("Hi!", 15)
    n1 = solution.telex_encode(3, s1)
    assert n1 == 18 and "".join(s1[:n1]) == "HiEXCLAMATION MARK"
    print("✓ Test 1 passed: 'Hi!' -> 'HiEXCLAMATION MARK'")

    # Test case 2: Dot and comma
    s2 = make_buffer("a.b,", 6)
    n2 = solution.telex_encode(4, s2)
    assert n2 == 10 and "".join(s2[:n2]) == "aDOTbCOMMA"
    print("✓ Test 2 passed: 'a.b,' -> 'aDOTbCOMMA'")

    # Test case 3: No punctuation
    s3 = make_buffer("abc 123", 0)
    n3 = solution.telex_encode(7, s3)
    assert n3 == 7 and "".join(s3[:n3]) == "abc 123"
    print("✓ Test 3 passed: No punctuation, unchanged")

    # Test case 4: Empty input
    s4: List[str] = []
    assert solution.telex_encode(0, s4) == 0
    print("✓ Test 4 passed: Empty input")

    # Test case 5: Only punctuation
    s5 = make_buffer("?.", 14)
    n5 = solution.telex_encode(2, s5)
    assert n5 == 16 and "".join(s5[:n5]) == "QUESTION MARKDOT"
    print("✓ Test 5 passed: '?.' -> 'QUESTION MARKDOT'")

    # Test case 6: Mixed sentence with blanks
    text = "Yes, go now!"
    expected = "YesCOMMA go nowEXCLAMATION MARK"
    s6 = make_buffer(text, len(expected) - len(text))
    n6 = solution.telex_encode(len(text), s6)
    assert n6 == len(expected) and "".join(s6[:n6]) == expected
    print("✓ Test 6 passed: Mixed sentence encoded")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_telex_encode()
