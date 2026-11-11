"""
EPI 5.2 - Increment an Arbitrary-Precision Integer

Problem:
A non-negative decimal integer D is stored as an array of digits, most
significant digit first. Update the array so that it represents D + 1 and
return it. The approach must not rely on converting the array to a
built-in integer, so that it would also work in a language with
fixed-width integers.

Constraints:
- 1 <= len(A) <= 10^5
- Each A[i] is in [0, 9]; no leading zeros unless the number is 0
- Must run in O(n) time

How it works (grade-school addition):
1. Add 1 to the last digit
2. Walk from the last digit toward the front: while a digit equals 10,
   set it to 0 and carry 1 into the digit before it
3. If the first digit becomes 10, set it to 1 and append a 0 (the result
   has one more digit, e.g. 99 + 1 = 100)

Example 1:
Input: A = [1, 2, 9]
Output: [1, 3, 0]
Explanation: 129 + 1 = 130.

Example 2:
Input: A = [9, 9]
Output: [1, 0, 0]
Explanation: 99 + 1 = 100 needs an extra digit.
"""

from typing import List


class Solution:
    def plus_one(self, A: List[int]) -> List[int]:
        """
        Increments the integer represented by a digit array.

        Args:
            A: Digits of a non-negative integer, most significant first

        Returns:
            The digit array of A + 1 (A itself, updated in place)

        Time Complexity: O(n)
        Space Complexity: O(1) beyond the possible extra digit
        """
        # TODO: Implement increment of a digit array
        pass


def test_plus_one():
    """Test cases for increment implementation"""
    solution = Solution()

    # Test case 1: Book example with a single carry
    assert solution.plus_one([1, 2, 9]) == [1, 3, 0]
    print("✓ Test 1 passed: [1, 2, 9] -> [1, 3, 0]")

    # Test case 2: No carry
    assert solution.plus_one([1, 2, 3]) == [1, 2, 4]
    print("✓ Test 2 passed: [1, 2, 3] -> [1, 2, 4]")

    # Test case 3: Carry produces an extra digit
    assert solution.plus_one([9, 9]) == [1, 0, 0]
    print("✓ Test 3 passed: [9, 9] -> [1, 0, 0]")

    # Test case 4: Zero
    assert solution.plus_one([0]) == [1]
    print("✓ Test 4 passed: [0] -> [1]")

    # Test case 5: Single nine
    assert solution.plus_one([9]) == [1, 0]
    print("✓ Test 5 passed: [9] -> [1, 0]")

    # Test case 6: Long run of nines in the middle, updated in place
    A = [4] + [9] * 30
    result = solution.plus_one(A)
    assert result == [5] + [0] * 30
    assert A == [5] + [0] * 30
    print("✓ Test 6 passed: 4 followed by thirty 9s (array updated in place)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_plus_one()
