"""
EPI 7.2 Variant - Reverse a Singly Linked List

Problem:
Reverse an entire singly linked list and return the new head. Use only
constant extra storage beyond the list itself, and reuse the existing
nodes.

Constraints:
- 0 <= length of the list <= 10^5
- O(n) time, O(1) extra space

How it works:
1. Keep two pointers: prev (initially None) and curr (initially the head)
2. While curr is not None: save curr.next, point curr.next at prev, then
   advance prev to curr and curr to the saved node
3. prev is the new head

Example 1:
Input: L = 2 -> 3 -> 5 -> 7 -> 11
Output: 11 -> 7 -> 5 -> 3 -> 2

Example 2:
Input: L = (empty)
Output: (empty)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def reverse_linked_list(self, L: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in place.

        Args:
            L: Head of the list

        Returns:
            Head of the reversed list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place list reversal
        pass


def build_list(values: List[int]) -> Optional[ListNode]:
    """Builds a linked list from a Python list."""
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a linked list back to a Python list."""
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result


def test_reverse_linked_list():
    """Test cases for reversing a linked list"""
    solution = Solution()

    # Test case 1: Several nodes
    result1 = solution.reverse_linked_list(build_list([2, 3, 5, 7, 11]))
    assert to_list(result1) == [11, 7, 5, 3, 2]
    print("✓ Test 1 passed: [2, 3, 5, 7, 11] -> [11, 7, 5, 3, 2]")

    # Test case 2: Empty list
    assert solution.reverse_linked_list(None) is None
    print("✓ Test 2 passed: Empty list")

    # Test case 3: Single node
    result3 = solution.reverse_linked_list(build_list([42]))
    assert to_list(result3) == [42]
    print("✓ Test 3 passed: Single node")

    # Test case 4: Two nodes
    result4 = solution.reverse_linked_list(build_list([1, 2]))
    assert to_list(result4) == [2, 1]
    print("✓ Test 4 passed: Two nodes")

    # Test case 5: Nodes are reused and the old head becomes the tail
    head = build_list([1, 2, 3])
    tail = head.next.next
    result5 = solution.reverse_linked_list(head)
    assert result5 is tail and head.next is None
    print("✓ Test 5 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_linked_list()
