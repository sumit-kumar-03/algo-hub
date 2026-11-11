"""
EPI 7.1 Extra Variant - Merge Into Descending Order
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Walking two sorted lists in step and always taking the smaller
head node, but splicing nodes at the front of the result instead of the
back.

Problem:
Given two singly linked lists, each sorted in ascending order, merge them
into one list sorted in descending order. Do it in a single pass over the
lists, reusing the existing nodes, with O(1) extra space. (Merging
ascending and then reversing is two passes; avoid it.)

Constraints:
- 0 <= length of each list <= 10^4
- O(n + m) time with one pass, O(1) extra space

How it works:
1. Keep a result head, initially None
2. While either list is non-empty, detach the smaller head node (or the
   only one left) from its list
3. Push that node onto the front of the result: node.next = result,
   result = node. Smaller values are pushed first, so they end up last.
4. Return the result head

Example 1:
Input: L1 = 1 -> 4 -> 9, L2 = 2 -> 3
Output: 9 -> 4 -> 3 -> 2 -> 1

Example 2:
Input: L1 = (empty), L2 = 5 -> 6
Output: 6 -> 5
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def merge_descending(
        self, L1: Optional[ListNode], L2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two ascending lists into one descending list.

        Args:
            L1: Head of the first ascending list
            L2: Head of the second ascending list

        Returns:
            Head of the merged list in descending order

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement one-pass descending merge
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


def test_merge_descending():
    """Test cases for merging into descending order"""
    solution = Solution()

    # Test case 1: Interleaved lists
    merged1 = solution.merge_descending(build_list([1, 4, 9]), build_list([2, 3]))
    assert to_list(merged1) == [9, 4, 3, 2, 1]
    print("✓ Test 1 passed: [1,4,9] + [2,3] -> [9,4,3,2,1]")

    # Test case 2: Both empty
    assert solution.merge_descending(None, None) is None
    print("✓ Test 2 passed: Both lists empty")

    # Test case 3: One list empty, the other must still be reversed
    merged3 = solution.merge_descending(None, build_list([5, 6, 7]))
    assert to_list(merged3) == [7, 6, 5]
    print("✓ Test 3 passed: Single non-empty list reversed")

    # Test case 4: Duplicates and negatives
    merged4 = solution.merge_descending(build_list([-2, 0, 0]), build_list([-2, 3]))
    assert to_list(merged4) == [3, 0, 0, -2, -2]
    print("✓ Test 4 passed: Duplicates and negatives")

    # Test case 5: One list entirely below the other
    merged5 = solution.merge_descending(build_list([10, 11]), build_list([1, 2, 3]))
    assert to_list(merged5) == [11, 10, 3, 2, 1]
    print("✓ Test 5 passed: Non-overlapping ranges")

    # Test case 6: Nodes are reused; the largest node becomes the head
    a, b = build_list([1, 5]), build_list([3])
    big, small = a.next, a
    merged6 = solution.merge_descending(a, b)
    assert merged6 is big and big.next is b and b.next is small
    assert small.next is None
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_descending()
