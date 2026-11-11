"""
EPI 9.13 Variant - Reconstruct a Binary Tree From a Postorder Traversal With Markers

Problem:
A postorder traversal (left subtree, right subtree, node) is written out
with None wherever a child is empty. Given such a marked postorder
sequence, rebuild the binary tree and return its root.

(The book also asks whether a marked inorder sequence would suffice. It
does not: for example, [None, 1, None, 2, None] is the marked inorder
sequence of both "1 with right child 2" and "2 with left child 1".)

Constraints:
- 1 <= len(postorder) <= 2 * 10^4 + 1 (a tree with n nodes yields 2n + 1 entries)
- The sequence is a valid marked postorder traversal
- Keys may repeat
- O(n) time, O(n) space

How it works (stack of finished subtrees):
1. Scan the sequence left to right with a stack of subtrees
2. A None entry pushes an empty subtree
3. A key pops the right subtree, then the left subtree, creates a node
   with those children, and pushes it
4. At the end the stack holds exactly the root
   (Equivalently, read the sequence right to left and build node, right,
   left recursively.)

Example 1 (Figure 9.5 in the book):
Input: [None, None, F, None, None, A, None, E, B,
        None, None, None, None, I, None, G, D, C, H]
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
Input: [None, None, 2, None, 1]
Output:   1
         /
        2
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
    def reconstruct_postorder(
        self, postorder: List[Optional[Hashable]]
    ) -> Optional[BinaryTreeNode]:
        """
        Rebuilds a binary tree from a postorder sequence with None markers.

        Args:
            postorder: Postorder keys with None for every empty child

        Returns:
            Root of the reconstructed tree (None for an empty tree)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement reconstruction from marked postorder
        pass


def same_tree(a: Optional[BinaryTreeNode], b: Optional[BinaryTreeNode]) -> bool:
    """Returns True if both trees have identical shape and keys."""
    if a is None or b is None:
        return a is None and b is None
    return a.data == b.data and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def test_reconstruct_postorder():
    """Test cases for marked postorder reconstruction"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.reconstruct_postorder([None]) is None
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert same_tree(solution.reconstruct_postorder([None, None, 1]), N(1))
    print("✓ Test 2 passed: Single node")

    # Test case 3: Same keys, different shapes are told apart by markers
    assert same_tree(
        solution.reconstruct_postorder([None, None, 2, None, 1]), N(1, N(2))
    )
    assert same_tree(
        solution.reconstruct_postorder([None, None, None, 2, 1]), N(1, None, N(2))
    )
    print("✓ Test 3 passed: Markers distinguish shapes")

    # Test case 4: Figure 9.5 tree
    seq4 = [None, None, "F", None, None, "A", None, "E", "B",
            None, None, None, None, "I", None, "G", "D", "C", "H"]
    expected4 = N(
        "H",
        N("B", N("F"), N("E", N("A"))),
        N("C", None, N("D", None, N("G", N("I")))),
    )
    assert same_tree(solution.reconstruct_postorder(seq4), expected4)
    print("✓ Test 4 passed: Figure 9.5 tree")

    # Test case 5: Perfect tree
    seq5 = [None, None, 1, None, None, 3, 2, None, None, 5, None, None, 7, 6, 4]
    expected5 = N(4, N(2, N(1), N(3)), N(6, N(5), N(7)))
    assert same_tree(solution.reconstruct_postorder(seq5), expected5)
    print("✓ Test 5 passed: Perfect tree")

    # Test case 6: Duplicate keys
    seq6 = [None, None, 5, None, None, 5, None, 5, 5]
    assert same_tree(solution.reconstruct_postorder(seq6), N(5, N(5), N(5, N(5))))
    print("✓ Test 6 passed: Duplicate keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reconstruct_postorder()
