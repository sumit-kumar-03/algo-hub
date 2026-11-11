"""
EPI 17.4 Extra Variant - List Every Distinct 3-Sum Triplet
(Practice problem, not in the book. Difficulty: Medium)
Builds on: sort + two pointers per first element, now continuing after a
hit and skipping repeated values so each triplet is reported once.

Problem:
Given an array of integers A and a target t, return every distinct triplet
of values (a, b, c) with a <= b <= c that can be formed from three
different positions of A and satisfies a + b + c == t. Each triplet of
values must appear exactly once, even if it can be formed from several
choices of positions. Return the triplets as tuples, sorted in increasing
lexicographic order.

Constraints:
- 0 <= len(A) <= 3000, -10^5 <= A[i], t <= 10^5
- O(n^2) time and O(1) extra space besides sorting and the output

How it works (sort, two pointers, skip duplicates):
1. Sort A
2. For each k, skip it if A[k] == A[k - 1] (same first value already done)
3. i = k + 1, j = n - 1; while i < j with s = A[k] + A[i] + A[j]:
   - s == t: record (A[k], A[i], A[j]), then move i past every copy of
     A[i] and j past every copy of A[j]
   - s < t: i += 1; s > t: j -= 1
4. Triplets come out already in sorted order

Example 1:
Input: A = [-1, 0, 1, 2, -1, -4], t = 0
Output: [(-1, -1, 2), (-1, 0, 1)]

Example 2:
Input: A = [0, 0, 0, 0], t = 0
Output: [(0, 0, 0)]
"""

from typing import List, Tuple


class Solution:
    def all_unique_triplets(self, A: List[int], t: int) -> List[Tuple[int, int, int]]:
        """
        Lists the distinct value triplets from distinct positions summing to t.

        Args:
            A: Input integers
            t: Target sum

        Returns:
            Sorted list of sorted triplets, each appearing once

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond sorting and the output
        """
        # TODO: Implement sort + two pointers with duplicate skipping
        pass


def test_all_unique_triplets():
    """Test cases for listing distinct 3-sum triplets"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.all_unique_triplets([-1, 0, 1, 2, -1, -4], 0) == [(-1, -1, 2), (-1, 0, 1)]
    print("✓ Test 1 passed: [-1, 0, 1, 2, -1, -4], 0 -> [(-1, -1, 2), (-1, 0, 1)]")

    # Test case 2: All zeros reported once
    assert solution.all_unique_triplets([0, 0, 0, 0], 0) == [(0, 0, 0)]
    print("✓ Test 2 passed: [0, 0, 0, 0], 0 -> [(0, 0, 0)]")

    # Test case 3: Too few entries, and no match
    assert solution.all_unique_triplets([], 0) == []
    assert solution.all_unique_triplets([1, 2], 3) == []
    assert solution.all_unique_triplets([1, 2, 3], 7) == []
    print("✓ Test 3 passed: no triplets -> []")

    # Test case 4: A value may repeat only as often as it appears
    assert solution.all_unique_triplets([3, 3, 1], 9) == []
    assert solution.all_unique_triplets([3, 3, 3, 1], 9) == [(3, 3, 3)]
    print("✓ Test 4 passed: repeats limited by occurrences")

    # Test case 5: Nonzero target with many duplicates
    A5 = [1, 1, 2, 2, 3, 3, 4, 4]
    assert solution.all_unique_triplets(A5, 7) == [(1, 2, 4), (1, 3, 3), (2, 2, 3)]
    print("✓ Test 5 passed: [1, 1, 2, 2, 3, 3, 4, 4], 7 -> 3 triplets")

    # Test case 6: Mixed signs, lexicographic order
    A6 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    assert solution.all_unique_triplets(A6, 0) == [
        (-4, -2, 6), (-4, 0, 4), (-4, 1, 3), (-4, 2, 2),
        (-2, -2, 4), (-2, 0, 2),
    ]
    print("✓ Test 6 passed: mixed signs -> 6 triplets in order")

    # Test case 7: Large input of repeated values stays fast
    A7 = [0] * 1500 + [1] * 1500
    assert solution.all_unique_triplets(A7, 1) == [(0, 0, 1)]
    print("✓ Test 7 passed: 3000 entries -> [(0, 0, 1)]")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_all_unique_triplets()
