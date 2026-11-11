"""
EPI 7.2 Extra Variant - Fold a List Into Front-Back Order
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Reversing part of a list in place (here, its second half),
then relinking nodes.

Problem:
Given a singly linked list L0 -> L1 -> ... -> Ln, rearrange its nodes into
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ..., alternating between the front
and the back. Change only next pointers, not node data, and use O(1)
extra space.

Constraints:
- 0 <= length of the list <= 10^5
- O(n) time, O(1) extra space

How it works:
1. Find the middle with a slow and a fast pointer
2. Cut the list after the middle and reverse the second half in place
3. Interleave the two halves: take a node from the first half, then one
   from the reversed second half, and so on
4. The first half is never shorter, so it supplies the last node when n
   is odd

Example 1:
Input: L = 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3

Example 2:
Input: L = 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def reorder_list(self, L: Optional[ListNode]) -> None:
        """
        Rearranges the list in place into front-back alternating order.

        Args:
            L: Head of the list (the head stays the head)

        Returns:
            None; the list is relinked in place

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place reordering
        pass


def build_list(values: List[int]) -> Optional[ListNode]:
    """Builds a linked list from a Python list."""
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode], limit: int = 10**6) -> List[int]:
    """Converts a linked list back to a Python list (stops on a cycle)."""
    result = []
    while head and len(result) < limit:
        result.append(head.data)
        head = head.next
    return result


def test_reorder_list():
    """Test cases for front-back reordering"""
    solution = Solution()

    # Test case 1: Even length
    head1 = build_list([1, 2, 3, 4])
    solution.reorder_list(head1)
    assert to_list(head1, 10) == [1, 4, 2, 3]
    print("✓ Test 1 passed: [1,2,3,4] -> [1,4,2,3]")

    # Test case 2: Odd length
    head2 = build_list([1, 2, 3, 4, 5])
    solution.reorder_list(head2)
    assert to_list(head2, 10) == [1, 5, 2, 4, 3]
    print("✓ Test 2 passed: [1,2,3,4,5] -> [1,5,2,4,3]")

    # Test case 3: Empty list and single node
    solution.reorder_list(None)
    head3 = build_list([9])
    solution.reorder_list(head3)
    assert to_list(head3, 10) == [9]
    print("✓ Test 3 passed: Empty list and single node")

    # Test case 4: Two and three nodes
    head4 = build_list([1, 2])
    solution.reorder_list(head4)
    head4b = build_list([1, 2, 3])
    solution.reorder_list(head4b)
    assert to_list(head4, 10) == [1, 2] and to_list(head4b, 10) == [1, 3, 2]
    print("✓ Test 4 passed: Two and three nodes")

    # Test case 5: Longer list with duplicates
    head5 = build_list([5, 1, 5, 2, 5, 3])
    solution.reorder_list(head5)
    assert to_list(head5, 20) == [5, 3, 1, 5, 5, 2]
    print("✓ Test 5 passed: Duplicates")

    # Test case 6: Nodes reused, tail terminated
    head6 = build_list(list(range(7)))
    nodes = []
    node = head6
    while node:
        nodes.append(node)
        node = node.next
    solution.reorder_list(head6)
    order = [0, 6, 1, 5, 2, 4, 3]
    node = head6
    for idx in order:
        assert node is nodes[idx]
        node = node.next
    assert node is None
    print("✓ Test 6 passed: Original nodes reused, list terminated")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reorder_list()
