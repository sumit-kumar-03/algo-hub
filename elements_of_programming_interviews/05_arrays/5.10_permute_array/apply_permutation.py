"""
EPI 5.10 - Permute the Elements of an Array

Problem:
A permutation of length n is given as an array P where P[i] is the index
the element currently at position i must move to. Given an array A of n
elements and such a permutation P, rearrange A in place according to P.
You may temporarily modify P, but leave it as you found it.

Constraints:
- 0 <= n <= 10^5
- P is a permutation of 0..n-1
- Aim for O(n) time and O(1) extra space (no copy of A)

How it works (follow cycles, mark visited entries in P):
1. A permutation splits into independent cycles
2. For each i whose P[i] is not yet marked:
   - Carry A[i] along its cycle: put it at P[i], pick up the element that
     was there, and continue until returning to i
   - Mark each visited P entry (e.g. subtract len(P) to make it negative)
3. Restore P by adding len(P) back to every entry

Example 1:
Input: A = ['a', 'b', 'c', 'd'], P = [2, 0, 1, 3]
Output: A = ['b', 'c', 'a', 'd']
Explanation: 'a' moves to index 2, 'b' to 0, 'c' to 1, 'd' stays.

Example 2:
Input: A = ['a', 'b', 'c', 'd'], P = [3, 2, 1, 0]
Output: A = ['d', 'c', 'b', 'a']
Explanation: Two swaps: positions 0 and 3, and positions 1 and 2.
"""

from typing import Any, List


class Solution:
    def apply_permutation(self, perm: List[int], A: List[Any]) -> None:
        """
        Applies a permutation to A in place.

        Args:
            perm: perm[i] is the destination index of the element at index i
            A: Elements to rearrange (modified in place)

        Returns:
            None (A is modified in place; perm is restored afterward)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place permutation by following cycles
        pass


def test_apply_permutation():
    """Test cases for apply permutation"""
    solution = Solution()

    # Test case 1: Book example
    A1 = ["a", "b", "c", "d"]
    P1 = [2, 0, 1, 3]
    solution.apply_permutation(P1, A1)
    assert A1 == ["b", "c", "a", "d"]
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Reversal (two 2-cycles)
    A2 = ["a", "b", "c", "d"]
    P2 = [3, 2, 1, 0]
    solution.apply_permutation(P2, A2)
    assert A2 == ["d", "c", "b", "a"]
    print(f"✓ Test 2 passed: {A2}")

    # Test case 3: Identity
    A3 = [10, 20, 30]
    solution.apply_permutation([0, 1, 2], A3)
    assert A3 == [10, 20, 30]
    print("✓ Test 3 passed: Identity leaves A unchanged")

    # Test case 4: One long cycle (rotate right by one)
    A4 = [1, 2, 3, 4, 5]
    P4 = [1, 2, 3, 4, 0]
    solution.apply_permutation(P4, A4)
    assert A4 == [5, 1, 2, 3, 4]
    assert P4 == [1, 2, 3, 4, 0]
    print(f"✓ Test 4 passed: Single cycle -> {A4}, perm restored")

    # Test case 5: Mixed cycles, compare against a copy-based result
    A5 = list("abcdefgh")
    P5 = [4, 0, 6, 7, 1, 5, 2, 3]
    expected = [None] * len(A5)
    for i, p in enumerate(P5):
        expected[p] = A5[i]
    solution.apply_permutation(P5, A5)
    assert A5 == expected
    assert P5 == [4, 0, 6, 7, 1, 5, 2, 3]
    print(f"✓ Test 5 passed: Mixed cycles -> {''.join(A5)}, perm restored")

    # Test case 6: Empty array
    A6: List[Any] = []
    solution.apply_permutation([], A6)
    assert A6 == []
    print("✓ Test 6 passed: Empty array")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_apply_permutation()
