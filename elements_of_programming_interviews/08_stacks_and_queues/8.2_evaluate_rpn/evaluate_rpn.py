"""
EPI 8.2 - Evaluate RPN Expressions

Problem:
An expression in Reverse Polish notation (RPN) is either an integer (an
optional "-" followed by one or more digits) or has the form "A,B,o", where
A and B are themselves RPN expressions and o is an operator among +, -, *,
and /. Tokens are separated by commas. Given an RPN expression, return the
integer it evaluates to.

Constraints:
- The expression is valid and non-empty
- Division truncates toward zero (e.g., -7 / 2 == -3)
- O(n) time where n is the length of the string, O(n) space

How it works (stack of partial results):
1. Split the string on commas and scan the tokens left to right
2. A number is pushed onto the stack
3. An operator pops the top two values (B on top, then A), computes A o B,
   and pushes the result
4. When the scan ends, the only value left on the stack is the answer

Example 1:
Input: "3,4,+,2,*,1,+"
Output: 15
Explanation: The infix form is (3 + 4) * 2 + 1.

Example 2:
Input: "-641,6,/,28,/"
Output: -3
Explanation: -641 / 6 truncates to -106, and -106 / 28 truncates to -3.
"""


class Solution:
    def evaluate(self, rpn_expression: str) -> int:
        """
        Evaluates a comma-separated RPN expression.

        Args:
            rpn_expression: Tokens separated by commas, e.g. "3,4,+"

        Returns:
            The integer value of the expression

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement RPN evaluation
        pass


def test_evaluate():
    """Test cases for RPN evaluation"""
    solution = Solution()

    # Test case 1: Single number
    assert solution.evaluate("1729") == 1729
    print("✓ Test 1 passed: Single number")

    # Test case 2: Book example (3 + 4) * 2 + 1
    assert solution.evaluate("3,4,+,2,*,1,+") == 15
    print("✓ Test 2 passed: Mixed addition and multiplication")

    # Test case 3: Negative operand
    assert solution.evaluate("1,1,+,-2,*") == -4
    print("✓ Test 3 passed: Negative operand")

    # Test case 4: Division truncates toward zero
    assert solution.evaluate("-641,6,/,28,/") == -3
    print("✓ Test 4 passed: Division truncates toward zero")

    # Test case 5: Subtraction order matters
    assert solution.evaluate("10,3,-") == 7
    assert solution.evaluate("3,10,-") == -7
    print("✓ Test 5 passed: Operand order for subtraction")

    # Test case 6: Nested expression 5 - (8 / (1 + 3))
    assert solution.evaluate("5,8,1,3,+,/,-") == 3
    print("✓ Test 6 passed: Nested expression")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_evaluate()
