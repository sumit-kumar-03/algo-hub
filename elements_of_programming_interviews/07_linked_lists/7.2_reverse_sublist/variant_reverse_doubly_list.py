"""
EPI 7.2 Extra Variant - Reverse a Doubly Linked List
(Practice problem, not in the book. Difficulty: Easy)
Builds on: In-place pointer reversal, now with two link fields per node.

Problem:
Reverse a doubly linked list in place and return the new head. After the
reversal every node's next must point to its new successor and its prev
to its new predecessor; the new head's prev and the new tail's next must
be None. Reuse the existing nodes and don't change any node's data.

Constraints:
- 0 <= length of the list <= 10^5
- O(n) time, O(1) extra space

How it works:
1. Walk the list with a pointer curr, starting at the head
2. At each node swap its prev and next fields
3. After the swap, the original next node is in curr.prev; remember curr
   as the latest node and move to curr.prev
4. The last node visited is the new head

Example 1:
Input: L = 1 <-> 2 <-> 3
Output: 3 <-> 2 <-> 1

Example 2:
Input: L = 7
Output: 7
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
    def reverse_doubly_list(
        self, L: Optional[DoublyListNode]
    ) -> Optional[DoublyListNode]:
        """
        Reverses a doubly linked list in place.

        Args:
            L: Head of the doubly linked list

        Returns:
            Head of the reversed list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement doubly linked list reversal
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


def test_reverse_doubly_list():
    """Test cases for reversing a doubly linked list"""
    solution = Solution()

    # Test case 1: Several nodes
    result1 = solution.reverse_doubly_list(build_doubly_list([1, 2, 3, 4]))
    assert to_list(result1) == [4, 3, 2, 1]
    print("✓ Test 1 passed: [1,2,3,4] -> [4,3,2,1]")

    # Test case 2: Empty list
    assert solution.reverse_doubly_list(None) is None
    print("✓ Test 2 passed: Empty list")

    # Test case 3: Single node keeps both links None
    single = build_doubly_list([7])
    result3 = solution.reverse_doubly_list(single)
    assert result3 is single and single.prev is None and single.next is None
    print("✓ Test 3 passed: Single node")

    # Test case 4: Two nodes
    result4 = solution.reverse_doubly_list(build_doubly_list([1, 2]))
    assert to_list(result4) == [2, 1]
    print("✓ Test 4 passed: Two nodes")

    # Test case 5: Duplicates
    result5 = solution.reverse_doubly_list(build_doubly_list([5, 5, 1, 5]))
    assert to_list(result5) == [5, 1, 5, 5]
    print("✓ Test 5 passed: Duplicate values")

    # Test case 6: Nodes reused, old head becomes the tail
    head = build_doubly_list([1, 2, 3])
    tail = head.next.next
    result6 = solution.reverse_doubly_list(head)
    assert result6 is tail and tail.prev is None
    assert head.next is None and head.prev is tail.next
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_doubly_list()
