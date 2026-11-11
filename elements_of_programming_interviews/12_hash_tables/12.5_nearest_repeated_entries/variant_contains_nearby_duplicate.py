"""
EPI 12.5 Extra Variant - Duplicate Within Distance k
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the hash table from each entry to the latest index where it was
seen, used in the nearest repeated entries scan.

Problem:
Given an array A and a nonnegative integer k, return True if there are two
different indices i and j with A[i] == A[j] and |i - j| <= k. Otherwise
return False.

Constraints:
- 0 <= len(A) <= 10^5
- 0 <= k <= 10^5
- O(n) time, O(d) space where d is the number of distinct entries (or
  O(min(n, k)) with a sliding window set)

How it works:
1. Scan left to right, keeping a hash table from each entry to the latest
   index where it appeared
2. If the current entry was seen before and the gap to its latest index is
   at most k, return True
3. Record the current index as the entry's latest index
4. Return False after the scan

Example 1:
Input: A = [1, 2, 3, 1], k = 3
Output: True
Explanation: A[0] == A[3] and 3 - 0 = 3 <= 3.

Example 2:
Input: A = [1, 2, 3, 1, 2, 3], k = 2
Output: False
Explanation: Equal entries are always exactly 3 apart.
"""

from typing import Hashable, List


class Solution:
    def contains_nearby_duplicate(self, A: List[Hashable], k: int) -> bool:
        """
        Checks for two equal entries at most k positions apart.

        Args:
            A: Array of hashable entries
            k: Maximum allowed index distance

        Returns:
            True if such a pair exists, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(d) where d is the number of distinct entries
        """
        # TODO: Implement nearby duplicate check
        pass


def test_contains_nearby_duplicate():
    """Test cases for duplicate within distance k"""
    solution = Solution()

    # Test case 1: Pair exactly k apart
    assert solution.contains_nearby_duplicate([1, 2, 3, 1], 3) is True
    print("✓ Test 1 passed: Gap equals k -> True")

    # Test case 2: All pairs too far apart
    assert solution.contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
    print("✓ Test 2 passed: Gaps of 3 with k=2 -> False")

    # Test case 3: Far pair first, close pair later (must keep latest index)
    assert solution.contains_nearby_duplicate(["a", "b", "c", "d", "a", "x", "a"], 2) is True
    print("✓ Test 3 passed: Later closer pair found")

    # Test case 4: k = 0 can never match distinct indices
    assert solution.contains_nearby_duplicate([5, 5, 5], 0) is False
    print("✓ Test 4 passed: k=0 -> False")

    # Test case 5: Empty and single-element arrays
    assert solution.contains_nearby_duplicate([], 3) is False
    assert solution.contains_nearby_duplicate([7], 3) is False
    print("✓ Test 5 passed: Empty / single -> False")

    # Test case 6: Adjacent duplicates with negatives
    assert solution.contains_nearby_duplicate([-1, 0, -1, -1], 1) is True
    print("✓ Test 6 passed: Adjacent -1s -> True")

    # Test case 7: No duplicates at all, huge k
    assert solution.contains_nearby_duplicate(list(range(1000)), 10**5) is False
    print("✓ Test 7 passed: Distinct entries -> False")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_contains_nearby_duplicate()
