"""
EPI 14.2 Extra Variant - Find the Last Key Less Than a Given Value in a BST
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the BST search that records a candidate and keeps descending,
mirrored so that it looks for the largest key below k instead of the
smallest key above it.

Problem:
Given the root of a BST and a value k, return the largest key in the tree
that is strictly less than k (the last such key in inorder order). If no
key is less than k, return None.

Constraints:
- 0 <= number of nodes <= 10^4
- Target: O(h) time and O(1) extra space, where h is the tree height

How it works (binary search with a candidate):
1. Start at the root with candidate = None
2. If node.data < k, it might be the answer: record it and go right to
   look for something larger that is still below k
3. Otherwise node.data >= k: the node and its right subtree are too big,
   so go left
4. When you fall off the tree, return the candidate

Example 1:
Input: BST below, k = 23
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
Output: 19
Explanation: Inorder order is 2 3 5 7 11 13 17 19 23 29 ...; the last key
before 23 that is below it is 19 (the root), even though 23 has no left
child.

Example 2:
Input: same BST, k = 2
Output: None
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
    def find_last_less_than_k(
        self, tree: Optional[BinaryTreeNode], k: int
    ) -> Optional[int]:
        """
        Finds the largest key in the BST that is strictly less than k.

        Args:
            tree: Root of the BST (None for an empty tree)
            k: The value to compare against

        Returns:
            The largest key below k, or None if none exists

        Time Complexity: O(h) where h is the tree height
        Space Complexity: O(1)
        """
        # TODO: Implement BST search that tracks the best candidate
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


def test_find_last_less_than_k():
    """Test cases for last key less than k"""
    solution = Solution()
    tree = build_sample_bst()
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # Test case 1: Answer is an ancestor
    assert solution.find_last_less_than_k(tree, 23) == 19
    print("✓ Test 1 passed: k=23 -> 19")

    # Test case 2: Nothing smaller than the minimum
    assert solution.find_last_less_than_k(tree, 2) is None
    print("✓ Test 2 passed: k=2 -> None")

    # Test case 3: k absent from the tree
    assert solution.find_last_less_than_k(tree, 30) == 29
    print("✓ Test 3 passed: k=30 -> 29")

    # Test case 4: k above every key
    assert solution.find_last_less_than_k(tree, 1000) == 53
    print("✓ Test 4 passed: k=1000 -> 53 (maximum)")

    # Test case 5: Empty tree and single node
    assert solution.find_last_less_than_k(None, 5) is None
    assert solution.find_last_less_than_k(BinaryTreeNode(4), 5) == 4
    assert solution.find_last_less_than_k(BinaryTreeNode(4), 4) is None
    print("✓ Test 5 passed: Empty / single node")

    # Test case 6: Exhaustive check against sorted keys
    for k in range(0, 56):
        expected = max((x for x in keys if x < k), default=None)
        assert solution.find_last_less_than_k(tree, k) == expected
    print("✓ Test 6 passed: Every k in [0, 55] matches the sorted keys")

    # Test case 7: Negative keys in a skewed tree
    skewed = build_bst_from_keys([-1, -5, -9, -20])
    assert solution.find_last_less_than_k(skewed, -6) == -9
    assert solution.find_last_less_than_k(skewed, 0) == -1
    print("✓ Test 7 passed: Negative keys in a left-skewed tree")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_last_less_than_k()
