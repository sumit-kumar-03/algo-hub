"""
EPI 11.8 Variant - Median of an Array

Problem:
Given a nonempty array of numbers, return its median. For an odd length that
is the middle element in sorted order; for an even length, the average of the
two middle elements. You may rearrange the array in place.

Constraints:
- 1 <= len(A) <= 10^5
- Duplicates allowed
- Expected O(n) time, O(1) extra space
- Do not fully sort the array

How it works (reuse quickselect):
1. n = len(A)
2. Odd n: return the element of rank n // 2 (0-based, ascending) via
   randomized selection
3. Even n: select ranks n // 2 - 1 and n // 2 (the second selection can run on
   the already-partitioned part) and return their average

Example 1:
Input: A = [7, 1, 5, 3, 9]
Output: 5

Example 2:
Input: A = [4, 1, 3, 2]
Output: 2.5
"""

import math
from typing import List


class Solution:
    def find_median(self, A: List[float]) -> float:
        """
        Finds the median using selection instead of sorting.

        Args:
            A: Nonempty array of numbers (may be reordered)

        Returns:
            The median (average of the two middle values for even length)

        Time Complexity: O(n) expected
        Space Complexity: O(1)
        """
        # TODO: Implement with randomized selection
        pass


def _close(a, b) -> bool:
    return a is not None and math.isclose(a, b)


def test_find_median():
    """Test cases for the median of an array"""
    solution = Solution()

    # Test case 1: Odd length
    assert _close(solution.find_median([7, 1, 5, 3, 9]), 5)
    print("✓ Test 1 passed: Odd length -> 5")

    # Test case 2: Even length
    assert _close(solution.find_median([4, 1, 3, 2]), 2.5)
    print("✓ Test 2 passed: Even length -> 2.5")

    # Test case 3: Single element
    assert _close(solution.find_median([-8]), -8)
    print("✓ Test 3 passed: Single element")

    # Test case 4: Duplicates
    assert _close(solution.find_median([2, 2, 2, 9, 1]), 2)
    assert _close(solution.find_median([5, 5, 1, 1]), 3)
    print("✓ Test 4 passed: Duplicates")

    # Test case 5: Larger arrays against sorting
    for n in (100, 101):
        data = [(i * 7919) % 211 - 100 for i in range(n)]
        s = sorted(data)
        expected = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
        assert _close(solution.find_median(list(data)), expected)
    print("✓ Test 5 passed: n = 100 and n = 101")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_median()
