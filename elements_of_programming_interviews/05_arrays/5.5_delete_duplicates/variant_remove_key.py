"""
EPI 5.5 Variant - Remove All Occurrences of a Key

Problem:
Given an array (not necessarily sorted) and a key, remove every occurrence
of the key in place, shifting the remaining elements left so they keep
their original relative order. Return the number of remaining elements k;
A[:k] must hold them, and anything after index k - 1 can be arbitrary.

Constraints:
- 0 <= len(A) <= 10^5
- Must run in O(n) time and O(1) extra space

How it works (read pointer and write pointer):
1. write_index = 0
2. For each element x in A: if x != key, copy it to A[write_index] and
   advance write_index
3. Return write_index

Example 1:
Input: A = [3, 1, 3, 2, 3, 4], key = 3
Output: 3, with A[:3] == [1, 2, 4]
Explanation: Three 3s are removed; the others keep their order.

Example 2:
Input: A = [5, 5], key = 5
Output: 0
Explanation: Every element equals the key.
"""

from typing import List


class Solution:
    def remove_key(self, A: List[int], key: int) -> int:
        """
        Removes all occurrences of key from A in place.

        Args:
            A: List of integers (modified in place)
            key: Value to remove

        Returns:
            Number of remaining elements k; A[:k] holds them in original order

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place key removal
        pass


def test_remove_key():
    """Test cases for remove key implementation"""
    solution = Solution()

    # Test case 1: Key scattered through the array
    A1 = [3, 1, 3, 2, 3, 4]
    k1 = solution.remove_key(A1, 3)
    assert k1 == 3 and A1[:k1] == [1, 2, 4]
    print(f"✓ Test 1 passed: k = {k1}, A[:k] = {A1[:k1]}")

    # Test case 2: Every element is the key
    A2 = [5, 5]
    assert solution.remove_key(A2, 5) == 0
    print("✓ Test 2 passed: All keys -> 0")

    # Test case 3: Key not present
    A3 = [1, 2, 3]
    k3 = solution.remove_key(A3, 9)
    assert k3 == 3 and A3[:k3] == [1, 2, 3]
    print("✓ Test 3 passed: Key absent -> unchanged")

    # Test case 4: Empty array
    A4: List[int] = []
    assert solution.remove_key(A4, 1) == 0
    print("✓ Test 4 passed: Empty array -> 0")

    # Test case 5: Key at both ends
    A5 = [0, 7, -1, 7, 0, 8, 0]
    k5 = solution.remove_key(A5, 0)
    assert k5 == 4 and A5[:k5] == [7, -1, 7, 8]
    print(f"✓ Test 5 passed: k = {k5}, A[:k] = {A5[:k5]}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_remove_key()
