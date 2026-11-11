"""
EPI 11.7 - Find the Min and Max Simultaneously

Problem:
Given a nonempty array of comparable items, return both its minimum and its
maximum. Comparisons are assumed to be expensive, so use noticeably fewer than
the 2(n - 1) comparisons needed to find each one separately.

Constraints:
- 1 <= len(A) <= 10^5
- O(n) time, O(1) extra space
- At most ceil(3n / 2) - 2 comparisons between elements (for n >= 2)
- Elements only support comparison; do not assume they are numbers

How it works (process pairs):
1. Compare the first two elements to initialize (min, max)
2. For each following pair (a, b):
   - Compare a with b (1 comparison) to find the smaller and larger
   - Compare the smaller with the current min, the larger with the current
     max (2 comparisons)
3. If n is odd, compare the leftover element with both min and max
That costs 3 comparisons per pair instead of 4.

Example 1:
Input: A = [3, 2, 5, 1, 2, 4]
Output: (1, 5)

Example 2:
Input: A = [7]
Output: (7, 7)
"""

import math
from typing import List, Tuple, TypeVar

T = TypeVar("T")


class Solution:
    def find_min_max(self, A: List[T]) -> Tuple[T, T]:
        """
        Finds the minimum and maximum with about 3n/2 comparisons.

        Args:
            A: Nonempty list of comparable items

        Returns:
            (smallest, largest)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement pairwise min/max
        pass


class _Counted:
    """Wraps a value and counts every comparison made on it."""

    count = 0

    def __init__(self, value):
        self.value = value

    def _cmp(self, other, op):
        _Counted.count += 1
        return op(self.value, other.value)

    def __lt__(self, other):
        return self._cmp(other, lambda a, b: a < b)

    def __le__(self, other):
        return self._cmp(other, lambda a, b: a <= b)

    def __gt__(self, other):
        return self._cmp(other, lambda a, b: a > b)

    def __ge__(self, other):
        return self._cmp(other, lambda a, b: a >= b)

    def __eq__(self, other):
        return self._cmp(other, lambda a, b: a == b)

    __hash__ = object.__hash__


def test_find_min_max():
    """Test cases for simultaneous min and max"""
    solution = Solution()

    # Test case 1: Book example
    assert tuple(solution.find_min_max([3, 2, 5, 1, 2, 4])) == (1, 5)
    print("✓ Test 1 passed: Book example -> (1, 5)")

    # Test case 2: Single element
    assert tuple(solution.find_min_max([7])) == (7, 7)
    print("✓ Test 2 passed: Single element")

    # Test case 3: Odd length, extremes at the ends
    assert tuple(solution.find_min_max([-9, 4, 0, 4, 12])) == (-9, 12)
    print("✓ Test 3 passed: Odd length")

    # Test case 4: All equal
    assert tuple(solution.find_min_max([2, 2, 2, 2])) == (2, 2)
    print("✓ Test 4 passed: All equal")

    # Test case 5: Strings
    assert tuple(solution.find_min_max(["pear", "apple", "zebra", "mango"])) == ("apple", "zebra")
    print("✓ Test 5 passed: Strings")

    # Test case 6: Comparison budget, even and odd lengths
    for n in (2, 3, 10, 101, 1000):
        values = [(i * 7919) % 1009 for i in range(n)]
        items = [_Counted(v) for v in values]
        _Counted.count = 0
        lo, hi = solution.find_min_max(items)
        assert (lo.value, hi.value) == (min(values), max(values))
        assert _Counted.count <= math.ceil(3 * n / 2) - 2, f"{_Counted.count} comparisons for n={n}"
    print("✓ Test 6 passed: At most ceil(3n/2) - 2 comparisons")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_min_max()
