"""
EPI 6.4 Extra Variant - Encode Spaces In Place
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Count first to find the final length, then fill the array from
the back so nothing is overwritten before it is read.

Problem:
You are given a character array s and an integer size. The first size
entries hold a piece of text; the rest of the array is spare room. Replace
every blank ' ' in the text with the three characters '%', '2', '0', in
place, and return the length of the result. The array is guaranteed to be
long enough.

Constraints:
- 0 <= size <= len(s)
- len(s) is large enough to hold the result
- O(n) time, O(1) extra space

How it works:
1. Count the blanks among the first size entries; the final length is
   size + 2 * blanks
2. Walk the text from its last character to its first while writing from
   the final end of the array backward
3. Write "%20" (last character first) for a blank and copy everything
   else; the write index never passes the read index, so no unread
   character is overwritten

Example 1:
Input: size = 13, s = list("Mr John Smith") + 4 spare slots
Output: 17, s[:17] == list("Mr%20John%20Smith")

Example 2:
Input: size = 2, s = [' ', ' ', '', '', '', '']
Output: 6, s == list("%20%20")
"""

from typing import List


class Solution:
    def encode_spaces(self, size: int, s: List[str]) -> int:
        """
        Replaces each blank in the first size entries of s with "%20".

        Args:
            size: Number of leading entries of s that hold the text
            s: Character array with enough room for the result

        Returns:
            Number of valid entries in s after encoding

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place space encoding
        pass


def make_buffer(text: str, extra: int) -> List[str]:
    """Builds a character array holding text followed by extra empty slots."""
    return list(text) + [""] * extra


def test_encode_spaces():
    """Test cases for encoding spaces in place"""
    solution = Solution()

    # Test case 1: Classic example
    s1 = make_buffer("Mr John Smith", 4)
    n1 = solution.encode_spaces(13, s1)
    assert n1 == 17 and "".join(s1[:n1]) == "Mr%20John%20Smith"
    print("✓ Test 1 passed: 'Mr John Smith' -> 'Mr%20John%20Smith'")

    # Test case 2: Only blanks
    s2 = make_buffer("  ", 4)
    n2 = solution.encode_spaces(2, s2)
    assert n2 == 6 and "".join(s2) == "%20%20"
    print("✓ Test 2 passed: Two blanks -> '%20%20'")

    # Test case 3: Empty input
    s3: List[str] = []
    assert solution.encode_spaces(0, s3) == 0
    print("✓ Test 3 passed: Empty input")

    # Test case 4: No blanks, unchanged
    s4 = make_buffer("abc", 0)
    n4 = solution.encode_spaces(3, s4)
    assert n4 == 3 and s4 == ["a", "b", "c"]
    print("✓ Test 4 passed: No blanks")

    # Test case 5: Leading, trailing and consecutive blanks
    s5 = make_buffer(" a  b ", 8)
    n5 = solution.encode_spaces(6, s5)
    assert n5 == 14 and "".join(s5[:n5]) == "%20a%20%20b%20"
    print("✓ Test 5 passed: Leading, trailing and repeated blanks")

    # Test case 6: Entries past size are ignored
    s6 = make_buffer("a b c", 2)
    n6 = solution.encode_spaces(3, s6)
    assert n6 == 5 and "".join(s6[:n6]) == "a%20b"
    print("✓ Test 6 passed: Only the first size entries are processed")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_encode_spaces()
