"""
EPI 14.1 Extra Variant - Largest Subtree That Is a BST
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the BST property check, turned inside out. Instead of passing
allowed ranges DOWN from the root, each subtree reports its own min, max,
and validity UP to its parent, so every subtree is checked in one pass.

Problem:
Given the root of a binary tree, return the number of nodes in the largest
subtree that is a BST. A subtree here means a node together with ALL of
its descendants. For this problem a BST requires distinct ordering: every
key in a node's left subtree is strictly less than the node's key and every
key in its right subtree is strictly greater. An empty tree has answer 0.

Constraints:
- 0 <= number of nodes <= 10^4
- Target: O(n) time, O(h) space; validating every subtree separately is
  O(n^2) in the worst case

How it works (postorder, report up):
1. For each node, recursively get from each child: (is_bst, size, min key,
   max key); an empty child is a BST of size 0 with min = +inf, max = -inf
2. The node's subtree is a BST iff both children are BSTs and
   left.max < node.data < right.min
3. If so, report (True, left.size + right.size + 1, min(left.min,
   node.data), max(right.max, node.data)) and update the global best
4. Otherwise report "not a BST" (its size no longer matters, and the
   bounds should make every ancestor fail too)

Example 1:
Input:      10
           /  \\
          5    15
         / \\     \\
        1   8     7
Output: 3
Explanation: The subtree rooted at 5 (1, 5, 8) is a BST. The subtree at 15
is not, because 7 < 15 sits on its right.

Example 2:
Input:   2
        / \\
       1   3
Output: 3
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
    def largest_bst_subtree(self, tree: Optional[BinaryTreeNode]) -> int:
        """
        Finds the size of the largest subtree that is a BST.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            Number of nodes in the largest BST subtree (0 for an empty tree)

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement postorder computation of BST info
        pass


def test_largest_bst_subtree():
    """Test cases for the largest BST subtree"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Left subtree is the largest BST
    tree = N(10, N(5, N(1), N(8)), N(15, None, N(7)))
    assert solution.largest_bst_subtree(tree) == 3
    print("✓ Test 1 passed: -> 3")

    # Test case 2: Whole tree is a BST
    assert solution.largest_bst_subtree(N(2, N(1), N(3))) == 3
    print("✓ Test 2 passed: Whole tree -> 3")

    # Test case 3: Empty and single node
    assert solution.largest_bst_subtree(None) == 0
    assert solution.largest_bst_subtree(N(4)) == 1
    print("✓ Test 3 passed: Empty -> 0, single -> 1")

    # Test case 4: Children are BSTs but the root breaks it via a deep node
    #        10
    #       /  \\
    #      5    20
    #     / \\
    #    2   12     <- 12 > 10, so the root's tree fails
    tree = N(10, N(5, N(2), N(12)), N(20))
    assert solution.largest_bst_subtree(tree) == 3
    print("✓ Test 4 passed: Deep violation -> 3")

    # Test case 5: Duplicate keys are not allowed in this definition
    assert solution.largest_bst_subtree(N(5, N(5), N(6))) == 1
    print("✓ Test 5 passed: Duplicates break the BST -> 1")

    # Test case 6: Largest BST is deep on the right
    big = N(50, N(30, N(20), N(40)), N(70, N(60), N(80)))
    tree = N(1, N(100), N(90, None, big))
    assert solution.largest_bst_subtree(tree) == 7
    print("✓ Test 6 passed: Deep right BST of 7 nodes")

    # Test case 7: Brute force on a mixed tree
    def keys(t):
        return keys(t.left) + [t.data] + keys(t.right) if t else []

    def is_bst(t):
        k = keys(t)
        return all(a < b for a, b in zip(k, k[1:]))

    def brute(t):
        if t is None:
            return 0
        here = len(keys(t)) if is_bst(t) else 0
        return max(here, brute(t.left), brute(t.right))

    tree = N(8,
             N(4, N(2, N(1), N(3)), N(6, N(5), N(9))),
             N(12, N(10, N(9), N(11)), N(14, N(13), N(15, None, N(16)))))
    assert solution.largest_bst_subtree(tree) == brute(tree) == 8
    print("✓ Test 7 passed: Mixed tree matches brute force -> 8")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_largest_bst_subtree()
