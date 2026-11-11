"""
EPI 7.1 Extra Variant - Difference of Two Sorted Lists
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Advancing two pointers through two sorted lists in step,
deciding at each comparison which side moves, while relinking nodes
behind a dummy head.

Problem:
Given two singly linked lists L1 and L2, each sorted in ascending order
(values may repeat), remove from L1 every node whose value occurs anywhere
in L2. Keep the remaining L1 nodes in order, including repeats of values
that are not in L2. Return the head of the updated L1. L2 must not be
changed.

Constraints:
- 0 <= length of each list <= 10^4
- O(n + m) time, O(1) extra space

How it works:
1. Put a dummy node before L1 and keep a tail pointer to the last kept
   node
2. Walk L1 with a pointer p and L2 with a pointer q
3. Advance q while q.data < p.data; then p is removed if q is not None
   and q.data == p.data, otherwise p is appended to tail
4. Because both lists are sorted, q never needs to move backward
5. Terminate the result with tail.next = None and return dummy.next

Example 1:
Input: L1 = 1 -> 2 -> 2 -> 4 -> 6, L2 = 2 -> 3 -> 6
Output: 1 -> 4

Example 2:
Input: L1 = 1 -> 1 -> 5, L2 = 2 -> 3
Output: 1 -> 1 -> 5
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def sorted_list_difference(
        self, L1: Optional[ListNode], L2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Removes from L1 every node whose value appears in L2.

        Args:
            L1: Head of the sorted list to filter
            L2: Head of the sorted list of values to remove (unchanged)

        Returns:
            Head of the filtered L1

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement sorted list difference
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


def test_sorted_list_difference():
    """Test cases for the difference of two sorted lists"""
    solution = Solution()

    # Test case 1: Repeated value removed entirely
    L2 = build_list([2, 3, 6])
    result1 = solution.sorted_list_difference(build_list([1, 2, 2, 4, 6]), L2)
    assert to_list(result1) == [1, 4]
    assert to_list(L2) == [2, 3, 6]
    print("✓ Test 1 passed: [1,2,2,4,6] - [2,3,6] -> [1,4]; L2 unchanged")

    # Test case 2: Nothing in common keeps repeats
    result2 = solution.sorted_list_difference(build_list([1, 1, 5]), build_list([2, 3]))
    assert to_list(result2) == [1, 1, 5]
    print("✓ Test 2 passed: No common values")

    # Test case 3: Empty lists
    assert solution.sorted_list_difference(None, build_list([1])) is None
    assert to_list(solution.sorted_list_difference(build_list([1, 2]), None)) == [1, 2]
    print("✓ Test 3 passed: Empty L1 or empty L2")

    # Test case 4: Everything removed, including the head
    result4 = solution.sorted_list_difference(build_list([3, 3, 3]), build_list([1, 3, 3]))
    assert result4 is None
    print("✓ Test 4 passed: All nodes removed")

    # Test case 5: Head and tail removed, middle kept
    result5 = solution.sorted_list_difference(
        build_list([-4, -1, 0, 8, 9]), build_list([-4, 2, 9, 10])
    )
    assert to_list(result5) == [-1, 0, 8]
    print("✓ Test 5 passed: Head and tail removed")

    # Test case 6: Kept nodes are the original nodes
    head = build_list([1, 2, 3])
    first, third = head, head.next.next
    result6 = solution.sorted_list_difference(head, build_list([2]))
    assert result6 is first and first.next is third and third.next is None
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_sorted_list_difference()
