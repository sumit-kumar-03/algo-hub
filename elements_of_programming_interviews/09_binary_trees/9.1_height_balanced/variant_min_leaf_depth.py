"""
EPI 9.1 Extra Variant - Minimum Leaf Depth
(Practice problem, not in the book. Difficulty: Easy)
Builds on: computing a subtree property (height) bottom-up in one post-order
traversal.

Problem:
Given the root of a binary tree, return the number of nodes on the shortest
path from the root down to any leaf (a node with no children). Return 0 for
an empty tree. Careful: a node with exactly one child is not a leaf, so the
missing side must not be treated as a path of length 0.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(h) space

How it works (post-order, but the empty side is not a leaf):
1. An empty tree has depth 0; a leaf has depth 1
2. If only one child exists, the answer is 1 + the depth of that child
3. Otherwise it is 1 + min(depth(left), depth(right))
(A BFS that stops at the first leaf also works and can be faster on
lopsided trees.)

Example 1:
Input:      1
           / \\
          2   3
         /
        4
Output: 2
Explanation: The path 1 -> 3 reaches a leaf after 2 nodes.

Example 2:
Input:      1
             \\
              2
               \\
                3
Output: 3
Explanation: The root is not a leaf; the only leaf is 3.
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
    def min_leaf_depth(self, tree: Optional[BinaryTreeNode]) -> int:
        """
        Returns the number of nodes on the shortest root-to-leaf path.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            Node count of the shortest root-to-leaf path (0 if empty)

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement minimum leaf depth
        pass


def test_min_leaf_depth():
    """Test cases for minimum leaf depth"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree
    assert solution.min_leaf_depth(None) == 0
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Single node is a leaf
    assert solution.min_leaf_depth(N(1)) == 1
    print("✓ Test 2 passed: Single node")

    # Test case 3: Short branch on the right
    tree3 = N(1, N(2, N(4)), N(3))
    assert solution.min_leaf_depth(tree3) == 2
    print("✓ Test 3 passed: Shortest branch on the right")

    # Test case 4: Right chain (one-child nodes are not leaves)
    tree4 = N(1, None, N(2, None, N(3)))
    assert solution.min_leaf_depth(tree4) == 3
    print("✓ Test 4 passed: Right chain")

    # Test case 5: Root with one child, deeper subtree below
    tree5 = N(1, N(2, N(3), N(4, N(5))))
    assert solution.min_leaf_depth(tree5) == 3
    print("✓ Test 5 passed: Root with a single child")

    # Test case 6: Perfect tree of height 2
    tree6 = N(1, N(2, N(4), N(5)), N(3, N(6), N(7)))
    assert solution.min_leaf_depth(tree6) == 3
    print("✓ Test 6 passed: Perfect tree")

    # Test case 7: Mixed shape, shortest leaf deep on the left
    tree7 = N(1, N(2, N(3, N(4)), N(5, None, N(6))), N(7, N(8, None, N(9, N(10)))))
    assert solution.min_leaf_depth(tree7) == 4
    print("✓ Test 7 passed: Mixed shape")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_leaf_depth()
