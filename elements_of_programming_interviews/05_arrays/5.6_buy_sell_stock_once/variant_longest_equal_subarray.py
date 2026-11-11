"""
EPI 5.6 Variant - Longest Subarray of Equal Entries

Problem:
Given an array of integers, return the length of the longest contiguous
subarray in which every entry is the same value.

Constraints:
- 0 <= len(A) <= 10^5 (return 0 for an empty array)
- Must run in O(n) time and O(1) extra space

How it works (track the current run):
1. best = 0, run = 0
2. For each index i: if i > 0 and A[i] == A[i - 1], run += 1; else run = 1
3. best = max(best, run)
4. Return best

Example 1:
Input: A = [1, 1, 2, 2, 2, 3, 2, 2]
Output: 3
Explanation: The run [2, 2, 2] at indices 2 to 4 is the longest.

Example 2:
Input: A = [4, 5, 6]
Output: 1
Explanation: No two neighbors are equal.
"""

from typing import List


class Solution:
    def longest_equal_subarray(self, A: List[int]) -> int:
        """
        Finds the length of the longest run of equal entries.

        Args:
            A: List of integers

        Returns:
            Length of the longest subarray whose entries are all equal

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement longest equal run
        pass


def test_longest_equal_subarray():
    """Test cases for longest equal subarray"""
    solution = Solution()

    # Test case 1: Longest run in the middle
    assert solution.longest_equal_subarray([1, 1, 2, 2, 2, 3, 2, 2]) == 3
    print("✓ Test 1 passed: [1, 1, 2, 2, 2, 3, 2, 2] -> 3")

    # Test case 2: All distinct
    assert solution.longest_equal_subarray([4, 5, 6]) == 1
    print("✓ Test 2 passed: All distinct -> 1")

    # Test case 3: Empty array
    assert solution.longest_equal_subarray([]) == 0
    print("✓ Test 3 passed: Empty -> 0")

    # Test case 4: Entire array equal
    assert solution.longest_equal_subarray([7] * 6) == 6
    print("✓ Test 4 passed: All equal -> 6")

    # Test case 5: Longest run at the end
    assert solution.longest_equal_subarray([3, 3, 1, 0, 0, 0, 0]) == 4
    print("✓ Test 5 passed: Run at the end -> 4")

    # Test case 6: Same value split into separate runs is not merged
    assert solution.longest_equal_subarray([5, 5, 1, 5, 5, 1, 5]) == 2
    print("✓ Test 6 passed: Separate runs of the same value -> 2")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_equal_subarray()
