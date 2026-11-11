"""
EPI 14.2 Extra Variant - Count Keys Greater Than k Using Subtree Sizes
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the O(h) walk from "first key greater than k". Every time that
walk goes left past a node with key > k, the node and its whole right
subtree are greater than k; subtree sizes let you count them without
visiting them.

Problem:
Each node of a BST stores, besides its key, the number of nodes in its
subtree (`size`, counting itself). Given the root and a value k, return how
many keys in the tree are strictly greater than k. Keys are distinct.

Constraints:
- 0 <= number of nodes <= 10^5
- Every node's size field is correct
- Target: O(h) time and O(1) extra space; an inorder walk is O(n)

How it works:
1. Start at the root with count = 0
2. If node.data > k: the node and its entire right subtree exceed k, so add
   1 + size(node.right), then go left (some keys there may also exceed k)
3. Otherwise node.data <= k: nothing in the node's left subtree can exceed
   k, so go right
4. Return the count when you fall off the tree (size(None) is 0)

Example 1:
Input: BST below (with sizes filled in), k = 23
                    19
                 /      \\
               7          43
              / \\        /   \\
             3   11     23     47
            / \\    \\     \\      \\
           2   5    17     37     53
                   /      /  \\
                 13      29   41
                           \\
                            31
Output: 7
Explanation: 29, 31, 37, 41, 43, 47, 53.

Example 2:
Input: same BST, k = 0
Output: 16
"""

from typing import List, Optional


class BinaryTreeNode:
    def __init__(
        self,
        data: int = 0,
        left: "Optional[BinaryTreeNode]" = None,
        right: "Optional[BinaryTreeNode]" = None,
        size: int = 1,
    ):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


class Solution:
    def count_greater_than_k(
        self, tree: Optional[BinaryTreeNode], k: int
    ) -> int:
        """
        Counts the keys greater than k using the size fields.

        Args:
            tree: Root of a size-augmented BST (None for an empty tree)
            k: The value to compare against

        Returns:
            Number of keys strictly greater than k

        Time Complexity: O(h) where h is the tree height
        Space Complexity: O(1)
        """
        # TODO: Implement size-guided counting walk
        pass


def fill_sizes(tree: Optional[BinaryTreeNode]) -> int:
    """Sets every node's size field; returns the size of tree."""
    if tree is None:
        return 0
    tree.size = 1 + fill_sizes(tree.left) + fill_sizes(tree.right)
    return tree.size


class _CountingNode(BinaryTreeNode):
    """Node that counts how many times its children are read."""
    reads = 0

    @property
    def left(self):
        _CountingNode.reads += 1
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        _CountingNode.reads += 1
        return self._right

    @right.setter
    def right(self, value):
        self._right = value


def build_sample_bst(node_class=BinaryTreeNode) -> BinaryTreeNode:
    """Builds the 16-node sample BST from EPI 14.2 with sizes filled in."""
    N = node_class
    left = N(7, N(3, N(2), N(5)), N(11, None, N(17, N(13))))
    right = N(
        43,
        N(23, None, N(37, N(29, None, N(31)), N(41))),
        N(47, None, N(53)),
    )
    root = N(19, left, right)
    fill_sizes(root)
    return root


def build_balanced(lo: int, hi: int, node_class=BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """Builds a balanced BST holding the keys lo..hi (sizes not filled)."""
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    return node_class(mid, build_balanced(lo, mid - 1, node_class),
                      build_balanced(mid + 1, hi, node_class))


def test_count_greater_than_k():
    """Test cases for counting keys greater than k"""
    solution = Solution()
    tree = build_sample_bst()
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # Test case 1: k in the tree
    assert solution.count_greater_than_k(tree, 23) == 7
    print("✓ Test 1 passed: k=23 -> 7")

    # Test case 2: k below every key
    assert solution.count_greater_than_k(tree, 0) == 16
    print("✓ Test 2 passed: k=0 -> 16")

    # Test case 3: k at or above the maximum
    assert solution.count_greater_than_k(tree, 53) == 0
    assert solution.count_greater_than_k(tree, 99) == 0
    print("✓ Test 3 passed: k >= max -> 0")

    # Test case 4: Empty tree
    assert solution.count_greater_than_k(None, 5) == 0
    print("✓ Test 4 passed: Empty tree -> 0")

    # Test case 5: Exhaustive check against sorted keys
    for k in range(-1, 56):
        assert solution.count_greater_than_k(tree, k) == sum(1 for x in keys if x > k)
    print("✓ Test 5 passed: Every k in [-1, 55] matches")

    # Test case 6: Must use sizes, not a full traversal
    #   On a balanced 1023-node tree an O(h) walk reads ~20 child links;
    #   a traversal reads ~2000
    big = build_balanced(1, 1023, _CountingNode)
    fill_sizes(big)
    _CountingNode.reads = 0
    assert solution.count_greater_than_k(big, 300) == 723
    assert _CountingNode.reads <= 60
    print("✓ Test 6 passed: O(h) child reads on a 1023-node tree")

    # Test case 7: Negative keys
    neg = build_balanced(-10, -1)
    fill_sizes(neg)
    assert solution.count_greater_than_k(neg, -4) == 3
    assert solution.count_greater_than_k(neg, -11) == 10
    print("✓ Test 7 passed: Negative keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_greater_than_k()
