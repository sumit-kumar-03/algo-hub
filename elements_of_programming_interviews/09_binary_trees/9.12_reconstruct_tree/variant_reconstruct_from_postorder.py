"""
EPI 9.12 Variant - Reconstruct a Binary Tree From Inorder and Postorder

Problem:
Given the inorder and postorder traversal sequences of a binary tree whose
keys are all distinct, rebuild the tree and return its root.

Constraints:
- 0 <= n <= 10^4, both sequences have length n
- All keys are distinct and the sequences describe a valid tree
- O(n) time, O(n) space

How it works (root is the last postorder key):
1. Build a hash map from each key to its index in the inorder sequence
2. The last postorder key is the root; its inorder index i splits the
   inorder range into left (before i) and right (after i) subtrees
3. If the left subtree has k keys, the first k keys of the postorder range
   are its postorder sequence; the next keys (excluding the root) belong to
   the right subtree
4. Recurse on index ranges to build both subtrees

Example 1 (Figure 9.5 in the book):
Input: inorder   = [F, B, A, E, H, C, D, I, G]
       postorder = [F, A, E, B, I, G, D, C, H]
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
Input: inorder = [1, 2, 3], postorder = [3, 2, 1]
Output: a right-skewed chain 1 -> 2 -> 3
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
    def binary_tree_from_inorder_postorder(
        self, inorder: List[Hashable], postorder: List[Hashable]
    ) -> Optional[BinaryTreeNode]:
        """
        Rebuilds a binary tree from its inorder and postorder sequences.

        Args:
            inorder: Keys in inorder
            postorder: Keys in postorder

        Returns:
            Root of the reconstructed tree (None if the sequences are empty)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement reconstruction from inorder and postorder
        pass


def same_tree(a: Optional[BinaryTreeNode], b: Optional[BinaryTreeNode]) -> bool:
    """Returns True if both trees have identical shape and keys."""
    if a is None or b is None:
        return a is None and b is None
    return a.data == b.data and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def test_binary_tree_from_inorder_postorder():
    """Test cases for inorder + postorder reconstruction"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty sequences
    assert solution.binary_tree_from_inorder_postorder([], []) is None
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert same_tree(solution.binary_tree_from_inorder_postorder([7], [7]), N(7))
    print("✓ Test 2 passed: Single node")

    # Test case 3: Book example (Figure 9.5)
    expected3 = N(
        "H",
        N("B", N("F"), N("E", N("A"))),
        N("C", None, N("D", None, N("G", N("I")))),
    )
    result3 = solution.binary_tree_from_inorder_postorder(
        list("FBAEHCDIG"), list("FAEBIGDCH")
    )
    assert same_tree(result3, expected3)
    print("✓ Test 3 passed: Figure 9.5 tree")

    # Test case 4: Right-skewed chain
    assert same_tree(
        solution.binary_tree_from_inorder_postorder([1, 2, 3], [3, 2, 1]),
        N(1, None, N(2, None, N(3))),
    )
    print("✓ Test 4 passed: Right-skewed chain")

    # Test case 5: Left-skewed chain
    assert same_tree(
        solution.binary_tree_from_inorder_postorder([3, 2, 1], [3, 2, 1]),
        N(1, N(2, N(3))),
    )
    print("✓ Test 5 passed: Left-skewed chain")

    # Test case 6: Perfect tree
    expected6 = N(4, N(2, N(1), N(3)), N(6, N(5), N(7)))
    assert same_tree(
        solution.binary_tree_from_inorder_postorder(
            [1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 5, 7, 6, 4]
        ),
        expected6,
    )
    print("✓ Test 6 passed: Perfect tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_binary_tree_from_inorder_postorder()
