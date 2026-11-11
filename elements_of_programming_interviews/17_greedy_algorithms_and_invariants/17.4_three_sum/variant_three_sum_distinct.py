"""
EPI 17.4 Variant - 3-Sum with Distinct Entries

Problem:
Same as 3-sum, but the three entries must be at three different positions
of the array (equal values at different positions are fine). Return whether
such a triple sums to t.

Constraints:
- 0 <= len(A) <= 10^4
- O(n^2) time and O(1) extra space (besides sorting)

How it works (sort + two pointers to the right of the first element):
1. Sort A
2. For each k, set i = k + 1, j = n - 1; while i < j:
   s = A[k] + A[i] + A[j]; found if s == t; move i up if s < t, else j down
3. Return False if nothing matches

Example 1:
Input: A = [5, 2, 3, 4, 3], t = 9
Output: True
Explanation: A[1] + A[2] + A[3] = 2 + 3 + 4. Using A[2] three times
(3 + 3 + 3) is not allowed, but 2 + 3 + 4 is.

Example 2:
Input: A = [5, 2, 3, 4, 3], t = 6
Output: False
Explanation: 2 + 2 + 2 would reuse A[1].
"""

from typing import List


class Solution:
    def has_three_sum_distinct(self, A: List[int], t: int) -> bool:
        """
        Checks whether entries at three distinct positions sum to t.

        Args:
            A: Input integers
            t: Target sum

        Returns:
            True if such a triple exists, False otherwise

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond sorting
        """
        # TODO: Implement distinct-index 3-sum
        pass


def test_has_three_sum_distinct():
    """Test cases for 3-sum with distinct entries"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.has_three_sum_distinct([5, 2, 3, 4, 3], 9) is True
    print("✓ Test 1 passed: [5, 2, 3, 4, 3], 9 -> True")

    # Test case 2: Would need reuse
    assert solution.has_three_sum_distinct([5, 2, 3, 4, 3], 6) is False
    print("✓ Test 2 passed: [5, 2, 3, 4, 3], 6 -> False")

    # Test case 3: Too large without reuse (5 + 5 + 5)
    assert solution.has_three_sum_distinct([5, 2, 3, 4, 3], 15) is False
    print("✓ Test 3 passed: [5, 2, 3, 4, 3], 15 -> False")

    # Test case 4: Fewer than three entries
    assert solution.has_three_sum_distinct([5], 15) is False
    print("✓ Test 4 passed: [5], 15 -> False")

    # Test case 5: Equal values at different positions are fine
    assert solution.has_three_sum_distinct([1, 1, 1], 3) is True
    print("✓ Test 5 passed: [1, 1, 1], 3 -> True")

    # Test case 6: 21 works with 3 + 7 + 11 even without reuse
    assert solution.has_three_sum_distinct([11, 2, 5, 7, 3], 21) is True
    print("✓ Test 6 passed: [11, 2, 5, 7, 3], 21 -> True")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_has_three_sum_distinct()
