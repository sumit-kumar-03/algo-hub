"""
EPI 8.6 Variant - Zigzag Depth Order

Problem:
Given the root of a binary tree, return its keys grouped by level from the
top down, alternating direction: the root level is read left to right, the
next level right to left, the next left to right, and so on.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(m) space where m is the maximum number of nodes at any depth

How it works (BFS with direction flag):
1. Process the tree level by level, collecting each level's keys left to
   right exactly as in plain depth order
2. Keep a flag for the current direction; reverse the level's keys when
   the flag says right to left
3. Flip the flag after every level

Example 1 (Figure 9.1 in the book):
Input:              314
                 /       \\
               6           6
             /   \\       /   \\
          271    561    2    271
          / \\      \\     \\      \\
        28   0      3     1     28
                   /     / \\
                 17    401  257
                         \\
                         641
Output: [[314], [6, 6], [271, 561, 2, 271], [28, 1, 3, 0, 28],
         [17, 401, 257], [641]]

Example 2:
Input:      1
           / \\
          2   3
         / \\
        4   5
Output: [[1], [3, 2], [4, 5]]
"""

from typing import List, Optional


class BinaryTreeNode:
    def __init__(
        self,
        data: int = 0,
        left: "Optional[BinaryTreeNode]" = None,
        right: "Optional[BinaryTreeNode]" = None,
    ):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def zigzag_depth_order(self, tree: Optional[BinaryTreeNode]) -> List[List[int]]:
        """
        Returns the keys grouped by depth in alternating directions.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            A list of levels; even depths left to right, odd depths right to left

        Time Complexity: O(n)
        Space Complexity: O(m) where m is the widest level
        """
        # TODO: Implement zigzag depth-order traversal
        pass


def build_figure_9_1() -> BinaryTreeNode:
    """Builds the sample tree from Figure 9.1 of the book."""
    N = BinaryTreeNode
    return N(
        314,
        N(6, N(271, N(28), N(0)), N(561, None, N(3, N(17)))),
        N(
            6,
            N(2, None, N(1, N(401, None, N(641)), N(257))),
            N(271, None, N(28)),
        ),
    )


def test_zigzag_depth_order():
    """Test cases for zigzag depth order"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.zigzag_depth_order(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.zigzag_depth_order(N(9)) == [[9]]
    print("✓ Test 2 passed: Single node")

    # Test case 3: Small tree with three levels
    assert solution.zigzag_depth_order(N(1, N(2, N(4), N(5)), N(3))) == [
        [1],
        [3, 2],
        [4, 5],
    ]
    print("✓ Test 3 passed: Small tree")

    # Test case 4: Figure 9.1 tree (book example)
    assert solution.zigzag_depth_order(build_figure_9_1()) == [
        [314],
        [6, 6],
        [271, 561, 2, 271],
        [28, 1, 3, 0, 28],
        [17, 401, 257],
        [641],
    ]
    print("✓ Test 4 passed: Figure 9.1 tree")

    # Test case 5: Perfect tree of height 3
    tree5 = N(
        1,
        N(2, N(4, N(8), N(9)), N(5, N(10), N(11))),
        N(3, N(6, N(12), N(13)), N(7, N(14), N(15))),
    )
    assert solution.zigzag_depth_order(tree5) == [
        [1],
        [3, 2],
        [4, 5, 6, 7],
        [15, 14, 13, 12, 11, 10, 9, 8],
    ]
    print("✓ Test 5 passed: Perfect tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_zigzag_depth_order()
