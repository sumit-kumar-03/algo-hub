"""
EPI 17.4 Extra Variant - Two Entries of a Sorted Array That Hit a Target
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the two-pointer inner loop of 3-sum, used on its own and
returning positions instead of a yes/no answer.

Problem:
Given an array A sorted in nondecreasing order and a target t, find two
different positions i < j with A[i] + A[j] == t. Return (i, j), or None if
no such pair exists. If several pairs work, any of them is accepted.

Constraints:
- 0 <= len(A) <= 10^5, A is sorted, -10^9 <= A[i], t <= 10^9
- O(n) time and O(1) extra space (no hash table)

How it works (two pointers from both ends):
1. i = 0, j = n - 1
2. While i < j:
   - if A[i] + A[j] == t: return (i, j)
   - if the sum is too small, i += 1 (only a bigger left value can help)
   - otherwise j -= 1
3. Return None
Invariant: no pair using a position outside [i, j] can reach t.

Example 1:
Input: A = [-3, 1, 4, 6, 9], t = 10
Output: (1, 4)
Explanation: 1 + 9 = 10 (4 + 6 also works, so (2, 3) is accepted too).

Example 2:
Input: A = [1, 2, 5], t = 4
Output: None
Explanation: 2 + 2 would reuse position 1.
"""

from typing import List, Optional, Tuple


class Solution:
    def two_sum_sorted(self, A: List[int], t: int) -> Optional[Tuple[int, int]]:
        """
        Finds positions i < j in a sorted array with A[i] + A[j] == t.

        Args:
            A: Integers sorted in nondecreasing order
            t: Target sum

        Returns:
            A pair (i, j) with i < j, or None if none exists

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement two pointers from both ends
        pass


def is_valid_pair(result, A: List[int], t: int) -> bool:
    """Checks result is a pair of positions i < j whose values sum to t."""
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    i, j = result
    return 0 <= i < j < len(A) and A[i] + A[j] == t


def test_two_sum_sorted():
    """Test cases for two-sum on a sorted array"""
    solution = Solution()

    # Test case 1: Example 1 (two valid answers)
    A1 = [-3, 1, 4, 6, 9]
    r1 = solution.two_sum_sorted(A1, 10)
    assert is_valid_pair(r1, A1, 10)
    print(f"✓ Test 1 passed: {A1}, 10 -> {r1}")

    # Test case 2: Example 2 (no reuse of a position)
    assert solution.two_sum_sorted([1, 2, 5], 4) is None
    print("✓ Test 2 passed: [1, 2, 5], 4 -> None")

    # Test case 3: Empty and single-element arrays
    assert solution.two_sum_sorted([], 0) is None
    assert solution.two_sum_sorted([5], 10) is None
    print("✓ Test 3 passed: empty and single element -> None")

    # Test case 4: Equal values at different positions
    assert solution.two_sum_sorted([2, 2], 4) == (0, 1)
    print("✓ Test 4 passed: [2, 2], 4 -> (0, 1)")

    # Test case 5: Negative numbers and a zero target
    A5 = [-8, -5, -1, 0, 3, 5, 12]
    r5 = solution.two_sum_sorted(A5, 0)
    assert is_valid_pair(r5, A5, 0)
    print(f"✓ Test 5 passed: {A5}, 0 -> {r5}")

    # Test case 6: Target too large and too small
    assert solution.two_sum_sorted([1, 3, 5, 7], 13) is None
    assert solution.two_sum_sorted([1, 3, 5, 7], 3) is None
    print("✓ Test 6 passed: out-of-range targets -> None")

    # Test case 7: Large array, only the two ends work
    A7 = list(range(0, 200000, 2)) + [10 ** 9]
    assert solution.two_sum_sorted(A7, 10 ** 9) == (0, len(A7) - 1)
    assert solution.two_sum_sorted(A7, 3) is None
    print("✓ Test 7 passed: large array")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_two_sum_sorted()
