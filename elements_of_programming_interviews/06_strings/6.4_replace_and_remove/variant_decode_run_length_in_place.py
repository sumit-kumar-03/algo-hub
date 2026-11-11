"""
EPI 6.4 Extra Variant - Decode Run-Length Encoding In Place
(Practice problem, not in the book. Difficulty: Hard)
Builds on: The two-pass in-place rewrite of replace and remove: a forward
pass for the parts that shrink and a backward pass for the parts that grow.

Problem:
The first size entries of a character array s hold a run-length encoded
string: a sequence of groups, each a positive decimal count (one or more
digit characters, no leading zeros) followed by a single letter. The group
"3a" stands for "aaa". Decode the string in place and return its decoded
length. Some groups shrink when decoded ("1a" -> "a") and others grow
("12x" -> twelve x's). The array is guaranteed to be long enough for the
decoded string.

Constraints:
- 0 <= size <= len(s), len(s) >= decoded length
- Letters are a-z or A-Z; counts are between 1 and 10^4
- O(n) time where n is size + decoded length, O(1) extra space

How it works:
1. Forward pass: read groups left to right with a write index that never
   passes the read index. Write a group decoded if that takes no more
   room than its encoding (count <= digits + 1); otherwise copy the group
   still encoded. Add up the counts to get the final length.
2. After the forward pass the prefix is a mix of decoded letters and
   still-encoded groups. A letter is part of an encoded group exactly
   when a digit comes right before it.
3. Backward pass: scan that prefix from its end while writing from the
   final length backward. A letter preceded by digits is expanded to its
   count; any other letter is copied once. The write index never falls
   behind the read index.

Example 1:
Input: size = 4, s = list("3a2b") + 1 spare slot
Output: 5, s[:5] == list("aaabb")

Example 2:
Input: size = 8, s = list("1a3b1c1d")
Output: 6, s[:6] == list("abbbcd")
Explanation: "1a" shrinks, "3b" grows, so both passes are needed
"""

from typing import List


class Solution:
    def decode_in_place(self, size: int, s: List[str]) -> int:
        """
        Decodes the run-length encoded prefix of s in place.

        Args:
            size: Number of leading entries of s holding the encoding
            s: Character array with room for the decoded string

        Returns:
            Length of the decoded string now stored at the front of s

        Time Complexity: O(size + decoded length)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place run-length decoding
        pass


def make_buffer(encoded: str, decoded_length: int) -> List[str]:
    """Builds an array holding encoded with room for the decoded result."""
    return list(encoded) + [""] * max(0, decoded_length - len(encoded))


def test_decode_in_place():
    """Test cases for in-place run-length decoding"""
    solution = Solution()

    # Test case 1: Every group grows
    s1 = make_buffer("3a2b", 5)
    n1 = solution.decode_in_place(4, s1)
    assert n1 == 5 and "".join(s1[:n1]) == "aaabb"
    print("✓ Test 1 passed: '3a2b' -> 'aaabb'")

    # Test case 2: Every group shrinks
    s2 = make_buffer("1a1b1c", 3)
    n2 = solution.decode_in_place(6, s2)
    assert n2 == 3 and "".join(s2[:n2]) == "abc"
    print("✓ Test 2 passed: '1a1b1c' -> 'abc'")

    # Test case 3: Shrinking groups before a growing one
    s3 = make_buffer("1a3b1c1d", 6)
    n3 = solution.decode_in_place(8, s3)
    assert n3 == 6 and "".join(s3[:n3]) == "abbbcd"
    print("✓ Test 3 passed: '1a3b1c1d' -> 'abbbcd'")

    # Test case 4: Empty input and a same-length group
    assert solution.decode_in_place(0, []) == 0
    s4 = make_buffer("2z", 2)
    n4 = solution.decode_in_place(2, s4)
    assert n4 == 2 and "".join(s4[:n4]) == "zz"
    print("✓ Test 4 passed: Empty input and '2z'")

    # Test case 5: Multi-digit counts mixed with shrinking groups
    encoded = "1a10b2c1d1E"
    expected = "a" + "b" * 10 + "cc" + "d" + "E"
    s5 = make_buffer(encoded, len(expected))
    n5 = solution.decode_in_place(len(encoded), s5)
    assert n5 == len(expected) and "".join(s5[:n5]) == expected
    print("✓ Test 5 passed: '1a10b2c1d1E' decoded")

    # Test case 6: Growing group first, then many shrinking ones
    encoded = "12x" + "1y" * 6
    expected = "x" * 12 + "y" * 6
    s6 = make_buffer(encoded, len(expected))
    n6 = solution.decode_in_place(len(encoded), s6)
    assert n6 == len(expected) and "".join(s6[:n6]) == expected
    print("✓ Test 6 passed: '12x' followed by six '1y' groups")

    # Test case 7: Entries past size are ignored
    s7 = list("2q9r") + [""] * 6
    n7 = solution.decode_in_place(2, s7)
    assert n7 == 2 and "".join(s7[:n7]) == "qq"
    print("✓ Test 7 passed: Only the first size entries are decoded")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_decode_in_place()
