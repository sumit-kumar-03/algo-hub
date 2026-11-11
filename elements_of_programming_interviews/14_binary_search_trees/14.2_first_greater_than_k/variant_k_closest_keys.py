"""
EPI 14.2 Extra Variant - Find the k Keys Closest to a Target in a BST
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the "first key greater than k" walk. That walk's path is
exactly what you need to start two iterators: one stepping to successive
larger keys (successors) and one stepping to successive smaller keys
(predecessors) from the target's position.

Problem:
Given the root of a BST with distinct keys, a real-valued target, and an
integer k, return the k keys closest to the target, listed in ascending
order. Distance is |key - target|; when two keys are equally close, the
smaller key is considered closer. If k exceeds the number of nodes, return
all keys.

Constraints:
- 0 <= number of nodes <= 10^4
- 0 <= k
- Target: O(h + k) time and O(h) extra space; collecting and sorting all
  keys is O(n log n)

How it works (two stacks):
1. Walk from the root toward target. Push nodes with key > target onto a
   "successor" stack (then go left), and nodes with key <= target onto a
   "predecessor" stack (then go right). The stack tops are the nearest keys
   above and at-or-below the target
2. Repeat k times: compare the two tops' distances (ties go to the
   predecessor, the smaller key), take the closer one, and advance that
   stack: for successors, pop and push the left spine of the popped node's
   right subtree; for predecessors, pop and push the right spine of the
   popped node's left subtree
3. Taken predecessors come out in descending order and successors in
   ascending order, so the result is reversed predecessors + successors

Example 1:
Input: BST below, target = 30.0, k = 3
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
Output: [23, 29, 31]
Explanation: 29 and 31 are 1 away. 23 and 37 are both 7 away, and the tie
is resolved toward the smaller key, 23.

Example 2:
Input: same BST, target = 1.0, k = 3
Output: [2, 3, 5]
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
    def k_closest_keys(
        self, tree: Optional[BinaryTreeNode], target: float, k: int
    ) -> List[int]:
        """
        Finds the k keys nearest to target, returned in ascending order.

        Args:
            tree: Root of a BST with distinct keys (None for an empty tree)
            target: The value to approach
            k: How many keys to return

        Returns:
            Up to k closest keys in ascending order (ties favor smaller keys)

        Time Complexity: O(h + k) where h is the tree height
        Space Complexity: O(h), excluding the output
        """
        # TODO: Implement predecessor/successor stacks
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


def test_k_closest_keys():
    """Test cases for k closest keys in a BST"""
    solution = Solution()
    tree = build_sample_bst()
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    def brute(target: float, k: int) -> List[int]:
        return sorted(sorted(keys, key=lambda x: (abs(x - target), x))[:k])

    # Test case 1: Tie on the outer pair resolved toward the smaller key
    assert solution.k_closest_keys(tree, 30.0, 3) == [23, 29, 31]
    assert solution.k_closest_keys(tree, 30.0, 4) == [23, 29, 31, 37]
    print("✓ Test 1 passed: target=30.0, k=3 -> [23, 29, 31]")

    # Test case 2: Target below every key
    assert solution.k_closest_keys(tree, 1.0, 3) == [2, 3, 5]
    print("✓ Test 2 passed: target=1.0, k=3 -> [2, 3, 5]")

    # Test case 3: Target above every key
    assert solution.k_closest_keys(tree, 100.0, 2) == [47, 53]
    print("✓ Test 3 passed: target=100.0, k=2 -> [47, 53]")

    # Test case 4: k = 0, empty tree, and k larger than the tree
    assert solution.k_closest_keys(tree, 20.0, 0) == []
    assert solution.k_closest_keys(None, 20.0, 3) == []
    assert solution.k_closest_keys(tree, 20.0, 50) == keys
    print("✓ Test 4 passed: k=0 / empty / k > n")

    # Test case 5: Target equal to a key
    assert solution.k_closest_keys(tree, 19.0, 1) == [19]
    assert solution.k_closest_keys(tree, 19.0, 3) == [17, 19, 23]
    print("✓ Test 5 passed: Target on a key")

    # Test case 6: Sweep of targets and k against brute force
    for t2 in range(-4, 115, 3):
        target = t2 / 2
        for k in [1, 2, 5, 9, 16]:
            assert solution.k_closest_keys(tree, target, k) == brute(target, k)
    print("✓ Test 6 passed: Target/k sweep matches brute force")

    # Test case 7: Skewed tree with negative keys
    skewed = build_bst_from_keys([0, -3, -6, -9, -12])
    assert solution.k_closest_keys(skewed, -7.5, 2) == [-9, -6]
    assert solution.k_closest_keys(skewed, -4.5, 2) == [-6, -3]
    print("✓ Test 7 passed: Skewed tree with negative keys")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_closest_keys()
