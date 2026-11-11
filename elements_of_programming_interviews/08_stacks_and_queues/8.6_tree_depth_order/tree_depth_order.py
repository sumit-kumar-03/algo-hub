"""
EPI 8.6 - Compute Binary Tree Nodes in Order of Increasing Depth

Problem:
Given the root of a binary tree, return its keys grouped by level: one list
per depth, starting at the root's depth (0), with the keys in each level
ordered from left to right.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(m) space where m is the maximum number of nodes at any depth

How it works (level-by-level BFS with two queues):
1. Start with a queue holding just the root (return [] for an empty tree)
2. Record the keys of every node in the current queue as one level
3. Build the next queue from the children of the current nodes, left child
   before right child
4. Repeat until the next queue is empty

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
Output: [[314], [6, 6], [271, 561, 2, 271], [28, 0, 3, 1, 28],
         [17, 401, 257], [641]]

Example 2:
Input:      1
           /
          2
           \\
            3
Output: [[1], [2], [3]]
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
    def binary_tree_depth_order(
        self, tree: Optional[BinaryTreeNode]
    ) -> List[List[int]]:
        """
        Returns the keys of the tree grouped by depth, left to right.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            A list of levels, each a list of keys

        Time Complexity: O(n)
        Space Complexity: O(m) where m is the widest level
        """
        # TODO: Implement depth-order traversal
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


def test_binary_tree_depth_order():
    """Test cases for depth-order traversal"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.binary_tree_depth_order(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.binary_tree_depth_order(N(7)) == [[7]]
    print("✓ Test 2 passed: Single node")

    # Test case 3: Figure 9.1 tree
    assert solution.binary_tree_depth_order(build_figure_9_1()) == [
        [314],
        [6, 6],
        [271, 561, 2, 271],
        [28, 0, 3, 1, 28],
        [17, 401, 257],
        [641],
    ]
    print("✓ Test 3 passed: Figure 9.1 tree")

    # Test case 4: Zigzag chain
    assert solution.binary_tree_depth_order(N(1, N(2, None, N(3)))) == [[1], [2], [3]]
    print("✓ Test 4 passed: Zigzag chain")

    # Test case 5: Gaps in a level keep left-to-right order
    tree5 = N(1, N(2, None, N(4)), N(3, N(5)))
    assert solution.binary_tree_depth_order(tree5) == [[1], [2, 3], [4, 5]]
    print("✓ Test 5 passed: Left-to-right order with gaps")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_binary_tree_depth_order()
