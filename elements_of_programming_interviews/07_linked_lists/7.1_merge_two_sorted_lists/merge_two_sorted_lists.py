"""
EPI 7.1 - Merge Two Sorted Lists

Problem:
Given two singly linked lists, each sorted in ascending order, merge them into
a single sorted list. Reuse the existing nodes: change next pointers instead
of allocating new nodes (a dummy head node is fine).

Constraints:
- 0 <= length of each list <= 10^4
- O(n + m) time, O(1) extra space

How it works:
1. Create a dummy head and a tail pointer to it
2. While both lists are non-empty:
   - Attach the smaller head node to tail and advance that list
   - Advance tail
3. Attach whatever remains of the non-empty list
4. Return dummy.next

Example 1:
Input: L1 = 2 -> 5 -> 7, L2 = 3 -> 11
Output: 2 -> 3 -> 5 -> 7 -> 11

Example 2:
Input: L1 = (empty), L2 = 1 -> 2
Output: 1 -> 2
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def merge_two_sorted_lists(
        self, L1: Optional[ListNode], L2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted list.

        Args:
            L1: Head of the first sorted list
            L2: Head of the second sorted list

        Returns:
            Head of the merged sorted list

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement merge of two sorted lists
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


def test_merge_two_sorted_lists():
    """Test cases for merging two sorted linked lists"""
    solution = Solution()

    # Test case 1: Interleaved lists
    merged1 = solution.merge_two_sorted_lists(build_list([2, 5, 7]), build_list([3, 11]))
    assert to_list(merged1) == [2, 3, 5, 7, 11]
    print("✓ Test 1 passed: [2, 5, 7] + [3, 11] -> [2, 3, 5, 7, 11]")

    # Test case 2: First list empty
    merged2 = solution.merge_two_sorted_lists(None, build_list([1, 2]))
    assert to_list(merged2) == [1, 2]
    print("✓ Test 2 passed: First list empty")

    # Test case 3: Second list empty
    merged3 = solution.merge_two_sorted_lists(build_list([4, 9]), None)
    assert to_list(merged3) == [4, 9]
    print("✓ Test 3 passed: Second list empty")

    # Test case 4: Duplicates across lists
    merged4 = solution.merge_two_sorted_lists(build_list([1, 3, 3]), build_list([1, 2, 3]))
    assert to_list(merged4) == [1, 1, 2, 3, 3, 3]
    print("✓ Test 4 passed: Duplicates handled correctly")

    # Test case 5: One list entirely before the other
    merged5 = solution.merge_two_sorted_lists(build_list([5, 6]), build_list([1, 2, 3]))
    assert to_list(merged5) == [1, 2, 3, 5, 6]
    print("✓ Test 5 passed: Non-overlapping ranges")

    # Test case 6: Nodes are reused, not copied
    a, b = build_list([1]), build_list([2])
    merged6 = solution.merge_two_sorted_lists(a, b)
    assert merged6 is a and merged6.next is b
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_two_sorted_lists()
