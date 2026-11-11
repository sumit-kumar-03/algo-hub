"""
EPI 8.2 Variant - Evaluate Polish Notation Expressions

Problem:
Same as evaluating RPN, but the operator comes first: a compound expression
has the form "o,A,B" instead of "A,B,o", where A and B are Polish notation
expressions and o is one of +, -, *, /. Tokens are separated by commas.
Return the integer the expression evaluates to.

Constraints:
- The expression is valid and non-empty
- A token like "-2" is a negative number; a lone "-" is the operator
- Division truncates toward zero
- O(n) time, O(n) space

How it works (scan right to left with a stack):
1. Split the string on commas and scan the tokens from right to left
2. A number is pushed onto the stack
3. An operator pops A (top) and then B, computes A o B, and pushes it
4. When the scan ends, the stack holds exactly the answer

Example 1:
Input: "+,*,+,3,4,2,1"
Output: 15
Explanation: The infix form is (3 + 4) * 2 + 1.

Example 2:
Input: "-,10,/,9,3"
Output: 7
Explanation: 10 - (9 / 3) = 7.
"""


class Solution:
    def evaluate_polish(self, expression: str) -> int:
        """
        Evaluates a comma-separated Polish (prefix) notation expression.

        Args:
            expression: Tokens separated by commas, e.g. "+,3,4"

        Returns:
            The integer value of the expression

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement Polish notation evaluation
        pass


def test_evaluate_polish():
    """Test cases for Polish notation evaluation"""
    solution = Solution()

    # Test case 1: Single number
    assert solution.evaluate_polish("1729") == 1729
    print("✓ Test 1 passed: Single number")

    # Test case 2: (3 + 4) * 2 + 1
    assert solution.evaluate_polish("+,*,+,3,4,2,1") == 15
    print("✓ Test 2 passed: Mixed addition and multiplication")

    # Test case 3: Operand order for subtraction and division
    assert solution.evaluate_polish("-,10,/,9,3") == 7
    assert solution.evaluate_polish("-,3,10") == -7
    print("✓ Test 3 passed: Operand order")

    # Test case 4: Negative numbers vs. minus operator
    assert solution.evaluate_polish("*,+,1,1,-2") == -4
    print("✓ Test 4 passed: Negative operand")

    # Test case 5: Division truncates toward zero
    assert solution.evaluate_polish("/,/,-641,6,28") == -3
    print("✓ Test 5 passed: Division truncates toward zero")

    # Test case 6: Right-nested expression 2 * (3 + (4 - 1))
    assert solution.evaluate_polish("*,2,+,3,-,4,1") == 12
    print("✓ Test 6 passed: Right-nested expression")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_evaluate_polish()
