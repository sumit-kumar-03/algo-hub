"""
EPI 8.6 Extra Variant - Vertical Order Traversal
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Level-by-level BFS, here combined with a horizontal coordinate
for every node and grouping by that coordinate.

Problem:
Give every node of a binary tree a row and a column: the root is at row 0,
column 0, and a node at (r, c) has its left child at (r + 1, c - 1) and
its right child at (r + 1, c + 1). Return the keys grouped by column, from
the leftmost column to the rightmost. Within a column, list keys from the
top row down; when two or more nodes share both the row and the column,
list their keys in increasing order.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n log n) time, O(n) space

How it works:
1. BFS level by level, carrying each node's column; the BFS already visits
   rows in increasing order
2. For each level, gather (column, key) pairs and sort them so that keys
   sharing a column within the level come out in increasing order
3. Append each level's keys to a dictionary of column -> keys and track
   the smallest and largest columns
4. Output the columns from the smallest to the largest

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
Output: [[28], [271], [6, 0], [314, 2, 561, 17, 401], [6, 1, 3, 641],
         [271, 257], [28]]
Explanation: 561 and 2 both sit at row 2, column 0, so they are listed
in increasing order: 2 before 561

Example 2:
Input:      3
           / \\
          9   20
             /  \\
            15   7
Output: [[9], [3, 15], [20], [7]]
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
    def vertical_order(self, tree: Optional[BinaryTreeNode]) -> List[List[int]]:
        """
        Returns the keys grouped by column, left to right.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            One list per column; each sorted by row, then by key on ties

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement vertical order traversal
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


def test_vertical_order():
    """Test cases for vertical order traversal"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree and single node
    assert solution.vertical_order(None) == []
    assert solution.vertical_order(N(4)) == [[4]]
    print("✓ Test 1 passed: Empty tree and single node")

    # Test case 2: Classic small tree
    tree2 = N(3, N(9), N(20, N(15), N(7)))
    assert solution.vertical_order(tree2) == [[9], [3, 15], [20], [7]]
    print("✓ Test 2 passed: Small tree")

    # Test case 3: Figure 9.1 tree (book example), ties in one cell
    assert solution.vertical_order(build_figure_9_1()) == [
        [28],
        [271],
        [6, 0],
        [314, 2, 561, 17, 401],
        [6, 1, 3, 641],
        [271, 257],
        [28],
    ]
    print("✓ Test 3 passed: Figure 9.1 tree")

    # Test case 4: Same cell sorted by key, not by left-to-right position
    tree4 = N(1, N(2, N(4), N(6)), N(3, N(5), N(7)))
    assert solution.vertical_order(tree4) == [[4], [2], [1, 5, 6], [3], [7]]
    print("✓ Test 4 passed: Ties in a cell sorted by key")

    # Test case 5: Higher row comes first even with a larger key
    tree5 = N(1, N(2, None, N(0)), N(3))
    assert solution.vertical_order(tree5) == [[2], [1, 0], [3]]
    print("✓ Test 5 passed: Rows ordered before keys")

    # Test case 6: Zigzag chain stays in two columns
    tree6 = N(1, N(2, None, N(3, N(4, None, N(5)))))
    assert solution.vertical_order(tree6) == [[2, 4], [1, 3, 5]]
    print("✓ Test 6 passed: Zigzag chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_vertical_order()
