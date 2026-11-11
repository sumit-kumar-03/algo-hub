"""
EPI 10.4 Variant - Online kth Largest Element

Problem:
Read a sequence of numbers whose length is not known in advance. Starting
with the kth number read, report the kth largest number seen so far after
each new number arrives. Use only O(k) extra storage. (Also think about which
inputs are the worst case for your approach.)

Constraints:
- 1 <= k; the sequence may be shorter than k (then nothing is reported)
- O(n log k) time, O(k) extra space (excluding the output list)
- Read the sequence only once

How it works:
1. Keep a min-heap of the k largest numbers seen so far
2. For each number: push it; if the heap has k + 1 entries, pop the minimum
3. Once the heap holds k numbers, its top (minimum) is the kth largest;
   append it to the output
4. Worst case: an increasing sequence, since every new number displaces
   the heap's minimum and triggers a full O(log k) push/pop

Example 1:
Input: sequence = [5, 1, 7, 3, 9, 2], k = 3
Output: [1, 3, 5, 5]
Explanation: After 5,1,7 -> 1; after 3 -> 3; after 9 -> 5; after 2 -> 5.

Example 2:
Input: sequence = [4, 8], k = 3
Output: []
Explanation: Fewer than k numbers were read.
"""

from typing import Iterable, List


class Solution:
    def kth_largest_online(self, sequence: Iterable[int], k: int) -> List[int]:
        """
        Reports the running kth largest element of a stream.

        Args:
            sequence: Iterable of numbers, read once
            k: Rank to report (1 = largest)

        Returns:
            The kth largest value after reading each element, starting
            with the kth element

        Time Complexity: O(n log k)
        Space Complexity: O(k) extra, excluding the output
        """
        # TODO: Implement with a min-heap of size k
        pass


def test_kth_largest_online():
    """Test cases for the online kth largest element"""
    solution = Solution()

    # Test case 1: Mixed sequence
    result1 = solution.kth_largest_online(iter([5, 1, 7, 3, 9, 2]), 3)
    assert result1 == [1, 3, 5, 5]
    print(f"✓ Test 1 passed: Mixed sequence -> {result1}")

    # Test case 2: Fewer than k elements
    assert solution.kth_largest_online(iter([4, 8]), 3) == []
    print("✓ Test 2 passed: Fewer than k elements")

    # Test case 3: k = 1 is the running maximum
    assert solution.kth_largest_online(iter([2, 5, 1, 6, 3]), 1) == [2, 5, 5, 6, 6]
    print("✓ Test 3 passed: k = 1 running max")

    # Test case 4: Increasing sequence (worst case)
    assert solution.kth_largest_online(iter(range(1, 8)), 2) == [1, 2, 3, 4, 5, 6]
    print("✓ Test 4 passed: Increasing sequence")

    # Test case 5: Duplicates and negatives
    result5 = solution.kth_largest_online(iter([-1, -1, 3, 3, -5, 0]), 2)
    assert result5 == [-1, -1, 3, 3, 3]
    print(f"✓ Test 5 passed: Duplicates/negatives -> {result5}")

    # Test case 6: Generator input, k equal to length
    assert solution.kth_largest_online((x for x in [9, 4, 6]), 3) == [4]
    print("✓ Test 6 passed: k equals stream length")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_largest_online()
