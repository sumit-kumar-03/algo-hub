"""
EPI 13.1 Extra Variant - Intersection of Two Sorted Interval Lists
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the two-pointer walk over two sorted arrays, where the "advance
the smaller one" rule becomes "advance the interval that ends first".

Problem:
You are given two lists of closed intervals [start, end]. Within each list
the intervals are sorted by start and pairwise disjoint (they do not even
touch). Return the list of intervals where the two lists overlap, sorted by
start. An overlap of a single point, such as [5, 5], counts.

Constraints:
- 0 <= len(A), len(B) <= 10^4
- start <= end for every interval
- O(m + n) time, O(1) extra space excluding the output

How it works (two pointers):
1. i, j = 0, 0
2. The overlap of A[i] and B[j] is [max(starts), min(ends)]; if that start
   is <= that end, append it
3. Advance the pointer whose interval ends first: it cannot overlap any
   later interval of the other list
4. Stop when either list is exhausted

Example 1:
Input: A = [[1, 4], [6, 9]], B = [[2, 7], [9, 12]]
Output: [[2, 4], [6, 7], [9, 9]]

Example 2:
Input: A = [[1, 3]], B = [[4, 6]]
Output: []
"""

from typing import List


class Solution:
    def interval_intersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        """
        Computes the overlaps between two sorted lists of disjoint intervals.

        Args:
            A: Sorted, pairwise-disjoint closed intervals
            B: Sorted, pairwise-disjoint closed intervals

        Returns:
            Sorted list of overlap intervals [start, end]

        Time Complexity: O(m + n)
        Space Complexity: O(1) extra, excluding the output
        """
        # TODO: Implement two-pointer interval intersection
        pass


def test_interval_intersection():
    """Test cases for interval list intersections"""
    solution = Solution()

    # Test case 1: Several overlaps including a single point
    assert solution.interval_intersection([[1, 4], [6, 9]], [[2, 7], [9, 12]]) == [[2, 4], [6, 7], [9, 9]]
    print("✓ Test 1 passed: -> [[2, 4], [6, 7], [9, 9]]")

    # Test case 2: No overlap
    assert solution.interval_intersection([[1, 3]], [[4, 6]]) == []
    print("✓ Test 2 passed: Disjoint -> []")

    # Test case 3: Empty list
    assert solution.interval_intersection([], [[1, 2]]) == []
    assert solution.interval_intersection([], []) == []
    print("✓ Test 3 passed: Empty -> []")

    # Test case 4: One long interval covers many short ones
    A = [[0, 100]]
    B = [[1, 2], [5, 5], [10, 20], [99, 150]]
    assert solution.interval_intersection(A, B) == [[1, 2], [5, 5], [10, 20], [99, 100]]
    print("✓ Test 4 passed: Long interval vs many short ones")

    # Test case 5: Identical lists
    A = [[-5, -2], [0, 0], [3, 8]]
    assert solution.interval_intersection(A, [list(x) for x in A]) == A
    print("✓ Test 5 passed: Identical lists (with negatives and a point)")

    # Test case 6: Touching endpoints across lists
    assert solution.interval_intersection([[1, 5], [8, 10]], [[5, 8]]) == [[5, 5], [8, 8]]
    print("✓ Test 6 passed: Touching endpoints -> single points")

    # Test case 7: Brute-force check over integer points
    A = [[0, 3], [6, 10], [14, 14], [17, 25], [30, 31]]
    B = [[2, 7], [9, 15], [20, 22], [24, 33]]
    covered = sorted(set(x for s, e in A for x in range(s, e + 1)) &
                     set(x for s, e in B for x in range(s, e + 1)))
    result = solution.interval_intersection(A, B)
    points = sorted(x for s, e in result for x in range(s, e + 1))
    assert points == covered
    assert result == sorted(result)
    print("✓ Test 7 passed: Covers exactly the shared integer points")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_interval_intersection()
