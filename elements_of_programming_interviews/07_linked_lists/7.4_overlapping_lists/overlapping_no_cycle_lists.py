"""
EPI 7.4 - Test for Overlapping Lists (Lists Are Cycle-Free)

Problem:
Two cycle-free singly linked lists may share nodes: once they reach a
common node, they share every node after it. Determine whether the two
lists overlap, and if they do, return the first node they have in common.
Return None if they don't overlap.

Constraints:
- 0 <= length of each list <= 10^4
- Neither list has a cycle
- O(n) time, O(1) extra space

How it works:
1. Compute the length of each list
2. Advance the head of the longer list by the difference in lengths
3. Step both pointers forward together; the first node where they are the
   same object is the first common node (None if they reach the end)

Example 1:
Input: L1 = 1 -> 2 -> [7 -> 8], L2 = 9 -> [7 -> 8] (bracketed nodes shared)
Output: the shared node holding 7

Example 2:
Input: L1 = 1 -> 2, L2 = 3 -> 4
Output: None
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def overlapping_no_cycle_lists(
        self, L1: Optional[ListNode], L2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Finds the first node common to two cycle-free lists.

        Args:
            L1: Head of the first list
            L2: Head of the second list

        Returns:
            The first shared node, or None if the lists don't overlap

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement overlap detection for cycle-free lists
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


def attach(prefix: List[int], shared: Optional[ListNode]) -> Optional[ListNode]:
    """Builds a list from prefix values whose tail links to shared."""
    head = build_list(prefix)
    if head is None:
        return shared
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = shared
    return head


def test_overlapping_no_cycle_lists():
    """Test cases for overlapping cycle-free lists"""
    solution = Solution()

    # Test case 1: Lists merge in the middle
    shared1 = build_list([7, 8])
    L1, L2 = attach([1, 2], shared1), attach([9], shared1)
    assert solution.overlapping_no_cycle_lists(L1, L2) is shared1
    print("✓ Test 1 passed: Lists merge at node 7")

    # Test case 2: No overlap, even with equal values
    assert solution.overlapping_no_cycle_lists(build_list([1, 2]), build_list([1, 2])) is None
    print("✓ Test 2 passed: Separate lists with equal values -> None")

    # Test case 3: One list empty
    assert solution.overlapping_no_cycle_lists(None, build_list([1])) is None
    print("✓ Test 3 passed: Empty list -> None")

    # Test case 4: Same list passed twice
    L4 = build_list([4, 5, 6])
    assert solution.overlapping_no_cycle_lists(L4, L4) is L4
    print("✓ Test 4 passed: Identical lists overlap at the head")

    # Test case 5: Overlap only at the tail
    shared5 = build_list([99])
    L1, L2 = attach([1, 2, 3, 4], shared5), attach([5], shared5)
    assert solution.overlapping_no_cycle_lists(L1, L2) is shared5
    print("✓ Test 5 passed: Overlap only at the last node")

    # Test case 6: One list is a suffix of the other
    L6 = build_list([1, 2, 3, 4])
    suffix = L6.next.next
    assert solution.overlapping_no_cycle_lists(suffix, L6) is suffix
    assert solution.overlapping_no_cycle_lists(L6, suffix) is suffix
    print("✓ Test 6 passed: Suffix overlap, either argument order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_overlapping_no_cycle_lists()
