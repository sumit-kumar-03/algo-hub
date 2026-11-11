"""
EPI 9.4 Extra Variant - Is One Node an Ancestor of Another
(Practice problem, not in the book. Difficulty: Easy)
Builds on: walking up a tree through parent pointers in O(h) time and O(1)
space.

Problem:
Every node in a binary tree stores a pointer to its parent (None for the
root). Given two nodes a and b of the same tree, return True if a is an
ancestor of b and False otherwise. A node counts as an ancestor of itself.

Constraints:
- Both nodes belong to the same tree
- O(h) time and O(1) extra space, where h is the tree height
- No hash sets; only follow parent pointers

How it works (climb from the lower node):
1. Start at b and follow parent pointers toward the root
2. If you ever reach a, return True
3. If you fall off the root (None), return False
(Optional speedup: compute both depths first; if a is deeper than b it
cannot be an ancestor, otherwise climb exactly depth(b) - depth(a) steps
and compare once.)

Example 1 (Figure 9.1 in the book):
Input: a = I (key 6, root's right child), b = M (key 641)
Output: True
Explanation: M -> L -> K -> J -> I.

Example 2:
Input: a = M, b = I
Output: False
Explanation: A deeper node cannot be an ancestor of a shallower one.
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
    def is_ancestor(self, a: BinaryTreeNode, b: BinaryTreeNode) -> bool:
        """
        Checks whether a is an ancestor of b (or the same node).

        Args:
            a: Candidate ancestor
            b: Candidate descendant in the same tree

        Returns:
            True if a lies on the path from b up to the root

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # TODO: Implement ancestor check with parent pointers
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


def test_is_ancestor():
    """Test cases for the ancestor check"""
    solution = Solution()
    t = build_figure_9_1()

    # Test case 1: Book example, deep descendant
    assert solution.is_ancestor(t["I"], t["M"]) is True
    print("✓ Test 1 passed: I is an ancestor of M")

    # Test case 2: Reversed arguments
    assert solution.is_ancestor(t["M"], t["I"]) is False
    print("✓ Test 2 passed: M is not an ancestor of I")

    # Test case 3: A node is its own ancestor
    assert solution.is_ancestor(t["G"], t["G"]) is True
    print("✓ Test 3 passed: Node is its own ancestor")

    # Test case 4: Root is an ancestor of everything
    assert all(solution.is_ancestor(t["A"], node) is True for node in t.values())
    print("✓ Test 4 passed: Root is an ancestor of every node")

    # Test case 5: Same depth, different subtrees
    assert solution.is_ancestor(t["C"], t["O"]) is False
    print("✓ Test 5 passed: Cousins are not ancestors")

    # Test case 6: Shallower node in a different subtree
    assert solution.is_ancestor(t["B"], t["P"]) is False
    assert solution.is_ancestor(t["F"], t["H"]) is True
    print("✓ Test 6 passed: Shallower node in another subtree")

    # Test case 7: Single-node tree
    lone = BinaryTreeNode(5)
    assert solution.is_ancestor(lone, lone) is True
    print("✓ Test 7 passed: Single-node tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_ancestor()
