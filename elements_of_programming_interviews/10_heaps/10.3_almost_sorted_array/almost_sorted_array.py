"""
EPI 10.3 - Sort an Almost-Sorted Array

Problem:
You receive a very long stream of numbers in which every number is at most k
positions away from where it belongs in sorted order (a "k-sorted" sequence).
Produce the numbers in sorted order. The input is an iterator, so you can only
read it once, front to back, and you should not buffer the whole thing.

Constraints:
- 0 <= k, stream length n <= 10^5
- Every element is at most k positions from its sorted position
- Use a min-heap of size k + 1: O(n log k) time, O(k) extra space
- Do not read the whole stream into a list and call sorted()

How it works:
1. Read the first k numbers into a min-heap
2. For every further number: push it onto the heap and pop the minimum into
   the result (once k + 1 numbers have been seen, the smallest among them
   must be the next number in sorted order)
3. When the stream runs out, pop the remaining heap elements into the result

Example 1:
Input: sequence = iter([3, -1, 2, 6, 4, 5, 8]), k = 2
Output: [-1, 2, 3, 4, 5, 6, 8]
Explanation: No number is more than 2 positions away from its sorted slot.

Example 2:
Input: sequence = iter([1, 2, 3]), k = 0
Output: [1, 2, 3]
Explanation: k = 0 means the input is already sorted.
"""

from typing import Iterator, List


class Solution:
    def sort_approximately_sorted_array(self, sequence: Iterator[int], k: int) -> List[int]:
        """
        Sorts a k-sorted stream using a bounded min-heap.

        Args:
            sequence: Iterator over the numbers (can only be consumed once)
            k: Maximum distance of any element from its sorted position

        Returns:
            The numbers in ascending order

        Time Complexity: O(n log k)
        Space Complexity: O(k) extra, excluding the output
        """
        # TODO: Implement with a min-heap of size k + 1
        pass


def test_sort_approximately_sorted_array():
    """Test cases for sorting an almost-sorted stream"""
    solution = Solution()

    # Test case 1: Book example
    result1 = solution.sort_approximately_sorted_array(iter([3, -1, 2, 6, 4, 5, 8]), 2)
    assert result1 == [-1, 2, 3, 4, 5, 6, 8]
    print(f"✓ Test 1 passed: Book example -> {result1}")

    # Test case 2: Already sorted, k = 0
    assert solution.sort_approximately_sorted_array(iter([1, 2, 3]), 0) == [1, 2, 3]
    print("✓ Test 2 passed: k = 0")

    # Test case 3: Empty stream
    assert solution.sort_approximately_sorted_array(iter([]), 3) == []
    print("✓ Test 3 passed: Empty stream")

    # Test case 4: k larger than the stream
    assert solution.sort_approximately_sorted_array(iter([2, 1]), 5) == [1, 2]
    print("✓ Test 4 passed: k larger than stream length")

    # Test case 5: Adjacent swaps with duplicates (k = 1)
    result5 = solution.sort_approximately_sorted_array(iter([2, 1, 4, 3, 3, 6, 5]), 1)
    assert result5 == [1, 2, 3, 3, 4, 5, 6]
    print(f"✓ Test 5 passed: Adjacent swaps -> {result5}")

    # Test case 6: Generator input, larger k-sorted sequence
    data = []
    for block in range(0, 100, 4):
        data.extend(reversed(range(block, block + 4)))  # each element <= 3 away
    result6 = solution.sort_approximately_sorted_array((x for x in data), 3)
    assert result6 == list(range(100))
    print("✓ Test 6 passed: Generator with 100 elements, k = 3")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_sort_approximately_sorted_array()
