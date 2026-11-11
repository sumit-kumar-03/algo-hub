"""
EPI 7.7 - Remove the kth Last Element From a List

Problem:
Given a singly linked list and an integer k, remove the kth node from the
end of the list (k = 1 is the tail) and return the head of the resulting
list. Use only a constant amount of extra storage; you may not compute
and store the length of the list up front.

Constraints:
- 1 <= k <= length of the list
- O(n) time, O(1) extra space

How it works:
1. Put a dummy node before the head
2. Advance a leading pointer k nodes into the list
3. Start a trailing pointer at the dummy and move both pointers together
   until the leading pointer falls off the end
4. The trailing pointer now sits just before the kth last node; unlink it
5. Return dummy.next

Example 1:
Input: L = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5

Example 2:
Input: L = 1 -> 2 -> 3, k = 3
Output: 2 -> 3
Explanation: The 3rd last node is the head
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def remove_kth_last(self, L: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Removes the kth last node of the list.

        Args:
            L: Head of the list (at least k nodes)
            k: 1-based position counted from the tail

        Returns:
            Head of the updated list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement removal with two pointers
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


def test_remove_kth_last():
    """Test cases for removing the kth last node"""
    solution = Solution()

    # Test case 1: Remove from the middle
    result1 = solution.remove_kth_last(build_list([1, 2, 3, 4, 5]), 2)
    assert to_list(result1) == [1, 2, 3, 5]
    print("✓ Test 1 passed: k=2 on [1..5] -> [1, 2, 3, 5]")

    # Test case 2: Remove the head
    result2 = solution.remove_kth_last(build_list([1, 2, 3]), 3)
    assert to_list(result2) == [2, 3]
    print("✓ Test 2 passed: Remove head")

    # Test case 3: Remove the tail
    result3 = solution.remove_kth_last(build_list([1, 2, 3]), 1)
    assert to_list(result3) == [1, 2]
    print("✓ Test 3 passed: Remove tail")

    # Test case 4: Single-node list becomes empty
    assert solution.remove_kth_last(build_list([9]), 1) is None
    print("✓ Test 4 passed: Single node removed -> empty list")

    # Test case 5: Remaining nodes are reused
    head = build_list([10, 20, 30, 40])
    third = head.next.next
    result5 = solution.remove_kth_last(head, 3)
    assert result5 is head and head.next is third and to_list(result5) == [10, 30, 40]
    print("✓ Test 5 passed: Nodes reused, 20 removed")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_remove_kth_last()
