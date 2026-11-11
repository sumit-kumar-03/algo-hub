"""
EPI 9.12 Variant - Build the Max-Tree of an Array

Problem:
Given an array A of distinct integers, its max-tree is defined recursively:
the root holds the maximum of A; if that maximum sits at index m, the left
subtree is the max-tree of A[:m] and the right subtree is the max-tree of
A[m + 1:]. An empty array gives an empty tree. Build the max-tree in O(n)
time.

Constraints:
- 0 <= len(A) <= 10^5
- All values are distinct
- O(n) time, O(n) space (the naive split-at-max recursion is O(n^2) for
  sorted input)
- The tests include a 20,000-element sorted array, which produces a tree
  that deep, so avoid recursion

How it works (monotonic stack):
1. Scan A left to right, keeping a stack of nodes with decreasing values
   (this stack is the right spine of the max-tree built so far)
2. For each new value, create a node and pop every stack node smaller
   than it; the last node popped becomes the new node's left child
3. If the stack is still non-empty, the new node becomes the right child of
   the node now on top
4. Push the new node; at the end, the bottom of the stack is the root

Example 1:
Input: A = [3, 1, 5, 2, 4]
Output:      5
            / \\
           3   4
            \\  /
            1 2

Example 2:
Input: A = [1, 2, 3]
Output: a left-skewed chain 3 -> 2 -> 1
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
    def build_max_tree(self, A: List[int]) -> Optional[BinaryTreeNode]:
        """
        Builds the max-tree of an array of distinct integers.

        Args:
            A: Array of distinct integers

        Returns:
            Root of the max-tree (None for an empty array)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement max-tree construction
        pass


def same_tree(a: Optional[BinaryTreeNode], b: Optional[BinaryTreeNode]) -> bool:
    """Returns True if both trees have identical shape and keys."""
    if a is None or b is None:
        return a is None and b is None
    return a.data == b.data and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def inorder_keys(tree: Optional[BinaryTreeNode]) -> List[int]:
    """Returns the inorder keys iteratively (safe for deep trees)."""
    result, stack, node = [], [], tree
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.data)
        node = node.right
    return result


def test_build_max_tree():
    """Test cases for max-tree construction"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Empty array
    assert solution.build_max_tree([]) is None
    print("✓ Test 1 passed: Empty array")

    # Test case 2: Single element
    assert same_tree(solution.build_max_tree([42]), N(42))
    print("✓ Test 2 passed: Single element")

    # Test case 3: Mixed array
    expected3 = N(5, N(3, None, N(1)), N(4, N(2)))
    assert same_tree(solution.build_max_tree([3, 1, 5, 2, 4]), expected3)
    print("✓ Test 3 passed: Mixed array")

    # Test case 4: Increasing array gives a left chain
    assert same_tree(solution.build_max_tree([1, 2, 3]), N(3, N(2, N(1))))
    print("✓ Test 4 passed: Increasing array")

    # Test case 5: Decreasing array gives a right chain
    assert same_tree(solution.build_max_tree([3, 2, 1]), N(3, None, N(2, None, N(1))))
    print("✓ Test 5 passed: Decreasing array")

    # Test case 6: Larger example
    expected6 = N(9, N(7, N(2), N(4, N(3))), N(8, N(6, None, N(5)), N(1)))
    assert same_tree(solution.build_max_tree([2, 7, 3, 4, 9, 6, 5, 8, 1]), expected6)
    print("✓ Test 6 passed: Larger example")

    # Test case 7: Long sorted input keeps array order in the inorder walk
    big = list(range(20000))
    root = solution.build_max_tree(big)
    assert root is not None and root.data == 19999
    assert inorder_keys(root) == big
    print("✓ Test 7 passed: Long sorted input")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_build_max_tree()
