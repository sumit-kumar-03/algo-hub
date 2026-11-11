"""
EPI 10.6 - Compute the k Largest Elements in a Max-Heap

Problem:
You are given a max-heap stored as an array A (A[i] >= A[2i + 1] and
A[i] >= A[2i + 2]). Return the k largest elements it contains without
modifying A.

Constraints:
- 0 <= k <= len(A) <= 10^5
- A must not be modified
- O(k log k) time, O(k) extra space (not O(n) or O(k log n) via extract-max)
- The returned elements may be in any order

How it works:
1. The root A[0] is the largest; the next candidates are always children of
   elements already taken
2. Keep a separate max-heap of candidate indices, keyed by A[index], seeded
   with index 0
3. Repeat k times: pop the best candidate, add its value to the result, and
   push its children (2i + 1, 2i + 2) if they exist

Example 1:
Input: A = [561, 314, 401, 28, 156, 359, 271, 11, 3], k = 4
Output: [561, 401, 359, 314]   (in any order)

Example 2:
Input: A = [10, 9, 8], k = 0
Output: []
"""

from typing import List


class Solution:
    def k_largest_in_binary_heap(self, A: List[int], k: int) -> List[int]:
        """
        Finds the k largest values in an array-based max-heap.

        Args:
            A: Max-heap in array form (must not be modified)
            k: Number of values to return

        Returns:
            The k largest values, in any order

        Time Complexity: O(k log k)
        Space Complexity: O(k)
        """
        # TODO: Implement with a candidate max-heap of indices
        pass


def test_k_largest_in_binary_heap():
    """Test cases for k largest elements in a max-heap"""
    solution = Solution()

    # Test case 1: Book example
    A = [561, 314, 401, 28, 156, 359, 271, 11, 3]
    original = list(A)
    result1 = solution.k_largest_in_binary_heap(A, 4)
    assert sorted(result1, reverse=True) == [561, 401, 359, 314]
    assert A == original
    print(f"✓ Test 1 passed: Book example -> {result1} (heap unchanged)")

    # Test case 2: k = 0
    assert solution.k_largest_in_binary_heap([10, 9, 8], 0) == []
    print("✓ Test 2 passed: k = 0")

    # Test case 3: k = 1 is the root
    assert solution.k_largest_in_binary_heap([10, 9, 8], 1) == [10]
    print("✓ Test 3 passed: k = 1")

    # Test case 4: k equals heap size
    result4 = solution.k_largest_in_binary_heap(A, len(A))
    assert sorted(result4) == sorted(original)
    print("✓ Test 4 passed: k equals heap size")

    # Test case 5: Duplicates
    B = [9, 9, 9, 5, 9, 1, 2]
    result5 = solution.k_largest_in_binary_heap(B, 5)
    assert sorted(result5, reverse=True) == [9, 9, 9, 9, 5]
    print(f"✓ Test 5 passed: Duplicates -> {result5}")

    # Test case 6: Larger heap where the answer is spread across subtrees
    C = [100, 50, 90, 49, 48, 89, 88, 1, 2, 3, 4, 87, 86, 85, 84]
    result6 = solution.k_largest_in_binary_heap(C, 6)
    assert sorted(result6, reverse=True) == [100, 90, 89, 88, 87, 86]
    print(f"✓ Test 6 passed: Larger heap -> {result6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_largest_in_binary_heap()
