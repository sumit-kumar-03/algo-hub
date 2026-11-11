"""
EPI 9.16 - Compute the Right Sibling Tree

Problem:
Each node of a perfect binary tree has an extra field, next, initially
None. Set every node's next field to the node immediately to its right on
the same level, leaving it None for the rightmost node of each level.

Constraints:
- The input is a perfect binary tree (or empty)
- Do not change the left and right child fields
- O(n) time, O(1) extra space

How it works (use the level above as a linked list):
1. Process the tree level by level, starting at the root
2. While walking a level through its next pointers, wire up the level
   below: a node's left child points to its right child, and its right
   child points to the left child of the node's own next (if any)
3. Move down to the leftmost node of the next level and repeat until the
   leaves are reached

Example 1:
Input:        1
            /   \\
           2     3
          / \\   / \\
         4   5 6   7
Output: next pointers 2 -> 3, 4 -> 5 -> 6 -> 7; 1, 3, and 7 point to None

Example 2:
Input: a single node
Output: its next stays None
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
        self.next: Optional[BinaryTreeNode] = None


class Solution:
    def construct_right_sibling(self, tree: Optional[BinaryTreeNode]) -> None:
        """
        Sets each node's next field to its right sibling, in place.

        Args:
            tree: Root of a perfect binary tree (None for an empty tree)

        Returns:
            None; the tree is modified in place

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement right sibling wiring
        pass


def build_perfect(height: int, start: int = 1) -> Optional[BinaryTreeNode]:
    """Builds a perfect tree of the given height with keys in BFS order."""
    if height < 0:
        return None
    nodes = [BinaryTreeNode(start + i) for i in range(2 ** (height + 1) - 1)]
    for i, node in enumerate(nodes):
        if 2 * i + 2 < len(nodes):
            node.left, node.right = nodes[2 * i + 1], nodes[2 * i + 2]
    return nodes[0]


def levels_of(tree: Optional[BinaryTreeNode]) -> List[List[BinaryTreeNode]]:
    """Returns the nodes grouped by level using the child fields."""
    levels, current = [], [tree] if tree else []
    while current:
        levels.append(current)
        current = [c for n in current for c in (n.left, n.right) if c]
    return levels


def next_pointers_correct(levels: List[List[BinaryTreeNode]]) -> bool:
    """Checks each node's next against the expected right sibling."""
    for level in levels:
        for i, node in enumerate(level):
            expected = level[i + 1] if i + 1 < len(level) else None
            if node.next is not expected:
                return False
    return True


def test_construct_right_sibling():
    """Test cases for right sibling tree"""
    solution = Solution()

    # Test case 1: Empty tree does not crash
    solution.construct_right_sibling(None)
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node keeps next = None
    single = BinaryTreeNode(1)
    solution.construct_right_sibling(single)
    assert single.next is None
    print("✓ Test 2 passed: Single node")

    # Test case 3: Perfect tree of height 1
    tree3 = build_perfect(1)
    solution.construct_right_sibling(tree3)
    assert tree3.left.next is tree3.right
    assert tree3.right.next is None and tree3.next is None
    print("✓ Test 3 passed: Height 1")

    # Test case 4: Perfect tree of height 2 (crosses a subtree boundary)
    tree4 = build_perfect(2)
    solution.construct_right_sibling(tree4)
    assert tree4.left.right.next is tree4.right.left
    assert next_pointers_correct(levels_of(tree4))
    print("✓ Test 4 passed: Height 2")

    # Test case 5: Perfect tree of height 4, children untouched
    tree5 = build_perfect(4)
    before = [[n.data for n in level] for level in levels_of(tree5)]
    solution.construct_right_sibling(tree5)
    levels5 = levels_of(tree5)
    assert [[n.data for n in level] for level in levels5] == before
    assert next_pointers_correct(levels5)
    print("✓ Test 5 passed: Height 4 with children unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_construct_right_sibling()
