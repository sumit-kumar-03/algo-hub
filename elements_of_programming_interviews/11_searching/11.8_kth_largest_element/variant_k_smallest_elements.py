"""
EPI 11.8 Extra Variant - The k Smallest Elements
(Practice problem, not in the book. Difficulty: Easy)
Builds on: quickselect's partition step; once the pivot lands at index
k - 1, everything to its left is already the answer.

Problem:
Given an array of numbers (duplicates allowed) and an integer k, rearrange
the array in place so that its first k positions hold the k smallest
values (in any order), and return those k values as a list. Every value in
A[k:] must be greater than or equal to every value in A[:k].

Constraints:
- 0 <= k <= len(A) <= 10^5
- Expected O(n) time, O(1) extra space besides the returned list
- Do not fully sort the array

How it works (quickselect, then stop):
1. If k == 0 or k == len(A), there is nothing to partition
2. Otherwise run quickselect for the element of rank k - 1 (0-based,
   ascending), partitioning around random pivots
3. When it finishes, A[:k] holds the k smallest values; return A[:k]
   (with duplicates, use a three-way partition or treat "equal to pivot"
   consistently so the loop always shrinks)

Example 1:
Input: A = [7, 2, 9, 4, 1, 8], k = 3
Output: [1, 2, 4]   (in any order)
Explanation: After the call, A[:3] is some ordering of 1, 2, 4.

Example 2:
Input: A = [5, 5, 5, 1], k = 2
Output: [1, 5]   (in any order)
"""

from typing import List


class Solution:
    def k_smallest(self, A: List[int], k: int) -> List[int]:
        """
        Moves the k smallest values to the front of A and returns them.

        Args:
            A: Array of numbers (rearranged in place)
            k: How many of the smallest values to collect

        Returns:
            The k smallest values (any order); they also occupy A[:k]

        Time Complexity: O(n) expected
        Space Complexity: O(1) extra, excluding the output
        """
        # TODO: Implement with quickselect partitioning
        pass


def _check(original: List[int], A: List[int], k: int, result: List[int]) -> bool:
    """Valid iff A is a rearrangement of original, A[:k] matches result,
    and they hold exactly the k smallest values."""
    if result is None or sorted(A) != sorted(original):
        return False
    if sorted(A[:k]) != sorted(result):
        return False
    return sorted(result) == sorted(original)[:k]


def test_k_smallest():
    """Test cases for the k smallest elements"""
    solution = Solution()

    # Test case 1: Basic example
    A1 = [7, 2, 9, 4, 1, 8]
    orig1 = list(A1)
    result1 = solution.k_smallest(A1, 3)
    assert _check(orig1, A1, 3, result1) is True
    print(f"✓ Test 1 passed: {result1}")

    # Test case 2: Duplicates
    A2 = [5, 5, 5, 1]
    orig2 = list(A2)
    assert _check(orig2, A2, 2, solution.k_smallest(A2, 2)) is True
    print("✓ Test 2 passed: Duplicates")

    # Test case 3: k = 0 and k = n
    A3 = [3, 1, 2]
    assert solution.k_smallest(list(A3), 0) == []
    A3b = list(A3)
    assert _check(A3, A3b, 3, solution.k_smallest(A3b, 3)) is True
    print("✓ Test 3 passed: k = 0 and k = n")

    # Test case 4: Single element and negatives
    A4 = [-4]
    assert _check([-4], A4, 1, solution.k_smallest(A4, 1)) is True
    A4b = [0, -7, 3, -7, 2]
    assert _check([0, -7, 3, -7, 2], A4b, 2, solution.k_smallest(A4b, 2)) is True
    print("✓ Test 4 passed: Single element and negatives")

    # Test case 5: All equal values (no endless partitioning)
    A5 = [9] * 2000
    assert _check([9] * 2000, A5, 1000, solution.k_smallest(A5, 1000)) is True
    print("✓ Test 5 passed: 2000 equal values")

    # Test case 6: Larger arrays, many k
    data = [(i * 7919) % 1013 - 500 for i in range(1500)]
    for k in (1, 10, 750, 1499):
        A6 = list(data)
        assert _check(data, A6, k, solution.k_smallest(A6, k)) is True
    print("✓ Test 6 passed: 1500 values, several k")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_smallest()
