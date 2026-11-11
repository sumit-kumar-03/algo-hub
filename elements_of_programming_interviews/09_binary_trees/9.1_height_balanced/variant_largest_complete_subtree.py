"""
EPI 9.1 Variant - Size of the Largest Complete Subtree

Problem:
A binary tree is complete if every level except possibly the last is fully
filled and the nodes on the last level are packed as far left as possible.
Given the root of a binary tree, return the number of nodes in the largest
subtree that is complete. A subtree here means a node together with all of
its descendants.

Constraints:
- 0 <= number of nodes <= 10^4
- Return 0 for an empty tree; every leaf is a complete subtree of size 1
- O(n) time, O(h) space

How it works (post-order, combine child summaries):
1. For each node, compute from its children: is the subtree perfect, is it
   complete, its height, and its size (an empty tree is perfect with
   height -1)
2. A node's subtree is perfect if both children are perfect with equal
   heights
3. It is complete if either the left child is perfect, the right child is
   complete, and the heights are equal; or the left child is complete, the
   right child is perfect, and the left is exactly one level taller
4. Track the largest size among complete subtrees while unwinding

Example 1:
Input:      1
           / \\
          2   3
         / \\  /
        4  5 6
Output: 6
Explanation: The whole tree is complete.

Example 2:
Input:      1
           / \\
          2   3
         /   / \\
        4   6   7
Output: 3
Explanation: Node 2 is missing its right child while level 2 continues to
its right, so the whole tree is not complete; the subtree at 3 has 3 nodes.
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
    def largest_complete_subtree_size(self, tree: Optional[BinaryTreeNode]) -> int:
        """
        Returns the size of the largest complete subtree.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            Number of nodes in the largest complete subtree (0 if empty)

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement largest complete subtree search
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


def test_largest_complete_subtree_size():
    """Test cases for largest complete subtree"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.largest_complete_subtree_size(None) == 0
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.largest_complete_subtree_size(N(1)) == 1
    print("✓ Test 2 passed: Single node")

    # Test case 3: Whole tree is complete (last level partially filled)
    tree3 = N(1, N(2, N(4), N(5)), N(3, N(6)))
    assert solution.largest_complete_subtree_size(tree3) == 6
    print("✓ Test 3 passed: Whole tree complete")

    # Test case 4: Gap on the last level breaks completeness at the root
    tree4 = N(1, N(2, N(4)), N(3, N(6), N(7)))
    assert solution.largest_complete_subtree_size(tree4) == 3
    print("✓ Test 4 passed: Gap on last level")

    # Test case 5: Large complete subtree hanging off a right-only root
    tree5 = N(0, None, N(1, N(2, N(4), N(5)), N(3, N(6))))
    assert solution.largest_complete_subtree_size(tree5) == 6
    print("✓ Test 5 passed: Complete subtree below an incomplete root")

    # Test case 6: Figure 9.1 tree
    assert solution.largest_complete_subtree_size(build_figure_9_1()) == 3
    print("✓ Test 6 passed: Figure 9.1 tree")

    # Test case 7: Perfect tree
    tree7 = N(1, N(2, N(4), N(5)), N(3, N(6), N(7)))
    assert solution.largest_complete_subtree_size(tree7) == 7
    print("✓ Test 7 passed: Perfect tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_largest_complete_subtree_size()
