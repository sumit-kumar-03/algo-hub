"""
EPI 12.6 Variant - Shortest Subarray Containing All Distinct Values

Problem:
Given an array A, find a shortest subarray A[i..j] that contains every
distinct value present anywhere in A. Return (i, j) as inclusive indices,
or (-1, -1) for an empty array.

Constraints:
- 0 <= len(A) <= 10^5
- O(n) time, O(d) space where d is the number of distinct values
- If several shortest subarrays exist, any one may be returned

How it works:
1. The "keywords" are simply the set of distinct values of A
2. Run a sliding window: extend the right end, and while the window holds all
   d distinct values, record it and shrink from the left
3. Track per-value counts in a hash table and how many distinct values the
   window currently holds

Example 1:
Input: A = [1, 2, 2, 3, 1, 3, 2]
Output: (2, 4)
Explanation: [2, 3, 1] has length 3; no window of length 2 holds 1, 2, 3.
(Note (4, 6) = [1, 3, 2] is equally short and also accepted.)

Example 2:
Input: A = [5, 5, 5]
Output: (0, 0)
"""

from typing import List, Tuple


class Solution:
    def shortest_subarray_with_all_values(self, A: List[int]) -> Tuple[int, int]:
        """
        Finds a shortest subarray containing every distinct value of A.

        Args:
            A: Input array

        Returns:
            (start, end) inclusive indices of a shortest such subarray,
            or (-1, -1) if A is empty

        Time Complexity: O(n)
        Space Complexity: O(d) where d is the number of distinct values
        """
        # TODO: Implement shortest subarray covering all distinct values
        pass


def _is_valid(A: List[int], result: Tuple[int, int], length: int) -> bool:
    """Checks that result covers all distinct values and has the given length."""
    start, end = result
    if not (0 <= start <= end < len(A)):
        return False
    return end - start + 1 == length and set(A[start:end + 1]) == set(A)


def test_shortest_subarray_with_all_values():
    """Test cases for shortest subarray covering all distinct values"""
    solution = Solution()

    # Test case 1: Two tied windows of length 3
    A1 = [1, 2, 2, 3, 1, 3, 2]
    assert _is_valid(A1, tuple(solution.shortest_subarray_with_all_values(A1)), 3)
    print("✓ Test 1 passed: [1, 2, 2, 3, 1, 3, 2] -> length 3")

    # Test case 2: Single distinct value
    assert _is_valid([5, 5, 5], tuple(solution.shortest_subarray_with_all_values([5, 5, 5])), 1)
    print("✓ Test 2 passed: All equal -> length 1")

    # Test case 3: Empty array
    assert tuple(solution.shortest_subarray_with_all_values([])) == (-1, -1)
    print("✓ Test 3 passed: Empty array -> (-1, -1)")

    # Test case 4: All distinct, whole array needed
    assert tuple(solution.shortest_subarray_with_all_values([4, 1, 3])) == (0, 2)
    print("✓ Test 4 passed: All distinct -> (0, 2)")

    # Test case 5: Unique answer in the middle
    A5 = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1]
    assert tuple(solution.shortest_subarray_with_all_values(A5)) == (2, 5)
    print("✓ Test 5 passed: Middle window -> (2, 5)")

    # Test case 6: Rare value at the end forces a long window
    A6 = [1, 2, 1, 2, 1, 2, 3]
    assert tuple(solution.shortest_subarray_with_all_values(A6)) == (4, 6)
    print("✓ Test 6 passed: Rare value at the end -> (4, 6)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shortest_subarray_with_all_values()
