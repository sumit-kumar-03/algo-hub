"""
EPI 16.2 Variant - Check for an Interleaving of Two Strings

Problem:
A string t is an interleaving of s1 and s2 if you can build t by merging
the characters of s1 and s2 while keeping each string's own left-to-right
order. Given s1, s2, and t, return whether t is an interleaving of s1 and s2.

Constraints:
- 0 <= len(s1), len(s2) <= 1000
- O(len(s1) * len(s2)) time

How it works (DP over prefixes):
1. If len(s1) + len(s2) != len(t), return False
2. I[i][j] = True if t[:i+j] is an interleaving of s1[:i] and s2[:j]
3. I[0][0] = True
4. I[i][j] = (I[i-1][j] and s1[i-1] == t[i+j-1])
             or (I[i][j-1] and s2[j-1] == t[i+j-1])
5. Return I[len(s1)][len(s2)]

Example 1:
Input: s1 = "gtaa", s2 = "atc", t = "gattaca"
Output: True

Example 2:
Input: s1 = "gtaa", s2 = "atc", t = "gatacta"
Output: False
"""


class Solution:
    def is_interleaving(self, s1: str, s2: str, t: str) -> bool:
        """
        Checks whether t is an interleaving of s1 and s2.

        Args:
            s1: First source string
            s2: Second source string
            t: Candidate interleaving

        Returns:
            True if t interleaves s1 and s2, False otherwise

        Time Complexity: O(len(s1) * len(s2))
        Space Complexity: O(len(s1) * len(s2)) (O(len(s2)) with one row)
        """
        # TODO: Implement interleaving DP
        pass


def test_is_interleaving():
    """Test cases for string interleaving"""
    solution = Solution()

    # Test case 1: Book example (valid)
    assert solution.is_interleaving("gtaa", "atc", "gattaca") is True
    print("✓ Test 1 passed: gattaca interleaves gtaa/atc")

    # Test case 2: Book example (valid)
    assert solution.is_interleaving("gtaa", "atc", "gtataac") is True
    print("✓ Test 2 passed: gtataac interleaves gtaa/atc")

    # Test case 3: Book example (invalid)
    assert solution.is_interleaving("gtaa", "atc", "gatacta") is False
    print("✓ Test 3 passed: gatacta does not interleave gtaa/atc")

    # Test case 4: Length mismatch
    assert solution.is_interleaving("ab", "cd", "abc") is False
    print("✓ Test 4 passed: length mismatch -> False")

    # Test case 5: All empty
    assert solution.is_interleaving("", "", "") is True
    print("✓ Test 5 passed: empty strings -> True")

    # Test case 6: Needs backtracking over equal characters
    assert solution.is_interleaving("aabcc", "dbbca", "aadbbcbcac") is True
    print("✓ Test 6 passed: aadbbcbcac interleaves aabcc/dbbca")

    # Test case 7: Same characters, wrong order
    assert solution.is_interleaving("aabcc", "dbbca", "aadbbbaccc") is False
    print("✓ Test 7 passed: aadbbbaccc does not interleave aabcc/dbbca")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_interleaving()
