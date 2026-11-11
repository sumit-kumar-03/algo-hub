"""
EPI 7.2 - Reverse a Single Sublist

Problem:
Given a singly linked list and two positions start and finish (1-based,
the head is position 1), reverse the order of the nodes from position
start through position finish, inclusive, and return the head of the
resulting list. Don't allocate new list nodes (a dummy head is fine).

Constraints:
- 1 <= start <= finish <= length of the list
- O(finish) time, O(1) extra space

How it works:
1. Put a dummy node before the head so start = 1 needs no special case
2. Walk to the node just before position start (call it sublist_head)
3. Repeat finish - start times: take the node after the current sublist
   iterator and move it to the front of the sublist, right after
   sublist_head
4. Return dummy.next

Example 1:
Input: L = 11 -> 3 -> 5 -> 7 -> 2, start = 2, finish = 4
Output: 11 -> 7 -> 5 -> 3 -> 2

Example 2:
Input: L = 1 -> 2 -> 3, start = 1, finish = 3
Output: 3 -> 2 -> 1
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def reverse_sublist(
        self, L: Optional[ListNode], start: int, finish: int
    ) -> Optional[ListNode]:
        """
        Reverses the nodes from position start to finish, inclusive.

        Args:
            L: Head of the list
            start: 1-based position of the first node to reverse
            finish: 1-based position of the last node to reverse

        Returns:
            Head of the updated list

        Time Complexity: O(finish)
        Space Complexity: O(1)
        """
        # TODO: Implement sublist reversal
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


def test_reverse_sublist():
    """Test cases for reversing a sublist"""
    solution = Solution()

    # Test case 1: Book example, middle sublist
    result1 = solution.reverse_sublist(build_list([11, 3, 5, 7, 2]), 2, 4)
    assert to_list(result1) == [11, 7, 5, 3, 2]
    print("✓ Test 1 passed: Reverse positions 2..4")

    # Test case 2: Whole list
    result2 = solution.reverse_sublist(build_list([1, 2, 3]), 1, 3)
    assert to_list(result2) == [3, 2, 1]
    print("✓ Test 2 passed: Reverse entire list")

    # Test case 3: start == finish leaves the list unchanged
    result3 = solution.reverse_sublist(build_list([1, 2, 3]), 2, 2)
    assert to_list(result3) == [1, 2, 3]
    print("✓ Test 3 passed: Single-node sublist")

    # Test case 4: Sublist at the head
    result4 = solution.reverse_sublist(build_list([1, 2, 3, 4, 5]), 1, 2)
    assert to_list(result4) == [2, 1, 3, 4, 5]
    print("✓ Test 4 passed: Sublist starting at head")

    # Test case 5: Sublist at the tail
    result5 = solution.reverse_sublist(build_list([1, 2, 3, 4, 5]), 3, 5)
    assert to_list(result5) == [1, 2, 5, 4, 3]
    print("✓ Test 5 passed: Sublist ending at tail")

    # Test case 6: Nodes are reused, not copied
    head = build_list([1, 2])
    first, second = head, head.next
    result6 = solution.reverse_sublist(head, 1, 2)
    assert result6 is second and result6.next is first and first.next is None
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_sublist()
