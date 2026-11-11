"""
EPI 8.3 - Test a String Over "{,},(,),[,]" for Well-Formedness

Problem:
Given a string made only of the characters '(', ')', '[', ']', '{' and '}',
decide whether it is well-formed: every closing character must close the
most recent unmatched opening character of the same type, and no opening
character may be left unmatched at the end.

Constraints:
- 0 <= len(s) <= 10^4
- s contains only the six bracket characters
- O(n) time, O(n) space

How it works (stack of unmatched openers):
1. Scan left to right; push every opening character onto a stack
2. For a closing character, the stack must be non-empty and its top must
   be the matching opener; pop it, otherwise return False
3. After the scan, the string is well-formed only if the stack is empty

Example 1:
Input: "([]){()}"
Output: True

Example 2:
Input: "[()[]{()()"
Output: False
Explanation: The leading '[' and the '{' are never closed.
"""


class Solution:
    def is_well_formed(self, s: str) -> bool:
        """
        Checks whether a bracket string is well-formed.

        Args:
            s: String over the characters ()[]{}

        Returns:
            True if all brackets match in the correct order

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement well-formedness check
        pass


def test_is_well_formed():
    """Test cases for bracket well-formedness"""
    solution = Solution()

    # Test case 1: Empty string
    assert solution.is_well_formed("") is True
    print("✓ Test 1 passed: Empty string is well-formed")

    # Test case 2: Book examples that are well-formed
    assert solution.is_well_formed("([]){()}") is True
    assert solution.is_well_formed("[()[]{()()}]") is True
    print("✓ Test 2 passed: Nested and sequential brackets")

    # Test case 3: Mismatched types
    assert solution.is_well_formed("{)") is False
    assert solution.is_well_formed("([)]") is False
    print("✓ Test 3 passed: Mismatched bracket types")

    # Test case 4: Unclosed openers
    assert solution.is_well_formed("[()[]{()()") is False
    assert solution.is_well_formed("((") is False
    print("✓ Test 4 passed: Unclosed openers")

    # Test case 5: Closer with nothing to match
    assert solution.is_well_formed(")(") is False
    assert solution.is_well_formed("()]") is False
    print("✓ Test 5 passed: Unmatched closer")

    # Test case 6: Deep nesting
    assert solution.is_well_formed("{[({[()]})]}") is True
    print("✓ Test 6 passed: Deep nesting")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_well_formed()
