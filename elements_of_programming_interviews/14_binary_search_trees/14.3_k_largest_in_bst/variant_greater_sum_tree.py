"""
EPI 14.3 Extra Variant - Convert a BST to a Greater Sum Tree
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the reverse inorder traversal (right, node, left), which visits
keys from largest to smallest. Carrying a running total along that order
gives each node the sum of everything at least as large as it.

Problem:
Given the root of a BST with distinct keys, replace every node's key with
the sum of all keys in the original tree that are greater than or equal to
that node's key. Modify the tree in place and keep its shape.

Constraints:
- 0 <= number of nodes <= 10^4
- Keys are distinct integers (they may be negative)
- O(n) time, O(h) space where h is the tree height

How it works:
1. Traverse in reverse inorder: right subtree, node, left subtree
2. Keep a running total of the ORIGINAL keys visited so far
3. At each node, add its original key to the total, then overwrite the key
   with the total
4. Because keys arrive in decreasing order, the total at each node is
   exactly the sum of all keys >= it

Example 1:
Input:      4
           / \\
          1   6
         / \\   \\
        0   2   7
Output:    17
           / \\
         20   13
         / \\    \\
       20   19    7
Explanation: For 4, the keys >= 4 are 4, 6, 7, so it becomes 17.

Example 2:
Input:   1
          \\
           2
Output:  3
          \\
           2
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
    def convert_to_greater_sum(self, tree: Optional[BinaryTreeNode]) -> None:
        """
        Replaces each key with the sum of all keys >= it, in place.

        Args:
            tree: Root of a BST with distinct keys (None for an empty tree)

        Returns:
            None; the tree's keys are updated in place

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement reverse inorder with a running sum
        pass


def preorder_keys(tree: Optional[BinaryTreeNode]) -> List[int]:
    """Returns the keys of the tree in preorder order."""
    if tree is None:
        return []
    return [tree.data] + preorder_keys(tree.left) + preorder_keys(tree.right)


def build_sample_bst() -> BinaryTreeNode:
    """Builds the 16-node sample BST from EPI 14.2 / 14.3."""
    N = BinaryTreeNode
    left = N(7, N(3, N(2), N(5)), N(11, None, N(17, N(13))))
    right = N(
        43,
        N(23, None, N(37, N(29, None, N(31)), N(41))),
        N(47, None, N(53)),
    )
    return N(19, left, right)


def build_bst_from_keys(keys: List[int]) -> Optional[BinaryTreeNode]:
    """Builds a BST by inserting keys in the given order (no balancing)."""
    root = None
    for key in keys:
        node = BinaryTreeNode(key)
        if root is None:
            root = node
            continue
        cur = root
        while True:
            if key < cur.data:
                if cur.left is None:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    break
                cur = cur.right
    return root


def test_convert_to_greater_sum():
    """Test cases for greater sum tree conversion"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Example tree
    tree = N(4, N(1, N(0), N(2)), N(6, None, N(7)))
    solution.convert_to_greater_sum(tree)
    assert preorder_keys(tree) == [17, 20, 20, 19, 13, 7]
    print("✓ Test 1 passed: -> preorder [17, 20, 20, 19, 13, 7]")

    # Test case 2: Two nodes
    tree = N(1, None, N(2))
    solution.convert_to_greater_sum(tree)
    assert preorder_keys(tree) == [3, 2]
    print("✓ Test 2 passed: Two nodes")

    # Test case 3: Empty tree and single node
    solution.convert_to_greater_sum(None)
    single = N(9)
    solution.convert_to_greater_sum(single)
    assert single.data == 9
    print("✓ Test 3 passed: Empty / single node")

    # Test case 4: Shape is preserved (same node objects)
    left, right = N(1), N(3)
    root = N(2, left, right)
    solution.convert_to_greater_sum(root)
    assert root.left is left and root.right is right
    assert (left.data, root.data, right.data) == (6, 5, 3)
    print("✓ Test 4 passed: Same nodes, new keys")

    # Test case 5: Negative keys
    tree = N(0, N(-5, N(-10)), N(5))
    solution.convert_to_greater_sum(tree)
    assert preorder_keys(tree) == [5, 0, -10, 5]
    print("✓ Test 5 passed: Negative keys")

    # Test case 6: Sample 16-node tree against a direct computation
    tree = build_sample_bst()
    original = preorder_keys(tree)
    solution.convert_to_greater_sum(tree)
    assert preorder_keys(tree) == [sum(y for y in original if y >= x) for x in original]
    print("✓ Test 6 passed: Sample tree matches direct sums")

    # Test case 7: Left-skewed chain
    chain = build_bst_from_keys([5, 4, 3, 2, 1])
    solution.convert_to_greater_sum(chain)
    assert preorder_keys(chain) == [5, 9, 12, 14, 15]
    print("✓ Test 7 passed: Left-skewed chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_convert_to_greater_sum()
