"""
EPI 9.4 - Compute the LCA When Nodes Have Parent Pointers

Problem:
Every node in the binary tree stores a pointer to its parent (None for the
root). Given two nodes of the same tree, return their lowest common
ancestor (LCA): the deepest node that has both as descendants. A node
counts as a descendant of itself.

Constraints:
- Both nodes belong to the same tree
- O(h) time and O(1) extra space, where h is the tree height

How it works (equalize depths, then climb together):
1. Compute each node's depth by following parent pointers to the root
2. Move the deeper node up until both are at the same depth
3. Move both nodes up in lockstep until they are the same node
4. That node is the LCA

Example 1 (Figure 9.1 in the book):
Input: nodes M (key 641, depth 5) and P (key 28, depth 3)
Output: node I (the root's right child, key 6)
Explanation: M climbs to K at depth 3; K and P then meet at I.

Example 2:
Input: nodes M (641) and N (257)
Output: node K (key 1)
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


class Solution:
    def lca(self, node_0: BinaryTreeNode, node_1: BinaryTreeNode) -> BinaryTreeNode:
        """
        Returns the lowest common ancestor of two nodes using parent pointers.

        Args:
            node_0: A node in the tree
            node_1: Another node in the same tree

        Returns:
            The deepest node that is an ancestor of both

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # TODO: Implement LCA with parent pointers
        pass


def set_parents(
    node: Optional[BinaryTreeNode], parent: Optional[BinaryTreeNode] = None
) -> None:
    """Fills in the parent field of every node in the tree."""
    if node:
        node.parent = parent
        set_parents(node.left, node)
        set_parents(node.right, node)


def test_lca():
    """Test cases for LCA with parent pointers"""
    solution = Solution()
    N = BinaryTreeNode

    # Figure 9.1 tree with named handles (letters match the book)
    D, E = N(28), N(0)
    C = N(271, D, E)
    H = N(17)
    G = N(3, H)
    F = N(561, None, G)
    B = N(6, C, F)
    M = N(641)
    L = N(401, None, M)
    Nn = N(257)
    K = N(1, L, Nn)
    J = N(2, None, K)
    P = N(28)
    O = N(271, None, P)
    I = N(6, J, O)
    A = N(314, B, I)
    set_parents(A)

    # Test case 1: Book example, different depths
    assert solution.lca(M, P) is I
    assert solution.lca(P, M) is I
    print("✓ Test 1 passed: LCA(M, P) is I")

    # Test case 2: Siblings' descendants
    assert solution.lca(M, Nn) is K
    print("✓ Test 2 passed: LCA(M, N) is K")

    # Test case 3: Same node
    assert solution.lca(G, G) is G
    print("✓ Test 3 passed: LCA of a node with itself")

    # Test case 4: One node is an ancestor of the other
    assert solution.lca(B, H) is B
    assert solution.lca(M, J) is J
    print("✓ Test 4 passed: Ancestor is the LCA")

    # Test case 5: Nodes in different subtrees of the root
    assert solution.lca(D, P) is A
    print("✓ Test 5 passed: LCA across the root")

    # Test case 6: Nodes in sibling subtrees below B
    assert solution.lca(E, H) is B
    print("✓ Test 6 passed: LCA(E, H) is B")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_lca()
