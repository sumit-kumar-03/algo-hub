"""
EPI 12.9 - Find the Length of a Longest Contained Interval

Problem:
Given an array of integers, find the size of the largest subset of its
values that forms a run of consecutive integers, i.e., if two integers are in
the subset, every integer between them is too. Duplicates count once.

Constraints:
- 0 <= len(A) <= 10^5
- O(n) time (no sorting), O(n) space

How it works:
1. Put all values into a hash set of unprocessed entries
2. While the set is nonempty, remove any value a
3. Expand downward (a - 1, a - 2, ...) and upward (a + 1, a + 2, ...) while
   the neighbors are in the set, removing each one as you go
4. The run length is upper - lower - 1; keep the maximum

Example 1:
Input: A = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
Output: 6
Explanation: {-2, -1, 0, 1, 2, 3} is the largest such subset.

Example 2:
Input: A = [10, 5, 3, 11, 6, 100, 4]
Output: 4
Explanation: {3, 4, 5, 6}.
"""

from typing import List


class Solution:
    def longest_contained_range(self, A: List[int]) -> int:
        """
        Computes the size of the longest run of consecutive integers in A.

        Args:
            A: Array of integers (may contain duplicates)

        Returns:
            Size of the largest contained interval (0 for an empty array)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement longest contained interval
        pass


def test_longest_contained_range():
    """Test cases for longest contained interval"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.longest_contained_range([3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]) == 6
    print("✓ Test 1 passed: Book example -> 6")

    # Test case 2: Second book example
    assert solution.longest_contained_range([10, 5, 3, 11, 6, 100, 4]) == 4
    print("✓ Test 2 passed: [10, 5, 3, 11, 6, 100, 4] -> 4")

    # Test case 3: Empty array
    assert solution.longest_contained_range([]) == 0
    print("✓ Test 3 passed: Empty array -> 0")

    # Test case 4: Single element
    assert solution.longest_contained_range([7]) == 1
    print("✓ Test 4 passed: Single element -> 1")

    # Test case 5: Duplicates count once
    assert solution.longest_contained_range([1, 1, 2, 2, 3, 3]) == 3
    print("✓ Test 5 passed: Duplicates -> 3")

    # Test case 6: No two consecutive values
    assert solution.longest_contained_range([1, 3, 5, 7]) == 1
    print("✓ Test 6 passed: Gaps everywhere -> 1")

    # Test case 7: Large range in reverse order
    assert solution.longest_contained_range(list(range(1000, 0, -1)) + [5000]) == 1000
    print("✓ Test 7 passed: Reverse-ordered run -> 1000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_contained_range()
