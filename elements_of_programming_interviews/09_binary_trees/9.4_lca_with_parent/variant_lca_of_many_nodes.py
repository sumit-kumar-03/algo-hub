"""
EPI 9.4 Extra Variant - LCA of Many Nodes
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the depth-equalize-then-climb LCA for two nodes with parent
pointers.

Problem:
Every node in a binary tree stores a pointer to its parent (None for the
root). Given a nonempty list of nodes from the same tree (the list may
contain the same node more than once), return their lowest common ancestor:
the deepest node that is an ancestor of every node in the list. A node
counts as an ancestor of itself.

Constraints:
- 1 <= len(nodes) <= 10^4; all nodes belong to the same tree
- O(m * h) time, where m = len(nodes) and h is the tree height
- O(1) extra space: no hash sets, no recorded paths

How it works (fold the two-node LCA, but keep the depth):
1. LCA is associative: lca(a, b, c) = lca(lca(a, b), c)
2. Keep a running answer and its depth; for each next node, compute its
   depth, equalize, and climb in lockstep to get the new running answer
3. Small optimization: once the running answer is the root, stop early
4. Return the running answer

Example 1 (Figure 9.1 in the book):
Input: nodes = [M (641), N (257), P (28)]
Output: node I (key 6)
Explanation: lca(M, N) = K, and lca(K, P) = I.

Example 2:
Input: nodes = [D (28), E (0), H (17)]
Output: node B (key 6)
"""

from typing import Dict, List, Optional


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
    def lca_of_nodes(self, nodes: List[BinaryTreeNode]) -> BinaryTreeNode:
        """
        Returns the lowest common ancestor of all given nodes.

        Args:
            nodes: Nonempty list of nodes from the same tree

        Returns:
            The deepest node that is an ancestor of every node in the list

        Time Complexity: O(m * h)
        Space Complexity: O(1)
        """
        # TODO: Implement LCA of many nodes with parent pointers
        pass


def set_parents(
    node: Optional[BinaryTreeNode], parent: Optional[BinaryTreeNode] = None
) -> None:
    """Fills in the parent field of every node in the tree."""
    if node:
        node.parent = parent
        set_parents(node.left, node)
        set_parents(node.right, node)


def build_figure_9_1() -> Dict[str, BinaryTreeNode]:
    """Builds the Figure 9.1 tree and returns its nodes keyed by letter."""
    N = BinaryTreeNode
    t = {}
    t["D"], t["E"] = N(28), N(0)
    t["C"] = N(271, t["D"], t["E"])
    t["H"] = N(17)
    t["G"] = N(3, t["H"])
    t["F"] = N(561, None, t["G"])
    t["B"] = N(6, t["C"], t["F"])
    t["M"] = N(641)
    t["L"] = N(401, None, t["M"])
    t["N"] = N(257)
    t["K"] = N(1, t["L"], t["N"])
    t["J"] = N(2, None, t["K"])
    t["P"] = N(28)
    t["O"] = N(271, None, t["P"])
    t["I"] = N(6, t["J"], t["O"])
    t["A"] = N(314, t["B"], t["I"])
    set_parents(t["A"])
    return t


def test_lca_of_nodes():
    """Test cases for LCA of many nodes"""
    solution = Solution()
    t = build_figure_9_1()

    # Test case 1: Single node is its own LCA
    assert solution.lca_of_nodes([t["G"]]) is t["G"]
    print("✓ Test 1 passed: Single node")

    # Test case 2: Two nodes (same as the main problem)
    assert solution.lca_of_nodes([t["M"], t["N"]]) is t["K"]
    print("✓ Test 2 passed: Two nodes")

    # Test case 3: Three nodes, answer moves up as nodes are added
    assert solution.lca_of_nodes([t["M"], t["N"], t["P"]]) is t["I"]
    assert solution.lca_of_nodes([t["P"], t["N"], t["M"]]) is t["I"]
    print("✓ Test 3 passed: Order does not matter")

    # Test case 4: Leaves under one subtree
    assert solution.lca_of_nodes([t["D"], t["E"], t["H"]]) is t["B"]
    print("✓ Test 4 passed: lca(D, E, H) is B")

    # Test case 5: One node in the list is an ancestor of the others
    assert solution.lca_of_nodes([t["L"], t["M"], t["J"]]) is t["J"]
    assert solution.lca_of_nodes([t["H"], t["G"], t["F"]]) is t["F"]
    print("✓ Test 5 passed: Ancestor inside the list")

    # Test case 6: Duplicates in the list
    assert solution.lca_of_nodes([t["M"], t["M"], t["M"]]) is t["M"]
    print("✓ Test 6 passed: Repeated node")

    # Test case 7: Nodes spread across the whole tree
    assert solution.lca_of_nodes([t[c] for c in "DHMNP"]) is t["A"]
    print("✓ Test 7 passed: Answer is the root")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_lca_of_nodes()
