"""
EPI 12.5 Extra Variant - Nearby Almost-Duplicate Values
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the nearest repeated entries scan with a hash table, but
"equal" is relaxed to "within t of each other", which requires hashing
values into buckets instead of hashing them exactly.

Problem:
Given an integer array A and nonnegative integers k and t, return True if
there are two different indices i and j such that |i - j| <= k and
|A[i] - A[j]| <= t. Otherwise return False.

Constraints:
- 0 <= len(A) <= 10^5
- -10^9 <= A[i] <= 10^9
- 0 <= k, t <= 10^9
- Target: O(n) time with bucketing (a balanced BST gives O(n log k));
  checking all pairs within distance k is O(nk) and too slow

How it works (buckets of width t + 1):
1. Map each value x to bucket id x // (t + 1) (floor division, which also
   works for negative x in Python). Two values in the same bucket differ by
   at most t, so finding one is an immediate True
2. A value within t could also sit in an adjacent bucket (id - 1 or
   id + 1); check those explicitly
3. Keep at most one value per bucket (a second one would already have
   returned True), and only for the last k indices: after processing index
   i, remove the bucket of A[i - k]
4. Return False if the scan completes

Example 1:
Input: A = [1, 5, 9, 1, 5, 9], k = 2, t = 3
Output: False
Explanation: Within any 2 positions the values differ by at least 4.

Example 2:
Input: A = [1, 2, 3, 1], k = 3, t = 0
Output: True
Explanation: A[0] == A[3] and they are 3 apart.
"""

from typing import List


class Solution:
    def contains_nearby_almost_duplicate(self, A: List[int], k: int, t: int) -> bool:
        """
        Checks for two values within t of each other at most k positions apart.

        Args:
            A: Array of integers
            k: Maximum index distance
            t: Maximum value difference

        Returns:
            True if such a pair exists, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(min(n, k))
        """
        # TODO: Implement bucketed sliding-window check
        pass


def test_contains_nearby_almost_duplicate():
    """Test cases for nearby almost-duplicate values"""
    solution = Solution()

    # Test case 1: Values never close enough within the window
    assert solution.contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], 2, 3) is False
    print("✓ Test 1 passed: Gaps of 4 with t=3 -> False")

    # Test case 2: t = 0 reduces to exact duplicates within k
    assert solution.contains_nearby_almost_duplicate([1, 2, 3, 1], 3, 0) is True
    print("✓ Test 2 passed: Exact duplicate within k -> True")

    # Test case 3: Close values in adjacent buckets
    assert solution.contains_nearby_almost_duplicate([1, 0, 1, 1], 1, 2) is True
    assert solution.contains_nearby_almost_duplicate([10, 30, 13], 2, 3) is True
    print("✓ Test 3 passed: Adjacent-bucket matches")

    # Test case 4: Negative numbers near zero
    assert solution.contains_nearby_almost_duplicate([-3, 3], 1, 6) is True
    assert solution.contains_nearby_almost_duplicate([-3, 3], 1, 5) is False
    print("✓ Test 4 passed: Negative values")

    # Test case 5: k = 0 and tiny arrays
    assert solution.contains_nearby_almost_duplicate([1, 1], 0, 5) is False
    assert solution.contains_nearby_almost_duplicate([], 3, 3) is False
    assert solution.contains_nearby_almost_duplicate([7], 3, 3) is False
    print("✓ Test 5 passed: k=0 / empty / single -> False")

    # Test case 6: Close values that are too far apart in index
    assert solution.contains_nearby_almost_duplicate([5, 100, 200, 6], 2, 1) is False
    assert solution.contains_nearby_almost_duplicate([5, 100, 200, 6], 3, 1) is True
    print("✓ Test 6 passed: Window size matters")

    # Test case 7: Extreme values and brute-force cross-check
    big = [-10**9, 10**9]
    assert solution.contains_nearby_almost_duplicate(big, 1, 2 * 10**9) is True
    assert solution.contains_nearby_almost_duplicate(big, 1, 2 * 10**9 - 1) is False
    A = [((i * 7919) % 101) - 50 for i in range(80)]
    for k in [1, 2, 5]:
        for t in [0, 1, 3]:
            expected = any(abs(A[i] - A[j]) <= t
                           for i in range(len(A))
                           for j in range(i + 1, min(len(A), i + k + 1)))
            assert solution.contains_nearby_almost_duplicate(A, k, t) is expected
    print("✓ Test 7 passed: Extremes and brute-force grid")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_contains_nearby_almost_duplicate()
