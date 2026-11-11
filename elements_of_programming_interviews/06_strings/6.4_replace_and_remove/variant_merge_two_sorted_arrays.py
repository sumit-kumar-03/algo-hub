"""
EPI 6.4 Variant - Merge Two Sorted Arrays In Place

Problem:
You are given two arrays of integers sorted in ascending order, A with m
valid entries and B with n entries. A has room for m + n entries (the last
n slots are free). Merge B into A so that A holds all m + n values in
sorted order, using O(1) additional storage.

Constraints:
- len(A) == m + n, len(B) == n
- 0 <= m, n <= 10^4
- O(m + n) time, O(1) extra space

How it works:
1. Use three indices: the last valid entry of A, the last entry of B, and
   the last slot of A (where the next largest value is written)
2. While B still has entries, write the larger of A[i] and B[j] to the
   write slot and move the corresponding indices left
3. Any remaining A entries are already in place

Example 1:
Input: A = [3, 13, 17, 0, 0, 0], m = 3, B = [3, 7, 11], n = 3
Output: A == [3, 3, 7, 11, 13, 17]

Example 2:
Input: A = [0, 0], m = 0, B = [1, 2], n = 2
Output: A == [1, 2]
"""

from typing import List


class Solution:
    def merge_two_sorted_arrays(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Merges sorted B into sorted A in place.

        Args:
            A: Sorted array whose first m entries are valid and which has
               n free slots at the end
            m: Number of valid entries in A
            B: Sorted array of n entries
            n: Number of entries in B

        Returns:
            None; A is modified in place

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place merge from the back
        pass


def test_merge_two_sorted_arrays():
    """Test cases for merging two sorted arrays in place"""
    solution = Solution()

    # Test case 1: Interleaved values
    A1 = [3, 13, 17, 0, 0, 0]
    solution.merge_two_sorted_arrays(A1, 3, [3, 7, 11], 3)
    assert A1 == [3, 3, 7, 11, 13, 17]
    print("✓ Test 1 passed: [3, 13, 17] + [3, 7, 11]")

    # Test case 2: A has no valid entries
    A2 = [0, 0]
    solution.merge_two_sorted_arrays(A2, 0, [1, 2], 2)
    assert A2 == [1, 2]
    print("✓ Test 2 passed: Empty A")

    # Test case 3: B is empty
    A3 = [1, 2, 3]
    solution.merge_two_sorted_arrays(A3, 3, [], 0)
    assert A3 == [1, 2, 3]
    print("✓ Test 3 passed: Empty B")

    # Test case 4: All of B is smaller than A
    A4 = [5, 6, 0, 0, 0]
    solution.merge_two_sorted_arrays(A4, 2, [1, 2, 3], 3)
    assert A4 == [1, 2, 3, 5, 6]
    print("✓ Test 4 passed: B entirely before A")

    # Test case 5: All of B is larger than A
    A5 = [1, 2, 0, 0]
    solution.merge_two_sorted_arrays(A5, 2, [8, 9], 2)
    assert A5 == [1, 2, 8, 9]
    print("✓ Test 5 passed: B entirely after A")

    # Test case 6: Negatives and duplicates
    A6 = [-5, 0, 0, 4, 0, 0, 0]
    solution.merge_two_sorted_arrays(A6, 4, [-5, 0, 10], 3)
    assert A6 == [-5, -5, 0, 0, 0, 4, 10]
    print("✓ Test 6 passed: Negatives and duplicates")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_two_sorted_arrays()
