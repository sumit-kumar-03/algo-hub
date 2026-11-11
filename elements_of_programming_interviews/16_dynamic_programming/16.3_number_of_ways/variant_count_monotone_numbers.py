"""
EPI 16.3 Variant - Count Monotone Decimal Numbers

Problem:
A decimal number is a non-empty digit sequence whose first digit is not 0.
Call it monotone if each digit is less than or equal to the next one
(D[i] <= D[i + 1]). Given k, count the monotone decimal numbers that have
exactly k digits.

Constraints:
- 1 <= k <= 1000
- O(k * 10) time

How it works (DP on the last digit, a 2D-traversal in disguise):
1. ways[d] = number of monotone numbers of the current length ending in d
2. Length 1: ways[d] = 1 for d in 1..9 (no leading zero), ways[0] = 0
3. Next length: new_ways[d] = sum(ways[0..d])
4. Answer = sum(ways) after k digits
(Closed form: C(k + 8, 8), since every digit must be 1..9.)

Example 1:
Input: k = 1
Output: 9

Example 2:
Input: k = 2
Output: 45
Explanation: 11, 12, ..., 19, 22, ..., 99
"""


class Solution:
    def count_monotone_numbers(self, k: int) -> int:
        """
        Counts k-digit decimal numbers whose digits never decrease.

        Args:
            k: Number of digits

        Returns:
            Number of monotone k-digit numbers

        Time Complexity: O(k * 10)
        Space Complexity: O(10)
        """
        # TODO: Implement monotone number counting DP
        pass


def test_count_monotone_numbers():
    """Test cases for monotone number counting"""
    solution = Solution()

    # Test case 1: One digit
    assert solution.count_monotone_numbers(1) == 9
    print("✓ Test 1 passed: k=1 -> 9")

    # Test case 2: Two digits
    assert solution.count_monotone_numbers(2) == 45
    print("✓ Test 2 passed: k=2 -> 45")

    # Test case 3: Three digits
    assert solution.count_monotone_numbers(3) == 165
    print("✓ Test 3 passed: k=3 -> 165")

    # Test case 4: Four digits
    assert solution.count_monotone_numbers(4) == 495
    print("✓ Test 4 passed: k=4 -> 495")

    # Test case 5: Ten digits
    assert solution.count_monotone_numbers(10) == 43758
    print("✓ Test 5 passed: k=10 -> 43758")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_monotone_numbers()
