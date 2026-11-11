"""
EPI 10.4 Extra Variant - k Values Closest to a Target
(Practice problem, not in the book. Difficulty: Easy)
Builds on: keeping the k best candidates seen so far in a bounded max-heap
keyed by "distance", evicting the worst one when the heap overflows.

Problem:
Given an unsorted list of integers, a target x, and an integer k, return the
k values closest to x. Value a is closer than value b if |a - x| < |b - x|,
or if the distances are equal and a < b. Return the chosen values sorted in
ascending order. If the list has fewer than k values, return all of them
(sorted).

Constraints:
- 0 <= len(nums) <= 10^5; 0 <= k
- Values may repeat and may be negative
- O(n log k) time, O(k) extra space; read the list once from left to right
  (do not sort the whole list)

How it works (bounded max-heap with a composite key):
1. The "badness" of a value a is the pair (|a - x|, a); smaller is better
2. Keep a max-heap of the k best values seen (store negated keys with
   heapq)
3. For each value, push it; if the heap holds k + 1 entries, pop the worst
4. Sort the k survivors in ascending order and return them

Example 1:
Input: nums = [5, 1, 9, 3, 7], x = 6, k = 3
Output: [3, 5, 7]
Explanation: Distances are 1, 5, 3, 3, 1; 5 and 7 are at distance 1, and the
tie at distance 3 between 3 and 9 goes to the smaller value 3.

Example 2:
Input: nums = [10, 20], x = 0, k = 5
Output: [10, 20]
"""

from typing import List


class Solution:
    def k_closest(self, nums: List[int], x: int, k: int) -> List[int]:
        """
        Returns the k values closest to x, sorted ascending.

        Args:
            nums: Unsorted list of integers
            x: Target value
            k: Number of values to return

        Returns:
            The min(k, len(nums)) closest values in ascending order

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # TODO: Implement with a bounded max-heap
        pass


def test_k_closest():
    """Test cases for k values closest to a target"""
    solution = Solution()

    # Test case 1: Example with a distance tie
    assert solution.k_closest([5, 1, 9, 3, 7], 6, 3) == [3, 5, 7]
    print("✓ Test 1 passed: [5, 1, 9, 3, 7], x = 6, k = 3")

    # Test case 2: Fewer values than k
    assert solution.k_closest([20, 10], 0, 5) == [10, 20]
    print("✓ Test 2 passed: Fewer values than k")

    # Test case 3: k = 0 and empty input
    assert solution.k_closest([1, 2, 3], 2, 0) == []
    assert solution.k_closest([], 2, 3) == []
    print("✓ Test 3 passed: k = 0 and empty input")

    # Test case 4: Duplicates of the target
    assert solution.k_closest([4, 4, 1, 4, 8], 4, 2) == [4, 4]
    print("✓ Test 4 passed: Duplicates")

    # Test case 5: Symmetric ties prefer smaller values
    assert solution.k_closest([-2, 2, -1, 1, 0], 0, 4) == [-2, -1, 0, 1]
    print("✓ Test 5 passed: Symmetric ties")

    # Test case 6: Target outside the value range
    assert solution.k_closest([3, -7, 12, 0, -20], 100, 2) == [3, 12]
    print("✓ Test 6 passed: Target above all values")

    # Test case 7: Larger deterministic input vs. sorting by key
    nums = [(i * 7919) % 1009 - 500 for i in range(2000)]
    expected = sorted(sorted(nums, key=lambda a: (abs(a - 37), a))[:25])
    assert solution.k_closest(nums, 37, 25) == expected
    print("✓ Test 7 passed: 2000 values, k = 25")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_closest()
