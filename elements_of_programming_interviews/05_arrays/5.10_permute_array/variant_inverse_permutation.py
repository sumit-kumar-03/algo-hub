"""
EPI 5.10 Variant - Invert a Permutation in Place

Problem:
An array A of length n holds a permutation of 0..n-1 (A[i] = j means i
maps to j). Update A in place so that it holds the inverse permutation:
afterward A[j] = i exactly when the original A[i] = j. Use only constant
extra storage.

Constraints:
- 0 <= n <= 10^5
- A is a permutation of 0..n-1
- Must run in O(n) time and O(1) extra space

How it works (walk each cycle, reversing its arrows):
1. For each start index i not yet processed:
   - prev = i, cur = A[i]
   - While cur != i: next = A[cur]; set A[cur] = prev (reverse the
     arrow); prev = cur; cur = next
   - Finally set A[i] = prev
2. Mark processed entries (e.g. store -(value) - 1) and decode at the end

Example 1:
Input: A = [2, 0, 1, 3]
Output: [1, 2, 0, 3]
Explanation: 0 -> 2 becomes 2 -> 0, 1 -> 0 becomes 0 -> 1, and so on.

Example 2:
Input: A = [3, 2, 1, 0]
Output: [3, 2, 1, 0]
Explanation: Every cycle has length 1 or 2, so the permutation is its own
inverse.
"""

from typing import List


class Solution:
    def invert_permutation(self, A: List[int]) -> None:
        """
        Replaces a permutation with its inverse, in place.

        Args:
            A: Permutation of 0..n-1 (modified in place)

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place permutation inversion
        pass


def test_invert_permutation():
    """Test cases for in-place permutation inversion"""
    solution = Solution()

    # Test case 1: Three-cycle plus a fixed point
    A1 = [2, 0, 1, 3]
    solution.invert_permutation(A1)
    assert A1 == [1, 2, 0, 3]
    print(f"✓ Test 1 passed: [2, 0, 1, 3] -> {A1}")

    # Test case 2: Self-inverse permutation
    A2 = [3, 2, 1, 0]
    solution.invert_permutation(A2)
    assert A2 == [3, 2, 1, 0]
    print("✓ Test 2 passed: Reversal is its own inverse")

    # Test case 3: Identity and empty
    A3 = [0, 1, 2]
    solution.invert_permutation(A3)
    A4: List[int] = []
    solution.invert_permutation(A4)
    assert A3 == [0, 1, 2] and A4 == []
    print("✓ Test 3 passed: Identity and empty")

    # Test case 4: One long cycle
    A5 = [1, 2, 3, 4, 0]
    solution.invert_permutation(A5)
    assert A5 == [4, 0, 1, 2, 3]
    print(f"✓ Test 4 passed: Rotation -> {A5}")

    # Test case 5: Inverting twice restores the original
    original = [4, 0, 6, 7, 1, 5, 2, 3]
    A6 = list(original)
    solution.invert_permutation(A6)
    assert all(A6[original[i]] == i for i in range(len(original)))
    solution.invert_permutation(A6)
    assert A6 == original
    print("✓ Test 5 passed: Mixed cycles, inverse of inverse is the original")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_invert_permutation()
