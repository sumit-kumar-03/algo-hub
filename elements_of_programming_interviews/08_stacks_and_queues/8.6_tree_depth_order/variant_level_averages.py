"""
EPI 8.6 Variant - Average of Keys at Each Level

Problem:
Given the root of a binary tree with integer keys, return a list holding
the average of the keys at each depth, from the root level down.

Constraints:
- 0 <= number of nodes <= 10^4
- Averages are returned as floats
- O(n) time, O(m) space where m is the maximum number of nodes at any depth

How it works (BFS with running sums):
1. Process the tree level by level
2. For each level, sum the keys and count the nodes
3. Append sum / count to the result

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
Output: [314.0, 6.0, 276.25, 12.0, 225.0, 641.0]
Explanation: Depth 2 averages (271 + 561 + 2 + 271) / 4 = 276.25.

Example 2:
Input:      3
           / \\
          9   20
             /  \\
            15   7
Output: [3.0, 14.5, 11.0]
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
    def level_averages(self, tree: Optional[BinaryTreeNode]) -> List[float]:
        """
        Computes the average key at every depth of the tree.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            One average per level, from the root level down

        Time Complexity: O(n)
        Space Complexity: O(m) where m is the widest level
        """
        # TODO: Implement per-level averages
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


def close_lists(actual: List[float], expected: List[float]) -> bool:
    """Returns True if both lists match element-wise within 1e-9."""
    return actual is not None and len(actual) == len(expected) and all(
        abs(a - e) < 1e-9 for a, e in zip(actual, expected)
    )


def test_level_averages():
    """Test cases for per-level averages"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.level_averages(None) == []
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node
    assert close_lists(solution.level_averages(N(4)), [4.0])
    print("✓ Test 2 passed: Single node")

    # Test case 3: Fractional averages
    tree3 = N(3, N(9), N(20, N(15), N(7)))
    assert close_lists(solution.level_averages(tree3), [3.0, 14.5, 11.0])
    print("✓ Test 3 passed: Fractional averages")

    # Test case 4: Figure 9.1 tree (book example)
    assert close_lists(
        solution.level_averages(build_figure_9_1()),
        [314.0, 6.0, 276.25, 12.0, 225.0, 641.0],
    )
    print("✓ Test 4 passed: Figure 9.1 tree")

    # Test case 5: Negative keys
    tree5 = N(-1, N(-2, N(-5)), N(4, None, N(2)))
    assert close_lists(solution.level_averages(tree5), [-1.0, 1.0, -1.5])
    print("✓ Test 5 passed: Negative keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_level_averages()
