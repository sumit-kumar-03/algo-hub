"""
EPI 13.1 Extra Variant - Smallest Range Covering k Sorted Lists
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the sorted-array intersection walk with one pointer per array.
Instead of waiting for all pointers to show the same value, you measure
how far apart they are and always advance the one at the minimum.

Problem:
Given k nonempty lists, each sorted in ascending order, find the smallest
range [lo, hi] (with lo <= hi) that contains at least one value from every
list. Range [a, b] is smaller than [c, d] if b - a < d - c, or if
b - a == d - c and a < c.

Constraints:
- 1 <= k <= 10^3
- 1 <= len(list) and total number of entries N <= 10^5
- O(N log k) time, O(k) extra space

How it works (k pointers + min-heap):
1. Put the first value of every list in a min-heap of (value, list index,
   position), and track the maximum value among them
2. The heap's minimum and the tracked maximum form a range that covers
   every list; compare it with the best range so far
3. Pop the minimum and push the next value from the same list, updating the
   maximum. Advancing any pointer other than the minimum's can only make
   the range wider, so the minimum is the only useful move
4. Stop as soon as the popped list has no next value: from then on no range
   can cover that list

Example 1:
Input: lists = [[1, 5, 9], [4, 8, 12], [7, 10, 16]]
Output: [7, 9]
Explanation: 9, 8, and 7 come from the three lists; width 2. [8, 10] also
has width 2 but starts later.

Example 2:
Input: lists = [[3], [3], [3]]
Output: [3, 3]
"""

from typing import List


class Solution:
    def smallest_range(self, lists: List[List[int]]) -> List[int]:
        """
        Finds the smallest range containing a value from each list.

        Args:
            lists: k nonempty sorted lists

        Returns:
            [lo, hi], the smallest covering range (ties broken by smaller lo)

        Time Complexity: O(N log k) where N is the total number of entries
        Space Complexity: O(k)
        """
        # TODO: Implement smallest covering range with a heap
        pass


def test_smallest_range():
    """Test cases for smallest range covering k sorted lists"""
    solution = Solution()

    # Test case 1: Tie on width broken by smaller start
    assert solution.smallest_range([[1, 5, 9], [4, 8, 12], [7, 10, 16]]) == [7, 9]
    print("✓ Test 1 passed: -> [7, 9]")

    # Test case 2: All lists share a value
    assert solution.smallest_range([[3], [3], [3]]) == [3, 3]
    assert solution.smallest_range([[1, 2, 3], [2, 5], [0, 2, 9]]) == [2, 2]
    print("✓ Test 2 passed: Common value -> zero-width range")

    # Test case 3: Single list
    assert solution.smallest_range([[4, 6, 8]]) == [4, 4]
    print("✓ Test 3 passed: k=1 -> [first, first]")

    # Test case 4: Single-element lists
    assert solution.smallest_range([[10], [1], [5]]) == [1, 10]
    print("✓ Test 4 passed: Singletons -> [min, max]")

    # Test case 5: Classic spread with negatives and duplicates
    lists = [[-10, -5, 0, 0, 20], [-7, 1, 1, 30], [-6, 2, 25]]
    assert solution.smallest_range(lists) == [-7, -5]
    print("✓ Test 5 passed: Negatives -> [-7, -5]")

    # Test case 6: Answer appears only after a list is nearly exhausted
    lists = [[1, 2, 3, 100], [50, 101], [99, 102]]
    assert solution.smallest_range(lists) == [99, 101]
    print("✓ Test 6 passed: Late answer -> [99, 101]")

    # Test case 7: Brute force over candidate ranges
    lists = [sorted((i * m + m) % 37 for i in range(m + 4)) for m in [3, 5, 7, 11]]
    values = sorted(set(v for lst in lists for v in lst))
    best = None
    for lo in values:
        for hi in values:
            if lo <= hi and all(any(lo <= v <= hi for v in lst) for lst in lists):
                if best is None or (hi - lo, lo) < (best[1] - best[0], best[0]):
                    best = [lo, hi]
    assert solution.smallest_range(lists) == best
    print("✓ Test 7 passed: Matches brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_smallest_range()
