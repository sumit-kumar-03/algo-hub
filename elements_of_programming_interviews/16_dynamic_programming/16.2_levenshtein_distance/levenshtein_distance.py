"""
EPI 16.2 - Compute the Levenshtein Distance

Problem:
The Levenshtein (edit) distance between two strings is the fewest
single-character edits needed to turn the first string into the second,
where an edit is inserting, deleting, or substituting one character.
Given two strings, return their Levenshtein distance.

Constraints:
- 0 <= len(a), len(b) <= 1000
- Comparison is case-sensitive
- O(len(a) * len(b)) time

How it works (DP over prefixes):
1. E[i][j] = distance between a[:i] and b[:j]
2. E[i][0] = i, E[0][j] = j (delete or insert everything)
3. If a[i-1] == b[j-1]: E[i][j] = E[i-1][j-1]
   Otherwise: E[i][j] = 1 + min(E[i-1][j-1]  (substitute),
                                E[i-1][j]    (delete from a),
                                E[i][j-1])   (insert into a)
4. Return E[len(a)][len(b)]

Example 1:
Input: a = "Saturday", b = "Sundays"
Output: 4
Explanation: Delete 'a' and 't', substitute 'r' with 'n', insert a trailing 's'.

Example 2:
Input: a = "Carthorse", b = "Orchestra"
Output: 8
"""


class Solution:
    def levenshtein_distance(self, a: str, b: str) -> int:
        """
        Computes the minimum number of edits that turn a into b.

        Args:
            a: Source string
            b: Target string

        Returns:
            The Levenshtein distance between a and b

        Time Complexity: O(len(a) * len(b))
        Space Complexity: O(len(a) * len(b)) (O(min(len(a), len(b))) with two rows)
        """
        # TODO: Implement Levenshtein distance DP
        pass


def test_levenshtein_distance():
    """Test cases for Levenshtein distance"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.levenshtein_distance("Saturday", "Sundays") == 4
    print("✓ Test 1 passed: Saturday -> Sundays = 4")

    # Test case 2: Book figure example (case-sensitive)
    assert solution.levenshtein_distance("Carthorse", "Orchestra") == 8
    print("✓ Test 2 passed: Carthorse -> Orchestra = 8")

    # Test case 3: Classic example
    assert solution.levenshtein_distance("kitten", "sitting") == 3
    print("✓ Test 3 passed: kitten -> sitting = 3")

    # Test case 4: Empty source means inserting everything
    assert solution.levenshtein_distance("", "abc") == 3
    print("✓ Test 4 passed: '' -> abc = 3")

    # Test case 5: Empty target means deleting everything
    assert solution.levenshtein_distance("abc", "") == 3
    print("✓ Test 5 passed: abc -> '' = 3")

    # Test case 6: Identical strings
    assert solution.levenshtein_distance("same", "same") == 0
    print("✓ Test 6 passed: identical strings = 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_levenshtein_distance()
