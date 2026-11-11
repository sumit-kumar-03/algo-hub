"""
EPI 16.3 Variant - Count Strictly Monotone Decimal Numbers

Problem:
A decimal number is a non-empty digit sequence whose first digit is not 0.
Call it strictly monotone if each digit is strictly less than the next one
(D[i] < D[i + 1]). Given k, count the strictly monotone decimal numbers that
have exactly k digits.

Constraints:
- 1 <= k <= 1000 (the answer is 0 once k > 9)
- O(k * 10) time

How it works (DP on the last digit):
1. ways[d] = number of strictly monotone numbers of the current length
   ending in digit d
2. Length 1: ways[d] = 1 for d in 1..9, ways[0] = 0
3. Next length: new_ways[d] = sum(ways[0..d-1])
4. Answer = sum(ways) after k digits
(Closed form: C(9, k), choosing k distinct digits from 1..9.)

Example 1:
Input: k = 2
Output: 36
Explanation: 12, 13, ..., 89

Example 2:
Input: k = 10
Output: 0
Explanation: Only nine nonzero digits exist.
"""


class Solution:
    def count_strictly_monotone_numbers(self, k: int) -> int:
        """
        Counts k-digit decimal numbers whose digits strictly increase.

        Args:
            k: Number of digits

        Returns:
            Number of strictly monotone k-digit numbers

        Time Complexity: O(k * 10)
        Space Complexity: O(10)
        """
        # TODO: Implement strictly monotone number counting DP
        pass


def test_count_strictly_monotone_numbers():
    """Test cases for strictly monotone number counting"""
    solution = Solution()

    # Test case 1: One digit
    assert solution.count_strictly_monotone_numbers(1) == 9
    print("✓ Test 1 passed: k=1 -> 9")

    # Test case 2: Two digits
    assert solution.count_strictly_monotone_numbers(2) == 36
    print("✓ Test 2 passed: k=2 -> 36")

    # Test case 3: Three digits
    assert solution.count_strictly_monotone_numbers(3) == 84
    print("✓ Test 3 passed: k=3 -> 84")

    # Test case 4: Only 123456789 has nine digits
    assert solution.count_strictly_monotone_numbers(9) == 1
    print("✓ Test 4 passed: k=9 -> 1")

    # Test case 5: Too many digits
    assert solution.count_strictly_monotone_numbers(10) == 0
    print("✓ Test 5 passed: k=10 -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_strictly_monotone_numbers()
