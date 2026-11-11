"""
EPI 14.2 Extra Variant - Find the Key Closest to a Target in a BST
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the single root-to-leaf walk of the "first greater than k"
search. The answer is either the first key above the target or the last key
below it, and both lie on the same search path.

Problem:
Given the root of a nonempty BST and a real-valued target, return the key
whose distance |key - target| is smallest. If two keys are equally close,
return the smaller key.

Constraints:
- 1 <= number of nodes <= 10^4
- target is a float
- Target: O(h) time and O(1) extra space, where h is the tree height

How it works:
1. Walk down from the root as in an ordinary BST search for target
2. At each node, compare its distance to the best so far (preferring the
   smaller key on ties) and update the best
3. Go left if target < node.data, otherwise go right
4. Any key off this path is farther away than some key on it, so the walk
   sees the answer

Example 1:
Input: BST below, target = 25.0
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
Output: 23
Explanation: 23 is 2 away; 29 is 4 away.

Example 2:
Input: same BST, target = 9.0
Output: 7
Explanation: 7 and 11 are both 2 away; the smaller one wins.
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
    def closest_key(self, tree: BinaryTreeNode, target: float) -> int:
        """
        Finds the key nearest to target (smaller key on ties).

        Args:
            tree: Root of a nonempty BST
            target: The value to approach

        Returns:
            The closest key

        Time Complexity: O(h) where h is the tree height
        Space Complexity: O(1)
        """
        # TODO: Implement closest key search along one path
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


def test_closest_key():
    """Test cases for closest key in a BST"""
    solution = Solution()
    tree = build_sample_bst()
    keys = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # Test case 1: Clear winner
    assert solution.closest_key(tree, 25.0) == 23
    print("✓ Test 1 passed: 25.0 -> 23")

    # Test case 2: Tie goes to the smaller key
    assert solution.closest_key(tree, 9.0) == 7
    print("✓ Test 2 passed: 9.0 -> 7 (tie)")

    # Test case 3: Exact match
    assert solution.closest_key(tree, 41.0) == 41
    print("✓ Test 3 passed: 41.0 -> 41")

    # Test case 4: Outside the key range
    assert solution.closest_key(tree, -100.5) == 2
    assert solution.closest_key(tree, 1e9) == 53
    print("✓ Test 4 passed: Far below / above")

    # Test case 5: Single node
    assert solution.closest_key(BinaryTreeNode(7), 3.3) == 7
    print("✓ Test 5 passed: Single node")

    # Test case 6: Fractional targets between neighbors
    assert solution.closest_key(tree, 18.1) == 19
    assert solution.closest_key(tree, 30.4) == 31
    print("✓ Test 6 passed: Fractional targets")

    # Test case 7: Sweep of targets against brute force
    for t10 in range(-20, 600, 7):
        target = t10 / 10
        expected = min(keys, key=lambda x: (abs(x - target), x))
        assert solution.closest_key(tree, target) == expected
    print("✓ Test 7 passed: Target sweep matches brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_closest_key()
