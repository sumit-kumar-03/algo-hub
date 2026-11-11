"""
EPI 14.1 Extra Variant - Is a Sequence the Preorder Traversal of a BST?
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the (low, high) bounds of the BST range check. Reading a
preorder sequence, each value must fit the bounds of the position it would
occupy; a stack recovers those bounds without building the tree.

Problem:
Given a list of distinct integers, return True if it could be the preorder
traversal (node, then left subtree, then right subtree) of some BST with
distinct keys, and False otherwise.

Constraints:
- 0 <= len(preorder) <= 10^4
- Values are distinct
- Target: O(n) time; O(n) space with a stack (O(1) is possible by reusing
  the input as the stack)

How it works (monotonic stack with a lower bound):
1. Keep a stack of ancestors whose right subtree hasn't started yet, and a
   lower bound `low` (initially -inf)
2. For each value v:
   - If v < low, it would have to go into a left subtree we have already
     left: return False
   - While the stack top is smaller than v, pop it and set low to it: v
     starts the right subtree of that node, so everything after must exceed
     it
   - Push v
3. If the scan finishes, the sequence is valid

Example 1:
Input: [5, 2, 1, 3, 6]
Output: True
Explanation: Root 5, left subtree 2 (with 1 and 3), right subtree 6.

Example 2:
Input: [5, 2, 6, 1, 3]
Output: False
Explanation: After 6 starts 5's right subtree, 1 cannot appear.
"""

from typing import List


class Solution:
    def is_bst_preorder(self, preorder: List[int]) -> bool:
        """
        Checks whether a sequence is a valid BST preorder traversal.

        Args:
            preorder: Distinct integers

        Returns:
            True if some BST has exactly this preorder traversal

        Time Complexity: O(n)
        Space Complexity: O(n) for the stack
        """
        # TODO: Implement stack-based preorder validation
        pass


def test_is_bst_preorder():
    """Test cases for BST preorder validation"""
    solution = Solution()

    # Test case 1: Valid preorder
    assert solution.is_bst_preorder([5, 2, 1, 3, 6]) is True
    print("✓ Test 1 passed: [5, 2, 1, 3, 6] -> True")

    # Test case 2: Value returns to a finished left subtree
    assert solution.is_bst_preorder([5, 2, 6, 1, 3]) is False
    print("✓ Test 2 passed: [5, 2, 6, 1, 3] -> False")

    # Test case 3: Empty and single
    assert solution.is_bst_preorder([]) is True
    assert solution.is_bst_preorder([7]) is True
    print("✓ Test 3 passed: Empty / single -> True")

    # Test case 4: Strictly increasing and strictly decreasing chains
    assert solution.is_bst_preorder([1, 2, 3, 4]) is True
    assert solution.is_bst_preorder([4, 3, 2, 1]) is True
    print("✓ Test 4 passed: Chains are valid")

    # Test case 5: Violation of a grandparent's bound, not the parent's
    #   10 -> left 5 -> right 7 ... then 4 would need to be in 5's left
    #   subtree, which already ended when 7 started
    assert solution.is_bst_preorder([10, 5, 7, 4]) is False
    assert solution.is_bst_preorder([10, 5, 4, 7, 12]) is True
    print("✓ Test 5 passed: Grandparent bound enforced")

    # Test case 6: Negative values
    assert solution.is_bst_preorder([0, -5, -8, -2, 3, 9]) is True
    assert solution.is_bst_preorder([0, -5, 3, -2]) is False
    print("✓ Test 6 passed: Negative values")

    # Test case 7: Every permutation of 1..6 checked by brute force.
    # A sequence is a BST preorder exactly when inserting its keys in order
    # into an empty BST produces a tree whose preorder is the sequence itself.
    from itertools import permutations

    def insert_then_preorder(seq):
        children = {}
        root = seq[0]
        children[root] = [None, None]
        for key in seq[1:]:
            cur = root
            while True:
                side = 0 if key < cur else 1
                if children[cur][side] is None:
                    children[cur][side] = key
                    children[key] = [None, None]
                    break
                cur = children[cur][side]
        out, stack = [], [root]
        while stack:
            node = stack.pop()
            if node is not None:
                out.append(node)
                stack.append(children[node][1])
                stack.append(children[node][0])
        return out

    valid_count = 0
    for perm in permutations(range(1, 7)):
        seq = list(perm)
        expected = insert_then_preorder(seq) == seq
        valid_count += expected
        assert solution.is_bst_preorder(seq) is expected
    assert valid_count == 132  # Catalan(6) distinct BST shapes
    print("✓ Test 7 passed: All 720 permutations of 1..6 match brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_bst_preorder()
