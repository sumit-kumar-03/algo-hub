"""
EPI 5.5 - Delete Duplicates from a Sorted Array

Problem:
Given a sorted array, remove repeated values in place so that each
distinct value appears once, shifted left to fill the gaps. Return the
number of valid entries k; A[:k] must hold the distinct values in sorted
order, and anything after index k - 1 can be arbitrary. Library helpers
that do this for you are not allowed.

Constraints:
- 0 <= len(A) <= 10^5
- A is sorted in non-decreasing order
- Must run in O(n) time and O(1) extra space

How it works (read pointer and write pointer):
1. If A is empty, return 0
2. write_index = 1
3. For i from 1 to n - 1: if A[i] != A[write_index - 1], copy A[i] to
   A[write_index] and advance write_index
4. Return write_index

Example 1:
Input: A = [2, 3, 5, 5, 7, 11, 11, 11, 13]
Output: 6, with A[:6] == [2, 3, 5, 7, 11, 13]
Explanation: The repeated 5 and 11s are removed.

Example 2:
Input: A = [1, 1, 1]
Output: 1, with A[:1] == [1]
Explanation: Only one distinct value.
"""

from typing import List


class Solution:
    def delete_duplicates(self, A: List[int]) -> int:
        """
        Removes duplicates from a sorted array in place.

        Args:
            A: Sorted list of integers (modified in place)

        Returns:
            Number of valid entries k; A[:k] holds the distinct values

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place duplicate deletion
        pass


def test_delete_duplicates():
    """Test cases for delete duplicates implementation"""
    solution = Solution()

    # Test case 1: Book example
    A1 = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    k1 = solution.delete_duplicates(A1)
    assert k1 == 6 and A1[:k1] == [2, 3, 5, 7, 11, 13]
    print(f"✓ Test 1 passed: k = {k1}, A[:k] = {A1[:k1]}")

    # Test case 2: Empty array
    A2: List[int] = []
    assert solution.delete_duplicates(A2) == 0
    print("✓ Test 2 passed: Empty array -> 0")

    # Test case 3: All equal
    A3 = [1, 1, 1]
    k3 = solution.delete_duplicates(A3)
    assert k3 == 1 and A3[:k3] == [1]
    print("✓ Test 3 passed: [1, 1, 1] -> k = 1")

    # Test case 4: Already distinct
    A4 = [-3, 0, 4, 9]
    k4 = solution.delete_duplicates(A4)
    assert k4 == 4 and A4[:k4] == [-3, 0, 4, 9]
    print("✓ Test 4 passed: No duplicates -> unchanged")

    # Test case 5: Duplicates at both ends, negative values
    A5 = [-2, -2, -1, 0, 0, 0, 5, 5]
    k5 = solution.delete_duplicates(A5)
    assert k5 == 4 and A5[:k5] == [-2, -1, 0, 5]
    print(f"✓ Test 5 passed: k = {k5}, A[:k] = {A5[:k5]}")

    # Test case 6: Single element
    A6 = [42]
    assert solution.delete_duplicates(A6) == 1 and A6 == [42]
    print("✓ Test 6 passed: Single element -> 1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_delete_duplicates()
