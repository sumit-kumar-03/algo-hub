"""
EPI 11.3 Variant - Search a Cyclically Sorted Array for k

Problem:
Given a cyclically sorted array of distinct elements and a key k, return the
index of k, or -1 if it is not present.

Constraints:
- 0 <= len(A) <= 10^5
- All elements are distinct
- Must run in O(log n) time

How it works (one approach):
1. Use the 11.3 binary search to find the index s of the smallest element
2. The array is then sorted when read starting at s and wrapping around
3. Binary search over logical positions 0..n-1, mapping position m to
   physical index (m + s) % n
(Alternative: a single binary search that decides which half is sorted.)

Example 1:
Input: A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368], k = 220
Output: 6

Example 2:
Input: A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368], k = 500
Output: -1
"""

from typing import List


class Solution:
    def search_cyclic(self, A: List[int], k: int) -> int:
        """
        Finds k in a cyclically sorted array.

        Args:
            A: Cyclically sorted array of distinct elements
            k: Key to search for

        Returns:
            Index of k, or -1 if absent

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on a rotated array
        pass


def test_search_cyclic():
    """Test cases for searching a cyclically sorted array"""
    solution = Solution()
    A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]

    # Test case 1: Key in the right part
    assert solution.search_cyclic(A, 220) == 6
    print("✓ Test 1 passed: k = 220 -> 6")

    # Test case 2: Key in the left part
    assert solution.search_cyclic(A, 550) == 2
    print("✓ Test 2 passed: k = 550 -> 2")

    # Test case 3: Absent key
    assert solution.search_cyclic(A, 500) == -1
    print("✓ Test 3 passed: Absent key")

    # Test case 4: Empty array
    assert solution.search_cyclic([], 1) == -1
    print("✓ Test 4 passed: Empty array")

    # Test case 5: Boundary elements
    assert solution.search_cyclic(A, 378) == 0
    assert solution.search_cyclic(A, 368) == 9
    assert solution.search_cyclic(A, 103) == 4
    print("✓ Test 5 passed: First, last, and minimum")

    # Test case 6: Every key in every rotation
    base = list(range(1, 60, 4))
    for shift in range(len(base)):
        rotated = base[shift:] + base[:shift]
        for i, v in enumerate(rotated):
            assert solution.search_cyclic(rotated, v) == i
        assert solution.search_cyclic(rotated, 0) == -1
        assert solution.search_cyclic(rotated, 2) == -1
    print("✓ Test 6 passed: All rotations, all keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_search_cyclic()
