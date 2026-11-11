"""
EPI 14.3 - Find the k Largest Elements in a BST

Problem:
Given the root of a BST and an integer k, return the k largest keys in the
tree, ordered from largest to smallest. If the tree has fewer than k nodes,
return all of its keys in decreasing order.

Constraints:
- 0 <= number of nodes <= 10^4
- 0 <= k
- Target: O(h + k) time, where h is the tree height (don't visit the
  whole tree when k is small)

How it works (reverse inorder traversal):
1. An inorder traversal visits keys in increasing order, so visiting
   right subtree -> node -> left subtree visits them in decreasing order
2. Append each visited key to the result
3. Stop recursing as soon as the result holds k keys

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
Output: [53, 47, 43]

Example 2:
Input: same BST, k = 5
Output: [53, 47, 43, 41, 37]
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
    def find_k_largest_in_bst(
        self, tree: Optional[BinaryTreeNode], k: int
    ) -> List[int]:
        """
        Returns the k largest keys of a BST in decreasing order.

        Args:
            tree: Root of the BST (None for an empty tree)
            k: How many keys to return

        Returns:
            Up to k keys, largest first

        Time Complexity: O(h + k) where h is the tree height
        Space Complexity: O(h) recursion depth, excluding the output
        """
        # TODO: Implement reverse inorder traversal with early stop
        pass


def build_sample_bst() -> BinaryTreeNode:
    """Builds the 16-node sample BST shown in Example 1."""
    N = BinaryTreeNode
    left = N(7, N(3, N(2), N(5)), N(11, None, N(17, N(13))))
    right = N(
        43,
        N(23, None, N(37, N(29, None, N(31)), N(41))),
        N(47, None, N(53)),
    )
    return N(19, left, right)


def test_find_k_largest_in_bst():
    """Test cases for k largest elements in a BST"""
    solution = Solution()
    tree = build_sample_bst()
    keys_desc = [53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]

    # Test case 1: Book example
    assert solution.find_k_largest_in_bst(tree, 3) == [53, 47, 43]
    print("✓ Test 1 passed: k=3 -> [53, 47, 43]")

    # Test case 2: Crossing into a left subtree
    assert solution.find_k_largest_in_bst(tree, 5) == [53, 47, 43, 41, 37]
    print("✓ Test 2 passed: k=5 -> [53, 47, 43, 41, 37]")

    # Test case 3: k = 0
    assert solution.find_k_largest_in_bst(tree, 0) == []
    print("✓ Test 3 passed: k=0 -> []")

    # Test case 4: k equals the number of nodes
    assert solution.find_k_largest_in_bst(tree, 16) == keys_desc
    print("✓ Test 4 passed: k=16 returns every key in decreasing order")

    # Test case 5: k larger than the number of nodes
    assert solution.find_k_largest_in_bst(tree, 100) == keys_desc
    print("✓ Test 5 passed: k=100 returns all 16 keys")

    # Test case 6: Empty tree
    assert solution.find_k_largest_in_bst(None, 3) == []
    print("✓ Test 6 passed: Empty tree -> []")

    # Test case 7: Left-skewed tree (largest key at the root)
    N = BinaryTreeNode
    skewed = N(5, N(4, N(3, N(2, N(1)))))
    assert solution.find_k_largest_in_bst(skewed, 2) == [5, 4]
    print("✓ Test 7 passed: Left-skewed tree, k=2 -> [5, 4]")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_k_largest_in_bst()
