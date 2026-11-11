"""
EPI 8.6 Variant - Bottom-Up Depth Order

Problem:
Given the root of a binary tree, return its keys grouped by level, starting
with the deepest level and ending with the root. Within each level, keys
are ordered from left to right.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(n) space

How it works (BFS, then reverse):
1. Collect the levels top-down with a level-by-level BFS
2. Reverse the list of levels (not the keys inside each level)

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
Output: [[641], [17, 401, 257], [28, 0, 3, 1, 28], [271, 561, 2, 271],
         [6, 6], [314]]

Example 2:
Input:      1
           / \\
          2   3
         /
        4
Output: [[4], [2, 3], [1]]
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
    def bottom_up_depth_order(
        self, tree: Optional[BinaryTreeNode]
    ) -> List[List[int]]:
        """
        Returns the keys grouped by depth, deepest level first.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            A list of levels from the deepest up to the root

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement bottom-up depth-order traversal
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


def test_bottom_up_depth_order():
    """Test cases for bottom-up depth order"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.bottom_up_depth_order(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert solution.bottom_up_depth_order(N(5)) == [[5]]
    print("✓ Test 2 passed: Single node")

    # Test case 3: Small tree
    assert solution.bottom_up_depth_order(N(1, N(2, N(4)), N(3))) == [
        [4],
        [2, 3],
        [1],
    ]
    print("✓ Test 3 passed: Small tree")

    # Test case 4: Figure 9.1 tree (book example)
    assert solution.bottom_up_depth_order(build_figure_9_1()) == [
        [641],
        [17, 401, 257],
        [28, 0, 3, 1, 28],
        [271, 561, 2, 271],
        [6, 6],
        [314],
    ]
    print("✓ Test 4 passed: Figure 9.1 tree")

    # Test case 5: Right-skewed chain
    assert solution.bottom_up_depth_order(N(1, None, N(2, None, N(3)))) == [
        [3],
        [2],
        [1],
    ]
    print("✓ Test 5 passed: Right-skewed chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_bottom_up_depth_order()
