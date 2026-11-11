"""
EPI 9.1 Extra Variant - Diameter of a Binary Tree
(Practice problem, not in the book. Difficulty: Medium)
Builds on: returning a node's height from a post-order traversal while
checking a condition that combines both subtree heights.

Problem:
The diameter of a binary tree is the number of edges on the longest path
between any two nodes. The path may or may not pass through the root and
never visits a node twice. Given the root, return the diameter. An empty
tree and a single node both have diameter 0.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time: compute heights once, bottom-up (do not recompute heights at
  every node)
- O(h) space

How it works (post-order, height plus a running best):
1. Define height(None) = -1 and height(node) = 1 + max of the child heights
2. The longest path that turns at a node has
   (height(left) + 1) + (height(right) + 1) edges
3. While computing heights, keep the maximum of that quantity over all nodes
4. Return the maximum (0 for an empty tree)

Example 1:
Input:      1
           / \\
          2   3
         / \\
        4   5
Output: 3
Explanation: The path 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3) has 3 edges.

Example 2:
Input:      1
           /
          2
         / \\
        3   4
       /     \\
      5       6
Output: 4
Explanation: The path 5 -> 3 -> 2 -> 4 -> 6 does not pass through the root.
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
    def diameter(self, tree: Optional[BinaryTreeNode]) -> int:
        """
        Returns the number of edges on the longest path in the tree.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            The diameter in edges (0 for an empty tree or a single node)

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement diameter via bottom-up heights
        pass


def test_diameter():
    """Test cases for tree diameter"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree and single node
    assert solution.diameter(None) == 0
    assert solution.diameter(N(1)) == 0
    print("✓ Test 1 passed: Empty tree and single node")

    # Test case 2: Path through the root
    tree2 = N(1, N(2, N(4), N(5)), N(3))
    assert solution.diameter(tree2) == 3
    print("✓ Test 2 passed: Path through the root")

    # Test case 3: Longest path avoids the root
    tree3 = N(1, N(2, N(3, N(5)), N(4, None, N(6))))
    assert solution.diameter(tree3) == 4
    print("✓ Test 3 passed: Path below the root")

    # Test case 4: Single chain
    tree4 = N(1, N(2, None, N(3, N(4, None, N(5)))))
    assert solution.diameter(tree4) == 4
    print("✓ Test 4 passed: Zigzag chain")

    # Test case 5: Perfect tree of height 2
    tree5 = N(1, N(2, N(4), N(5)), N(3, N(6), N(7)))
    assert solution.diameter(tree5) == 4
    print("✓ Test 5 passed: Perfect tree")

    # Test case 6: Two long arms deep in one subtree beat the root path
    left = N(2, N(3, N(4, N(5))), N(6, None, N(7, None, N(8))))
    tree6 = N(1, left, N(9))
    assert solution.diameter(tree6) == 6
    print("✓ Test 6 passed: Deep subtree wins")

    # Test case 7: Long left-only chain (deep recursion is fine)
    chain = None
    for i in range(500):
        chain = N(i, chain)
    assert solution.diameter(chain) == 499
    print("✓ Test 7 passed: 500-node chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_diameter()
