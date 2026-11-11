"""
EPI 12.6 Variant - Rearrange So Equal Elements Are More Than k Apart

Problem:
Given an array A and a positive integer k, rearrange the elements so that no
two equal elements are k or fewer positions apart, i.e., whenever
A[i] == A[j] with i != j, we need |i - j| > k. Return the rearranged array,
or an empty list if no valid arrangement exists.

Constraints:
- 0 <= len(A) <= 10^5
- 1 <= k
- O(n log d) time, O(n) space where d is the number of distinct values
- Any valid arrangement is accepted

How it works (greedy with a max-heap and a cooldown queue):
1. Count occurrences with a hash table and push (count, value) pairs onto a
   max-heap keyed by remaining count
2. At each position, pop the value with the most remaining copies, place it,
   and put it in a cooldown queue with its remaining count
3. Once a value has waited k positions in the cooldown queue, push it back
   onto the heap if it still has copies left
4. If the heap is empty before all positions are filled, no arrangement
   exists

Example 1:
Input: A = [1, 1, 2, 2, 3, 3], k = 2
Output: [1, 2, 3, 1, 2, 3]
Explanation: Equal values are exactly 3 positions apart, which is more than 2.

Example 2:
Input: A = [1, 1, 1, 2], k = 1
Output: []
Explanation: Three 1s need at least five positions to stay 2 apart.
"""

from typing import List


class Solution:
    def rearrange_k_apart(self, A: List[int], k: int) -> List[int]:
        """
        Rearranges A so that equal elements are more than k positions apart.

        Args:
            A: Input array
            k: Positive integer; equal elements must be at distance > k

        Returns:
            A valid rearrangement of A, or [] if none exists

        Time Complexity: O(n log d)
        Space Complexity: O(n)
        """
        # TODO: Implement k-apart rearrangement
        pass


def _is_valid(A: List[int], result: List[int], k: int) -> bool:
    """Checks result is a permutation of A with equal elements more than k apart."""
    if result is None or sorted(result) != sorted(A):
        return False
    last_seen = {}
    for i, x in enumerate(result):
        if x in last_seen and i - last_seen[x] <= k:
            return False
        last_seen[x] = i
    return True


def test_rearrange_k_apart():
    """Test cases for k-apart rearrangement"""
    solution = Solution()

    # Test case 1: Book-style example
    A1 = [1, 1, 2, 2, 3, 3]
    assert _is_valid(A1, solution.rearrange_k_apart(list(A1), 2), 2)
    print("✓ Test 1 passed: [1, 1, 2, 2, 3, 3], k=2 -> valid arrangement")

    # Test case 2: Impossible, too many copies of one value
    assert solution.rearrange_k_apart([1, 1, 1, 2], 1) == []
    print("✓ Test 2 passed: [1, 1, 1, 2], k=1 -> []")

    # Test case 3: Dominant value placed first is required
    A3 = [1, 1, 1, 2, 2, 3]
    assert _is_valid(A3, solution.rearrange_k_apart(list(A3), 1), 1)
    print("✓ Test 3 passed: [1, 1, 1, 2, 2, 3], k=1 -> valid arrangement")

    # Test case 4: Impossible with larger k
    assert solution.rearrange_k_apart([1, 1, 2, 2], 2) == []
    print("✓ Test 4 passed: [1, 1, 2, 2], k=2 -> []")

    # Test case 5: All distinct values, any order works
    A5 = [5, 4, 3, 2, 1]
    assert _is_valid(A5, solution.rearrange_k_apart(list(A5), 10), 10)
    print("✓ Test 5 passed: All distinct -> valid arrangement")

    # Test case 6: Tight fit
    A6 = [1, 1, 1, 2, 2, 2, 3, 3, 4]
    assert _is_valid(A6, solution.rearrange_k_apart(list(A6), 2), 2)
    print("✓ Test 6 passed: Tight fit with k=2 -> valid arrangement")

    # Test case 7: Empty array
    assert solution.rearrange_k_apart([], 3) == []
    print("✓ Test 7 passed: Empty array -> []")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_rearrange_k_apart()
