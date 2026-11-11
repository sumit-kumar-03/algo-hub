"""
EPI 17.4 Variant - Closest 3-Sum

Problem:
Given an array of integers A (at least three entries) and a target T, find
three entries at distinct positions p, q, r whose sum is as close to T as
possible, i.e. minimizing |T - (A[p] + A[q] + A[r])|. Return their values
as a tuple sorted in nondecreasing order. If several triples are equally
close, any of them is accepted.

Constraints:
- 3 <= len(A) <= 10^4
- O(n^2) time

How it works (sort + two pointers, tracking the best gap):
1. Sort A
2. For each k, set i = k + 1, j = n - 1; while i < j:
   - s = A[k] + A[i] + A[j]; keep (A[k], A[i], A[j]) if |T - s| improves
   - if s == T stop early; if s < T move i up; else move j down
3. Return the best triple

Example 1:
Input: A = [-1, 2, 1, -4], T = 1
Output: (-1, 1, 2)
Explanation: The sum 2 is the closest possible to 1.

Example 2:
Input: A = [1, 2, 4, 8, 16, 32], T = 50
Output: (2, 16, 32)
"""

from itertools import combinations
from typing import List, Tuple


class Solution:
    def three_sum_closest(self, A: List[int], T: int) -> Tuple[int, int, int]:
        """
        Finds three distinct-position entries whose sum is closest to T.

        Args:
            A: Input integers (length >= 3)
            T: Target sum

        Returns:
            The three values, sorted in nondecreasing order

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond sorting
        """
        # TODO: Implement closest 3-sum
        pass


def is_valid_closest(result, A: List[int], T: int) -> bool:
    """Checks result is a sorted triple drawn from A that is optimally close to T."""
    if not isinstance(result, tuple) or len(result) != 3 or list(result) != sorted(result):
        return False
    remaining = list(A)
    for x in result:
        if x not in remaining:
            return False
        remaining.remove(x)
    best_gap = min(abs(T - sum(c)) for c in combinations(A, 3))
    return abs(T - sum(result)) == best_gap


def test_three_sum_closest():
    """Test cases for closest 3-sum"""
    solution = Solution()

    # Test case 1: Classic example
    assert solution.three_sum_closest([-1, 2, 1, -4], 1) == (-1, 1, 2)
    print("✓ Test 1 passed: [-1, 2, 1, -4], 1 -> (-1, 1, 2)")

    # Test case 2: Exact match
    assert solution.three_sum_closest([1, 2, 4, 8, 16, 32], 50) == (2, 16, 32)
    print("✓ Test 2 passed: exact match -> (2, 16, 32)")

    # Test case 3: All zeros
    assert solution.three_sum_closest([0, 0, 0], 1) == (0, 0, 0)
    print("✓ Test 3 passed: [0, 0, 0], 1 -> (0, 0, 0)")

    # Test case 4: Target far below every sum
    assert solution.three_sum_closest([1, 1, 1, 0], -100) == (0, 1, 1)
    print("✓ Test 4 passed: [1, 1, 1, 0], -100 -> (0, 1, 1)")

    # Test case 5: Several equally good triples
    A5 = [5, 2, 3, 4, 3]
    r5 = solution.three_sum_closest(A5, 9)
    assert is_valid_closest(r5, A5, 9)
    print(f"✓ Test 5 passed: [5, 2, 3, 4, 3], 9 -> {r5}")

    # Test case 6: Ties between a sum above and a sum below
    A6 = [1, 2, 4, 10]  # 1 + 2 + 4 = 7 and 1 + 2 + 10 = 13 are both 3 away
    r6 = solution.three_sum_closest(A6, 10)
    assert is_valid_closest(r6, A6, 10)
    print(f"✓ Test 6 passed: [1, 2, 4, 10], 10 -> {r6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_three_sum_closest()
