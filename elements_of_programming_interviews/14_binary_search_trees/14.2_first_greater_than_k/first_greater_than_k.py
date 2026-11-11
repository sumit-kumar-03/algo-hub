"""
EPI 14.2 - Find the First Key Greater Than a Given Value in a BST

Problem:
Given the root of a BST and a value k, return the first key that an inorder
traversal would visit that is strictly greater than k. If no key in the tree
is greater than k, return None.

Constraints:
- 0 <= number of nodes <= 10^4
- Target: O(h) time and O(1) extra space, where h is the tree height
- A full inorder walk (O(n)) ignores the BST property and is too slow

How it works (binary search with a candidate):
1. Start at the root with candidate = None
2. If node.data > k, it might be the answer: record it as the candidate
   and continue into the left subtree to look for something smaller
3. Otherwise node.data <= k, so the node and its whole left subtree are
   too small: continue into the right subtree
4. When you fall off the tree, the candidate is the answer

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
Output: 29
Explanation: Inorder order is 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53;
the first key after 23 that exceeds it is 29.

Example 2:
Input: same BST, k = 53
Output: None
Explanation: No key is greater than 53.
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
    def find_first_greater_than_k(
        self, tree: Optional[BinaryTreeNode], k: int
    ) -> Optional[int]:
        """
        Finds the smallest key in the BST that is strictly greater than k.

        Args:
            tree: Root of the BST (None for an empty tree)
            k: The value to compare against

        Returns:
            The first key greater than k in inorder order, or None if none exists

        Time Complexity: O(h) where h is the tree height
        Space Complexity: O(1)
        """
        # TODO: Implement BST search that tracks the best candidate
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


def test_find_first_greater_than_k():
    """Test cases for first key greater than k"""
    solution = Solution()
    tree = build_sample_bst()

    # Test case 1: Book example
    assert solution.find_first_greater_than_k(tree, 23) == 29
    print("✓ Test 1 passed: k=23 -> 29")

    # Test case 2: k not present in the tree
    assert solution.find_first_greater_than_k(tree, 12) == 13
    print("✓ Test 2 passed: k=12 -> 13")

    # Test case 3: Answer is an ancestor (successor of 17 is the root 19)
    assert solution.find_first_greater_than_k(tree, 17) == 19
    print("✓ Test 3 passed: k=17 -> 19")

    # Test case 4: k smaller than every key
    assert solution.find_first_greater_than_k(tree, -100) == 2
    print("✓ Test 4 passed: k=-100 -> 2 (minimum)")

    # Test case 5: Nothing greater than the maximum
    assert solution.find_first_greater_than_k(tree, 53) is None
    print("✓ Test 5 passed: k=53 -> None")

    # Test case 6: Empty tree
    assert solution.find_first_greater_than_k(None, 5) is None
    print("✓ Test 6 passed: Empty tree -> None")

    # Test case 7: Exhaustive check against sorted keys
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for k in range(0, 56):
        expected = next((x for x in keys if x > k), None)
        assert solution.find_first_greater_than_k(tree, k) == expected
    print("✓ Test 7 passed: Every k in [0, 55] matches the sorted keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_first_greater_than_k()
