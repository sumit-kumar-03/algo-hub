"""
EPI 14.1 Extra Variant - Minimum Difference Between Any Two Keys in a BST
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the inorder view of the BST property used to validate a BST:
an inorder walk of a valid BST visits keys in sorted order, so neighbors in
that walk are the only pairs worth comparing.

Problem:
Given the root of a BST with at least two nodes, return the smallest
difference between the keys of any two different nodes.

Constraints:
- 2 <= number of nodes <= 10^4
- Keys are integers; duplicates are allowed (left <= node <= right), in
  which case the answer is 0
- O(n) time, O(h) space where h is the tree height

How it works:
1. Do an inorder traversal, remembering the previously visited key
2. At each node, compare node.data - previous with the best so far
3. Comparing only consecutive keys is enough: in sorted order the closest
   pair is always adjacent

Example 1:
Input:      10
           /  \\
          4    15
         / \\
        1   7
Output: 3
Explanation: Sorted keys are 1 4 7 10 15; the closest neighbors differ by 3.

Example 2:
Input:   1
          \\
           48
          /  \\
         12   49
Output: 1
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
    def min_difference(self, tree: BinaryTreeNode) -> int:
        """
        Finds the smallest difference between keys of two different nodes.

        Args:
            tree: Root of a BST with at least two nodes

        Returns:
            The minimum absolute difference between any two keys

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement inorder scan comparing consecutive keys
        pass


def test_min_difference():
    """Test cases for minimum key difference in a BST"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Balanced tree
    tree = N(10, N(4, N(1), N(7)), N(15))
    assert solution.min_difference(tree) == 3
    print("✓ Test 1 passed: -> 3")

    # Test case 2: Closest pair is root's right subtree internals
    tree = N(1, None, N(48, N(12), N(49)))
    assert solution.min_difference(tree) == 1
    print("✓ Test 2 passed: -> 1")

    # Test case 3: Two nodes
    assert solution.min_difference(N(5, N(-5))) == 10
    print("✓ Test 3 passed: Two nodes -> 10")

    # Test case 4: Closest pair is an ancestor and a deep descendant
    #        50
    #       /  \\
    #     20    80
    #       \\
    #        45
    #          \\
    #           49
    tree = N(50, N(20, None, N(45, None, N(49))), N(80))
    assert solution.min_difference(tree) == 1
    print("✓ Test 4 passed: Ancestor/descendant pair -> 1")

    # Test case 5: Duplicate keys
    tree = N(8, N(8), N(12))
    assert solution.min_difference(tree) == 0
    print("✓ Test 5 passed: Duplicates -> 0")

    # Test case 6: Negative keys in a left-leaning chain
    tree = N(-1, N(-10, N(-30)))
    assert solution.min_difference(tree) == 9
    print("✓ Test 6 passed: Negative chain -> 9")

    # Test case 7: Larger tree versus sorted keys
    keys = [(i * 7919) % 1009 for i in range(1, 300)]
    root = None
    for key in keys:
        node = N(key)
        if root is None:
            root = node
            continue
        cur = root
        while True:
            nxt = cur.left if key < cur.data else cur.right
            if nxt is None:
                if key < cur.data:
                    cur.left = node
                else:
                    cur.right = node
                break
            cur = nxt
    s = sorted(keys)
    assert solution.min_difference(root) == min(b - a for a, b in zip(s, s[1:]))
    print("✓ Test 7 passed: 299-node tree matches sorted keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_difference()
