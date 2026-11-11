"""
EPI 14.1 - Test if a Binary Tree Satisfies the BST Property

Problem:
Given the root of a binary tree, return True if it is a binary search tree:
for every node, all keys in its left subtree are <= its key and all keys in
its right subtree are >= its key.

Constraints:
- 0 <= number of nodes <= 10^4
- Checking only each node against its direct children is NOT enough;
  a violation can be several levels deep

How it works (range checking):
1. Recurse with an allowed range (low, high), starting at (-inf, +inf)
2. An empty tree is valid
3. If node.data is outside [low, high], return False
4. Check left with (low, node.data) and right with (node.data, high)

Example 1:
Input:      10
           /  \\
          5    15
         / \\
        2   7
Output: True

Example 2:
Input:      10
           /  \\
          5    15
           \\
            12
Output: False
Explanation: 12 is in the left subtree of 10 but is greater than 10.
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
    def is_binary_tree_bst(self, tree: Optional[BinaryTreeNode]) -> bool:
        """
        Checks whether a binary tree satisfies the BST property.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            True if the tree is a valid binary search tree

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement BST property check
        pass


def test_is_binary_tree_bst():
    """Test cases for BST property check"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.is_binary_tree_bst(None) is True
    print("✓ Test 1 passed: Empty tree is a BST")

    # Test case 2: Single node
    assert solution.is_binary_tree_bst(N(42)) is True
    print("✓ Test 2 passed: Single node is a BST")

    # Test case 3: Valid BST
    tree3 = N(10, N(5, N(2), N(7)), N(15, N(12), N(20)))
    assert solution.is_binary_tree_bst(tree3) is True
    print("✓ Test 3 passed: Valid BST")

    # Test case 4: Direct child violation
    tree4 = N(10, N(11), N(15))
    assert solution.is_binary_tree_bst(tree4) is False
    print("✓ Test 4 passed: Left child larger than root")

    # Test case 5: Deep violation (each parent/child pair looks fine)
    tree5 = N(10, N(5, None, N(12)), N(15))
    assert solution.is_binary_tree_bst(tree5) is False
    print("✓ Test 5 passed: Deep violation detected")

    # Test case 6: Deep violation on the right side
    tree6 = N(10, N(5), N(15, N(8), N(20)))
    assert solution.is_binary_tree_bst(tree6) is False
    print("✓ Test 6 passed: Right-side deep violation detected")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_binary_tree_bst()
