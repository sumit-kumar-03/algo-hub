"""
EPI 17.4 - The 3-Sum Problem

Problem:
Given an array of integers and a target t, decide whether three entries of
the array add up to t. The same entry may be used more than once (so
5 + 5 + 11 is allowed when 5 appears only once).

Constraints:
- 0 <= len(A) <= 10^4, -10^9 <= A[i], t <= 10^9
- O(n^2) time and O(1) extra space (besides sorting)

How it works (sort + two pointers per first element):
1. Sort A
2. For each a in A, check whether two entries (repeats allowed) sum to
   t - a:
   - i = 0, j = n - 1; while i <= j:
     if A[i] + A[j] == target: found
     elif the sum is too small: i += 1
     else: j -= 1
3. Return False if no first element works

Example 1:
Input: A = [11, 2, 5, 7, 3], t = 21
Output: True
Explanation: 3 + 7 + 11, or 5 + 5 + 11

Example 2:
Input: A = [11, 2, 5, 7, 3], t = 22
Output: False
"""

from typing import List


class Solution:
    def has_three_sum(self, A: List[int], t: int) -> bool:
        """
        Checks whether three entries (repeats allowed) sum to t.

        Args:
            A: Input integers
            t: Target sum

        Returns:
            True if such a triple exists, False otherwise

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond sorting
        """
        # TODO: Implement 3-sum with sorting and two pointers
        pass


def test_has_three_sum():
    """Test cases for the 3-sum problem"""
    solution = Solution()

    # Test case 1: Book example (present)
    assert solution.has_three_sum([11, 2, 5, 7, 3], 21) is True
    print("✓ Test 1 passed: [11, 2, 5, 7, 3], 21 -> True")

    # Test case 2: Book example (absent)
    assert solution.has_three_sum([11, 2, 5, 7, 3], 22) is False
    print("✓ Test 2 passed: [11, 2, 5, 7, 3], 22 -> False")

    # Test case 3: Same entry used three times
    assert solution.has_three_sum([5], 15) is True
    print("✓ Test 3 passed: [5], 15 -> True")

    # Test case 4: Single entry, wrong target
    assert solution.has_three_sum([5], 10) is False
    print("✓ Test 4 passed: [5], 10 -> False")

    # Test case 5: Negative numbers
    assert solution.has_three_sum([-1, 0, 4], -3) is True
    print("✓ Test 5 passed: [-1, 0, 4], -3 -> True")

    # Test case 6: Target too large
    assert solution.has_three_sum([1, 2], 100) is False
    print("✓ Test 6 passed: [1, 2], 100 -> False")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_has_three_sum()
