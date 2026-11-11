"""
EPI 14.1 Extra Variant - Validate a BST Where Duplicates Must Go Left
(Practice problem, not in the book. Difficulty: Medium)
Builds on: range checking from the BST validation problem, where the
allowed range for each subtree now has one closed end and one open end.

Problem:
Some BST implementations insert a key equal to a node's key into its LEFT
subtree. Under that convention a tree is valid when, for every node, all
keys in its left subtree are <= the node's key and all keys in its right
subtree are STRICTLY greater. Return True if the given binary tree is valid
under this rule.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(h) space where h is the tree height

How it works (half-open ranges):
1. Recurse with a range (low, high] meaning low < key <= high, starting at
   (-inf, +inf]
2. A node is valid if low < node.data <= high
3. The left child inherits (low, node.data]: keys may equal node.data
4. The right child gets (node.data, high]: keys must exceed node.data
5. Careful: the bounds' strictness is inherited, so a right-subtree node
   deep in a left subtree still cannot equal an ancestor whose right
   subtree it belongs to

Example 1:
Input:      5
           / \\
          5   7
         /
        3
Output: True

Example 2:
Input:      5
           / \\
          3   5
Output: False
Explanation: The 5 in the right subtree is not strictly greater than 5.
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
    def is_bst_duplicates_left(self, tree: Optional[BinaryTreeNode]) -> bool:
        """
        Checks the BST property with duplicates allowed only on the left.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            True if every left subtree key is <= its ancestor and every right
            subtree key is > its ancestor

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement half-open range check
        pass


def test_is_bst_duplicates_left():
    """Test cases for BST with left-side duplicates"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Duplicate on the left is fine
    assert solution.is_bst_duplicates_left(N(5, N(5, N(3)), N(7))) is True
    print("✓ Test 1 passed: Left duplicate -> True")

    # Test case 2: Duplicate on the right is not
    assert solution.is_bst_duplicates_left(N(5, N(3), N(5))) is False
    print("✓ Test 2 passed: Right duplicate -> False")

    # Test case 3: Empty tree and single node
    assert solution.is_bst_duplicates_left(None) is True
    assert solution.is_bst_duplicates_left(N(0)) is True
    print("✓ Test 3 passed: Empty / single node")

    # Test case 4: Deep duplicate of an ancestor inside its right subtree
    #       10
    #         \\
    #          20
    #         /
    #        10    <- equals the root but lies in the root's right subtree
    tree = N(10, None, N(20, N(10)))
    assert solution.is_bst_duplicates_left(tree) is False
    print("✓ Test 4 passed: Deep right-side duplicate -> False")

    # Test case 5: Deep duplicate of an ancestor inside its left subtree
    #       10
    #      /
    #     4
    #      \\
    #       10    <- allowed: in the root's left subtree, > 4
    tree = N(10, N(4, None, N(10)))
    assert solution.is_bst_duplicates_left(tree) is True
    print("✓ Test 5 passed: Deep left-side duplicate -> True")

    # Test case 6: Ordinary violation several levels down
    tree = N(10, N(5, None, N(12)), N(15))
    assert solution.is_bst_duplicates_left(tree) is False
    print("✓ Test 6 passed: 12 in left subtree of 10 -> False")

    # Test case 7: All-equal left chain is valid; same chain to the right is not
    assert solution.is_bst_duplicates_left(N(2, N(2, N(2, N(2))))) is True
    assert solution.is_bst_duplicates_left(N(2, None, N(2, None, N(2)))) is False
    print("✓ Test 7 passed: Equal chains")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_bst_duplicates_left()
