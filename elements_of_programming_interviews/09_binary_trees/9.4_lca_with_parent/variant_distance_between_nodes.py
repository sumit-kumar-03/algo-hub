"""
EPI 9.4 Extra Variant - Distance Between Two Nodes
(Practice problem, not in the book. Difficulty: Medium)
Builds on: equalizing depths and climbing in lockstep through parent
pointers to find the LCA.

Problem:
Every node in a binary tree stores a pointer to its parent (None for the
root). Given two nodes of the same tree, return the number of edges on the
path between them. The distance from a node to itself is 0.

Constraints:
- Both nodes belong to the same tree
- O(h) time and O(1) extra space, where h is the tree height
- No hash sets or recorded paths

How it works (count the steps of the LCA walk):
1. Compute depth(a) and depth(b) by following parent pointers
2. Move the deeper node up until both are at the same depth, counting steps
3. Move both up in lockstep until they meet, adding 2 per lockstep move
4. The total count is the distance (equivalently,
   depth(a) + depth(b) - 2 * depth(lca))

Example 1 (Figure 9.1 in the book):
Input: nodes M (key 641, depth 5) and P (key 28, depth 3)
Output: 6
Explanation: The LCA is I at depth 1, so (5 - 1) + (3 - 1) = 6.

Example 2:
Input: nodes M (641) and N (257)
Output: 3
Explanation: M -> L -> K -> N.
"""

from typing import Dict, Optional


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
    def distance(self, node_0: BinaryTreeNode, node_1: BinaryTreeNode) -> int:
        """
        Returns the number of edges between two nodes using parent pointers.

        Args:
            node_0: A node in the tree
            node_1: Another node in the same tree

        Returns:
            Edge count of the path between the two nodes

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # TODO: Implement node distance with parent pointers
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


def test_distance():
    """Test cases for distance between two nodes"""
    solution = Solution()
    t = build_figure_9_1()

    # Test case 1: Book LCA example, different depths
    assert solution.distance(t["M"], t["P"]) == 6
    assert solution.distance(t["P"], t["M"]) == 6
    print("✓ Test 1 passed: dist(M, P) = 6")

    # Test case 2: Nodes under a shared parent
    assert solution.distance(t["M"], t["N"]) == 3
    print("✓ Test 2 passed: dist(M, N) = 3")

    # Test case 3: Same node
    assert solution.distance(t["G"], t["G"]) == 0
    print("✓ Test 3 passed: Distance to itself is 0")

    # Test case 4: Ancestor and descendant
    assert solution.distance(t["B"], t["H"]) == 3
    assert solution.distance(t["A"], t["M"]) == 5
    print("✓ Test 4 passed: Ancestor/descendant pairs")

    # Test case 5: Path through the root
    assert solution.distance(t["H"], t["M"]) == 9
    print("✓ Test 5 passed: Longest path through the root")

    # Test case 6: Siblings and cousins
    assert solution.distance(t["D"], t["E"]) == 2
    assert solution.distance(t["D"], t["H"]) == 5
    print("✓ Test 6 passed: Siblings and cousins")

    # Test case 7: Long chain, nodes at both ends
    N = BinaryTreeNode
    root = N(0)
    cur = root
    for i in range(1, 300):
        cur.right = N(i)
        cur = cur.right
    set_parents(root)
    assert solution.distance(cur, root) == 299
    print("✓ Test 7 passed: 300-node chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_distance()
