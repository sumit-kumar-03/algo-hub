"""
EPI 9.1 - Test if a Binary Tree is Height-Balanced

Problem:
A binary tree is height-balanced if, for every node, the heights of its left
and right subtrees differ by at most one. Given the root of a binary tree,
return True if it is height-balanced and False otherwise.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time: compute heights bottom-up in a single traversal instead of
  recomputing heights for every node

How it works (post-order traversal):
1. For a node, recursively get (is_balanced, height) for left and right
2. If either subtree is unbalanced, propagate False immediately
3. The node is balanced if abs(left_height - right_height) <= 1
4. Its height is max(left_height, right_height) + 1 (empty tree has height -1)

Example 1:
Input:      1
           / \\
          2   3
         /
        4
Output: True

Example 2:
Input:      1
           /
          2
         /
        3
Output: False
Explanation: At the root, the left subtree has height 1 and the right is empty.
"""

from typing import Optional


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
    def is_balanced_binary_tree(self, tree: Optional[BinaryTreeNode]) -> bool:
        """
        Checks whether a binary tree is height-balanced.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            True if every node's subtrees differ in height by at most one

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement height-balanced check
        pass


def test_is_balanced_binary_tree():
    """Test cases for height-balanced check"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.is_balanced_binary_tree(None) is True
    print("✓ Test 1 passed: Empty tree is balanced")

    # Test case 2: Single node
    assert solution.is_balanced_binary_tree(N(1)) is True
    print("✓ Test 2 passed: Single node is balanced")

    # Test case 3: Balanced but not perfect
    tree3 = N(1, N(2, N(4)), N(3))
    assert solution.is_balanced_binary_tree(tree3) is True
    print("✓ Test 3 passed: Balanced tree")

    # Test case 4: Left chain of three nodes
    tree4 = N(1, N(2, N(3)))
    assert solution.is_balanced_binary_tree(tree4) is False
    print("✓ Test 4 passed: Left chain is unbalanced")

    # Test case 5: Root heights equal, but a subtree is unbalanced
    tree5 = N(1, N(2, N(3, N(4))), N(5, None, N(6, None, N(7))))
    assert solution.is_balanced_binary_tree(tree5) is False
    print("✓ Test 5 passed: Unbalanced subtree detected")

    # Test case 6: Perfect tree of height 2
    tree6 = N(1, N(2, N(4), N(5)), N(3, N(6), N(7)))
    assert solution.is_balanced_binary_tree(tree6) is True
    print("✓ Test 6 passed: Perfect tree is balanced")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_balanced_binary_tree()
