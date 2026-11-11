"""
EPI 7.3 Extra Variant - Happy Numbers
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Fast and slow pointers detecting a cycle in a sequence where
each element determines the next.

Problem:
Start from a positive integer n and repeatedly replace it by the sum of
the squares of its decimal digits. The sequence either reaches 1 (and
stays there) or loops forever through a cycle that does not contain 1.
Call n happy if the sequence reaches 1. Decide whether n is happy using
O(1) extra space (no set of seen values).

Constraints:
- 1 <= n <= 2^31 - 1
- O(log n) time per step, O(1) extra space

How it works:
1. Treat next(x) = sum of the squared digits of x as a "next pointer"
2. Advance slow by one step and fast by two steps until they are equal
3. Every sequence ends in a cycle (1 -> 1 is a cycle of length one), so
   they always meet
4. n is happy exactly when the meeting value is 1

Example 1:
Input: n = 19
Output: True
Explanation: 19 -> 82 -> 68 -> 100 -> 1

Example 2:
Input: n = 2
Output: False
Explanation: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ...
"""


class Solution:
    def is_happy(self, n: int) -> bool:
        """
        Checks whether n is a happy number.

        Args:
            n: Positive integer

        Returns:
            True if the squared-digit-sum sequence from n reaches 1

        Time Complexity: O(log n) per step; the number of steps is small
        Space Complexity: O(1)
        """
        # TODO: Implement happy number check with fast and slow pointers
        pass


def test_is_happy():
    """Test cases for happy numbers"""
    solution = Solution()

    # Test case 1: Classic happy number
    assert solution.is_happy(19) is True
    print("✓ Test 1 passed: 19 is happy")

    # Test case 2: Classic unhappy number
    assert solution.is_happy(2) is False
    print("✓ Test 2 passed: 2 is not happy")

    # Test case 3: 1 is happy, 4 lies on the unhappy cycle
    assert solution.is_happy(1) is True
    assert solution.is_happy(4) is False
    print("✓ Test 3 passed: 1 and 4")

    # Test case 4: Powers of ten reach 1 in one step
    assert solution.is_happy(100) is True
    assert solution.is_happy(10**9) is True
    print("✓ Test 4 passed: Powers of ten")

    # Test case 5: Mixed values
    assert solution.is_happy(7) is True
    assert solution.is_happy(116) is False
    assert solution.is_happy(2**31 - 1) is False
    print("✓ Test 5 passed: 7, 116 and 2^31 - 1")

    # Test case 6: The happy numbers below 50
    happy = [n for n in range(1, 50) if solution.is_happy(n)]
    assert happy == [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
    print("✓ Test 6 passed: Happy numbers below 50")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_happy()
