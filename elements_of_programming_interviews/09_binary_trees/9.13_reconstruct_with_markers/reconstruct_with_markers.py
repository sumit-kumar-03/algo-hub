"""
EPI 9.13 - Reconstruct a Binary Tree From a Preorder Traversal With Markers

Problem:
A preorder traversal can be made unambiguous by writing None wherever a
child is empty. Given such a marked preorder sequence, rebuild the binary
tree and return its root.

Constraints:
- 1 <= len(preorder) <= 2 * 10^4 + 1 (a tree with n nodes yields 2n + 1 entries)
- The sequence is a valid marked preorder traversal
- Keys may repeat (the markers alone determine the shape)
- O(n) time, O(h) space beyond the output

How it works (recursion that consumes the sequence):
1. Keep a shared position (or iterator) into the sequence
2. To build a subtree, read the next entry; if it is None, the subtree is
   empty
3. Otherwise create a node with that key, build its left subtree (which
   consumes exactly the left subtree's entries), then build its right
   subtree from what follows
4. Building from the start of the sequence yields the root

Example 1 (Figure 9.5 in the book):
Input: [H, B, F, None, None, E, A, None, None, None, C, None, D, None,
        G, I, None, None, None]
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
Input: [None]
Output: None (empty tree)
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
    def reconstruct_preorder(
        self, preorder: List[Optional[Hashable]]
    ) -> Optional[BinaryTreeNode]:
        """
        Rebuilds a binary tree from a preorder sequence with None markers.

        Args:
            preorder: Preorder keys with None for every empty child

        Returns:
            Root of the reconstructed tree (None for an empty tree)

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement reconstruction from marked preorder
        pass


def same_tree(a: Optional[BinaryTreeNode], b: Optional[BinaryTreeNode]) -> bool:
    """Returns True if both trees have identical shape and keys."""
    if a is None or b is None:
        return a is None and b is None
    return a.data == b.data and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def test_reconstruct_preorder():
    """Test cases for marked preorder reconstruction"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.reconstruct_preorder([None]) is None
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert same_tree(solution.reconstruct_preorder([1, None, None]), N(1))
    print("✓ Test 2 passed: Single node")

    # Test case 3: Book example (Figure 9.5)
    seq3 = ["H", "B", "F", None, None, "E", "A", None, None, None,
            "C", None, "D", None, "G", "I", None, None, None]
    expected3 = N(
        "H",
        N("B", N("F"), N("E", N("A"))),
        N("C", None, N("D", None, N("G", N("I")))),
    )
    assert same_tree(solution.reconstruct_preorder(seq3), expected3)
    print("✓ Test 3 passed: Figure 9.5 tree")

    # Test case 4: Same keys, different shapes are told apart by markers
    left_child = solution.reconstruct_preorder([1, 2, None, None, None])
    right_child = solution.reconstruct_preorder([1, None, 2, None, None])
    assert same_tree(left_child, N(1, N(2)))
    assert same_tree(right_child, N(1, None, N(2)))
    print("✓ Test 4 passed: Markers distinguish shapes")

    # Test case 5: Duplicate keys
    seq5 = [5, 5, None, None, 5, 5, None, None, None]
    assert same_tree(solution.reconstruct_preorder(seq5), N(5, N(5), N(5, N(5))))
    print("✓ Test 5 passed: Duplicate keys")

    # Test case 6: Perfect tree
    seq6 = [4, 2, 1, None, None, 3, None, None, 6, 5, None, None, 7, None, None]
    expected6 = N(4, N(2, N(1), N(3)), N(6, N(5), N(7)))
    assert same_tree(solution.reconstruct_preorder(seq6), expected6)
    print("✓ Test 6 passed: Perfect tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reconstruct_preorder()
