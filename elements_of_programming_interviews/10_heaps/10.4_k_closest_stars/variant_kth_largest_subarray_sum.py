"""
EPI 10.4 Extra Variant - kth Largest Subarray Sum
(Practice problem, not in the book. Difficulty: Medium)
Builds on: streaming a huge set of candidates through a heap of size k, so
memory stays O(k) even though the candidates are never stored.

Problem:
Given an array of integers, consider the sums of all of its nonempty
contiguous subarrays. There are n * (n + 1) / 2 of them, one per pair of
indices i <= j, and equal sums from different index pairs count
separately. Return the kth largest of these sums (k = 1 is the maximum).

Constraints:
- 1 <= n <= 300; 1 <= k <= min(2000, n * (n + 1) / 2)
- Values may be negative
- O(n^2 log k) time and O(k) extra space: do not build the list of all sums

How it works (generate candidates, keep the k largest):
1. Use prefix sums, or extend a running sum for each start index i, to
   produce every subarray sum in O(1) each
2. Feed each sum into a min-heap; when the heap grows past k, pop its
   minimum
3. After all sums are processed, the heap's minimum is the kth largest

Example 1:
Input: A = [2, 1, 3], k = 4
Output: 3
Explanation: The sums are 2, 3, 6 (starting at 0), 1, 4 (starting at 1) and
3; in descending order 6, 4, 3, 3, 2, 1.

Example 2:
Input: A = [-2, -1], k = 1
Output: -1
"""

from typing import List


class Solution:
    def kth_largest_subarray_sum(self, A: List[int], k: int) -> int:
        """
        Returns the kth largest sum among all contiguous subarrays.

        Args:
            A: Nonempty array of integers
            k: 1-based rank from the top

        Returns:
            The kth largest subarray sum

        Time Complexity: O(n^2 log k)
        Space Complexity: O(k)
        """
        # TODO: Implement with a min-heap of size k
        pass


def _all_sums(A: List[int]) -> List[int]:
    sums = []
    for i in range(len(A)):
        total = 0
        for j in range(i, len(A)):
            total += A[j]
            sums.append(total)
    return sorted(sums, reverse=True)


def test_kth_largest_subarray_sum():
    """Test cases for kth largest subarray sum"""
    solution = Solution()

    # Test case 1: Example, every rank
    expected1 = [6, 4, 3, 3, 2, 1]
    assert [solution.kth_largest_subarray_sum([2, 1, 3], k) for k in range(1, 7)] == expected1
    print("✓ Test 1 passed: [2, 1, 3] for k = 1..6")

    # Test case 2: All negative
    assert solution.kth_largest_subarray_sum([-2, -1], 1) == -1
    assert solution.kth_largest_subarray_sum([-2, -1], 3) == -3
    print("✓ Test 2 passed: All negative")

    # Test case 3: Single element
    assert solution.kth_largest_subarray_sum([7], 1) == 7
    print("✓ Test 3 passed: Single element")

    # Test case 4: Duplicate sums counted separately
    assert solution.kth_largest_subarray_sum([1, 1, 1], 3) == 2
    assert solution.kth_largest_subarray_sum([1, 1, 1], 4) == 1
    print("✓ Test 4 passed: Duplicate sums")

    # Test case 5: Mixed signs, compared with brute force
    A5 = [3, -4, 5, -1, 2, -6, 4]
    ranked = _all_sums(A5)
    for k in (1, 5, 14, 28):
        assert solution.kth_largest_subarray_sum(A5, k) == ranked[k - 1]
    print("✓ Test 5 passed: Mixed signs")

    # Test case 6: Larger deterministic array
    A6 = [(i * 37) % 41 - 20 for i in range(300)]
    ranked6 = _all_sums(A6)
    for k in (1, 777, 2000):
        assert solution.kth_largest_subarray_sum(A6, k) == ranked6[k - 1]
    print("✓ Test 6 passed: 300 elements")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_largest_subarray_sum()
