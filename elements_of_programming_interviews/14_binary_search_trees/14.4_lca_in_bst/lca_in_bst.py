"""
EPI 14.4 - Compute the LCA in a BST

Problem:
Given the root of a BST with distinct keys and two nodes s and b that are
in the tree, return their lowest common ancestor (LCA): the deepest node
that has both s and b as descendants (a node counts as its own
descendant). Nodes have no parent pointers.

Constraints:
- 1 <= number of nodes <= 10^4
- All keys are distinct; s and b are both in the tree
- Target: O(h) time and O(1) extra space, where h is the tree height

How it works (use the BST property):
1. Let lo = min(s.data, b.data) and hi = max(s.data, b.data)
2. Starting at the root, if node.data < lo both nodes are on the right,
   so move right; if node.data > hi both are on the left, so move left
3. Otherwise lo <= node.data <= hi: the nodes split here (or the node is
   one of them), so this node is the LCA

Example 1:
Input: BST below, s = node 3, b = node 17
                    19
                 /      \\
               7          43
              / \\        /   \\
             3   11     23     47
            / \\    \\     \\      \\
           2   5    17     37     53
                   /      /  \\
                 13      29   41
                           \\
                            31
Output: node 7
Explanation: 3 < 7 < 17, so the paths to 3 and 17 split at 7.

Example 2:
Input: same BST, s = node 37, b = node 31
Output: node 37
Explanation: 31 is a descendant of 37, so 37 is the LCA.
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
    def find_lca(
        self, tree: BinaryTreeNode, s: BinaryTreeNode, b: BinaryTreeNode
    ) -> BinaryTreeNode:
        """
        Finds the lowest common ancestor of two nodes in a BST.

        Args:
            tree: Root of the BST (keys are distinct)
            s: First node (in the tree)
            b: Second node (in the tree); its key may be smaller or larger than s's

        Returns:
            The LCA node

        Time Complexity: O(h) where h is the tree height
        Space Complexity: O(1)
        """
        # TODO: Implement LCA search using the BST property
        pass


def test_find_lca():
    """Test cases for LCA in a BST"""
    solution = Solution()
    N = BinaryTreeNode

    n2, n5, n13 = N(2), N(5), N(13)
    n3 = N(3, n2, n5)
    n17 = N(17, n13)
    n11 = N(11, None, n17)
    n7 = N(7, n3, n11)
    n31 = N(31)
    n29 = N(29, None, n31)
    n41 = N(41)
    n37 = N(37, n29, n41)
    n23 = N(23, None, n37)
    n53 = N(53)
    n47 = N(47, None, n53)
    n43 = N(43, n23, n47)
    root = N(19, n7, n43)

    # Test case 1: Split inside the left subtree
    assert solution.find_lca(root, n3, n17) is n7
    print("✓ Test 1 passed: LCA(3, 17) = 7")

    # Test case 2: One node is an ancestor of the other, arguments reversed
    assert solution.find_lca(root, n37, n31) is n37
    print("✓ Test 2 passed: LCA(37, 31) = 37")

    # Test case 3: Nodes on opposite sides of the root
    assert solution.find_lca(root, n5, n53) is root
    print("✓ Test 3 passed: LCA(5, 53) = 19 (root)")

    # Test case 4: Same node twice
    assert solution.find_lca(root, n13, n13) is n13
    print("✓ Test 4 passed: LCA(13, 13) = 13")

    # Test case 5: Deep nodes in the right subtree
    assert solution.find_lca(root, n31, n41) is n37
    print("✓ Test 5 passed: LCA(31, 41) = 37")

    # Test case 6: Root is one of the nodes
    assert solution.find_lca(root, root, n2) is root
    print("✓ Test 6 passed: LCA(19, 2) = 19")

    # Test case 7: Siblings
    assert solution.find_lca(root, n2, n5) is n3
    print("✓ Test 7 passed: LCA(2, 5) = 3")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_lca()
