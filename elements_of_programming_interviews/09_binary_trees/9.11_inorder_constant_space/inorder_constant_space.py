"""
EPI 9.11 - Implement an Inorder Traversal With O(1) Space

Problem:
Each node of the binary tree has a parent pointer (None for the root).
Return the keys in inorder (left subtree, node, right subtree) without
recursion and without an explicit stack, using only O(1) extra space
beyond the output list. The tree must not be modified.

Constraints:
- 0 <= number of nodes <= 10^4
- Parent pointers are correct
- O(n) time, O(1) additional space

How it works (track where you came from):
1. Walk the tree keeping the current node and the previously visited node
2. If you arrived from the parent: go to the left child if there is one;
   otherwise emit the node and go right (or back up if there is no right)
3. If you arrived from the left child: emit the node and go right (or up)
4. If you arrived from the right child: the subtree is done, go up
5. Stop when you move above the root

Example 1:
Input:      2
           / \\
          1   3
Output: [1, 2, 3]

Example 2 (Figure 9.1 in the book):
Input: the 16-node sample tree with root 314
Output: [28, 271, 0, 6, 561, 17, 3, 314, 2, 401, 641, 1, 257, 6, 271, 28]
"""

from typing import List, Optional


class BinaryTreeNode:
    def __init__(
        self,
        data: int = 0,
        left: "Optional[BinaryTreeNode]" = None,
        right: "Optional[BinaryTreeNode]" = None,
        parent: "Optional[BinaryTreeNode]" = None,
    ):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def inorder_traversal(self, tree: Optional[BinaryTreeNode]) -> List[int]:
        """
        Returns the inorder sequence using parent pointers and O(1) space.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            Keys in inorder

        Time Complexity: O(n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement constant-space inorder traversal
        pass


def set_parents(
    node: Optional[BinaryTreeNode], parent: Optional[BinaryTreeNode] = None
) -> None:
    """Fills in the parent field of every node in the tree."""
    if node:
        node.parent = parent
        set_parents(node.left, node)
        set_parents(node.right, node)


def build_figure_9_1() -> BinaryTreeNode:
    """Builds the sample tree from Figure 9.1 of the book, with parents."""
    N = BinaryTreeNode
    root = N(
        314,
        N(6, N(271, N(28), N(0)), N(561, None, N(3, N(17)))),
        N(
            6,
            N(2, None, N(1, N(401, None, N(641)), N(257))),
            N(271, None, N(28)),
        ),
    )
    set_parents(root)
    return root


def test_inorder_traversal():
    """Test cases for constant-space inorder traversal"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.inorder_traversal(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.inorder_traversal(N(5)) == [5]
    print("✓ Test 2 passed: Single node")

    # Test case 3: Three-node tree
    tree3 = N(2, N(1), N(3))
    set_parents(tree3)
    assert solution.inorder_traversal(tree3) == [1, 2, 3]
    print("✓ Test 3 passed: Three-node tree")

    # Test case 4: Left-skewed and right-skewed chains
    left_chain = N(3, N(2, N(1)))
    right_chain = N(1, None, N(2, None, N(3)))
    set_parents(left_chain)
    set_parents(right_chain)
    assert solution.inorder_traversal(left_chain) == [1, 2, 3]
    assert solution.inorder_traversal(right_chain) == [1, 2, 3]
    print("✓ Test 4 passed: Skewed chains")

    # Test case 5: Figure 9.1 tree
    assert solution.inorder_traversal(build_figure_9_1()) == [
        28, 271, 0, 6, 561, 17, 3, 314, 2, 401, 641, 1, 257, 6, 271, 28
    ]
    print("✓ Test 5 passed: Figure 9.1 tree")

    # Test case 6: Tree is unchanged after traversal
    tree6 = build_figure_9_1()
    first = solution.inorder_traversal(tree6)
    assert solution.inorder_traversal(tree6) == first
    print("✓ Test 6 passed: Traversal is repeatable")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_inorder_traversal()
