"""
EPI 15.1 Extra Variant - Scrambled Strings
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Hanoi's recursive decomposition into smaller subproblems of the
same shape, here with a choice at each split (swap or keep) and memoization.

Problem:
A string s can be scrambled as follows. If len(s) == 1, it stays as is.
Otherwise, cut s into two nonempty pieces x and y (s = x + y) at any
position, then either keep the order (x + y) or swap it (y + x), and
scramble each piece again in the same way, independently. Given two strings
a and b of equal length, return whether b can be obtained by scrambling a.

Constraints:
- 1 <= len(a) == len(b) <= 30
- Lowercase English letters only
- O(n^4) time with memoization, where n = len(a)

How it works (recursion over matching splits, memoized):
1. If a == b, return True; if the letter counts differ, return False
2. For each cut length i from 1 to n - 1:
   - no swap: a[:i] scrambles to b[:i] and a[i:] scrambles to b[i:]
   - swap:    a[:i] scrambles to b[n-i:] and a[i:] scrambles to b[:n-i]
   If either works, return True
3. Return False
Memoize on the (a, b) pair (or on start indices and length).

Example 1:
Input: a = "great", b = "rgeat"
Output: True
Explanation: Cut "great" into "gr" + "eat", swap "gr" into "rg", and keep
"eat" as is.

Example 2:
Input: a = "abcde", b = "caebd"
Output: False
"""


class Solution:
    def is_scramble(self, a: str, b: str) -> bool:
        """
        Checks whether b can be obtained by scrambling a.

        Args:
            a: Original string
            b: Candidate scrambled string (same length as a)

        Returns:
            True if b is a scramble of a, False otherwise

        Time Complexity: O(n^4) with memoization
        Space Complexity: O(n^3) memo entries
        """
        # TODO: Implement memoized recursion over all cut positions
        pass


def all_scrambles(s: str) -> set:
    """Enumerates every scramble of a short string (brute force)."""
    if len(s) <= 1:
        return {s}
    result = set()
    for i in range(1, len(s)):
        lefts, rights = all_scrambles(s[:i]), all_scrambles(s[i:])
        for x in lefts:
            for y in rights:
                result.add(x + y)
                result.add(y + x)
    return result


def test_is_scramble():
    """Test cases for scrambled strings"""
    solution = Solution()

    # Test case 1: Single characters
    assert solution.is_scramble("a", "a") is True
    assert solution.is_scramble("a", "b") is False
    print("✓ Test 1 passed: single characters")

    # Test case 2: Examples from the statement
    assert solution.is_scramble("great", "rgeat") is True
    assert solution.is_scramble("abcde", "caebd") is False
    print("✓ Test 2 passed: great/rgeat -> True, abcde/caebd -> False")

    # Test case 3: Same letters, but not reachable by scrambling
    assert solution.is_scramble("abcd", "bdac") is False
    print("✓ Test 3 passed: abcd/bdac -> False")

    # Test case 4: Duplicated letters
    assert solution.is_scramble("aabb", "abab") is True
    assert solution.is_scramble("abb", "bba") is True
    print("✓ Test 4 passed: duplicated letters")

    # Test case 5: Every permutation of a 5-letter string vs brute force
    from itertools import permutations
    reachable = all_scrambles("abcde")
    for p in permutations("abcde"):
        b = "".join(p)
        assert solution.is_scramble("abcde", b) is (b in reachable)
    print(f"✓ Test 5 passed: {len(reachable)} of 120 permutations reachable")

    # Test case 6: Longer strings (needs memoization)
    assert solution.is_scramble("abcdbdacbdac", "bdacabcdbdac") is True
    a6 = "abcdefghijklmnopqrstuvwxyzabcd"
    assert solution.is_scramble(a6, a6[::-1]) is True
    print("✓ Test 6 passed: long reachable scrambles")

    # Test case 7: Long and unreachable
    assert solution.is_scramble(
        "eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"
    ) is False
    print("✓ Test 7 passed: long unreachable scramble")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_scramble()
