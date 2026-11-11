"""
EPI 9.16 Variant - Compute the Right Sibling Tree for a General Binary Tree

Problem:
Same as the right sibling problem, but the tree is an arbitrary binary
tree rather than a perfect one. Set every node's next field to the next
node to its right on the same level (which may be in a distant subtree),
or None if it is the rightmost node of its level.

Constraints:
- 0 <= number of nodes <= 10^4
- Do not change the left and right child fields
- O(n) time; O(1) extra space is achievable

How it works (walk each level as a linked list):
1. Keep a pointer to the leftmost node of the current level
2. Walk the current level through its next pointers; for each child found,
   append it to the next level's list using a dummy head and a tail pointer
3. When the level is done, the dummy's next is the leftmost node of the
   next level; repeat until a level has no children

Example 1:
Input:        1
            /   \\
           2     3
          /       \\
         4         7
Output: next pointers 2 -> 3 and 4 -> 7

Example 2:
Input:        1
            /   \\
           2     3
            \\
             5
Output: 2 -> 3; 5 has no node to its right, so its next is None
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
    def construct_right_sibling_general(self, tree: Optional[BinaryTreeNode]) -> None:
        """
        Sets each node's next field to the node on its right, in place.

        Args:
            tree: Root of a binary tree (None for an empty tree)

        Returns:
            None; the tree is modified in place

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement right sibling wiring for general trees
        pass


def levels_of(tree: Optional[BinaryTreeNode]) -> List[List[BinaryTreeNode]]:
    """Returns the nodes grouped by level using the child fields."""
    levels, current = [], [tree] if tree else []
    while current:
        levels.append(current)
        current = [c for n in current for c in (n.left, n.right) if c]
    return levels


def next_pointers_correct(levels: List[List[BinaryTreeNode]]) -> bool:
    """Checks each node's next against the expected right neighbor."""
    for level in levels:
        for i, node in enumerate(level):
            expected = level[i + 1] if i + 1 < len(level) else None
            if node.next is not expected:
                return False
    return True


def test_construct_right_sibling_general():
    """Test cases for right sibling wiring in general trees"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree and single node
    solution.construct_right_sibling_general(None)
    single = N(1)
    solution.construct_right_sibling_general(single)
    assert single.next is None
    print("✓ Test 1 passed: Empty tree and single node")

    # Test case 2: Gap in the middle of a level
    n4, n7 = N(4), N(7)
    tree2 = N(1, N(2, n4), N(3, None, n7))
    solution.construct_right_sibling_general(tree2)
    assert tree2.left.next is tree2.right
    assert n4.next is n7 and n7.next is None
    print("✓ Test 2 passed: Gap in the middle of a level")

    # Test case 3: Rightmost node of a level is a left subtree node
    n5 = N(5)
    tree3 = N(1, N(2, None, n5), N(3))
    solution.construct_right_sibling_general(tree3)
    assert tree3.left.next is tree3.right
    assert n5.next is None
    print("✓ Test 3 passed: Short right side")

    # Test case 4: Figure 9.1-shaped tree
    tree4 = N(
        314,
        N(6, N(271, N(28), N(0)), N(561, None, N(3, N(17)))),
        N(6, N(2, None, N(1, N(401, None, N(641)), N(257))), N(271, None, N(28))),
    )
    solution.construct_right_sibling_general(tree4)
    assert next_pointers_correct(levels_of(tree4))
    print("✓ Test 4 passed: Figure 9.1 tree")

    # Test case 5: Skewed zigzag chain (one node per level)
    tree5 = N(1, N(2, None, N(3, N(4, None, N(5)))))
    solution.construct_right_sibling_general(tree5)
    assert next_pointers_correct(levels_of(tree5))
    print("✓ Test 5 passed: Zigzag chain")

    # Test case 6: Children are left untouched
    tree6 = N(1, N(2, N(4), N(5)), N(3, None, N(6, N(8))))
    before = [[n.data for n in level] for level in levels_of(tree6)]
    solution.construct_right_sibling_general(tree6)
    levels6 = levels_of(tree6)
    assert [[n.data for n in level] for level in levels6] == before
    assert next_pointers_correct(levels6)
    assert tree6.left.right.next is tree6.right.right
    print("✓ Test 6 passed: Long-distance neighbors, children unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_construct_right_sibling_general()
