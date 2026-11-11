"""
EPI 7.1 Variant - Merge Two Sorted Doubly Linked Lists

Problem:
Given two doubly linked lists, each sorted in ascending order, merge them
into a single sorted doubly linked list. Reuse the existing nodes: only
the prev and next fields may change. In the result, the head's prev must be
None, the tail's next must be None, and every node's prev must point back
to its predecessor.

Constraints:
- 0 <= length of each list <= 10^4
- O(n + m) time, O(1) extra space

How it works:
1. Create a dummy head and a tail pointer to it
2. While both lists are non-empty, take the smaller head node, link it
   after tail (set tail.next and node.prev), and advance
3. Attach the remaining list and fix its first node's prev
4. Detach the dummy: set the real head's prev to None and return it

Example 1:
Input: L1 = 2 <-> 5 <-> 7, L2 = 3 <-> 11
Output: 2 <-> 3 <-> 5 <-> 7 <-> 11

Example 2:
Input: L1 = (empty), L2 = 1 <-> 2
Output: 1 <-> 2
"""

from typing import List, Optional


class DoublyListNode:
    def __init__(
        self,
        data: int = 0,
        prev: "Optional[DoublyListNode]" = None,
        next: "Optional[DoublyListNode]" = None,
    ):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def merge_two_sorted_doubly_lists(
        self, L1: Optional[DoublyListNode], L2: Optional[DoublyListNode]
    ) -> Optional[DoublyListNode]:
        """
        Merges two sorted doubly linked lists into one sorted list.

        Args:
            L1: Head of the first sorted doubly linked list
            L2: Head of the second sorted doubly linked list

        Returns:
            Head of the merged sorted doubly linked list

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement merge of two sorted doubly linked lists
        pass


def build_doubly_list(values: List[int]) -> Optional[DoublyListNode]:
    """Builds a doubly linked list from a Python list."""
    head: Optional[DoublyListNode] = None
    tail: Optional[DoublyListNode] = None
    for v in values:
        node = DoublyListNode(v, tail)
        if tail:
            tail.next = node
        else:
            head = node
        tail = node
    return head


def to_list(head: Optional[DoublyListNode]) -> List[int]:
    """Converts a doubly linked list to a Python list, checking prev links."""
    result = []
    prev = None
    while head:
        assert head.prev is prev, "prev pointer is inconsistent"
        result.append(head.data)
        prev, head = head, head.next
    return result


def test_merge_two_sorted_doubly_lists():
    """Test cases for merging two sorted doubly linked lists"""
    solution = Solution()

    # Test case 1: Interleaved lists
    merged1 = solution.merge_two_sorted_doubly_lists(
        build_doubly_list([2, 5, 7]), build_doubly_list([3, 11])
    )
    assert to_list(merged1) == [2, 3, 5, 7, 11]
    print("✓ Test 1 passed: [2, 5, 7] + [3, 11] -> [2, 3, 5, 7, 11]")

    # Test case 2: First list empty
    merged2 = solution.merge_two_sorted_doubly_lists(None, build_doubly_list([1, 2]))
    assert to_list(merged2) == [1, 2]
    print("✓ Test 2 passed: First list empty")

    # Test case 3: Both lists empty
    assert solution.merge_two_sorted_doubly_lists(None, None) is None
    print("✓ Test 3 passed: Both lists empty")

    # Test case 4: Duplicates across lists
    merged4 = solution.merge_two_sorted_doubly_lists(
        build_doubly_list([1, 3, 3]), build_doubly_list([1, 2, 3])
    )
    assert to_list(merged4) == [1, 1, 2, 3, 3, 3]
    print("✓ Test 4 passed: Duplicates handled correctly")

    # Test case 5: One list entirely before the other
    merged5 = solution.merge_two_sorted_doubly_lists(
        build_doubly_list([5, 6]), build_doubly_list([1, 2, 3])
    )
    assert to_list(merged5) == [1, 2, 3, 5, 6]
    print("✓ Test 5 passed: Non-overlapping ranges, prev links consistent")

    # Test case 6: Nodes are reused, not copied
    a, b = build_doubly_list([2]), build_doubly_list([1])
    merged6 = solution.merge_two_sorted_doubly_lists(a, b)
    assert merged6 is b and merged6.next is a and a.prev is b and b.prev is None
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_two_sorted_doubly_lists()
