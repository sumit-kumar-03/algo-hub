"""
EPI 9.16 Variant - Right Sibling Tree Without a Next Field

Problem:
The nodes of a perfect binary tree have only left and right child fields
(no extra next field). Rewire the tree in place so that every node's right
field points to the node immediately to its right on the same level, or
None for the rightmost node of each level. Left fields must stay as they
are.

Observation: in a perfect tree, a node's original right child is exactly
the right sibling of its left child, so after the rewiring every level is
still reachable: go down through left fields and across through right
fields.

Constraints:
- The input is a perfect binary tree (or empty)
- Left fields must not change
- O(n) time, O(h) extra space (an O(n)-space level-order solution also
  passes the tests)

How it works (save the child before overwriting, then recurse):
1. Define a helper that takes a node and the node that should end up as
   its right sibling (None for the root)
2. Save the node's original right child, then overwrite node.right with
   the given sibling
3. Recurse on the left child with the saved original right child as its
   sibling
4. Recurse on the saved right child with the sibling's left child as its
   sibling (left fields never change, so this is still valid), or None if
   there is no sibling

Example 1:
Input:        1
            /   \\
           2     3
          / \\   / \\
         4   5 6   7
Output: right fields become 1 -> None, 2 -> 3 -> None, 4 -> 5 -> 6 -> 7 -> None;
        left fields stay 1 -> 2, 2 -> 4, 3 -> 6

Example 2:
Input: a single node
Output: its right field stays None
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
    def construct_right_sibling_in_place(self, tree: Optional[BinaryTreeNode]) -> None:
        """
        Overwrites each node's right field with its right sibling, in place.

        Args:
            tree: Root of a perfect binary tree (None for an empty tree)

        Returns:
            None; the tree is modified in place

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement right sibling wiring through the right field
        pass


def build_perfect(height: int) -> Optional[BinaryTreeNode]:
    """Builds a perfect tree of the given height with keys 1.. in BFS order."""
    if height < 0:
        return None
    nodes = [BinaryTreeNode(i + 1) for i in range(2 ** (height + 1) - 1)]
    for i, node in enumerate(nodes):
        if 2 * i + 2 < len(nodes):
            node.left, node.right = nodes[2 * i + 1], nodes[2 * i + 2]
    return nodes[0]


def levels_of(tree: Optional[BinaryTreeNode]) -> List[List[BinaryTreeNode]]:
    """Returns the nodes grouped by level using the original child fields."""
    levels, current = [], [tree] if tree else []
    while current:
        levels.append(current)
        current = [c for n in current for c in (n.left, n.right) if c]
    return levels


def rewired_correctly(
    levels: List[List[BinaryTreeNode]], lefts: List[List[Optional[BinaryTreeNode]]]
) -> bool:
    """Checks right fields hold siblings and left fields are unchanged."""
    for level, level_lefts in zip(levels, lefts):
        for i, node in enumerate(level):
            expected = level[i + 1] if i + 1 < len(level) else None
            if node.right is not expected or node.left is not level_lefts[i]:
                return False
    return True


def check_height(solution: "Solution", height: int) -> bool:
    """Builds a perfect tree, rewires it, and validates the result."""
    tree = build_perfect(height)
    levels = levels_of(tree)
    lefts = [[n.left for n in level] for level in levels]
    solution.construct_right_sibling_in_place(tree)
    return rewired_correctly(levels, lefts)


def test_construct_right_sibling_in_place():
    """Test cases for right sibling wiring through the right field"""
    solution = Solution()

    # Test case 1: Empty tree does not crash
    solution.construct_right_sibling_in_place(None)
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert check_height(solution, 0)
    print("✓ Test 2 passed: Single node")

    # Test case 3: Height 1 (root loses its right child pointer)
    tree3 = build_perfect(1)
    left3, right3 = tree3.left, tree3.right
    solution.construct_right_sibling_in_place(tree3)
    assert tree3.right is None and tree3.left is left3
    assert left3.right is right3 and right3.right is None
    print("✓ Test 3 passed: Height 1")

    # Test case 4: Height 2 (crosses a subtree boundary)
    assert check_height(solution, 2)
    print("✓ Test 4 passed: Height 2")

    # Test case 5: Height 4
    assert check_height(solution, 4)
    print("✓ Test 5 passed: Height 4")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_construct_right_sibling_in_place()
