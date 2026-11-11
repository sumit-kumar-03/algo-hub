"""
EPI 13.2 - Merge Two Sorted Arrays

Problem:
You are given two sorted integer arrays A and B. A holds m real entries
followed by enough empty slots (None) to also fit the n entries of B. Update A
in place so that its first m + n entries are the combined entries of both
arrays in sorted order.

Constraints:
- 0 <= m, n <= 10^5
- len(A) >= m + n
- O(m + n) time, O(1) extra space

How it works (fill from the back):
1. Use three indices: a = m - 1, b = n - 1, write = m + n - 1
2. While both a and b are valid, copy the larger of A[a] and B[b] to
   A[write] and move that index and write one step left
3. Copy any remaining entries of B (remaining entries of A are already in
   place)
4. Writing from the end never overwrites an unprocessed entry of A, so there
   is no need to shift elements

Example 1:
Input: A = [5, 13, 17, None, None, None, None, None], m = 3,
       B = [3, 7, 11, 19], n = 4
Output: A = [3, 5, 7, 11, 13, 17, 19, None]

Example 2:
Input: A = [None, None], m = 0, B = [1, 2], n = 2
Output: A = [1, 2]
"""

from typing import List, Optional


class Solution:
    def merge_two_sorted_arrays(
        self, A: List[Optional[int]], m: int, B: List[int], n: int
    ) -> None:
        """
        Merges sorted B into sorted A in place.

        Args:
            A: Sorted array whose first m entries are valid, with room for n more
            m: Number of valid entries in A
            B: Sorted array
            n: Number of entries in B

        Returns:
            None; A[:m + n] holds the merged sorted entries afterward

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place merge of two sorted arrays
        pass


def test_merge_two_sorted_arrays():
    """Test cases for in-place merge of two sorted arrays"""
    solution = Solution()

    # Test case 1: Book example
    A1 = [5, 13, 17, None, None, None, None, None]
    solution.merge_two_sorted_arrays(A1, 3, [3, 7, 11, 19], 4)
    assert A1[:7] == [3, 5, 7, 11, 13, 17, 19]
    print("✓ Test 1 passed: Book example -> [3, 5, 7, 11, 13, 17, 19]")

    # Test case 2: A has no real entries
    A2 = [None, None]
    solution.merge_two_sorted_arrays(A2, 0, [1, 2], 2)
    assert A2 == [1, 2]
    print("✓ Test 2 passed: Empty A")

    # Test case 3: B is empty
    A3 = [1, 4, 9]
    solution.merge_two_sorted_arrays(A3, 3, [], 0)
    assert A3 == [1, 4, 9]
    print("✓ Test 3 passed: Empty B")

    # Test case 4: All of B is smaller than A
    A4 = [10, 20, None, None, None]
    solution.merge_two_sorted_arrays(A4, 2, [1, 2, 3], 3)
    assert A4 == [1, 2, 3, 10, 20]
    print("✓ Test 4 passed: B entirely before A")

    # Test case 5: All of B is larger than A
    A5 = [1, 2, None, None]
    solution.merge_two_sorted_arrays(A5, 2, [8, 9], 2)
    assert A5 == [1, 2, 8, 9]
    print("✓ Test 5 passed: B entirely after A")

    # Test case 6: Duplicates and negative numbers
    A6 = [-5, 0, 0, 7, None, None, None]
    solution.merge_two_sorted_arrays(A6, 4, [-5, 0, 8], 3)
    assert A6 == [-5, -5, 0, 0, 0, 7, 8]
    print("✓ Test 6 passed: Duplicates and negatives")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_two_sorted_arrays()
