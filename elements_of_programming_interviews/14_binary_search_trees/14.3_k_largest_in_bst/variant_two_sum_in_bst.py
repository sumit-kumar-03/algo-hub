"""
EPI 14.3 Extra Variant - Two Keys in a BST That Sum to a Target
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the reverse inorder traversal from the k-largest problem, run
step by step alongside an ordinary inorder traversal so the BST behaves
like a sorted array scanned from both ends.

Problem:
Given the root of a BST with distinct keys and an integer target, return
True if two DIFFERENT nodes have keys that add up to target, and False
otherwise.

Constraints:
- 0 <= number of nodes <= 10^4
- Keys are distinct integers
- Target: O(n) time and O(h) extra space; copying all keys into an array
  or a hash set uses O(n) space

How it works (two iterators):
1. Build an ascending iterator (stack holding the left spine) and a
   descending iterator (stack holding the right spine); this is the
   reverse inorder traversal from 14.3, paused after each key
2. Let lo be the next ascending key and hi the next descending key
3. While lo < hi: if lo + hi == target, return True; if the sum is too
   small, advance the ascending iterator; if too large, advance the
   descending one
4. When the iterators meet, no pair exists

Example 1:
Input: BST below, target = 60
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
Output: True
Explanation: 7 + 53 = 60 (also 13 + 47, 17 + 43, 19 + 41, 23 + 37, 29 + 31).

Example 2:
Input: same BST, target = 4
Output: False
Explanation: 2 + 2 would need the same node twice.
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
    def has_two_sum(self, tree: Optional[BinaryTreeNode], target: int) -> bool:
        """
        Checks whether two different nodes' keys sum to target.

        Args:
            tree: Root of a BST with distinct keys (None for an empty tree)
            target: The desired sum

        Returns:
            True if such a pair exists, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement two-iterator search
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


def test_has_two_sum():
    """Test cases for two-sum in a BST"""
    solution = Solution()
    tree = build_sample_bst()
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # Test case 1: Pair exists
    assert solution.has_two_sum(tree, 60) is True
    print("✓ Test 1 passed: 60 -> True")

    # Test case 2: Would require reusing one node
    assert solution.has_two_sum(tree, 4) is False
    print("✓ Test 2 passed: 4 -> False")

    # Test case 3: Smallest and largest possible sums
    assert solution.has_two_sum(tree, 5) is True
    assert solution.has_two_sum(tree, 100) is True
    assert solution.has_two_sum(tree, 101) is False
    print("✓ Test 3 passed: Extreme sums")

    # Test case 4: Empty tree and single node
    assert solution.has_two_sum(None, 0) is False
    assert solution.has_two_sum(BinaryTreeNode(5), 10) is False
    print("✓ Test 4 passed: Empty / single -> False")

    # Test case 5: Negative keys and zero target
    tree5 = build_bst_from_keys([0, -4, 4, -7, 2])
    assert solution.has_two_sum(tree5, 0) is True
    assert solution.has_two_sum(tree5, -11) is True
    assert solution.has_two_sum(tree5, 1) is False
    print("✓ Test 5 passed: Negative keys")

    # Test case 6: Every target from 0 to 110 against brute force
    for target in range(0, 111):
        expected = any(keys[i] + keys[j] == target
                       for i in range(len(keys)) for j in range(i + 1, len(keys)))
        assert solution.has_two_sum(tree, target) is expected
    print("✓ Test 6 passed: All targets 0..110 match brute force")

    # Test case 7: Skewed tree
    chain = build_bst_from_keys([10, 20, 30, 40])
    assert solution.has_two_sum(chain, 70) is True
    assert solution.has_two_sum(chain, 80) is False
    print("✓ Test 7 passed: Right-skewed chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_has_two_sum()
