"""
EPI 9.1 Extra Variant - Maximum Path Sum
(Practice problem, not in the book. Difficulty: Hard)
Builds on: a post-order traversal where each call returns one summary to its
parent (like height) while a second quantity is checked at every node.

Problem:
A path in a binary tree is a sequence of nodes where each consecutive pair is
joined by an edge, and no node appears more than once. A path contains at
least one node and need not pass through the root. Its sum is the total of
its node values. Given a nonempty binary tree whose values may be negative,
return the largest path sum.

Constraints:
- 1 <= number of nodes <= 10^4
- -1000 <= node value <= 1000
- O(n) time, O(h) space

How it works (post-order, "best downward chain" plus a running answer):
1. For each node, compute gain(node): the largest sum of a path that starts
   at the node and goes straight down (it may stop at the node itself)
2. gain(node) = node.data + max(0, gain(left), gain(right)); a negative child
   gain is dropped rather than added
3. The best path that bends at the node is
   node.data + max(0, gain(left)) + max(0, gain(right)); track the maximum
   of this over all nodes
4. Return the tracked maximum (it is negative when every value is negative)

Example 1:
Input:     -10
           /  \\
          9    20
              /  \\
             15   7
Output: 42
Explanation: The path 15 -> 20 -> 7 sums to 42.

Example 2:
Input:      -3
           /  \\
         -2    -5
Output: -2
Explanation: Every value is negative, so the best path is the single node -2.
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
    def max_path_sum(self, tree: BinaryTreeNode) -> int:
        """
        Returns the largest sum over all paths in the tree.

        Args:
            tree: Root of a nonempty binary tree

        Returns:
            The maximum path sum

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement maximum path sum
        pass


def test_max_path_sum():
    """Test cases for maximum path sum"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Single node (negative)
    assert solution.max_path_sum(N(-7)) == -7
    print("✓ Test 1 passed: Single negative node")

    # Test case 2: Best path avoids the negative root
    tree2 = N(-10, N(9), N(20, N(15), N(7)))
    assert solution.max_path_sum(tree2) == 42
    print("✓ Test 2 passed: Path 15 -> 20 -> 7")

    # Test case 3: All negative values
    tree3 = N(-3, N(-2), N(-5))
    assert solution.max_path_sum(tree3) == -2
    print("✓ Test 3 passed: All negative")

    # Test case 4: All positive, path bends at the root
    tree4 = N(1, N(2, N(4), N(5)), N(3, N(6), N(7)))
    assert solution.max_path_sum(tree4) == 5 + 2 + 1 + 3 + 7
    print("✓ Test 4 passed: Bend at the root")

    # Test case 5: Dropping a negative branch
    tree5 = N(5, N(4, N(11, N(7), N(-2))), N(8, N(13), N(4, None, N(1))))
    assert solution.max_path_sum(tree5) == 7 + 11 + 4 + 5 + 8 + 13
    print("✓ Test 5 passed: Negative leaf dropped")

    # Test case 6: Negative node worth crossing to join two big sides
    tree6 = N(-1, N(10), N(10))
    assert solution.max_path_sum(tree6) == 19
    print("✓ Test 6 passed: Crossing a negative node")

    # Test case 7: Negative node not worth crossing
    tree7 = N(2, N(-6, N(3), N(4)), N(1))
    assert solution.max_path_sum(tree7) == 4
    print("✓ Test 7 passed: Best path is a single leaf")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_max_path_sum()
