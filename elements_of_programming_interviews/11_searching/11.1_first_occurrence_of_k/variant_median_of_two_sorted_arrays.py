"""
EPI 11.1 Extra Variant - Median of Two Sorted Arrays
(Practice problem, not in the book. Difficulty: Hard)
Builds on: binary search for the first index at which a monotone condition
becomes true, here over the ways to split the shorter array.

Problem:
Given two sorted arrays A and B (either may be empty, but not both), return
the median of all their elements combined. For an odd total count it is the
middle element; for an even count it is the average of the two middle
elements (returned as a float).

Constraints:
- 0 <= len(A), len(B) <= 10^5; len(A) + len(B) >= 1
- Values may be negative and may repeat
- O(log min(len(A), len(B))) time, O(1) space; do not merge the arrays

How it works (binary search on the split point):
1. Make A the shorter array. Let half = (len(A) + len(B) + 1) // 2
2. For a split i of A (0 <= i <= len(A)), take j = half - i from B, so the
   "left part" A[:i] + B[:j] has half elements
3. The split is correct when A[i - 1] <= B[j] and B[j - 1] <= A[i]
   (treating out-of-range values as -inf / +inf). The condition
   "B[j - 1] <= A[i]" is false for small i and true from some point on, so
   binary search for the first i where it holds
4. Median = max of the left part if the total is odd, otherwise the average
   of max(left part) and min(right part)

Example 1:
Input: A = [1, 3], B = [2]
Output: 2.0

Example 2:
Input: A = [1, 2], B = [3, 4]
Output: 2.5
"""

import math
from typing import List


class Solution:
    def find_median(self, A: List[int], B: List[int]) -> float:
        """
        Returns the median of the union of two sorted arrays.

        Args:
            A: Sorted array
            B: Sorted array (len(A) + len(B) >= 1)

        Returns:
            The median as a float

        Time Complexity: O(log min(len(A), len(B)))
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on the split of the shorter array
        pass


def _slow_median(A: List[int], B: List[int]) -> float:
    merged = sorted(A + B)
    n = len(merged)
    if n % 2:
        return float(merged[n // 2])
    return (merged[n // 2 - 1] + merged[n // 2]) / 2


def _close(a, b) -> bool:
    return a is not None and math.isclose(a, b, abs_tol=1e-9)


def test_find_median():
    """Test cases for median of two sorted arrays"""
    solution = Solution()

    # Test case 1: Odd total
    assert _close(solution.find_median([1, 3], [2]), 2.0) is True
    print("✓ Test 1 passed: [1, 3] + [2] -> 2.0")

    # Test case 2: Even total
    assert _close(solution.find_median([1, 2], [3, 4]), 2.5) is True
    print("✓ Test 2 passed: [1, 2] + [3, 4] -> 2.5")

    # Test case 3: One array empty
    assert _close(solution.find_median([], [5]), 5.0) is True
    assert _close(solution.find_median([1, 2, 3, 4], []), 2.5) is True
    print("✓ Test 3 passed: One empty array")

    # Test case 4: All of A before all of B, and interleaved
    assert _close(solution.find_median([1, 2, 3], [10, 11, 12, 13]), 10.0) is True
    assert _close(solution.find_median([1, 5, 9], [2, 6, 10]), 5.5) is True
    print("✓ Test 4 passed: Disjoint and interleaved")

    # Test case 5: Duplicates and negatives
    assert _close(solution.find_median([-5, -5, 0], [-5, 0, 0, 7]), 0.0) is True
    assert _close(solution.find_median([2, 2, 2], [2, 2]), 2.0) is True
    print("✓ Test 5 passed: Duplicates and negatives")

    # Test case 6: Very different lengths
    A6 = [-10 ** 6]
    B6 = list(range(0, 2000, 2))
    assert _close(solution.find_median(A6, B6), _slow_median(A6, B6)) is True
    assert _close(solution.find_median(B6, A6), _slow_median(A6, B6)) is True
    print("✓ Test 6 passed: Lengths 1 and 1000")

    # Test case 7: Many deterministic pairs vs. merging
    for s in range(60):
        A7 = sorted((i * (s + 3)) % 23 - 11 for i in range(s % 9))
        B7 = sorted((i * (s + 7)) % 19 - 9 for i in range(1 + s % 13))
        assert _close(solution.find_median(A7, B7), _slow_median(A7, B7)) is True
    print("✓ Test 7 passed: 60 random-looking pairs")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_median()
