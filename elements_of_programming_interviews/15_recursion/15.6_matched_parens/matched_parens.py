"""
EPI 15.6 - Generate Strings of Matched Parens

Problem:
Given a number k, return every string made of k "(" characters and k ")"
characters in which the parens are matched (balanced). Each string must
appear exactly once; the order of the strings does not matter.

Constraints:
- 0 <= k <= 10
- The number of results is the k-th Catalan number: 1, 1, 2, 5, 14, 42, ...
- Don't enumerate all 2^(2k) strings and filter them

How it works (build only valid prefixes):
1. Track how many "(" and ")" are still needed (both start at k)
2. You may add "(" whenever some are still needed
3. You may add ")" only when fewer "(" than ")" remain, i.e. there is an
   unmatched "(" in the prefix
4. When nothing remains to add, record the string

Example 1:
Input: k = 2
Output: ["(())", "()()"]  (any order)

Example 2:
Input: k = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]  (any order)
"""

from typing import List


class Solution:
    def generate_balanced_parentheses(self, num_pairs: int) -> List[str]:
        """
        Generates all strings with num_pairs matched pairs of parens.

        Args:
            num_pairs: Number of "(" / ")" pairs

        Returns:
            List of all balanced strings, in any order

        Time Complexity: O(k * C(k)) where C(k) is the k-th Catalan number
        Space Complexity: O(k) recursion depth, excluding the output
        """
        # TODO: Implement directed generation of balanced strings
        pass


def is_balanced(s: str) -> bool:
    """True if every prefix has at least as many '(' as ')' and totals match."""
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
        else:
            return False
    return depth == 0


def test_generate_balanced_parentheses():
    """Test cases for matched parens generation"""
    solution = Solution()

    # Test case 1: Zero pairs -> just the empty string
    assert solution.generate_balanced_parentheses(0) == [""]
    print('✓ Test 1 passed: k=0 -> [""]')

    # Test case 2: One pair
    assert solution.generate_balanced_parentheses(1) == ["()"]
    print('✓ Test 2 passed: k=1 -> ["()"]')

    # Test case 3: Book example, two pairs
    assert sorted(solution.generate_balanced_parentheses(2)) == ["(())", "()()"]
    print('✓ Test 3 passed: k=2 -> ["(())", "()()"]')

    # Test case 4: Book example, three pairs
    expected4 = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert sorted(solution.generate_balanced_parentheses(3)) == expected4
    print("✓ Test 4 passed: k=3 -> 5 strings")

    # Test case 5: Catalan counts, all distinct, all balanced, right length
    catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    for k in range(4, 10):
        result = solution.generate_balanced_parentheses(k)
        assert len(result) == len(set(result)) == catalan[k]
        assert all(len(s) == 2 * k and is_balanced(s) for s in result)
    print("✓ Test 5 passed: k=4..9 match Catalan numbers, all valid and distinct")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_generate_balanced_parentheses()
