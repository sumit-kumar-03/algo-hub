"""
EPI 14.3 Extra Variant - Dynamic kth Largest with a Size-Augmented BST
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the reverse inorder idea of the k-largest problem ("right
subtree first, then the node, then the left subtree"). Storing subtree
sizes lets you skip whole right subtrees, turning an O(h + k) walk into an
O(h) descent, even while keys are inserted and deleted.

Problem:
Implement a set of distinct integer keys backed by a binary search tree
whose nodes store the size of their subtrees.
- insert(key): add key; return False (and change nothing) if it is
  already present, True otherwise.
- delete(key): remove key; return True if it was present.
- kth_largest(k): return the kth largest key (k = 1 is the maximum), or
  None if k < 1 or k exceeds the number of keys.
- size(): return the number of keys.

Constraints:
- Up to 10^4 operations
- O(h) time per operation, where h is the tree height (no balancing is
  required); kth_largest must not traverse the tree

How it works:
1. Each node stores key, left, right, and size = 1 + size(left) +
   size(right)
2. insert/delete walk down from the root like an ordinary BST and fix the
   sizes on the path (only after confirming the operation will happen, or
   by recomputing sizes on the way back up)
3. Deleting a node with two children: replace its key with its successor
   (the minimum of its right subtree) and delete that successor instead
4. kth_largest(k) at a node: let r = size(node.right). If k <= r, go right;
   if k == r + 1, the node is the answer; otherwise go left with
   k - r - 1

Example 1:
Input: insert 50, 30, 70, 20, 40, 60, 80; kth_largest(1); kth_largest(3);
       kth_largest(7)
Output: 80, 60, 20

Example 2:
Input: (same keys) delete(70); kth_largest(2); insert(30); size()
Output: 60, then insert returns False, size() -> 6
"""

from typing import Optional


class OrderStatisticBST:
    def __init__(self):
        """
        Initializes an empty set.
        """
        # TODO: Initialize the root (and define a node type with a size field)
        pass

    def insert(self, key: int) -> bool:
        """
        Adds key to the set.

        Args:
            key: Integer key

        Returns:
            True if key was added, False if it was already present

        Time Complexity: O(h)
        Space Complexity: O(1) iterative, O(h) recursive
        """
        # TODO: Implement insert that maintains subtree sizes
        pass

    def delete(self, key: int) -> bool:
        """
        Removes key from the set.

        Args:
            key: Integer key

        Returns:
            True if key was present and removed, False otherwise

        Time Complexity: O(h)
        Space Complexity: O(1) iterative, O(h) recursive
        """
        # TODO: Implement delete that maintains subtree sizes
        pass

    def kth_largest(self, k: int) -> Optional[int]:
        """
        Returns the kth largest key using subtree sizes.

        Args:
            k: 1-indexed rank from the largest

        Returns:
            The kth largest key, or None if k is out of range

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        # TODO: Implement size-guided descent
        pass

    def size(self) -> int:
        """
        Returns the number of keys in the set.

        Returns:
            Number of keys

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement size
        pass


def test_order_statistic_bst():
    """Test cases for the size-augmented BST"""

    # Test case 1: Basic ranks
    s = OrderStatisticBST()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        assert s.insert(key) is True
    assert s.kth_largest(1) == 80
    assert s.kth_largest(3) == 60
    assert s.kth_largest(7) == 20
    print("✓ Test 1 passed: kth_largest on 7 keys")

    # Test case 2: Delete a node with two children, duplicate insert
    assert s.delete(70) is True
    assert s.kth_largest(2) == 60
    assert s.insert(30) is False
    assert s.size() == 6
    assert [s.kth_largest(k) for k in range(1, 7)] == [80, 60, 50, 40, 30, 20]
    print("✓ Test 2 passed: Delete and duplicate insert")

    # Test case 3: Out-of-range ranks and missing deletes
    assert s.kth_largest(0) is None
    assert s.kth_largest(7) is None
    assert s.delete(999) is False
    assert s.size() == 6
    print("✓ Test 3 passed: Out of range / missing key")

    # Test case 4: Empty set
    e = OrderStatisticBST()
    assert e.size() == 0
    assert e.kth_largest(1) is None
    assert e.delete(1) is False
    print("✓ Test 4 passed: Empty set")

    # Test case 5: Delete the root repeatedly until empty
    s = OrderStatisticBST()
    for key in [5, 3, 8, 1, 4, 7, 9]:
        s.insert(key)
    for expected_max in [9, 8, 7, 5, 4, 3, 1]:
        assert s.kth_largest(1) == expected_max
        assert s.delete(expected_max) is True
    assert s.size() == 0
    print("✓ Test 5 passed: Delete maximums until empty")

    # Test case 6: Negative keys, skewed insert order
    s = OrderStatisticBST()
    for key in range(-1, -11, -1):
        s.insert(key)
    assert s.kth_largest(1) == -1
    assert s.kth_largest(10) == -10
    s.delete(-5)
    assert s.kth_largest(5) == -6
    print("✓ Test 6 passed: Negative keys, skewed tree")

    # Test case 7: Long scripted sequence against a sorted list
    s = OrderStatisticBST()
    model = []
    for i in range(600):
        key = (i * 7919) % 97 - 48
        if i % 3 == 2:
            assert s.delete(key) is (key in model)
            if key in model:
                model.remove(key)
        else:
            assert s.insert(key) is (key not in model)
            if key not in model:
                model.append(key)
        desc = sorted(model, reverse=True)
        assert s.size() == len(desc)
        for k in (1, len(desc) // 2, len(desc)):
            if 1 <= k <= len(desc):
                assert s.kth_largest(k) == desc[k - 1]
    print("✓ Test 7 passed: 600 mixed operations match a sorted list")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_order_statistic_bst()
