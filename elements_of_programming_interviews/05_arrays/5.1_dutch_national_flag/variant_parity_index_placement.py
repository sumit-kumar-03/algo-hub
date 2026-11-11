"""
EPI 5.1 Extra Variant - Even Values at Even Indices
(Practice problem, not in the book. Difficulty: Medium)
Builds on: in-place partitioning with pointers that each guard a region
of "already correct" positions, swapping only misplaced elements.

Problem:
Given an array of integers that contains exactly as many even values as
odd values, rearrange it in place so that every even index holds an even
value and every odd index holds an odd value. Any arrangement with this
property is accepted.

Constraints:
- 0 <= len(A) <= 10^5, len(A) is even, half the values are even
- Values may be negative (-3 is odd, -4 is even)
- Must run in O(n) time and use O(1) extra space

How it works (two pointers on interleaved positions):
1. even = 0 walks the even indices, odd = 1 walks the odd indices
2. Advance even (by 2) past positions that already hold even values, and
   advance odd (by 2) past positions that already hold odd values
3. If both are still in range, A[even] is odd and A[odd] is even, so
   swapping them fixes both positions. Repeat until even runs off the end
   (the counts guarantee odd does too)

Example 1:
Input: A = [4, 2, 5, 7]
Output: [4, 5, 2, 7] (one valid answer)
Explanation: Indices 0 and 2 hold 4 and 2; indices 1 and 3 hold 5 and 7.

Example 2:
Input: A = [3, 0]
Output: [0, 3]
"""

from typing import List


class Solution:
    def sort_by_parity_index(self, A: List[int]) -> None:
        """
        Places even values at even indices and odd values at odd indices.

        Args:
            A: Array with equally many even and odd values (in place)

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement parity-by-index placement
        pass


def is_parity_placed(A: List[int]) -> bool:
    """Checks that A[i] % 2 == i % 2 for every index i."""
    return all(x % 2 == i % 2 for i, x in enumerate(A))


def test_sort_by_parity_index():
    """Test cases for parity-by-index placement"""
    solution = Solution()

    # Test case 1: Example 1
    A1 = [4, 2, 5, 7]
    solution.sort_by_parity_index(A1)
    assert sorted(A1) == [2, 4, 5, 7] and is_parity_placed(A1)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Example 2 and empty array
    A2 = [3, 0]
    solution.sort_by_parity_index(A2)
    assert A2 == [0, 3]
    A3: List[int] = []
    solution.sort_by_parity_index(A3)
    assert A3 == []
    print("✓ Test 2 passed: [3, 0] -> [0, 3] and empty array")

    # Test case 3: All odds first, then all evens
    A4 = [1, 3, 5, 7, 2, 4, 6, 8]
    solution.sort_by_parity_index(A4)
    assert sorted(A4) == [1, 2, 3, 4, 5, 6, 7, 8] and is_parity_placed(A4)
    print(f"✓ Test 3 passed: {A4}")

    # Test case 4: Negative values and zero
    A5 = [-3, -1, -4, 0, 7, 10]
    solution.sort_by_parity_index(A5)
    assert sorted(A5) == [-4, -3, -1, 0, 7, 10] and is_parity_placed(A5)
    print(f"✓ Test 4 passed: {A5}")

    # Test case 5: Already placed stays valid
    A6 = [2, 1, 4, 3, 6, 5]
    solution.sort_by_parity_index(A6)
    assert sorted(A6) == [1, 2, 3, 4, 5, 6] and is_parity_placed(A6)
    print("✓ Test 5 passed: Already placed")

    # Test case 6: Large input with duplicates
    A7 = [1] * 25000 + [2] * 25000
    solution.sort_by_parity_index(A7)
    assert A7.count(1) == 25000 and A7.count(2) == 25000 and is_parity_placed(A7)
    print("✓ Test 6 passed: 50,000 elements")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_sort_by_parity_index()
