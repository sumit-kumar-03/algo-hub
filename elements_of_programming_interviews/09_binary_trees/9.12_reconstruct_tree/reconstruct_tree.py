"""
EPI 9.12 - Reconstruct a Binary Tree From Traversal Data

Problem:
Given the preorder and inorder traversal sequences of a binary tree whose
keys are all distinct, rebuild the tree and return its root.

Constraints:
- 0 <= n <= 10^4, both sequences have length n
- All keys are distinct and the sequences describe a valid tree
- O(n) time, O(n) space

How it works (root splits the inorder sequence):
1. Build a hash map from each key to its index in the inorder sequence
2. The first preorder key is the root; its inorder index i splits the
   inorder range into the left subtree (before i) and right subtree (after)
3. The left subtree's size k tells you that the next k preorder keys form
   the left subtree's preorder sequence, and the rest form the right's
4. Recurse on index ranges (no slicing) to build both subtrees

Example 1 (Figure 9.5 in the book):
Input: preorder = [H, B, F, E, A, C, D, G, I]
       inorder  = [F, B, A, E, H, C, D, I, G]
Output:         H
              /   \\
             B     C
            / \\     \\
           F   E     D
              /       \\
             A         G
                      /
                     I

Example 2:
Input: preorder = [1, 2, 3], inorder = [3, 2, 1]
Output: a left-skewed chain 1 -> 2 -> 3
"""

from typing import Hashable, List, Optional


class BinaryTreeNode:
    def __init__(
        self,
        data: Hashable = 0,
        left: "Optional[BinaryTreeNode]" = None,
        right: "Optional[BinaryTreeNode]" = None,
    ):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def binary_tree_from_preorder_inorder(
        self, preorder: List[Hashable], inorder: List[Hashable]
    ) -> Optional[BinaryTreeNode]:
        """
        Rebuilds a binary tree from its preorder and inorder sequences.

        Args:
            preorder: Keys in preorder
            inorder: Keys in inorder

        Returns:
            Root of the reconstructed tree (None if the sequences are empty)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement reconstruction from preorder and inorder
        pass


def same_tree(a: Optional[BinaryTreeNode], b: Optional[BinaryTreeNode]) -> bool:
    """Returns True if both trees have identical shape and keys."""
    if a is None or b is None:
        return a is None and b is None
    return a.data == b.data and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def test_binary_tree_from_preorder_inorder():
    """Test cases for preorder + inorder reconstruction"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty sequences
    assert solution.binary_tree_from_preorder_inorder([], []) is None
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert same_tree(solution.binary_tree_from_preorder_inorder([7], [7]), N(7))
    print("✓ Test 2 passed: Single node")

    # Test case 3: Book example (Figure 9.5)
    expected3 = N(
        "H",
        N("B", N("F"), N("E", N("A"))),
        N("C", None, N("D", None, N("G", N("I")))),
    )
    result3 = solution.binary_tree_from_preorder_inorder(
        list("HBFEACDGI"), list("FBAEHCDIG")
    )
    assert same_tree(result3, expected3)
    print("✓ Test 3 passed: Figure 9.5 tree")

    # Test case 4: Left-skewed chain
    assert same_tree(
        solution.binary_tree_from_preorder_inorder([1, 2, 3], [3, 2, 1]),
        N(1, N(2, N(3))),
    )
    print("✓ Test 4 passed: Left-skewed chain")

    # Test case 5: Right-skewed chain
    assert same_tree(
        solution.binary_tree_from_preorder_inorder([1, 2, 3], [1, 2, 3]),
        N(1, None, N(2, None, N(3))),
    )
    print("✓ Test 5 passed: Right-skewed chain")

    # Test case 6: Perfect tree
    expected6 = N(4, N(2, N(1), N(3)), N(6, N(5), N(7)))
    assert same_tree(
        solution.binary_tree_from_preorder_inorder(
            [4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7]
        ),
        expected6,
    )
    print("✓ Test 6 passed: Perfect tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_binary_tree_from_preorder_inorder()
