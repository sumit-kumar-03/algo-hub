"""
EPI 15.1 Extra Variant - Every Result of Parenthesizing an Expression
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Hanoi's "split the problem around one pivot step and solve the
two sides recursively" (here the pivot is the last operator applied).

Problem:
You are given an arithmetic expression made of nonnegative integers and
the binary operators '+', '-', and '*', with no spaces and no parentheses.
Every way of fully parenthesizing the expression may give a different
value. Return the values of all full parenthesizations, one value per
parenthesization (so a value appears as many times as it is produced),
sorted in nondecreasing order.

Constraints:
- 1 <= len(expression) <= 30
- Numbers have no sign and may have several digits
- The expression has at most 10 operators
- The output has Catalan(number of operators) values

How it works (divide at each operator):
1. If the expression is a plain number, return [that number]
2. Otherwise, for each operator position i, treat that operator as the one
   applied last: recursively get all values of the left part and of the
   right part, and combine every left value with every right value
3. Collect everything and sort
Tip: memoize on (start, end) to avoid solving the same piece many times.

Example 1:
Input: expression = "2-1-1"
Output: [0, 2]
Explanation: ((2-1)-1) = 0 and (2-(1-1)) = 2.

Example 2:
Input: expression = "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: (2*(3-(4*5))) = -34, ((2*3)-(4*5)) = -14,
((2*(3-4))*5) = -10, (2*((3-4)*5)) = -10, (((2*3)-4)*5) = 10.
"""

from typing import List


class Solution:
    def all_results(self, expression: str) -> List[int]:
        """
        Computes the value of every full parenthesization of expression.

        Args:
            expression: Digits and '+', '-', '*' only

        Returns:
            Sorted list with one value per parenthesization

        Time Complexity: O(Catalan(m) * m) for m operators (output-bound)
        Space Complexity: O(Catalan(m)) for the results, plus memoization
        """
        # TODO: Implement divide at each operator, recurse on both sides
        pass


def test_all_results():
    """Test cases for all parenthesization results"""
    solution = Solution()

    # Test case 1: A single number
    assert solution.all_results("7") == [7]
    print("✓ Test 1 passed: '7' -> [7]")

    # Test case 2: Example 1
    assert solution.all_results("2-1-1") == [0, 2]
    print("✓ Test 2 passed: '2-1-1' -> [0, 2]")

    # Test case 3: Example 2 (duplicates kept)
    assert solution.all_results("2*3-4*5") == [-34, -14, -10, -10, 10]
    print("✓ Test 3 passed: '2*3-4*5' -> [-34, -14, -10, -10, 10]")

    # Test case 4: Multi-digit numbers
    assert solution.all_results("10*10-1") == [90, 99]
    print("✓ Test 4 passed: '10*10-1' -> [90, 99]")

    # Test case 5: Only additions, so all 14 values agree
    assert solution.all_results("1+2+3+4+5") == [15] * 14
    print("✓ Test 5 passed: '1+2+3+4+5' -> fourteen 15s")

    # Test case 6: Zeros and subtraction
    assert solution.all_results("0-0*5") == [0, 0]
    print("✓ Test 6 passed: '0-0*5' -> [0, 0]")

    # Test case 7: Ten operators give Catalan(10) = 16796 values
    r7 = solution.all_results("1-2+3*4-5+6*7-8+9*1-2")
    assert len(r7) == 16796 and r7 == sorted(r7)
    assert min(r7) == -781 and max(r7) == 1301
    print("✓ Test 7 passed: ten operators -> 16796 sorted values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_all_results()
