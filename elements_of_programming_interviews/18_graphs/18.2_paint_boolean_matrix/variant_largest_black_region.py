"""
EPI 18.2 Variant - Largest Black Region

Problem:
A Boolean 2D array encodes a black-and-white image, with True meaning
black. Regions are formed by entries of the same color connected through
up/down/left/right neighbors. Return the number of entries in the largest
black region (0 if the image has no black entries).

Constraints:
- 1 <= rows, cols <= 1000
- Do not modify the caller's image
- O(rows * cols) time

How it works (connected components with BFS/DFS):
1. Keep a visited set (or a copy of the image)
2. For each unvisited black entry, run BFS over black neighbors and count
   the entries reached
3. Return the largest count

Example 1:
Input: image = [[T, T, F],
                [F, T, F],
                [F, F, T]]
Output: 3

Example 2:
Input: image = [[T, F, T],
                [F, T, F],
                [T, F, T]]
Output: 1
Explanation: Diagonal neighbors are not adjacent.
"""

from typing import List


class Solution:
    def largest_black_region(self, image: List[List[bool]]) -> int:
        """
        Computes the size of the largest black (True) region.

        Args:
            image: Boolean 2D array where True is black

        Returns:
            Number of entries in the largest black region

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols)
        """
        # TODO: Implement largest connected component search
        pass


def test_largest_black_region():
    """Test cases for largest black region"""
    solution = Solution()
    T, F = True, False

    # Test case 1: One region of three
    assert solution.largest_black_region([[T, T, F], [F, T, F], [F, F, T]]) == 3
    print("✓ Test 1 passed: region of 3")

    # Test case 2: No black entries
    assert solution.largest_black_region([[F, F], [F, F]]) == 0
    print("✓ Test 2 passed: all white -> 0")

    # Test case 3: Single black entry
    assert solution.largest_black_region([[T]]) == 1
    print("✓ Test 3 passed: [[T]] -> 1")

    # Test case 4: Checkerboard
    assert solution.largest_black_region([[T, F, T], [F, T, F], [T, F, T]]) == 1
    print("✓ Test 4 passed: checkerboard -> 1")

    # Test case 5: Several regions of different sizes
    img5 = [
        [T, T, F, F, T],
        [F, T, F, T, T],
        [F, F, F, T, F],
        [T, T, T, T, F],
    ]
    snapshot = [row[:] for row in img5]
    assert solution.largest_black_region(img5) == 8
    assert img5 == snapshot
    print("✓ Test 5 passed: largest of several regions -> 8, image unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_largest_black_region()
