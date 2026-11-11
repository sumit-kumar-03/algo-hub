"""
EPI 7.10 - Implement Even-Odd Merge

Problem:
Number the nodes of a singly linked list starting from 0. Rearrange the
list so that all even-numbered nodes come first (in their original order),
followed by all odd-numbered nodes (in their original order). Reuse the
existing nodes and return the new head.

Constraints:
- 0 <= length of the list <= 10^5
- O(n) time, O(1) extra space

How it works:
1. Keep two dummy heads, one for the even list and one for the odd list,
   each with its own tail pointer
2. Walk the original list, appending nodes alternately to the even tail
   and the odd tail
3. Terminate the odd list with None and link the even tail to the first
   odd node
4. Return the head of the even list

Example 1:
Input: L = 0 -> 1 -> 2 -> 3 -> 4
Output: 0 -> 2 -> 4 -> 1 -> 3

Example 2:
Input: L = 10 -> 20
Output: 10 -> 20
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def even_odd_merge(self, L: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reorders the list so even-indexed nodes precede odd-indexed nodes.

        Args:
            L: Head of the list

        Returns:
            Head of the reordered list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement even-odd merge
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


def test_even_odd_merge():
    """Test cases for even-odd merge"""
    solution = Solution()

    # Test case 1: Odd number of nodes
    result1 = solution.even_odd_merge(build_list([0, 1, 2, 3, 4]))
    assert to_list(result1) == [0, 2, 4, 1, 3]
    print("✓ Test 1 passed: [0..4] -> [0, 2, 4, 1, 3]")

    # Test case 2: Even number of nodes
    result2 = solution.even_odd_merge(build_list([5, 6, 7, 8, 9, 10]))
    assert to_list(result2) == [5, 7, 9, 6, 8, 10]
    print("✓ Test 2 passed: Six nodes")

    # Test case 3: Empty list
    assert solution.even_odd_merge(None) is None
    print("✓ Test 3 passed: Empty list")

    # Test case 4: Single node
    assert to_list(solution.even_odd_merge(build_list([1]))) == [1]
    print("✓ Test 4 passed: Single node")

    # Test case 5: Two nodes stay in place
    assert to_list(solution.even_odd_merge(build_list([10, 20]))) == [10, 20]
    print("✓ Test 5 passed: Two nodes")

    # Test case 6: Nodes are reused, not copied
    head = build_list([1, 2, 3])
    n0, n1, n2 = head, head.next, head.next.next
    result6 = solution.even_odd_merge(head)
    assert result6 is n0 and n0.next is n2 and n2.next is n1 and n1.next is None
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_even_odd_merge()
