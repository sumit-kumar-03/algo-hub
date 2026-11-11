"""
EPI 10.1 Extra Variant - k Pairs with the Smallest Sums
(Practice problem, not in the book. Difficulty: Medium)
Builds on: k-way merging with a min-heap; here the "sorted files" are
implicit rows of a sum table that are never built.

Problem:
Given two arrays A and B sorted in ascending order and an integer k, return
the k pairs (a, b), with a taken from A and b taken from B, that have the
smallest sums a + b. Each index pair (i, j) may be used at most once. Return
the pairs in nondecreasing order of sum; pairs with equal sums may appear in
any order. If there are fewer than k pairs in total, return all of them.

Constraints:
- 0 <= len(A), len(B) <= 10^5; 0 <= k <= 10^4
- Values may be negative and may repeat
- O(k log min(k, len(A))) time; do not generate all len(A) * len(B) pairs

How it works (merge the rows of an implicit table):
1. Row i is the sorted sequence A[i] + B[0], A[i] + B[1], ...
2. Seed a min-heap with (A[i] + B[0], i, 0) for the first min(k, len(A))
   rows
3. Pop the smallest entry (s, i, j), output (A[i], B[j]), and push
   (A[i] + B[j + 1], i, j + 1) if j + 1 < len(B)
4. Stop after k pops or when the heap is empty

Example 1:
Input: A = [1, 7, 11], B = [2, 4, 6], k = 3
Output: [(1, 2), (1, 4), (1, 6)]
Explanation: Sums 3, 5, 7; the next smallest would be 7 + 2 = 9.

Example 2:
Input: A = [1, 1, 2], B = [1, 2, 3], k = 2
Output: [(1, 1), (1, 1)]
Explanation: Both 1s in A pair with B[0]; each index pair is distinct.
"""

from typing import List, Tuple


class Solution:
    def k_smallest_pairs(self, A: List[int], B: List[int], k: int) -> List[Tuple[int, int]]:
        """
        Returns the k pairs with the smallest sums.

        Args:
            A: Sorted array
            B: Sorted array
            k: Number of pairs to return

        Returns:
            Up to k pairs (a, b), in nondecreasing order of a + b

        Time Complexity: O(k log min(k, len(A)))
        Space Complexity: O(min(k, len(A)))
        """
        # TODO: Implement with a min-heap over implicit rows
        pass


def _check(A: List[int], B: List[int], k: int, result: List[Tuple[int, int]]) -> bool:
    """Valid iff result has the right size, is sorted by sum, uses each
    (value, value) pair no more often than it exists, and its sums match
    the k smallest sums."""
    if result is None or len(result) != min(k, len(A) * len(B)):
        return False
    sums = [a + b for a, b in result]
    if sums != sorted(sums):
        return False
    available = {}
    for a in A:
        for b in B:
            available[(a, b)] = available.get((a, b), 0) + 1
    for pair in result:
        pair = tuple(pair)
        if available.get(pair, 0) == 0:
            return False
        available[pair] -= 1
    expected = sorted(a + b for a in A for b in B)[:k]
    return sums == expected


def test_k_smallest_pairs():
    """Test cases for k smallest pair sums"""
    solution = Solution()

    # Test case 1: Basic example (all from the first row)
    A1, B1 = [1, 7, 11], [2, 4, 6]
    result1 = solution.k_smallest_pairs(A1, B1, 3)
    assert _check(A1, B1, 3, result1) is True
    print(f"✓ Test 1 passed: {result1}")

    # Test case 2: Duplicate values in A
    A2, B2 = [1, 1, 2], [1, 2, 3]
    result2 = solution.k_smallest_pairs(A2, B2, 2)
    assert _check(A2, B2, 2, result2) is True
    print(f"✓ Test 2 passed: Duplicates -> {result2}")

    # Test case 3: k larger than the number of pairs
    A3, B3 = [1, 2], [3]
    result3 = solution.k_smallest_pairs(A3, B3, 10)
    assert _check(A3, B3, 10, result3) is True
    print("✓ Test 3 passed: Fewer than k pairs")

    # Test case 4: An empty array or k = 0
    assert solution.k_smallest_pairs([], [1, 2], 3) == []
    assert solution.k_smallest_pairs([1, 2], [3, 4], 0) == []
    print("✓ Test 4 passed: Empty input and k = 0")

    # Test case 5: Answer zigzags across rows, with negatives
    A5, B5 = [-10, -4, 0, 3], [-2, 1, 5, 9]
    result5 = solution.k_smallest_pairs(A5, B5, 7)
    assert _check(A5, B5, 7, result5) is True
    print(f"✓ Test 5 passed: Negatives -> {result5}")

    # Test case 6: Larger deterministic arrays
    A6 = sorted((i * 37) % 101 - 50 for i in range(80))
    B6 = sorted((i * 53) % 97 - 48 for i in range(90))
    result6 = solution.k_smallest_pairs(A6, B6, 150)
    assert _check(A6, B6, 150, result6) is True
    print("✓ Test 6 passed: 80 x 90 arrays, k = 150")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_smallest_pairs()
