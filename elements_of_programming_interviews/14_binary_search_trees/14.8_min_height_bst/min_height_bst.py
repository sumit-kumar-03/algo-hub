"""
EPI 14.8 - Build a Minimum Height BST from a Sorted Array

Problem:
Given an array of distinct integers sorted in increasing order, build a
BST containing exactly those keys whose height is as small as possible.
Return its root.

Constraints:
- 0 <= len(A) <= 10^5
- A is sorted in increasing order with distinct entries
- Target: O(n) time
- A tree with n nodes has minimum height ceil(log2(n + 1)) levels

How it works (pick the middle as the root):
1. If the subarray is empty, return None
2. Make the middle element the root so both sides are as close in size as
   possible
3. Recursively build the left subtree from the elements before the middle
   and the right subtree from the elements after it
Tip: pass index bounds instead of slicing to stay O(n).

Example 1:
Input: A = [2, 3, 5, 7, 11, 13, 17, 19, 23]
Output: A BST rooted at 11 with 4 levels, e.g.
                11
             /      \\
            5        19
           / \\      /   \\
          3   7    17     23
         /         /
        2         13
Explanation: Left subtree holds [2, 3, 5, 7], right holds [13, 17, 19, 23].
(Either middle of an even-length subarray is acceptable.)

Example 2:
Input: A = [1, 2, 3]
Output:   2
         / \\
        1   3
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
    def build_min_height_bst(self, A: List[int]) -> Optional[BinaryTreeNode]:
        """
        Builds a minimum height BST from a sorted array.

        Args:
            A: Sorted list of distinct integers

        Returns:
            Root of a BST of minimum possible height (None for an empty array)

        Time Complexity: O(n)
        Space Complexity: O(log n) recursion depth, excluding the tree itself
        """
        # TODO: Implement recursive middle-element construction
        pass


def inorder(node: Optional[BinaryTreeNode]) -> List[int]:
    """Returns the keys of the tree in inorder order."""
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def height(node: Optional[BinaryTreeNode]) -> int:
    """Number of levels in the tree (0 for an empty tree)."""
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_valid_min_bst(root: Optional[BinaryTreeNode], A: List[int]) -> bool:
    """True if root is a BST holding exactly A with minimum height."""
    n = len(A)
    return inorder(root) == A and height(root) == n.bit_length()


def test_build_min_height_bst():
    """Test cases for minimum height BST construction"""
    solution = Solution()

    # Test case 1: Empty array
    assert solution.build_min_height_bst([]) is None
    print("✓ Test 1 passed: Empty array -> None")

    # Test case 2: Single element
    root2 = solution.build_min_height_bst([42])
    assert root2 is not None and is_valid_min_bst(root2, [42])
    print("✓ Test 2 passed: Single element")

    # Test case 3: Three elements must be perfectly balanced
    root3 = solution.build_min_height_bst([1, 2, 3])
    assert root3 is not None and root3.data == 2 and is_valid_min_bst(root3, [1, 2, 3])
    print("✓ Test 3 passed: [1, 2, 3] -> root 2")

    # Test case 4: Book example (9 primes)
    A4 = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    root4 = solution.build_min_height_bst(A4)
    assert root4 is not None and root4.data == 11 and is_valid_min_bst(root4, A4)
    print("✓ Test 4 passed: Book example, root 11, height 4")

    # Test case 5: Perfect tree size (15 nodes -> 4 levels)
    A5 = list(range(-7, 8))
    assert is_valid_min_bst(solution.build_min_height_bst(A5), A5)
    print("✓ Test 5 passed: 15 nodes -> height 4")

    # Test case 6: Every size from 1 to 70
    for n in range(1, 71):
        A = [3 * i for i in range(n)]
        assert is_valid_min_bst(solution.build_min_height_bst(A), A)
    print("✓ Test 6 passed: Sizes 1..70 all minimum height")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_build_min_height_bst()
