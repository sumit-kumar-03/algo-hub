"""
EPI 14.2 Variant - Find the First Node Whose Key Equals k in a BST

Problem:
Given the root of a BST that may contain duplicate keys and a value k,
return the node whose key equals k and that comes first in an inorder
traversal. Return None if no node holds k. (Duplicates may appear in
either subtree, as allowed by the BST property: left <= node <= right.)

Constraints:
- 0 <= number of nodes <= 10^4
- Target: O(h) time and O(1) extra space, where h is the tree height
- You must return the node object itself, not just its key

How it works:
1. Walk down from the root keeping a candidate (initially None)
2. If node.data < k, go right; if node.data > k, go left
3. If node.data == k, record the node as the candidate and keep going
   left, since an earlier equal key can only live in the left subtree
4. Return the candidate once you fall off the tree

Example 1:
Input:              108 (A)
                  /        \\
             108 (B)        285 (G)
             /     \\        /     \\
        -10 (C)  108 (F)  243 (H)  285 (I)
         /   \\                       \\
     -14 (D)  2 (E)                   401 (J)
k = 108
Output: Node B
Explanation: Inorder order is D C E B F A H G I J; B is the first 108.

Example 2:
Input: same BST, k = 143
Output: None
Explanation: No node holds 143. (For k = 285 the answer is Node G.)
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
    def find_first_equal_k(
        self, tree: Optional[BinaryTreeNode], k: int
    ) -> Optional[BinaryTreeNode]:
        """
        Finds the first node in inorder order whose key equals k.

        Args:
            tree: Root of the BST, which may contain duplicate keys
            k: The key to look for

        Returns:
            The first matching node in inorder order, or None if k is absent

        Time Complexity: O(h) where h is the tree height
        Space Complexity: O(1)
        """
        # TODO: Implement search for the first occurrence of k
        pass


def test_find_first_equal_k():
    """Test cases for first node equal to k"""
    solution = Solution()
    N = BinaryTreeNode

    d, e = N(-14), N(2)
    c = N(-10, d, e)
    f = N(108)
    b = N(108, c, f)
    j = N(401)
    i = N(285, None, j)
    h = N(243)
    g = N(285, h, i)
    a = N(108, b, g)

    # Test case 1: Book example, duplicates at root, left child, grandchild
    assert solution.find_first_equal_k(a, 108) is b
    print("✓ Test 1 passed: k=108 -> Node B")

    # Test case 2: Book example, duplicate in right subtree
    assert solution.find_first_equal_k(a, 285) is g
    print("✓ Test 2 passed: k=285 -> Node G")

    # Test case 3: Missing key
    assert solution.find_first_equal_k(a, 143) is None
    print("✓ Test 3 passed: k=143 -> None")

    # Test case 4: Unique key deep in the tree
    assert solution.find_first_equal_k(a, -14) is d
    print("✓ Test 4 passed: k=-14 -> Node D")

    # Test case 5: Empty tree
    assert solution.find_first_equal_k(None, 7) is None
    print("✓ Test 5 passed: Empty tree -> None")

    # Test case 6: All keys equal (left-leaning chain), first is the deepest
    deepest = N(5)
    chain = N(5, N(5, deepest))
    assert solution.find_first_equal_k(chain, 5) is deepest
    print("✓ Test 6 passed: All-equal chain -> deepest left node")

    # Test case 7: Equal key hidden in the right subtree of a smaller left child
    #        10
    #       /  \\
    #      5    12
    #       \\
    #        10   <- this comes before the root in inorder order
    inner = N(10)
    tree7 = N(10, N(5, None, inner), N(12))
    assert solution.find_first_equal_k(tree7, 10) is inner
    print("✓ Test 7 passed: Earlier duplicate in left subtree's right side")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_first_equal_k()
