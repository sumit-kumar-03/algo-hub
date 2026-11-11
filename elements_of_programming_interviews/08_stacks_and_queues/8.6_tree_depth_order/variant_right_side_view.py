"""
EPI 8.6 Extra Variant - Right Side View
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Level-by-level BFS that knows where each level ends.

Problem:
Imagine standing to the right of a binary tree and looking at it. At each
depth you see only the rightmost node of that level. Given the root,
return the keys you see, from the root level down.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(m) space where m is the maximum number of nodes at any depth

How it works (level-by-level BFS):
1. Start with a queue holding just the root (return [] for an empty tree)
2. For each level, the last node in the current queue is the rightmost
   one: record its key
3. Build the next queue from the children of the current nodes, left
   child before right child, and repeat

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
Output: [314, 6, 271, 28, 257, 641]

Example 2:
Input:      1
           / \\
          2   3
           \\
            5
Output: [1, 3, 5]
Explanation: 5 is visible from the right because nothing at depth 2 lies
to its right
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
    def right_side_view(self, tree: Optional[BinaryTreeNode]) -> List[int]:
        """
        Returns the rightmost key at every depth, from the root down.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            One key per level: the rightmost key on that level

        Time Complexity: O(n)
        Space Complexity: O(m) where m is the widest level
        """
        # TODO: Implement the right side view
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


def test_right_side_view():
    """Test cases for the right side view"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.right_side_view(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.right_side_view(N(8)) == [8]
    print("✓ Test 2 passed: Single node")

    # Test case 3: Node on the left subtree is visible
    assert solution.right_side_view(N(1, N(2, None, N(5)), N(3))) == [1, 3, 5]
    print("✓ Test 3 passed: Deeper left node visible")

    # Test case 4: Figure 9.1 tree (book example)
    assert solution.right_side_view(build_figure_9_1()) == [314, 6, 271, 28, 257, 641]
    print("✓ Test 4 passed: Figure 9.1 tree")

    # Test case 5: Left-skewed chain
    assert solution.right_side_view(N(1, N(2, N(3, N(4))))) == [1, 2, 3, 4]
    print("✓ Test 5 passed: Left-skewed chain")

    # Test case 6: Negative keys and duplicates
    tree6 = N(0, N(-1, N(-3), N(-3)), N(-1, N(-2)))
    assert solution.right_side_view(tree6) == [0, -1, -2]
    print("✓ Test 6 passed: Negative and repeated keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_right_side_view()
