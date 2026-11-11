"""
EPI 9.1 Variant - Find a Lowest k-Unbalanced Node

Problem:
Call a node k-balanced if the number of nodes in its left subtree and the
number of nodes in its right subtree differ by at most k. Given a binary
tree and an integer k >= 0, return a node that is NOT k-balanced but all of
whose descendants ARE k-balanced. Return None if every node is k-balanced.

Constraints:
- 0 <= number of nodes <= 10^4
- k >= 0
- O(n) time, O(h) space

How it works (post-order with early exit):
1. Recursively process the left and right subtrees; each call returns
   either a found node or the subtree's size
2. If a child call already found a qualifying node, propagate it upward
3. Otherwise compare the two subtree sizes: if they differ by more than k,
   this node is the answer (all its descendants were k-balanced)
4. Otherwise return the size left_size + right_size + 1

Example 1 (Figure 9.1 in the book, k = 3):
Input:              314
                 /       \\
               6           6
             /   \\       /   \\
          271    561   [2]   271
          / \\      \\     \\      \\
        28   0      3     1     28
                   /     / \\
                 17    401  257
                         \\
                         641
Output: the node with key 2 (node J in the book)
Explanation: Its left subtree is empty and its right subtree has 4 nodes.

Example 2:
Input: a perfect tree with 7 nodes, k = 0
Output: None
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
    def find_k_unbalanced_node(
        self, tree: Optional[BinaryTreeNode], k: int
    ) -> Optional[BinaryTreeNode]:
        """
        Finds a node that is not k-balanced but whose descendants all are.

        Args:
            tree: Root of the binary tree (None for an empty tree)
            k: Allowed difference in subtree sizes

        Returns:
            Such a node, or None if every node is k-balanced

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement k-unbalanced node search
        pass


def test_find_k_unbalanced_node():
    """Test cases for lowest k-unbalanced node"""
    solution = Solution()
    N = BinaryTreeNode

    # Build the Figure 9.1 tree, keeping a handle on node J (key 2)
    node_j = N(2, None, N(1, N(401, None, N(641)), N(257)))
    node_i = N(6, node_j, N(271, None, N(28)))
    figure = N(314, N(6, N(271, N(28), N(0)), N(561, None, N(3, N(17)))), node_i)

    # Test case 1: Empty tree
    assert solution.find_k_unbalanced_node(None, 1) is None
    print("✓ Test 1 passed: Empty tree")

    # Test case 2: Perfect tree is 0-balanced everywhere
    perfect = N(1, N(2, N(4), N(5)), N(3, N(6), N(7)))
    assert solution.find_k_unbalanced_node(perfect, 0) is None
    print("✓ Test 2 passed: Perfect tree has no unbalanced node")

    # Test case 3: Book example, k = 3 -> node J
    assert solution.find_k_unbalanced_node(figure, 3) is node_j
    print("✓ Test 3 passed: Figure 9.1 with k = 3")

    # Test case 4: k = 2 -> node J again (its ancestor I is also unbalanced)
    assert solution.find_k_unbalanced_node(figure, 2) is node_j
    print("✓ Test 4 passed: Lowest node is chosen over its ancestor")

    # Test case 5: Large k -> everything balanced
    assert solution.find_k_unbalanced_node(figure, 10) is None
    print("✓ Test 5 passed: Large k")

    # Test case 6: Left chain with k = 1
    deep = N(4)
    node_2 = N(2, N(3, deep))
    chain = N(1, node_2)
    assert solution.find_k_unbalanced_node(chain, 1) is node_2
    print("✓ Test 6 passed: Left chain")

    # Test case 7: Root with one child, k = 0
    root = N(1, N(2))
    assert solution.find_k_unbalanced_node(root, 0) is root
    print("✓ Test 7 passed: Root is the answer")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_k_unbalanced_node()
