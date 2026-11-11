"""
EPI 10.1 Extra Variant - kth Smallest Entry in a Row-Sorted Matrix
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the k-way merge with a min-heap, stopped early once enough
elements have been produced.

Problem:
Given an m x n matrix in which every row is sorted in ascending order (and,
in some inputs, every column too), and an integer k, return the kth
smallest entry of the matrix (1-based, counting duplicates separately).

Constraints:
- 1 <= m, n <= 300; 1 <= k <= m * n
- Values may be negative and may repeat
- O(k log m) time and O(m) extra space with a heap; do not flatten and sort
  (Stretch: when columns are also sorted, a binary search on the value
  range gives O(n log(max - min)) time)

How it works (lazy k-way merge of the rows):
1. Push (matrix[r][0], r, 0) for every row r onto a min-heap
2. Pop k - 1 times; after popping (v, r, c), push (matrix[r][c + 1], r,
   c + 1) if that column exists
3. The top of the heap is now the kth smallest

Example 1:
Input: matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
Output: 13
Explanation: In sorted order: 1, 5, 9, 10, 11, 12, 13, 13, 15.

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""

from typing import List


class Solution:
    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Returns the kth smallest entry of a matrix with sorted rows.

        Args:
            matrix: Matrix whose rows are sorted ascending
            k: 1-based rank

        Returns:
            The kth smallest value

        Time Complexity: O(k log m)
        Space Complexity: O(m)
        """
        # TODO: Implement with a min-heap over the rows
        pass


def test_kth_smallest():
    """Test cases for kth smallest in a sorted matrix"""
    solution = Solution()

    # Test case 1: Classic row- and column-sorted matrix
    m1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    assert solution.kth_smallest(m1, 8) == 13
    print("✓ Test 1 passed: k = 8 -> 13")

    # Test case 2: Every rank of the same matrix
    expected2 = [1, 5, 9, 10, 11, 12, 13, 13, 15]
    assert [solution.kth_smallest(m1, k) for k in range(1, 10)] == expected2
    print("✓ Test 2 passed: All ranks k = 1..9")

    # Test case 3: Single entry
    assert solution.kth_smallest([[-5]], 1) == -5
    print("✓ Test 3 passed: 1 x 1 matrix")

    # Test case 4: Rows sorted, columns not sorted
    m4 = [[7, 8, 20], [1, 2, 3], [4, 4, 50]]
    assert solution.kth_smallest(m4, 4) == 4
    assert solution.kth_smallest(m4, 6) == 7
    assert solution.kth_smallest(m4, 9) == 50
    print("✓ Test 4 passed: Only rows sorted")

    # Test case 5: Single row and single column
    assert solution.kth_smallest([[-3, -1, 0, 0, 6]], 4) == 0
    assert solution.kth_smallest([[2], [-8], [5]], 2) == 2
    print("✓ Test 5 passed: Single row / single column")

    # Test case 6: Larger matrix with duplicates, checked against sorting
    m6 = [sorted((r * 31 + c * 17) % 50 - 25 for c in range(40)) for r in range(30)]
    flat = sorted(v for row in m6 for v in row)
    for k in (1, 37, 600, 1199, 1200):
        assert solution.kth_smallest(m6, k) == flat[k - 1]
    print("✓ Test 6 passed: 30 x 40 matrix")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_smallest()
