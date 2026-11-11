"""
EPI 13.2 Extra Variant - Count Cross Inversions Between Two Sorted Arrays
(Practice problem, not in the book. Difficulty: Medium)
Builds on: walking two sorted arrays in merge order; instead of copying the
smaller value, you count how many entries it jumps over. (This is the
counting step that turns merge sort into an inversion counter.)

Problem:
Given two arrays A and B, each sorted in ascending order, count the pairs
(i, j) with A[i] > B[j]. Equal values do not count.

Constraints:
- 0 <= len(A), len(B) <= 10^5
- O(m + n) time, O(1) extra space; checking every pair is O(mn)

How it works (merge walk):
1. i, j = 0, 0
2. While both arrays have entries left:
   - If B[j] < A[i], then B[j] is smaller than A[i] and every later entry
     of A, so it forms len(A) - i pairs; add that and advance j
   - Otherwise (A[i] <= B[j]) advance i: A[i] is not larger than B[j] or
     any later entry of B
3. Once A runs out, the remaining B entries form no more pairs

Example 1:
Input: A = [2, 5, 8], B = [1, 5, 6]
Output: 5
Explanation: Pairs are (2,1), (5,1), (8,1), (8,5), (8,6).

Example 2:
Input: A = [1, 2], B = [3, 4]
Output: 0
"""

from typing import List


class Solution:
    def count_cross_inversions(self, A: List[int], B: List[int]) -> int:
        """
        Counts pairs (i, j) with A[i] > B[j] for sorted A and B.

        Args:
            A: First sorted array
            B: Second sorted array

        Returns:
            Number of pairs where the A entry exceeds the B entry

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement merge-walk inversion counting
        pass


def test_count_cross_inversions():
    """Test cases for cross inversions between sorted arrays"""
    solution = Solution()

    # Test case 1: Example with a tie that doesn't count
    assert solution.count_cross_inversions([2, 5, 8], [1, 5, 6]) == 5
    print("✓ Test 1 passed: -> 5")

    # Test case 2: A entirely smaller
    assert solution.count_cross_inversions([1, 2], [3, 4]) == 0
    print("✓ Test 2 passed: A before B -> 0")

    # Test case 3: A entirely larger
    assert solution.count_cross_inversions([7, 8, 9], [1, 2]) == 6
    print("✓ Test 3 passed: A after B -> m * n = 6")

    # Test case 4: Empty arrays
    assert solution.count_cross_inversions([], [1, 2]) == 0
    assert solution.count_cross_inversions([1, 2], []) == 0
    print("✓ Test 4 passed: Empty -> 0")

    # Test case 5: All equal values
    assert solution.count_cross_inversions([3, 3, 3], [3, 3]) == 0
    print("✓ Test 5 passed: All equal -> 0")

    # Test case 6: Duplicates and negatives
    assert solution.count_cross_inversions([-1, -1, 4], [-2, -1, 0, 4]) == 5
    print("✓ Test 6 passed: Duplicates and negatives -> 5")

    # Test case 7: Larger arrays versus brute force
    A = sorted((i * 31) % 101 for i in range(120))
    B = sorted((i * 17) % 97 for i in range(110))
    expected = sum(1 for a in A for b in B if a > b)
    assert solution.count_cross_inversions(A, B) == expected
    print("✓ Test 7 passed: Matches brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_cross_inversions()
