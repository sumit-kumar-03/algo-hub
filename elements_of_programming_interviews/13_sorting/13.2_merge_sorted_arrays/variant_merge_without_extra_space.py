"""
EPI 13.2 Extra Variant - Merge Two Sorted Arrays Across Both Arrays
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the in-place merge, but now there are no empty slots: the merged
result must be spread over the two existing arrays, so you can't simply
fill from the back of one of them.

Problem:
Given two arrays A (length m) and B (length n), each sorted in ascending
order, rearrange their entries in place so that A holds the m smallest
values in ascending order and B holds the remaining n values in ascending
order. In other words, A + B becomes the sorted merge of the two arrays.
Do not allocate another array of size m + n (or of size m or n).

Constraints:
- 0 <= m, n <= 10^5
- O(1) extra space
- Target: O((m + n) log(m + n)) time with the "gap" method; an O(m * n)
  insertion approach also works but is slower

How it works (shrinking gap, as in Shell sort):
1. Treat A and B as one virtual array C of length m + n, where C[k] is A[k]
   for k < m and B[k - m] otherwise
2. Start with gap = ceil((m + n) / 2)
3. Compare C[k] with C[k + gap] for every valid k and swap them if they are
   out of order
4. If gap was 1, stop; otherwise set gap = ceil(gap / 2) and repeat
5. Because both halves start sorted, each pass leaves elements at most
   `gap` positions from their final place, so the gap-1 pass finishes the
   job

Example 1:
Input: A = [1, 4, 7, 8, 10], B = [2, 3, 9]
Output: A = [1, 2, 3, 4, 7], B = [8, 9, 10]

Example 2:
Input: A = [10, 12], B = [5, 18, 20]
Output: A = [5, 10], B = [12, 18, 20]
"""

from typing import List


class Solution:
    def merge_across_arrays(self, A: List[int], B: List[int]) -> None:
        """
        Rearranges sorted A and B so that A + B is sorted, using O(1) space.

        Args:
            A: First sorted array (keeps its length)
            B: Second sorted array (keeps its length)

        Returns:
            None; A holds the len(A) smallest values and B the rest, both sorted

        Time Complexity: O((m + n) log(m + n))
        Space Complexity: O(1)
        """
        # TODO: Implement gap-method merge across the two arrays
        pass


def test_merge_across_arrays():
    """Test cases for merging across two arrays without extra space"""
    solution = Solution()

    # Test case 1: Interleaved values
    A, B = [1, 4, 7, 8, 10], [2, 3, 9]
    solution.merge_across_arrays(A, B)
    assert A == [1, 2, 3, 4, 7] and B == [8, 9, 10]
    print("✓ Test 1 passed: -> A=[1, 2, 3, 4, 7], B=[8, 9, 10]")

    # Test case 2: Smaller first array
    A, B = [10, 12], [5, 18, 20]
    solution.merge_across_arrays(A, B)
    assert A == [5, 10] and B == [12, 18, 20]
    print("✓ Test 2 passed: -> A=[5, 10], B=[12, 18, 20]")

    # Test case 3: Already in order, and fully reversed blocks
    A, B = [1, 2], [3, 4]
    solution.merge_across_arrays(A, B)
    assert A == [1, 2] and B == [3, 4]
    A, B = [7, 8, 9], [1, 2]
    solution.merge_across_arrays(A, B)
    assert A == [1, 2, 7] and B == [8, 9]
    print("✓ Test 3 passed: Ordered / swapped blocks")

    # Test case 4: Empty arrays
    A, B = [], [3, 4]
    solution.merge_across_arrays(A, B)
    assert A == [] and B == [3, 4]
    A, B = [2, 5], []
    solution.merge_across_arrays(A, B)
    assert A == [2, 5] and B == []
    print("✓ Test 4 passed: One side empty")

    # Test case 5: Duplicates and negatives
    A, B = [-1, 0, 0, 6], [-3, 0, 6]
    solution.merge_across_arrays(A, B)
    assert A == [-3, -1, 0, 0] and B == [0, 6, 6]
    print("✓ Test 5 passed: Duplicates and negatives")

    # Test case 6: Single elements
    A, B = [5], [1]
    solution.merge_across_arrays(A, B)
    assert A == [1] and B == [5]
    print("✓ Test 6 passed: Single elements swap")

    # Test case 7: Many size combinations versus sorted()
    for m in range(0, 9):
        for n in range(0, 9):
            a = sorted((i * 7 + m) % 11 for i in range(m))
            b = sorted((i * 5 + n) % 13 for i in range(n))
            merged = sorted(a + b)
            solution.merge_across_arrays(a, b)
            assert a == merged[:m] and b == merged[m:]
    print("✓ Test 7 passed: All sizes 0..8 x 0..8 match sorted()")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_across_arrays()
