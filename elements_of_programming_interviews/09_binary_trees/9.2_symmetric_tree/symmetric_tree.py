"""
EPI 9.2 - Test if a Binary Tree is Symmetric

Problem:
A binary tree is symmetric if its left subtree is the mirror image of its
right subtree, both in shape and in keys: reflecting the tree across a
vertical line through the root yields the same tree. Given the root of a
binary tree, return True if it is symmetric.

Constraints:
- 0 <= number of nodes <= 10^4
- An empty tree is symmetric
- O(n) time, O(h) space, without building a mirrored copy

How it works (paired recursion):
1. Compare the root's left and right subtrees as a pair
2. Two empty subtrees mirror each other; exactly one empty does not
3. Two non-empty subtrees mirror each other if their keys are equal, the
   first's left mirrors the second's right, and the first's right mirrors
   the second's left
4. Stop as soon as any pair fails

Example 1:
Input:       314
            /   \\
           6     6
            \\   /
             2 2
              \\ /
              3 3
Output: True
Explanation: Left 6 -> right 2 -> right 3 mirrors right 6 -> left 2 -> left 3.

Example 2:
Input:       314
            /   \\
           6     6
            \\   /
           561 2
Output: False
Explanation: The shape is symmetric, but the mirrored keys 561 and 2 differ.
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
    def is_symmetric(self, tree: Optional[BinaryTreeNode]) -> bool:
        """
        Checks whether a binary tree is symmetric.

        Args:
            tree: Root of the binary tree (None for an empty tree)

        Returns:
            True if the left subtree mirrors the right subtree

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement symmetry check
        pass


def test_is_symmetric():
    """Test cases for symmetric tree check"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty tree and single node
    assert solution.is_symmetric(None) is True
    assert solution.is_symmetric(N(1)) is True
    print("✓ Test 1 passed: Empty tree and single node")

    # Test case 2: Book Figure 9.3(a), symmetric
    tree2 = N(314, N(6, None, N(2, None, N(3))), N(6, N(2, N(3)), None))
    assert solution.is_symmetric(tree2) is True
    print("✓ Test 2 passed: Figure 9.3(a) is symmetric")

    # Test case 3: Book Figure 9.3(b), same shape but keys differ
    tree3 = N(314, N(6, None, N(561, None, N(3))), N(6, N(2, N(1)), None))
    assert solution.is_symmetric(tree3) is False
    print("✓ Test 3 passed: Figure 9.3(b) keys break symmetry")

    # Test case 4: Book Figure 9.3(c), shape differs
    tree4 = N(314, N(6, None, N(561, None, N(3))), N(6, N(561), None))
    assert solution.is_symmetric(tree4) is False
    print("✓ Test 4 passed: Figure 9.3(c) shape breaks symmetry")

    # Test case 5: Same subtrees (not mirrored) are not symmetric
    tree5 = N(1, N(2, N(3), N(4)), N(2, N(3), N(4)))
    assert solution.is_symmetric(tree5) is False
    print("✓ Test 5 passed: Identical but not mirrored subtrees")

    # Test case 6: Full mirrored tree
    tree6 = N(1, N(2, N(3), N(4)), N(2, N(4), N(3)))
    assert solution.is_symmetric(tree6) is True
    print("✓ Test 6 passed: Full mirrored tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_symmetric()
