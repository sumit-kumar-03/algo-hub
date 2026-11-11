"""
EPI 18.2 - Paint a Boolean Matrix

Problem:
A Boolean 2D array encodes a black-and-white image. Two entries are
adjacent if one is directly above, below, left, or right of the other. The
region of an entry (x, y) is every entry reachable from it through adjacent
entries of the same color. Flip the color of every entry in the region of
(x, y), modifying the image in place.

Constraints:
- 1 <= rows, cols <= 1000
- 0 <= x < rows, 0 <= y < cols
- O(rows * cols) time; prefer BFS (or an explicit stack) over deep
  recursion to avoid stack overflow on large regions

How it works (flood fill with BFS):
1. Remember color = image[x][y]; flip it and enqueue (x, y)
2. Pop a cell; for each in-bounds neighbor still equal to color, flip it
   and enqueue it (flipping on enqueue doubles as the visited mark)
3. Stop when the queue is empty

Example 1:
Input: image = [[T, T, F],
                [T, F, F],
                [F, F, T]], (x, y) = (0, 0)
Output: image becomes [[F, F, F],
                       [F, F, F],
                       [F, F, T]]

Example 2:
Input: same original image, (x, y) = (2, 2)
Output: only (2, 2) flips, since it is cut off from the other True cells
"""

from typing import List


class Solution:
    def flip_color(self, image: List[List[bool]], x: int, y: int) -> None:
        """
        Flips the color of the region containing (x, y), in place.

        Args:
            image: Boolean 2D array (modified in place)
            x: Row of the starting entry
            y: Column of the starting entry

        Returns:
            None

        Time Complexity: O(rows * cols)
        Space Complexity: O(rows * cols) for the queue in the worst case
        """
        # TODO: Implement BFS flood fill
        pass


def test_flip_color():
    """Test cases for painting a Boolean matrix"""
    solution = Solution()
    T, F = True, False

    # Test case 1: Flip a True region
    img1 = [[T, T, F], [T, F, F], [F, F, T]]
    solution.flip_color(img1, 0, 0)
    assert img1 == [[F, F, F], [F, F, F], [F, F, T]]
    print("✓ Test 1 passed: True region flipped")

    # Test case 2: Isolated cell
    img2 = [[T, T, F], [T, F, F], [F, F, T]]
    solution.flip_color(img2, 2, 2)
    assert img2 == [[T, T, F], [T, F, F], [F, F, F]]
    print("✓ Test 2 passed: isolated cell flipped alone")

    # Test case 3: Flip a False region
    img3 = [[T, T, F], [T, F, F], [F, F, T]]
    solution.flip_color(img3, 1, 1)
    assert img3 == [[T, T, T], [T, T, T], [T, T, T]]
    print("✓ Test 3 passed: False region flipped")

    # Test case 4: Diagonal cells are not adjacent
    img4 = [[T, F], [F, T]]
    solution.flip_color(img4, 0, 0)
    assert img4 == [[F, F], [F, T]]
    print("✓ Test 4 passed: diagonal not connected")

    # Test case 5: A second flip uses the new, larger region
    img5 = [[F, T, F], [F, T, T], [T, F, F]]
    solution.flip_color(img5, 0, 1)
    assert img5 == [[F, F, F], [F, F, F], [T, F, F]]
    solution.flip_color(img5, 0, 1)
    assert img5 == [[T, T, T], [T, T, T], [T, T, T]]
    print("✓ Test 5 passed: second flip covers the merged region")

    # Test case 6: Large single-color image
    img6 = [[F] * 300 for _ in range(300)]
    solution.flip_color(img6, 150, 150)
    assert all(all(row) for row in img6)
    print("✓ Test 6 passed: 300x300 image fully flipped")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_flip_color()
