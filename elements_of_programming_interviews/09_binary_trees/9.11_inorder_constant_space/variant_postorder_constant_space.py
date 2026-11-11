"""
EPI 9.11 Variant - Postorder Traversal With O(1) Space

Problem:
Each node of the binary tree has a parent pointer (None for the root).
Return the keys in postorder (left subtree, right subtree, node) without
recursion, without an explicit stack, and without modifying the tree.

Constraints:
- 0 <= number of nodes <= 10^4
- Parent pointers are correct
- O(n) time, O(1) additional space

How it works (track where you came from):
1. Walk the tree keeping the current node and the previously visited node
2. Arriving from the parent: go left if possible, else right if possible,
   else emit the node and go up
3. Arriving from the left child: go right if possible, else emit and go up
4. Arriving from the right child: emit the node and go up
5. Stop when you move above the root

Example 1:
Input:      2
           / \\
          1   3
Output: [1, 3, 2]

Example 2 (Figure 9.1 in the book):
Input: the 16-node sample tree with root 314
Output: [28, 0, 271, 17, 3, 561, 6, 641, 401, 257, 1, 2, 28, 271, 6, 314]
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
    def postorder_traversal(self, tree: Optional[BinaryTreeNode]) -> List[int]:
        """
        Returns the postorder sequence using parent pointers and O(1) space.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            Keys in postorder

        Time Complexity: O(n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement constant-space postorder traversal
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


def test_postorder_traversal():
    """Test cases for constant-space postorder traversal"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.postorder_traversal(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.postorder_traversal(N(5)) == [5]
    print("✓ Test 2 passed: Single node")

    # Test case 3: Three-node tree
    tree3 = N(2, N(1), N(3))
    set_parents(tree3)
    assert solution.postorder_traversal(tree3) == [1, 3, 2]
    print("✓ Test 3 passed: Three-node tree")

    # Test case 4: Skewed chains
    left_chain = N(3, N(2, N(1)))
    right_chain = N(1, None, N(2, None, N(3)))
    set_parents(left_chain)
    set_parents(right_chain)
    assert solution.postorder_traversal(left_chain) == [1, 2, 3]
    assert solution.postorder_traversal(right_chain) == [3, 2, 1]
    print("✓ Test 4 passed: Skewed chains")

    # Test case 5: Figure 9.1 tree
    assert solution.postorder_traversal(build_figure_9_1()) == [
        28, 0, 271, 17, 3, 561, 6, 641, 401, 257, 1, 2, 28, 271, 6, 314
    ]
    print("✓ Test 5 passed: Figure 9.1 tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_postorder_traversal()
