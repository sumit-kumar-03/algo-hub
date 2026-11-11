"""
EPI 18.2 Variant - Largest Black Region Under Repeated Updates

Problem:
Start from a Boolean image (True means black). Then repeatedly receive a
point (a, b): set that entry to black and report the size of the largest
black region in the updated image. Regions connect through up/down/left/
right neighbors. Many updates will be made, so keep the total running time
low: re-scanning the whole image after every update is too slow.

Constraints:
- 1 <= rows, cols <= 1000, up to 10^6 updates
- Setting an entry that is already black is allowed (no change)
- Near O(1) amortized time per update (inverse Ackermann)

How it works (union-find over black cells):
1. In __init__, create a union-find structure and add every black cell,
   unioning it with black neighbors; track each root's size and the
   largest size seen
2. set_black(a, b): if the cell is already black, return the current max;
   otherwise make it a new set of size 1 and union it with each black
   neighbor (union by size + path compression)
3. Update and return the largest size (black regions only grow, so the
   maximum never decreases)

Example 1:
Input: image = all white 3x3; updates (0, 0), (2, 2), (0, 1), (1, 1)
Output: 1, 1, 2, 3

Example 2:
Input: image = [[T, F, T],
                [F, F, F],
                [T, T, F]]; updates (1, 1), (0, 1), (1, 0)
Output: 3, 6, 7
"""

from typing import List


class Solution:
    def __init__(self, image: List[List[bool]]) -> None:
        """
        Builds the union-find structure for the initial image.

        Args:
            image: Boolean 2D array where True is black (do not keep a
                reference that the caller could mutate)

        Time Complexity: O(rows * cols * alpha(rows * cols))
        Space Complexity: O(rows * cols)
        """
        # TODO: Initialize union-find over the black cells
        pass

    def set_black(self, a: int, b: int) -> int:
        """
        Sets (a, b) to black and reports the largest black region size.

        Args:
            a: Row of the entry
            b: Column of the entry

        Returns:
            Size of the largest black region after the update

        Time Complexity: O(alpha(rows * cols)) amortized
        Space Complexity: O(1) additional
        """
        # TODO: Implement incremental update with union-find
        pass


def test_incremental_largest_black_region():
    """Test cases for incremental largest black region"""
    T, F = True, False

    # Test case 1: Growing from an all-white image
    s1 = Solution([[F, F, F], [F, F, F], [F, F, F]])
    assert [s1.set_black(0, 0), s1.set_black(2, 2), s1.set_black(0, 1), s1.set_black(1, 1)] == [1, 1, 2, 3]
    print("✓ Test 1 passed: 1, 1, 2, 3")

    # Test case 2: Re-setting a black cell changes nothing
    assert s1.set_black(1, 1) == 3
    print("✓ Test 2 passed: repeated update -> 3")

    # Test case 3: An update can merge two regions
    assert s1.set_black(2, 0) == 3
    assert s1.set_black(2, 1) == 6
    print("✓ Test 3 passed: merge into a region of 6")

    # Test case 4: Initial black cells are counted
    s4 = Solution([[T, F, T], [F, F, F], [T, T, F]])
    assert [s4.set_black(1, 1), s4.set_black(0, 1), s4.set_black(1, 0)] == [3, 6, 7]
    print("✓ Test 4 passed: 3, 6, 7")

    # Test case 5: Caller's image is not modified
    img5 = [[F, F], [F, F]]
    s5 = Solution(img5)
    assert s5.set_black(0, 0) == 1 and s5.set_black(1, 1) == 1 and s5.set_black(0, 1) == 3
    assert img5 == [[F, F], [F, F]]
    print("✓ Test 5 passed: 1, 1, 3 and image unchanged")

    # Test case 6: Many updates stay fast
    n = 200
    s6 = Solution([[F] * n for _ in range(n)])
    last = 0
    for i in range(n):
        for j in range(n):
            last = s6.set_black(i, j)
    assert last == n * n
    print("✓ Test 6 passed: 40,000 updates -> region of 40,000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_incremental_largest_black_region()
