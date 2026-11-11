"""
EPI 8.6 Extra Variant - Maximum Width of a Level
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Level-by-level BFS, now carrying a position with every node.

Problem:
Number the slots of each level of a binary tree as if the tree were
complete: the root is slot 0, and a node in slot p has its left child in
slot 2p and its right child in slot 2p + 1 on the next level. The width
of a level is (rightmost occupied slot) - (leftmost occupied slot) + 1, so
empty slots between the two ends count. Return the largest width over all
levels, or 0 for an empty tree.

Constraints:
- 0 <= number of nodes <= 10^4 (the tree may be very deep, so slot
  numbers can be huge; renumber each level relative to its first slot)
- O(n) time, O(m) space where m is the maximum number of nodes at any depth

How it works (BFS with positions):
1. Queue (node, slot) pairs, starting with (root, 0)
2. For each level, the width is last slot - first slot + 1; update the
   answer
3. Enqueue the children with slots 2(p - first) and 2(p - first) + 1;
   subtracting the level's first slot keeps the numbers small

Example 1 (Figure 9.1 in the book):
Input:              314
                 /       \\
               6           6
             /   \\       /   \\
          271    561    2    271
          / \\      \\     \\      \\
        28   0      3     1     28
                   /     / \\
                 17    401  257
                         \\
                         641
Output: 8
Explanation: Depth 3 uses slots 0, 1, 3, 5 and 7

Example 2:
Input:      1
           / \\
          3   2
         /     \\
        5       9
Output: 4
Explanation: Depth 2 uses slots 0 and 3; slots 1 and 2 are empty but count
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
    def max_level_width(self, tree: Optional[BinaryTreeNode]) -> int:
        """
        Computes the largest level width, counting empty slots in between.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            The maximum width over all levels

        Time Complexity: O(n)
        Space Complexity: O(m) where m is the widest level
        """
        # TODO: Implement maximum level width
        pass


def build_figure_9_1() -> BinaryTreeNode:
    """Builds the sample tree from Figure 9.1 of the book."""
    N = BinaryTreeNode
    return N(
        314,
        N(6, N(271, N(28), N(0)), N(561, None, N(3, N(17)))),
        N(
            6,
            N(2, None, N(1, N(401, None, N(641)), N(257))),
            N(271, None, N(28)),
        ),
    )


def test_max_level_width():
    """Test cases for the maximum level width"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree and single node
    assert solution.max_level_width(None) == 0
    assert solution.max_level_width(N(1)) == 1
    print("✓ Test 1 passed: Empty tree and single node")

    # Test case 2: Gaps in the middle count
    tree2 = N(1, N(3, N(5)), N(2, None, N(9)))
    assert solution.max_level_width(tree2) == 4
    print("✓ Test 2 passed: Middle gaps counted")

    # Test case 3: Figure 9.1 tree (book example)
    assert solution.max_level_width(build_figure_9_1()) == 8
    print("✓ Test 3 passed: Figure 9.1 tree")

    # Test case 4: Width grows on a deeper, sparser level
    tree4 = N(1, N(3, N(5, N(6))), N(2, None, N(9, None, N(7))))
    assert solution.max_level_width(tree4) == 8
    print("✓ Test 4 passed: Deep sparse level is widest")

    # Test case 5: A chain has width 1 at every level
    tree5 = N(1, N(2, None, N(3, N(4))))
    assert solution.max_level_width(tree5) == 1
    print("✓ Test 5 passed: Chain")

    # Test case 6: Very deep tree with two far-apart leaves
    left = right = None
    for _ in range(3000):
        left = N(0, left)
        right = N(0, None, right)
    tree6 = N(0, left, right)
    assert solution.max_level_width(tree6) == 2**3000
    print("✓ Test 6 passed: 3000 levels below the root, width 2^3000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_level_width()
