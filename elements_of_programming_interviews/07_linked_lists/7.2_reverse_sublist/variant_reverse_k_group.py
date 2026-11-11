"""
EPI 7.2 Variant - Reverse a List k Nodes at a Time

Problem:
Given a singly linked list and a nonnegative integer k, reverse the list
in consecutive groups of k nodes. If the number of nodes n is not a
multiple of k, the final n mod k nodes stay in their original order.
Rearrange nodes by changing next pointers; don't change any node's data.

Constraints:
- 0 <= length of the list <= 10^5
- k >= 0; for k <= 1 the list is unchanged
- O(n) time, O(1) extra space

How it works:
1. Put a dummy node before the head; keep a pointer to the node before the
   current group
2. Check that at least k nodes remain; if not, stop
3. Reverse the next k nodes (as in the sublist reversal) and reconnect
   them between the node before the group and the node after it
4. The group's original first node is now its last; continue from there

Example 1:
Input: L = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 2 -> 1 -> 4 -> 3 -> 5
Explanation: The last node is left alone because 5 mod 2 = 1

Example 2:
Input: L = 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output: 3 -> 2 -> 1 -> 4 -> 5
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def reverse_k_group(self, L: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses the list k nodes at a time.

        Args:
            L: Head of the list
            k: Group size (nonnegative)

        Returns:
            Head of the updated list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement k-group reversal
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


def test_reverse_k_group():
    """Test cases for reversing k nodes at a time"""
    solution = Solution()

    # Test case 1: k = 2 with a leftover node
    result1 = solution.reverse_k_group(build_list([1, 2, 3, 4, 5]), 2)
    assert to_list(result1) == [2, 1, 4, 3, 5]
    print("✓ Test 1 passed: k=2 -> [2, 1, 4, 3, 5]")

    # Test case 2: k = 3 with two leftover nodes
    result2 = solution.reverse_k_group(build_list([1, 2, 3, 4, 5]), 3)
    assert to_list(result2) == [3, 2, 1, 4, 5]
    print("✓ Test 2 passed: k=3 -> [3, 2, 1, 4, 5]")

    # Test case 3: Length is a multiple of k
    result3 = solution.reverse_k_group(build_list([1, 2, 3, 4, 5, 6]), 3)
    assert to_list(result3) == [3, 2, 1, 6, 5, 4]
    print("✓ Test 3 passed: k=3 on six nodes")

    # Test case 4: k = 1 and k = 0 leave the list unchanged
    assert to_list(solution.reverse_k_group(build_list([1, 2, 3]), 1)) == [1, 2, 3]
    assert to_list(solution.reverse_k_group(build_list([1, 2, 3]), 0)) == [1, 2, 3]
    print("✓ Test 4 passed: k=1 and k=0 are no-ops")

    # Test case 5: k larger than the list
    result5 = solution.reverse_k_group(build_list([1, 2]), 3)
    assert to_list(result5) == [1, 2]
    print("✓ Test 5 passed: k larger than list length")

    # Test case 6: k equals the length; nodes reused
    head = build_list([7, 8, 9])
    nodes = [head, head.next, head.next.next]
    result6 = solution.reverse_k_group(head, 3)
    assert to_list(result6) == [9, 8, 7] and result6 is nodes[2] and nodes[0].next is None
    print("✓ Test 6 passed: k equals length, nodes reused")

    # Test case 7: Empty list
    assert solution.reverse_k_group(None, 2) is None
    print("✓ Test 7 passed: Empty list")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_k_group()
