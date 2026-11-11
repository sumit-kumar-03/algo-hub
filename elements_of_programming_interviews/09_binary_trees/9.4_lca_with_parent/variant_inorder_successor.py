"""
EPI 9.4 Extra Variant - Inorder Successor with Parent Pointers
(Practice problem, not in the book. Difficulty: Medium)
Builds on: navigating a tree upward through parent pointers, using O(h) time
and O(1) space instead of a full traversal.

Problem:
Every node in a binary tree (not necessarily a BST) stores a pointer to its
parent (None for the root). Given a node, return the node that comes right
after it in an inorder traversal of the whole tree, or None if it is the
last node. Keys may repeat, so return the node object, not a key.

Constraints:
- O(h) time and O(1) extra space, where h is the tree height
- Do not traverse the whole tree or store a list of nodes

How it works (two cases):
1. If the node has a right subtree, the successor is the leftmost node of
   that right subtree
2. Otherwise climb through parent pointers while the current node is its
   parent's right child; the first parent reached from a left child is the
   successor (None if you climb past the root)

Example 1 (Figure 9.1 in the book):
Input: node G (key 3)
Output: node A (key 314, the root)
Explanation: G is a right child of F, which is a right child of B, which is
the left child of A.

Example 2:
Input: node A (the root)
Output: node J (key 2)
Explanation: J is the leftmost node of A's right subtree.
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
    def inorder_successor(self, node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        """
        Returns the next node in inorder, using parent pointers.

        Args:
            node: A node in the tree

        Returns:
            The inorder successor node, or None if node is the last one

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # TODO: Implement inorder successor
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


def test_inorder_successor():
    """Test cases for inorder successor"""
    solution = Solution()
    t = build_figure_9_1()

    # Test case 1: Climb several levels to the root
    assert solution.inorder_successor(t["G"]) is t["A"]
    print("✓ Test 1 passed: succ(G) is A")

    # Test case 2: Leftmost node of the right subtree
    assert solution.inorder_successor(t["A"]) is t["J"]
    assert solution.inorder_successor(t["B"]) is t["F"]
    print("✓ Test 2 passed: Right subtree cases")

    # Test case 3: Leaf that is a left child
    assert solution.inorder_successor(t["D"]) is t["C"]
    assert solution.inorder_successor(t["H"]) is t["G"]
    print("✓ Test 3 passed: Left-child leaves")

    # Test case 4: Leaf that is a right child, climb once
    assert solution.inorder_successor(t["E"]) is t["B"]
    assert solution.inorder_successor(t["N"]) is t["I"]
    print("✓ Test 4 passed: Right-child leaves")

    # Test case 5: Last node in inorder
    assert solution.inorder_successor(t["P"]) is None
    print("✓ Test 5 passed: Last node has no successor")

    # Test case 6: Walk the whole tree from the leftmost node
    order = []
    node = t["D"]
    while node is not None and len(order) <= 16:  # guard against cycles
        order.append(node)
        node = solution.inorder_successor(node)
    expected = [t[c] for c in "DCEBFHGAJLMKNIOP"]
    assert len(order) == len(expected)
    assert all(got is want for got, want in zip(order, expected))
    print("✓ Test 6 passed: Full inorder walk")

    # Test case 7: Single node
    lone = BinaryTreeNode(1)
    assert solution.inorder_successor(lone) is None
    print("✓ Test 7 passed: Single node")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_inorder_successor()
