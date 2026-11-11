"""
EPI 5.5 Variant - Trim Frequent Values to min(2, m) Copies

Problem:
Given a sorted array A and a positive integer m, update A in place so that
every value appearing at least m times is trimmed to exactly min(2, m)
copies. Values that appear fewer than m times are left alone. Survivors
are shifted left and stay in sorted order. Return the number of valid
entries k; anything after index k - 1 can be arbitrary.
(The book's wording is terse; this is the interpretation used here. With
m = 1 it reduces to removing all duplicates.)

Constraints:
- 0 <= len(A) <= 10^5, A sorted in non-decreasing order
- m >= 1
- One pass over A, O(1) extra space

How it works (process one run of equal values at a time):
1. write_index = 0, i = 0
2. While i < n: find the end j of the run of A[i] (A[i:j] all equal)
3. count = j - i; keep = min(2, m) if count >= m else count
4. Write `keep` copies of A[i] starting at write_index; advance it
5. Set i = j and repeat; return write_index

Example 1:
Input: A = [1, 1, 1, 2, 3, 3, 3, 3, 4, 4], m = 3
Output: 7, with A[:7] == [1, 1, 2, 3, 3, 4, 4]
Explanation: 1 (3 copies) and 3 (4 copies) are trimmed to 2 copies each;
2 and 4 appear fewer than 3 times, so they are unchanged.

Example 2:
Input: A = [5, 5, 5, 6], m = 1
Output: 2, with A[:2] == [5, 6]
Explanation: With m = 1 every value keeps min(2, 1) = 1 copy.
"""

from typing import List


class Solution:
    def limit_duplicates(self, A: List[int], m: int) -> int:
        """
        Trims every value that appears at least m times to min(2, m) copies.

        Args:
            A: Sorted list of integers (modified in place)
            m: Positive threshold on the number of occurrences

        Returns:
            Number of valid entries k; A[:k] holds the result in sorted order

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement one-pass trimming of frequent values
        pass


def test_limit_duplicates():
    """Test cases for limit duplicates implementation"""
    solution = Solution()

    # Test case 1: m = 3, two values trimmed, two untouched
    A1 = [1, 1, 1, 2, 3, 3, 3, 3, 4, 4]
    k1 = solution.limit_duplicates(A1, 3)
    assert k1 == 7 and A1[:k1] == [1, 1, 2, 3, 3, 4, 4]
    print(f"✓ Test 1 passed: m = 3 -> {A1[:k1]}")

    # Test case 2: m = 1 behaves like deleting duplicates
    A2 = [5, 5, 5, 6]
    k2 = solution.limit_duplicates(A2, 1)
    assert k2 == 2 and A2[:k2] == [5, 6]
    print(f"✓ Test 2 passed: m = 1 -> {A2[:k2]}")

    # Test case 3: m = 2 keeps at most two copies of everything
    A3 = [0, 0, 0, 0, 1, 2, 2, 2]
    k3 = solution.limit_duplicates(A3, 2)
    assert k3 == 5 and A3[:k3] == [0, 0, 1, 2, 2]
    print(f"✓ Test 3 passed: m = 2 -> {A3[:k3]}")

    # Test case 4: Large m, nothing reaches the threshold
    A4 = [1, 1, 2, 2, 2]
    k4 = solution.limit_duplicates(A4, 5)
    assert k4 == 5 and A4[:k4] == [1, 1, 2, 2, 2]
    print("✓ Test 4 passed: m = 5 -> unchanged")

    # Test case 5: Exactly m copies get trimmed
    A5 = [7, 7, 7, 7, 7, 8]
    k5 = solution.limit_duplicates(A5, 5)
    assert k5 == 3 and A5[:k5] == [7, 7, 8]
    print(f"✓ Test 5 passed: m = 5 with five 7s -> {A5[:k5]}")

    # Test case 6: Empty array
    A6: List[int] = []
    assert solution.limit_duplicates(A6, 2) == 0
    print("✓ Test 6 passed: Empty array -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_limit_duplicates()
