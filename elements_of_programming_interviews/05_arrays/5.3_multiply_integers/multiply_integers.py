"""
EPI 5.3 - Multiply Two Arbitrary-Precision Integers

Problem:
Integers are stored as arrays of decimal digits, most significant digit
first. A negative number is marked by making its leading digit negative,
e.g. [-7, 6, 1] represents -761. Given two such arrays, return the array
that represents their product. Do not convert the arrays to built-in
integers.

Constraints:
- 1 <= len(num1), len(num2) <= 10^3
- No leading zeros except for the number 0, which is [0]
- The product of zero is [0] (never [-0] or with leading zeros)
- Aim for O(n * m) time

How it works (grade-school multiplication):
1. Determine the sign from the two leading digits, then make both
   leading digits non-negative
2. Allocate result with len(num1) + len(num2) zeros
3. For i from the right of num1, for j from the right of num2:
   - result[i + j + 1] += num1[i] * num2[j]
   - result[i + j] += result[i + j + 1] // 10
   - result[i + j + 1] %= 10
4. Strip leading zeros (keep at least one digit) and apply the sign to
   the first digit

Example 1:
Input: num1 = [1, 9, 3, 7, 0, 7, 7, 2, 1],
       num2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
Output: [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
Explanation: 193707721 * -761838257287 = -147573952589676412927.

Example 2:
Input: num1 = [9, 9], num2 = [9, 9]
Output: [9, 8, 0, 1]
Explanation: 99 * 99 = 9801.
"""

from typing import List


class Solution:
    def multiply(self, num1: List[int], num2: List[int]) -> List[int]:
        """
        Multiplies two integers stored as digit arrays.

        Args:
            num1: Digits of the first integer (negative leading digit = negative)
            num2: Digits of the second integer

        Returns:
            Digit array of num1 * num2, in the same format

        Time Complexity: O(n * m)
        Space Complexity: O(n + m) for the result
        """
        # TODO: Implement grade-school multiplication
        pass


def test_multiply():
    """Test cases for digit-array multiplication"""
    solution = Solution()

    # Test case 1: Book example (positive times negative)
    num1 = [1, 9, 3, 7, 0, 7, 7, 2, 1]
    num2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
    expected = [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
    assert solution.multiply(num1, num2) == expected
    print("✓ Test 1 passed: 193707721 * -761838257287")

    # Test case 2: Carries everywhere
    assert solution.multiply([9, 9], [9, 9]) == [9, 8, 0, 1]
    print("✓ Test 2 passed: 99 * 99 == 9801")

    # Test case 3: Multiplying by zero (no negative zero, no leading zeros)
    assert solution.multiply([0], [1, 2, 3]) == [0]
    assert solution.multiply([-4, 5], [0]) == [0]
    print("✓ Test 3 passed: Anything times 0 == [0]")

    # Test case 4: Two negatives give a positive
    assert solution.multiply([-1, 2], [-3]) == [3, 6]
    print("✓ Test 4 passed: -12 * -3 == 36")

    # Test case 5: Single digits
    assert solution.multiply([7], [8]) == [5, 6]
    assert solution.multiply([-1], [1]) == [-1]
    print("✓ Test 5 passed: 7 * 8 == 56, -1 * 1 == -1")

    # Test case 6: Powers of ten
    assert solution.multiply([1, 0, 0], [1, 0, 0, 0]) == [1, 0, 0, 0, 0, 0]
    print("✓ Test 6 passed: 100 * 1000 == 100000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_multiply()
