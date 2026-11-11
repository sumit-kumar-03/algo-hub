"""
EPI 14.3 Extra Variant - Find the kth Smallest Key in a BST
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the reverse inorder traversal with an early stop, flipped back
to an ordinary inorder traversal and returning a single key.

Problem:
Given the root of a BST and an integer k (1-indexed), return the kth
smallest key. If the tree has fewer than k nodes, return None.

Constraints:
- 0 <= number of nodes <= 10^4
- 1 <= k
- Target: O(h + k) time; stop as soon as the kth key is visited

How it works:
1. An inorder traversal (left, node, right) visits keys in increasing order
2. Count nodes as they are visited; when the count reaches k, return that
   node's key
3. An iterative traversal with an explicit stack makes the early stop easy

Example 1:
Input: BST below, k = 3
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
Output: 5

Example 2:
Input: same BST, k = 17
Output: None
Explanation: The tree has only 16 keys.
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
    def kth_smallest(self, tree: Optional[BinaryTreeNode], k: int) -> Optional[int]:
        """
        Returns the kth smallest key of a BST.

        Args:
            tree: Root of the BST (None for an empty tree)
            k: 1-indexed rank from the smallest

        Returns:
            The kth smallest key, or None if the tree has fewer than k keys

        Time Complexity: O(h + k) where h is the tree height
        Space Complexity: O(h)
        """
        # TODO: Implement inorder traversal with early stop
        pass


def build_sample_bst() -> BinaryTreeNode:
    """Builds the 16-node sample BST from EPI 14.2 / 14.3."""
    N = BinaryTreeNode
    left = N(7, N(3, N(2), N(5)), N(11, None, N(17, N(13))))
    right = N(
        43,
        N(23, None, N(37, N(29, None, N(31)), N(41))),
        N(47, None, N(53)),
    )
    return N(19, left, right)


def build_bst_from_keys(keys: List[int]) -> Optional[BinaryTreeNode]:
    """Builds a BST by inserting keys in the given order (no balancing)."""
    root = None
    for key in keys:
        node = BinaryTreeNode(key)
        if root is None:
            root = node
            continue
        cur = root
        while True:
            if key < cur.data:
                if cur.left is None:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    break
                cur = cur.right
    return root


def test_kth_smallest():
    """Test cases for kth smallest key in a BST"""
    solution = Solution()
    tree = build_sample_bst()
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # Test case 1: Example
    assert solution.kth_smallest(tree, 3) == 5
    print("✓ Test 1 passed: k=3 -> 5")

    # Test case 2: k beyond the tree size
    assert solution.kth_smallest(tree, 17) is None
    print("✓ Test 2 passed: k=17 -> None")

    # Test case 3: Minimum and maximum
    assert solution.kth_smallest(tree, 1) == 2
    assert solution.kth_smallest(tree, 16) == 53
    print("✓ Test 3 passed: k=1 -> 2, k=16 -> 53")

    # Test case 4: Every rank
    assert [solution.kth_smallest(tree, k) for k in range(1, 17)] == keys
    print("✓ Test 4 passed: All ranks match sorted keys")

    # Test case 5: Empty tree and single node
    assert solution.kth_smallest(None, 1) is None
    assert solution.kth_smallest(BinaryTreeNode(-4), 1) == -4
    print("✓ Test 5 passed: Empty / single node")

    # Test case 6: Right-skewed chain
    chain = build_bst_from_keys([1, 2, 3, 4, 5, 6])
    assert solution.kth_smallest(chain, 4) == 4
    print("✓ Test 6 passed: Right-skewed chain")

    # Test case 7: Duplicates (left <= node <= right) count separately
    dup = BinaryTreeNode(5, BinaryTreeNode(5), BinaryTreeNode(7))
    assert [solution.kth_smallest(dup, k) for k in (1, 2, 3)] == [5, 5, 7]
    print("✓ Test 7 passed: Duplicate keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_smallest()
