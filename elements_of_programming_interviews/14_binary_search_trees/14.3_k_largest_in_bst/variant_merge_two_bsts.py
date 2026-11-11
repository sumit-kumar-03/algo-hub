"""
EPI 14.3 Extra Variant - List All Keys of Two BSTs in Sorted Order
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the inorder traversal behind the k-largest problem, made
iterative so it can be paused. Two paused traversals are merged like two
sorted arrays.

Problem:
Given the roots of two BSTs, return a list of all keys from both trees in
ascending order (keep duplicates, including keys that appear in both
trees).

Constraints:
- 0 <= number of nodes in each tree <= 10^4
- Target: O(m + n) time and O(h1 + h2) extra space excluding the output;
  dumping both trees and sorting is O((m + n) log(m + n))

How it works (two paused inorder traversals):
1. For each tree, keep a stack holding the left spine; its top is that
   tree's next smallest unvisited key
2. Repeatedly pop the smaller of the two tops (either when tied), append
   it, and push the left spine of the popped node's right subtree
3. When one stack empties, drain the other the same way

Example 1:
Input:   2        1
        / \\        \\
       1   4        3
Output: [1, 1, 2, 3, 4]

Example 2:
Input: tree1 = empty, tree2 = 5 -> left 3
Output: [3, 5]
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
    def merge_bsts(
        self, tree1: Optional[BinaryTreeNode], tree2: Optional[BinaryTreeNode]
    ) -> List[int]:
        """
        Returns all keys of both BSTs in ascending order.

        Args:
            tree1: Root of the first BST (may be None)
            tree2: Root of the second BST (may be None)

        Returns:
            Sorted list of every key in both trees

        Time Complexity: O(m + n)
        Space Complexity: O(h1 + h2), excluding the output
        """
        # TODO: Implement merge of two iterative inorder traversals
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


def test_merge_bsts():
    """Test cases for merging two BSTs into a sorted list"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Example with a shared key
    assert solution.merge_bsts(N(2, N(1), N(4)), N(1, None, N(3))) == [1, 1, 2, 3, 4]
    print("✓ Test 1 passed: -> [1, 1, 2, 3, 4]")

    # Test case 2: One empty tree
    assert solution.merge_bsts(None, N(5, N(3))) == [3, 5]
    assert solution.merge_bsts(N(5, N(3)), None) == [3, 5]
    print("✓ Test 2 passed: One empty tree")

    # Test case 3: Both empty
    assert solution.merge_bsts(None, None) == []
    print("✓ Test 3 passed: Both empty -> []")

    # Test case 4: Disjoint ranges
    t1 = build_bst_from_keys([2, 1, 3])
    t2 = build_bst_from_keys([20, 10, 30])
    assert solution.merge_bsts(t1, t2) == [1, 2, 3, 10, 20, 30]
    print("✓ Test 4 passed: Disjoint ranges")

    # Test case 5: Negative keys and skewed shapes
    t1 = build_bst_from_keys([-1, -2, -3, -4])
    t2 = build_bst_from_keys([-10, -5, 0, 5])
    assert solution.merge_bsts(t1, t2) == [-10, -5, -4, -3, -2, -1, 0, 5]
    print("✓ Test 5 passed: Negative keys, skewed trees")

    # Test case 6: Sample tree merged with itself
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    merged = solution.merge_bsts(build_sample_bst(), build_sample_bst())
    assert merged == sorted(keys + keys)
    print("✓ Test 6 passed: Sample tree with itself")

    # Test case 7: Larger interleaved trees against sorted()
    a = [(i * 37) % 211 for i in range(1, 150)]
    b = [(i * 53) % 199 for i in range(1, 120)]
    assert solution.merge_bsts(build_bst_from_keys(a), build_bst_from_keys(b)) == sorted(a + b)
    print("✓ Test 7 passed: Larger trees match sorted()")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_bsts()
