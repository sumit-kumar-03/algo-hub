"""
EPI 10.1 Extra Variant - kth Smallest Sum Picking One Entry per Row
(Practice problem, not in the book. Difficulty: Hard)
Builds on: heap-driven merging of sorted sequences, applied repeatedly so
that each round merges a running list of best sums with the next row.

Problem:
Given a matrix with m rows, each sorted in ascending order (rows may have
different lengths), build
a "pick" by choosing exactly one entry from every row; its sum is the total
of the chosen entries. Different choices of column indices count as
different picks even if their sums are equal. Return the kth smallest sum
over all possible picks.

Constraints:
- 1 <= m <= 40; 1 <= row length <= 40; 1 <= k <= number of picks, k <= 200
- Values may be negative and may repeat
- O(m * k log k) time and O(k) extra space; do not enumerate all picks

How it works (fold rows with "k smallest pair sums"):
1. Keep best: a sorted list of the k smallest sums using the rows seen so
   far (start with best = the first row, truncated to k)
2. To add the next row R, you need the k smallest values of b + r over
   b in best and r in R. Both lists are sorted, so this is a k-way merge of
   implicit sorted rows: seed a min-heap with (best[i] + R[0], i, 0) and
   pop k times, pushing (best[i] + R[j + 1], i, j + 1) after each pop
3. Keeping only k sums per round is safe: any sum outside the k smallest
   partial sums cannot help form one of the k smallest totals
4. After the last row, return best[k - 1]

Example 1:
Input: matrix = [[1, 3, 11], [2, 4, 6]], k = 5
Output: 7
Explanation: The sums in order are 3, 5, 5, 7, 7, 9, ...

Example 2:
Input: matrix = [[1, 10, 10], [1, 4, 5], [2, 3, 6]], k = 7
Output: 9
Explanation: The smallest sums are 4, 5, 7, 8, 8, 9, 9, ...
"""

from typing import List


class Solution:
    def kth_smallest_pick_sum(self, matrix: List[List[int]], k: int) -> int:
        """
        Returns the kth smallest sum of picks with one entry per row.

        Args:
            matrix: Matrix whose rows are sorted ascending
            k: 1-based rank

        Returns:
            The kth smallest pick sum

        Time Complexity: O(m * k log k)
        Space Complexity: O(k)
        """
        # TODO: Implement by merging rows with a min-heap, keeping k sums
        pass


def _brute(matrix: List[List[int]], k: int) -> int:
    sums = [0]
    for row in matrix:
        sums = [s + v for s in sums for v in row]
    return sorted(sums)[k - 1]


def test_kth_smallest_pick_sum():
    """Test cases for kth smallest pick sum"""
    solution = Solution()

    # Test case 1: Two rows (this is the pair-sum problem)
    assert solution.kth_smallest_pick_sum([[1, 3, 11], [2, 4, 6]], 5) == 7
    print("✓ Test 1 passed: Two rows, k = 5")

    # Test case 2: Three rows
    assert solution.kth_smallest_pick_sum([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 7) == 9
    print("✓ Test 2 passed: Three rows, k = 7")

    # Test case 3: Single row
    assert solution.kth_smallest_pick_sum([[-4, 0, 9]], 2) == 0
    print("✓ Test 3 passed: Single row")

    # Test case 4: Single column (only one pick exists)
    assert solution.kth_smallest_pick_sum([[5], [-2], [7]], 1) == 10
    print("✓ Test 4 passed: Single column")

    # Test case 5: Equal entries create many equal sums
    m5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert solution.kth_smallest_pick_sum(m5, 27) == 3
    print("✓ Test 5 passed: All entries equal, last rank")

    # Test case 6: Uneven rows with negatives, every k vs. brute force
    m6 = [[-5, -1, 3], [-2, 0, 0, 8], [1, 4]]
    for k in range(1, 25):
        assert solution.kth_smallest_pick_sum(m6, k) == _brute(m6, k)
    print("✓ Test 6 passed: Negatives, all ranks")

    # Test case 7: Larger matrix, checked against all 6^7 picks
    m7 = [sorted((r * 13 + c * 29) % 37 - 18 for c in range(6)) for r in range(7)]
    assert solution.kth_smallest_pick_sum(m7, 150) == _brute(m7, 150)
    print("✓ Test 7 passed: 7 x 6 matrix, k = 150")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_smallest_pick_sum()
