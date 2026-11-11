"""
EPI 5.1 Extra Variant - Strict Wiggle Rearrangement
(Practice problem, not in the book. Difficulty: Hard)
Builds on: three-way partitioning around a pivot (here, the median) so
that duplicates of the pivot are kept apart.

Problem:
Given an array of integers, rearrange it in place so that it strictly
alternates down and up:

    A[0] < A[1] > A[2] < A[3] > A[4] < ...

The input is guaranteed to have at least one such arrangement; return any
of them. Duplicates are what make this hard: copies of the median value
must never end up next to each other.

Constraints:
- 1 <= len(A) <= 10^5; a valid arrangement exists
- Target: O(n) average time (find the median with quickselect, then a
  Dutch flag partition); an O(n log n) sort-based solution is a good
  first step
- O(n) extra space is acceptable; O(1) extra space with index remapping
  is the stretch goal

How it works (median + Dutch flag + interleave):
1. Find the median value m (the element of rank (n - 1) // 2)
2. Three-way partition around m so the array is: < m, == m, > m
3. Split into a lower half L = A[:(n + 1) // 2] and an upper half
   U = A[(n + 1) // 2:]
4. Write L in reverse into the even indices and U in reverse into the odd
   indices. Reversing pushes copies of m to opposite ends of the two
   halves, so they never touch
   (O(1)-space version: run the Dutch flag pass on the virtual index
   (1 + 2 * i) % (n | 1), which visits odd slots first, then even slots)

Example 1:
Input: A = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4] (one valid answer)
Explanation: 1 < 6 > 1 < 5 > 1 < 4.

Example 2:
Input: A = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2] (one valid answer)
Explanation: 2 < 3 > 1 < 3 > 1 < 2.
"""

import random
from typing import List


class Solution:
    def wiggle_sort(self, A: List[int]) -> None:
        """
        Rearranges A so that A[0] < A[1] > A[2] < A[3] > ...

        Args:
            A: Array that admits a strict wiggle arrangement (in place)

        Returns:
            None (A is modified in place)

        Time Complexity: O(n) average (O(n log n) with sorting)
        Space Complexity: O(n), or O(1) with virtual indexing
        """
        # TODO: Implement strict wiggle rearrangement
        pass


def is_wiggle(A: List[int]) -> bool:
    """Checks A[0] < A[1] > A[2] < A[3] > ..."""
    for i in range(1, len(A)):
        if i % 2 == 1 and not A[i - 1] < A[i]:
            return False
        if i % 2 == 0 and not A[i - 1] > A[i]:
            return False
    return True


def test_wiggle_sort():
    """Test cases for strict wiggle rearrangement"""
    solution = Solution()

    # Test case 1: Example 1
    A1 = [1, 5, 1, 1, 6, 4]
    solution.wiggle_sort(A1)
    assert sorted(A1) == [1, 1, 1, 4, 5, 6] and is_wiggle(A1)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Example 2
    A2 = [1, 3, 2, 2, 3, 1]
    solution.wiggle_sort(A2)
    assert sorted(A2) == [1, 1, 2, 2, 3, 3] and is_wiggle(A2)
    print(f"✓ Test 2 passed: {A2}")

    # Test case 3: Tiny inputs
    A3 = [7]
    solution.wiggle_sort(A3)
    assert A3 == [7]
    A4 = [2, 1]
    solution.wiggle_sort(A4)
    assert A4 == [1, 2]
    print("✓ Test 3 passed: Single element and [2, 1] -> [1, 2]")

    # Test case 4: Median value repeated in both halves
    A5 = [4, 5, 5, 6]
    solution.wiggle_sort(A5)
    assert sorted(A5) == [4, 5, 5, 6] and is_wiggle(A5)
    A6 = [1, 1, 2, 2, 3]
    solution.wiggle_sort(A6)
    assert sorted(A6) == [1, 1, 2, 2, 3] and is_wiggle(A6)
    print(f"✓ Test 4 passed: {A5} and {A6}")

    # Test case 5: Sorted input with negatives and odd length
    A7 = [-5, -3, -3, 0, 0, 2, 8]
    solution.wiggle_sort(A7)
    assert sorted(A7) == [-5, -3, -3, 0, 0, 2, 8] and is_wiggle(A7)
    print(f"✓ Test 5 passed: {A7}")

    # Test case 6: Large shuffled input where every value appears twice
    rng = random.Random(51)
    A8 = list(range(5000)) * 2
    rng.shuffle(A8)
    original8 = sorted(A8)
    solution.wiggle_sort(A8)
    assert sorted(A8) == original8 and is_wiggle(A8)
    print("✓ Test 6 passed: 10,000 elements with duplicates")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_wiggle_sort()
