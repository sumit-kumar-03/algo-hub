"""
EPI 11.8 Extra Variant - k Values Closest to the Median
(Practice problem, not in the book. Difficulty: Medium)
Builds on: randomized selection, used twice: once to find the median and
once more on a derived key (distance to the median).

Problem:
Given an array of n integers with n odd (so the median is the element of
rank n // 2 in sorted order) and an integer k, return the k values closest
to the median. Value a is closer than value b if |a - m| < |b - m|, or if
the distances are equal and a < b, where m is the median. The median itself
(and any copies of it) counts as a candidate at distance 0. Return the
chosen values sorted in ascending order.

Constraints:
- 1 <= k <= n <= 10^5, n odd
- Duplicates allowed; values may be negative
- Expected O(n + k log k) time (the final sort of k values is fine); do
  not sort the whole array

How it works (select, transform, select again):
1. Quickselect the median m (rank n // 2)
2. Build keys (|a - m|, a) for every value a; these keys are totally
   ordered and break ties toward smaller values
3. Quickselect on the keys to bring the k smallest keys to the front
4. Return the values of those k keys, sorted

Example 1:
Input: A = [7, 14, 10, 12, 2, 11, 29, 3, 4], k = 5
Output: [7, 10, 11, 12, 14]
Explanation: The median is 10; distances are 3, 4, 0, 2, 8, 1, 19, 7, 6.

Example 2:
Input: A = [1, 2, 3, 4, 5], k = 2
Output: [2, 3]
Explanation: The median is 3; 2 and 4 tie at distance 1 and 2 is smaller.
"""

from typing import List


class Solution:
    def k_closest_to_median(self, A: List[int], k: int) -> List[int]:
        """
        Returns the k values closest to the median, sorted ascending.

        Args:
            A: Array of integers with odd length (may be reordered)
            k: Number of values to return

        Returns:
            The k closest values (ties toward smaller values), ascending

        Time Complexity: O(n + k log k) expected
        Space Complexity: O(n)
        """
        # TODO: Implement with two rounds of quickselect
        pass


def _slow(A: List[int], k: int) -> List[int]:
    m = sorted(A)[len(A) // 2]
    return sorted(sorted(A, key=lambda a: (abs(a - m), a))[:k])


def test_k_closest_to_median():
    """Test cases for k values closest to the median"""
    solution = Solution()

    # Test case 1: Example 1
    A1 = [7, 14, 10, 12, 2, 11, 29, 3, 4]
    assert solution.k_closest_to_median(list(A1), 5) == [7, 10, 11, 12, 14]
    print("✓ Test 1 passed: Example 1")

    # Test case 2: Tie broken toward the smaller value
    assert solution.k_closest_to_median([1, 2, 3, 4, 5], 2) == [2, 3]
    print("✓ Test 2 passed: Tie toward smaller value")

    # Test case 3: Single element
    assert solution.k_closest_to_median([42], 1) == [42]
    print("✓ Test 3 passed: Single element")

    # Test case 4: k = n returns everything sorted
    assert solution.k_closest_to_median([9, -1, 4], 3) == [-1, 4, 9]
    print("✓ Test 4 passed: k = n")

    # Test case 5: Copies of the median and negatives
    A5 = [-3, 5, 5, 5, -8, 6, 100]
    assert solution.k_closest_to_median(list(A5), 4) == [5, 5, 5, 6]
    print("✓ Test 5 passed: Copies of the median")

    # Test case 6: Skewed values (median far from the mean)
    A6 = [1, 2, 3, 1000, 1001, 1002, 4, 1003, 5]
    assert solution.k_closest_to_median(list(A6), 3) == [3, 4, 5]
    print("✓ Test 6 passed: Skewed values")

    # Test case 7: Larger deterministic arrays vs. sorting
    data = [(i * 7919) % 2003 - 1000 for i in range(1501)]
    for k in (1, 100, 1501):
        assert solution.k_closest_to_median(list(data), k) == _slow(data, k)
    print("✓ Test 7 passed: 1501 values")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_closest_to_median()
