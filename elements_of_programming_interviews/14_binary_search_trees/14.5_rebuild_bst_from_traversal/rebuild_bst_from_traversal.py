"""
EPI 14.5 - Reconstruct a BST from Traversal Data

Problem:
A BST with distinct keys is visited in some traversal order and you are
given only the sequence of keys. An inorder sequence is NOT enough to
recover the tree (for example [1, 2, 3] fits five different BSTs), but a
preorder sequence or a postorder sequence is. Rebuild the unique BST from
a preorder sequence, and separately from a postorder sequence.

Constraints:
- 0 <= len(sequence) <= 10^4
- All keys are distinct and the sequence is a valid traversal of some BST
- Target: O(n) time (the simple "split at the first larger key" recursion
  is O(n^2) in the worst case)

How it works (preorder, value-range recursion):
1. Keep a shared index into the sequence
2. build(lower, upper): if the next key is outside (lower, upper), this
   subtree is empty, so return None
3. Otherwise consume the key as the root, then build the left subtree with
   range (lower, key) and the right subtree with range (key, upper)
4. Postorder works the same way but reads the sequence from the back and
   builds the right subtree before the left one

Example 1:
Input: preorder = [43, 23, 37, 29, 31, 41, 47, 53]
Output:       43
            /    \\
          23      47
            \\       \\
            37       53
           /  \\
         29    41
           \\
            31

Example 2:
Input: postorder = [1, 3, 2]
Output:   2
         / \\
        1   3
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
    def rebuild_bst_from_preorder(
        self, preorder: List[int]
    ) -> Optional[BinaryTreeNode]:
        """
        Rebuilds a BST from its preorder traversal sequence.

        Args:
            preorder: Keys in preorder (distinct)

        Returns:
            Root of the reconstructed BST (None for an empty sequence)

        Time Complexity: O(n)
        Space Complexity: O(h) recursion depth where h is the tree height
        """
        # TODO: Implement preorder reconstruction with value ranges
        pass

    def rebuild_bst_from_postorder(
        self, postorder: List[int]
    ) -> Optional[BinaryTreeNode]:
        """
        Rebuilds a BST from its postorder traversal sequence.

        Args:
            postorder: Keys in postorder (distinct)

        Returns:
            Root of the reconstructed BST (None for an empty sequence)

        Time Complexity: O(n)
        Space Complexity: O(h) recursion depth where h is the tree height
        """
        # TODO: Implement postorder reconstruction with value ranges
        pass


def to_tuple(node: Optional[BinaryTreeNode]):
    """Serializes a tree as nested (data, left, right) tuples for comparison."""
    if node is None:
        return None
    return (node.data, to_tuple(node.left), to_tuple(node.right))


def test_rebuild_bst_from_traversal():
    """Test cases for BST reconstruction from traversal data"""
    solution = Solution()

    book_tree = (
        43,
        (23, None, (37, (29, None, (31, None, None)), (41, None, None))),
        (47, None, (53, None, None)),
    )

    # Test case 1: Book preorder example
    root1 = solution.rebuild_bst_from_preorder([43, 23, 37, 29, 31, 41, 47, 53])
    assert to_tuple(root1) == book_tree
    print("✓ Test 1 passed: Preorder book example")

    # Test case 2: Same tree from its postorder sequence
    root2 = solution.rebuild_bst_from_postorder([31, 29, 41, 37, 23, 53, 47, 43])
    assert to_tuple(root2) == book_tree
    print("✓ Test 2 passed: Postorder of the same tree")

    # Test case 3: Empty sequences
    assert solution.rebuild_bst_from_preorder([]) is None
    assert solution.rebuild_bst_from_postorder([]) is None
    print("✓ Test 3 passed: Empty sequence -> None")

    # Test case 4: Single key
    assert to_tuple(solution.rebuild_bst_from_preorder([7])) == (7, None, None)
    assert to_tuple(solution.rebuild_bst_from_postorder([7])) == (7, None, None)
    print("✓ Test 4 passed: Single key")

    # Test case 5: Balanced three-node tree
    balanced = (2, (1, None, None), (3, None, None))
    assert to_tuple(solution.rebuild_bst_from_preorder([2, 1, 3])) == balanced
    assert to_tuple(solution.rebuild_bst_from_postorder([1, 3, 2])) == balanced
    print("✓ Test 5 passed: Balanced tree from preorder and postorder")

    # Test case 6: Left-skewed and right-skewed trees
    left_skewed = (3, (2, (1, None, None), None), None)
    right_skewed = (1, None, (2, None, (3, None, None)))
    assert to_tuple(solution.rebuild_bst_from_preorder([3, 2, 1])) == left_skewed
    assert to_tuple(solution.rebuild_bst_from_preorder([1, 2, 3])) == right_skewed
    assert to_tuple(solution.rebuild_bst_from_postorder([1, 2, 3])) == left_skewed
    assert to_tuple(solution.rebuild_bst_from_postorder([3, 2, 1])) == right_skewed
    print("✓ Test 6 passed: Skewed trees")

    # Test case 7: Larger tree with negative keys
    expected7 = (
        10,
        (-5, (-8, None, None), (0, None, (4, None, None))),
        (20, (15, None, None), (30, (25, None, None), None)),
    )
    assert (
        to_tuple(solution.rebuild_bst_from_preorder([10, -5, -8, 0, 4, 20, 15, 30, 25]))
        == expected7
    )
    assert (
        to_tuple(solution.rebuild_bst_from_postorder([-8, 4, 0, -5, 15, 25, 30, 20, 10]))
        == expected7
    )
    print("✓ Test 7 passed: Larger tree with negative keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_rebuild_bst_from_traversal()
