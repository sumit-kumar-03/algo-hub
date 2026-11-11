"""
EPI 12.4 - Compute the LCA, Optimizing for Close Ancestors

Problem:
Each node of a binary tree has a parent pointer. Given two nodes, return their
lowest common ancestor (LCA). The running time should depend only on how far
the two nodes are from their LCA, not on the height of the tree. For example,
two siblings deep in a tall tree should be handled in constant time.

Constraints:
- 1 <= number of nodes <= 10^5
- Both nodes belong to the same tree (raise ValueError otherwise)
- O(D0 + D1) time and space, where D0 and D1 are the distances from the two
  nodes to their LCA

How it works:
1. Walk upward from both nodes in tandem, one step each per round
2. Record every visited node in a hash set
3. The first time a walker reaches a node already in the set, that node is
   the LCA
4. If both walkers run past the root without a match, the nodes are in
   different trees

Example 1:
Input:        1
            /   \\
           2     3
          / \\
         4   5
        node0 = 4, node1 = 5
Output: 2

Example 2:
Input: same tree, node0 = 4, node1 = 3
Output: 1
"""

from typing import Optional


class BinaryTreeNode:
    def __init__(
        self,
        data: int = 0,
        left: "Optional[BinaryTreeNode]" = None,
        right: "Optional[BinaryTreeNode]" = None,
        parent: "Optional[BinaryTreeNode]" = None,
    ):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        if left:
            left.parent = self
        if right:
            right.parent = self


class Solution:
    def lca(self, node0: BinaryTreeNode, node1: BinaryTreeNode) -> BinaryTreeNode:
        """
        Computes the lowest common ancestor of two nodes using parent pointers.

        Args:
            node0: First node
            node1: Second node

        Returns:
            The LCA node of node0 and node1

        Raises:
            ValueError: If the nodes are not in the same tree

        Time Complexity: O(D0 + D1)
        Space Complexity: O(D0 + D1)
        """
        # TODO: Implement LCA optimized for close ancestors
        pass


def test_lca():
    """Test cases for LCA optimized for close ancestors"""
    solution = Solution()
    N = BinaryTreeNode

    #         1
    #       /   \
    #      2     3
    #     / \     \
    #    4   5     6
    #       / \
    #      7   8
    n7, n8 = N(7), N(8)
    n4, n5 = N(4), N(5, n7, n8)
    n6 = N(6)
    n2, n3 = N(2, n4, n5), N(3, None, n6)
    root = N(1, n2, n3)

    # Test case 1: Siblings
    assert solution.lca(n4, n5) is n2
    print("✓ Test 1 passed: Siblings 4 and 5 -> 2")

    # Test case 2: Nodes in different subtrees of the root
    assert solution.lca(n7, n6) is root
    print("✓ Test 2 passed: 7 and 6 -> 1")

    # Test case 3: One node is the ancestor of the other
    assert solution.lca(n2, n8) is n2
    print("✓ Test 3 passed: 2 and 8 -> 2")

    # Test case 4: Same node twice
    assert solution.lca(n7, n7) is n7
    print("✓ Test 4 passed: 7 and 7 -> 7")

    # Test case 5: Uneven depths
    assert solution.lca(n8, n4) is n2
    print("✓ Test 5 passed: 8 and 4 -> 2")

    # Test case 6: Root with a leaf
    assert solution.lca(root, n6) is root
    print("✓ Test 6 passed: root and 6 -> root")

    # Test case 7: Nodes from different trees
    other = N(42)
    try:
        solution.lca(n7, other)
        raised = False
    except ValueError:
        raised = True
    assert raised is True
    print("✓ Test 7 passed: Different trees raise ValueError")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_lca()
