"""
EPI 13.2 Extra Variant - Merge an Ascending and a Descending Array in Place
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the fill-from-the-back in-place merge; the twist is that the
largest remaining entry of B is now at its FRONT, so B's pointer must move
in the opposite direction.

Problem:
A holds m real entries sorted in ascending order followed by empty slots
(None). B holds n entries sorted in DESCENDING order. Update A in place so
that its first m + n entries are all the entries of both arrays in
ascending order. B must not be reversed or copied.

Constraints:
- 0 <= m, n <= 10^5
- len(A) >= m + n
- O(m + n) time, O(1) extra space

How it works:
1. a = m - 1 walks A from its largest entry downward
2. b = 0 walks B from its largest entry (the front) toward the back
3. write = m + n - 1; repeatedly copy the larger of A[a] and B[b] into
   A[write], advancing the pointer that supplied it
4. When B runs out, the remaining A entries are already in place; when A
   runs out, copy the rest of B (continuing from b toward the back)

Example 1:
Input: A = [2, 6, 9, None, None, None], m = 3, B = [10, 5, 1], n = 3
Output: A = [1, 2, 5, 6, 9, 10]

Example 2:
Input: A = [None, None], m = 0, B = [4, 3], n = 2
Output: A = [3, 4]
"""

from typing import List, Optional


class Solution:
    def merge_opposite_orders(
        self, A: List[Optional[int]], m: int, B: List[int], n: int
    ) -> None:
        """
        Merges descending B into ascending A in place.

        Args:
            A: Ascending array with m valid entries and room for n more
            m: Number of valid entries in A
            B: Array sorted in descending order
            n: Number of entries in B

        Returns:
            None; A[:m + n] holds all entries in ascending order afterward

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place merge with B read front to back
        pass


def test_merge_opposite_orders():
    """Test cases for merging ascending A with descending B"""
    solution = Solution()

    # Test case 1: Interleaved values
    A = [2, 6, 9, None, None, None]
    solution.merge_opposite_orders(A, 3, [10, 5, 1], 3)
    assert A == [1, 2, 5, 6, 9, 10]
    print("✓ Test 1 passed: -> [1, 2, 5, 6, 9, 10]")

    # Test case 2: A has no real entries
    A = [None, None]
    solution.merge_opposite_orders(A, 0, [4, 3], 2)
    assert A == [3, 4]
    print("✓ Test 2 passed: Empty A")

    # Test case 3: B empty
    A = [1, 5, 8]
    solution.merge_opposite_orders(A, 3, [], 0)
    assert A == [1, 5, 8]
    print("✓ Test 3 passed: Empty B")

    # Test case 4: All of B is smaller than A
    A = [10, 20, None, None, None]
    solution.merge_opposite_orders(A, 2, [3, 2, 1], 3)
    assert A == [1, 2, 3, 10, 20]
    print("✓ Test 4 passed: B entirely before A")

    # Test case 5: All of B is larger than A, with extra slack at the end
    A = [1, 2, None, None, None]
    solution.merge_opposite_orders(A, 2, [9, 8], 2)
    assert A[:4] == [1, 2, 8, 9]
    print("✓ Test 5 passed: B entirely after A (extra slack)")

    # Test case 6: Duplicates and negatives
    A = [-4, 0, 0, 7, None, None, None, None]
    solution.merge_opposite_orders(A, 4, [7, 0, -4, -9], 4)
    assert A == [-9, -4, -4, 0, 0, 0, 7, 7]
    print("✓ Test 6 passed: Duplicates and negatives")

    # Test case 7: Larger arrays versus sorted()
    a = sorted((i * 13) % 97 for i in range(60))
    b = sorted(((i * 29) % 89 for i in range(45)), reverse=True)
    A = a + [None] * len(b)
    solution.merge_opposite_orders(A, len(a), b, len(b))
    assert A == sorted(a + b)
    print("✓ Test 7 passed: Matches sorted(a + b)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_opposite_orders()
