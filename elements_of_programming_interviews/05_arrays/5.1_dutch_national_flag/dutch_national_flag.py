"""
EPI 5.1 - The Dutch National Flag Problem

Problem:
Given an array A and an index i, rearrange A in place so that all elements
less than A[i] (the pivot) come first, followed by all elements equal to the
pivot, followed by all elements greater than the pivot.

Constraints:
- Must run in O(n) time and use O(1) extra space
- 1 <= len(A) <= 10^5
- 0 <= pivot_index < len(A)

How it works (single pass, three regions):
1. Keep three pointers: smaller = 0, equal = 0, larger = len(A)
2. While equal < larger:
   - A[equal] < pivot: swap A[smaller], A[equal]; advance both
   - A[equal] == pivot: advance equal
   - A[equal] > pivot: decrement larger; swap A[equal], A[larger]
3. Regions are: [0, smaller) less, [smaller, equal) equal, [larger, n) greater

Example 1:
Input: A = [0, 1, 2, 0, 2, 1, 1], pivot_index = 3 (pivot = 0)
Output: [0, 0, 1, 2, 2, 1, 1] (any order where all 0s come first is valid)

Example 2:
Input: A = [0, 1, 2, 0, 2, 1, 1], pivot_index = 2 (pivot = 2)
Output: [0, 1, 0, 1, 1, 2, 2] (any order with all 2s last is valid)
"""

from typing import List


class Solution:
    def dutch_flag_partition(self, pivot_index: int, A: List[int]) -> None:
        """
        Partitions A in place around A[pivot_index].

        Args:
            pivot_index: Index of the pivot element in A
            A: Array to partition in place

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Dutch national flag partition
        pass


def is_partitioned(A: List[int], pivot: int) -> bool:
    """Checks that A is ordered as: < pivot, then == pivot, then > pivot."""
    stage = 0  # 0: less, 1: equal, 2: greater
    for x in A:
        current = 0 if x < pivot else 1 if x == pivot else 2
        if current < stage:
            return False
        stage = current
    return True


def test_dutch_flag_partition():
    """Test cases for Dutch national flag implementation"""
    solution = Solution()

    # Test case 1: Pivot is the smallest value
    A1 = [0, 1, 2, 0, 2, 1, 1]
    original1 = sorted(A1)
    solution.dutch_flag_partition(3, A1)
    assert sorted(A1) == original1 and is_partitioned(A1, 0)
    assert A1[:2] == [0, 0]
    print(f"✓ Test 1 passed: Pivot 0 -> {A1}")

    # Test case 2: Pivot is the middle value
    A2 = [0, 1, 2, 0, 2, 1, 1]
    solution.dutch_flag_partition(1, A2)
    assert sorted(A2) == original1 and is_partitioned(A2, 1)
    assert A2 != [0, 1, 2, 0, 2, 1, 1]
    print(f"✓ Test 2 passed: Pivot 1 -> {A2}")

    # Test case 3: Pivot is the largest value
    A3 = [0, 1, 2, 0, 2, 1, 1]
    solution.dutch_flag_partition(2, A3)
    assert sorted(A3) == original1 and is_partitioned(A3, 2)
    assert A3[-2:] == [2, 2]
    print(f"✓ Test 3 passed: Pivot 2 -> {A3}")

    # Test case 4: Single element
    A4 = [7]
    solution.dutch_flag_partition(0, A4)
    assert A4 == [7]
    print("✓ Test 4 passed: Single element")

    # Test case 5: Reverse sorted with negatives
    A5 = [5, 3, 0, -2, -4]
    solution.dutch_flag_partition(2, A5)
    assert sorted(A5) == [-4, -2, 0, 3, 5] and is_partitioned(A5, 0)
    assert A5[2] == 0
    print(f"✓ Test 5 passed: Negatives -> {A5}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_dutch_flag_partition()
