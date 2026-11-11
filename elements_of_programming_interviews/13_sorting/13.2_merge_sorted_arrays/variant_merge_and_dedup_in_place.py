"""
EPI 13.2 Extra Variant - Merge Two Sorted Arrays in Place Without Duplicates
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the fill-from-the-back in-place merge, combined with skipping
values equal to the last one written.

Problem:
A holds m real entries sorted in ascending order followed by at least n
empty slots (None). B holds n entries sorted in ascending order. Either
array may contain repeated values. Rearrange A in place so that its first
k entries are the DISTINCT values of A[:m] and B combined, in ascending
order, and return k. Entries of A beyond index k - 1 may hold anything.

Constraints:
- 0 <= m, n <= 10^5
- len(A) >= m + n
- O(m + n) time, O(1) extra space

How it works:
1. Merge from the back as in the original problem (write starts at
   m + n - 1), but only write a value if it differs from the value most
   recently written; otherwise just advance the source pointer
2. Writing from the back never overwrites an unread entry of A, because
   at most as many slots are written as entries consumed
3. The distinct values now occupy A[write + 1 : m + n]; shift that block to
   the front of A and return its length

Example 1:
Input: A = [1, 3, 3, 7, None, None, None], m = 4, B = [3, 4, 7], n = 3
Output: 4, with A[:4] == [1, 3, 4, 7]

Example 2:
Input: A = [None, None, None], m = 0, B = [2, 2, 2], n = 3
Output: 1, with A[:1] == [2]
"""

from typing import List, Optional


class Solution:
    def merge_and_dedup(
        self, A: List[Optional[int]], m: int, B: List[int], n: int
    ) -> int:
        """
        Merges sorted B into sorted A in place, keeping each value once.

        Args:
            A: Sorted array with m valid entries and room for n more
            m: Number of valid entries in A
            B: Sorted array
            n: Number of entries in B

        Returns:
            k, the number of distinct values; A[:k] holds them in ascending order

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place merge that drops duplicates
        pass


def test_merge_and_dedup():
    """Test cases for in-place merge with deduplication"""
    solution = Solution()

    # Test case 1: Duplicates within and across arrays
    A = [1, 3, 3, 7, None, None, None]
    k = solution.merge_and_dedup(A, 4, [3, 4, 7], 3)
    assert k == 4 and A[:k] == [1, 3, 4, 7]
    print("✓ Test 1 passed: -> [1, 3, 4, 7]")

    # Test case 2: A empty, B all equal
    A = [None, None, None]
    k = solution.merge_and_dedup(A, 0, [2, 2, 2], 3)
    assert k == 1 and A[:k] == [2]
    print("✓ Test 2 passed: Empty A -> [2]")

    # Test case 3: Both empty
    A = []
    assert solution.merge_and_dedup(A, 0, [], 0) == 0
    print("✓ Test 3 passed: Both empty -> 0")

    # Test case 4: B empty, A has duplicates
    A = [5, 5, 6, 6, 6, 9]
    k = solution.merge_and_dedup(A, 6, [], 0)
    assert k == 3 and A[:k] == [5, 6, 9]
    print("✓ Test 4 passed: Empty B -> [5, 6, 9]")

    # Test case 5: No overlap, no duplicates
    A = [10, 20, None, None, None]
    k = solution.merge_and_dedup(A, 2, [1, 2, 3], 3)
    assert k == 5 and A[:k] == [1, 2, 3, 10, 20]
    print("✓ Test 5 passed: Nothing removed")

    # Test case 6: Identical arrays with negatives
    A = [-3, -1, -1, 0, None, None, None, None]
    k = solution.merge_and_dedup(A, 4, [-3, -1, -1, 0], 4)
    assert k == 3 and A[:k] == [-3, -1, 0]
    print("✓ Test 6 passed: Identical arrays -> [-3, -1, 0]")

    # Test case 7: Larger arrays versus sorted(set())
    a = sorted((i * 7) % 40 for i in range(70))
    b = sorted((i * 11) % 55 for i in range(50))
    A = a + [None] * len(b)
    k = solution.merge_and_dedup(A, len(a), b, len(b))
    assert A[:k] == sorted(set(a) | set(b))
    print("✓ Test 7 passed: Matches sorted(set(a) | set(b))")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_and_dedup()
