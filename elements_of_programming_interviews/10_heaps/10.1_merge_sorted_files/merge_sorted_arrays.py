"""
EPI 10.1 - Merge Sorted Files

Problem:
Given k arrays, each sorted in ascending order, merge them into a single
sorted array. (The book frames this as merging sorted stock-trade log files.)

Constraints:
- 0 <= k <= 10^3, total elements n <= 10^5
- Use a min-heap of size k: O(n log k) time, O(k) extra space
- Do not just concatenate and call sorted()

How it works:
1. Push (first element, array index) of each non-empty array onto a min-heap,
   along with an iterator for that array
2. While the heap is not empty:
   - Pop the smallest (value, index) and append value to the result
   - Push the next element from the same array, if any
3. Return the result

Example 1:
Input: [[3, 5, 7], [0, 6], [0, 6, 28]]
Output: [0, 0, 3, 5, 6, 6, 7, 28]

Example 2:
Input: [[], [1]]
Output: [1]
"""

from typing import List


class Solution:
    def merge_sorted_arrays(self, sorted_arrays: List[List[int]]) -> List[int]:
        """
        Merges k sorted arrays into one sorted array using a min-heap.

        Args:
            sorted_arrays: List of arrays, each sorted in ascending order

        Returns:
            A single sorted array containing every element

        Time Complexity: O(n log k)
        Space Complexity: O(k) extra, excluding the output
        """
        # TODO: Implement k-way merge with heapq
        pass


def test_merge_sorted_arrays():
    """Test cases for merging k sorted arrays"""
    solution = Solution()

    # Test case 1: Three arrays with overlaps
    result1 = solution.merge_sorted_arrays([[3, 5, 7], [0, 6], [0, 6, 28]])
    assert result1 == [0, 0, 3, 5, 6, 6, 7, 28]
    print(f"✓ Test 1 passed: Three arrays -> {result1}")

    # Test case 2: No arrays
    assert solution.merge_sorted_arrays([]) == []
    print("✓ Test 2 passed: No arrays")

    # Test case 3: Some arrays empty
    assert solution.merge_sorted_arrays([[], [1], []]) == [1]
    print("✓ Test 3 passed: Empty arrays skipped")

    # Test case 4: Single array
    assert solution.merge_sorted_arrays([[1, 2, 3]]) == [1, 2, 3]
    print("✓ Test 4 passed: Single array")

    # Test case 5: Negatives and duplicates
    result5 = solution.merge_sorted_arrays([[-5, 0, 0], [-5, 2], [-10, 10]])
    assert result5 == [-10, -5, -5, 0, 0, 2, 10]
    print(f"✓ Test 5 passed: Negatives and duplicates -> {result5}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_sorted_arrays()
