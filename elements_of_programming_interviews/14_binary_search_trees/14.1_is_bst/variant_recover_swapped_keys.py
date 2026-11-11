"""
EPI 14.1 Extra Variant - Repair a BST Whose Two Keys Were Swapped
(Practice problem, not in the book. Difficulty: Medium)
Builds on: detecting BST violations. In the inorder view a valid BST is
sorted, so the violations you would detect while validating pinpoint
exactly which two keys were exchanged.

Problem:
A BST with distinct keys was corrupted: the keys of exactly two nodes were
swapped (the tree's shape is unchanged). Restore the BST in place by
swapping those two keys back. Do not change the tree's structure.

Constraints:
- 2 <= number of nodes <= 10^4
- Keys are distinct
- O(n) time, O(h) space where h is the tree height (O(1) is possible with
  a Morris traversal)

How it works (inorder with a previous pointer):
1. Walk the tree inorder, remembering the previously visited node
2. Each time prev.data > node.data, you have found a descent
3. At the first descent, the misplaced larger key is prev; record
   first = prev and second = node
4. If a second descent occurs, the misplaced smaller key is that node:
   update second = node
5. After the walk, swap first.data and second.data. (Swapping adjacent
   keys in sorted order produces only one descent; otherwise there are two)

Example 1:
Input:      3
           / \\
          1   4
             /
            2
Output:     2
           / \\
          1   4
             /
            3
Explanation: Inorder was 1 3 2 4; keys 3 and 2 were swapped.

Example 2:
Input:   1
        /
       3
        \\
         2
Output:  3
        /
       1
        \\
         2
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
    def recover_tree(self, tree: BinaryTreeNode) -> None:
        """
        Swaps back the two misplaced keys so the tree is a BST again.

        Args:
            tree: Root of a BST in which exactly two keys were exchanged

        Returns:
            None; the tree is fixed in place

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the tree height
        """
        # TODO: Implement inorder detection of the two swapped keys
        pass


def inorder_keys(tree: Optional[BinaryTreeNode]) -> List[int]:
    """Returns the keys of the tree in inorder order."""
    return inorder_keys(tree.left) + [tree.data] + inorder_keys(tree.right) if tree else []


def test_recover_tree():
    """Test cases for repairing a BST with two swapped keys"""
    solution = Solution()
    N = BinaryTreeNode

    # Test case 1: Non-adjacent swap (two descents)
    tree = N(3, N(1), N(4, N(2)))
    solution.recover_tree(tree)
    assert tree.data == 2 and tree.right.left.data == 3
    assert inorder_keys(tree) == [1, 2, 3, 4]
    print("✓ Test 1 passed: Root and deep node swapped")

    # Test case 2: Adjacent swap (one descent)
    tree = N(1, N(3, None, N(2)))
    solution.recover_tree(tree)
    assert tree.data == 3 and tree.left.data == 1 and tree.left.right.data == 2
    print("✓ Test 2 passed: Adjacent keys swapped")

    # Test case 3: Two-node tree
    tree = N(1, N(2))
    solution.recover_tree(tree)
    assert tree.data == 2 and tree.left.data == 1
    print("✓ Test 3 passed: Two nodes")

    # Test case 4: Structure is unchanged (same node objects)
    a, b, c = N(10), N(20), N(30)
    b.left, b.right = c, a
    solution.recover_tree(b)
    assert b.left is c and b.right is a
    assert (c.data, b.data, a.data) == (10, 20, 30)
    print("✓ Test 4 passed: Only keys move, not nodes")

    # Test case 5: Smallest and largest keys swapped, negatives
    tree = N(0, N(-5, N(9), N(-2)), N(5, N(3), N(-9)))
    solution.recover_tree(tree)
    assert inorder_keys(tree) == [-9, -5, -2, 0, 3, 5, 9]
    print("✓ Test 5 passed: Min and max swapped")

    # Test case 6: Every possible swap on the sample-shaped tree
    def build():
        left = N(7, N(3, N(2), N(5)), N(11, None, N(17, N(13))))
        right = N(43, N(23, None, N(37, N(29, None, N(31)), N(41))), N(47, None, N(53)))
        return N(19, left, right)

    def nodes_inorder(t):
        return nodes_inorder(t.left) + [t] + nodes_inorder(t.right) if t else []

    expected = inorder_keys(build())
    count = 0
    for i in range(16):
        for j in range(i + 1, 16):
            tree = build()
            nodes = nodes_inorder(tree)
            nodes[i].data, nodes[j].data = nodes[j].data, nodes[i].data
            solution.recover_tree(tree)
            assert inorder_keys(tree) == expected
            count += 1
    assert count == 120
    print("✓ Test 6 passed: All 120 swaps on a 16-node tree repaired")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_recover_tree()
