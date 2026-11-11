"""
EPI 7.11 Variant - Test Whether a Doubly Linked List Is Palindromic

Problem:
Given pointers to both the head and the tail of a doubly linked list,
determine whether the sequence of values reads the same forward and
backward. Don't modify the list.

Constraints:
- 0 <= length of the list <= 10^5
- head and tail are both None for an empty list
- O(n) time, O(1) extra space

How it works:
1. Start one pointer at the head and one at the tail
2. While the pointers haven't met or crossed, compare their values and
   return False on a mismatch; move the head pointer forward (next) and
   the tail pointer backward (prev)
3. Stop when the pointers are the same node or the front pointer has just
   passed the back pointer; return True

Example 1:
Input: 1 <-> 2 <-> 2 <-> 1
Output: True

Example 2:
Input: 1 <-> 2 <-> 3
Output: False
"""

from typing import List, Optional, Tuple


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
    def is_doubly_list_palindromic(
        self, head: Optional[DoublyListNode], tail: Optional[DoublyListNode]
    ) -> bool:
        """
        Tests whether a doubly linked list's values form a palindrome.

        Args:
            head: First node of the list
            tail: Last node of the list

        Returns:
            True if the list is palindromic, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement two-pointer palindrome check
        pass


def build_doubly_list(
    values: List[int],
) -> Tuple[Optional[DoublyListNode], Optional[DoublyListNode]]:
    """Builds a doubly linked list and returns (head, tail)."""
    head: Optional[DoublyListNode] = None
    tail: Optional[DoublyListNode] = None
    for v in values:
        node = DoublyListNode(v, tail)
        if tail:
            tail.next = node
        else:
            head = node
        tail = node
    return head, tail


def test_is_doubly_list_palindromic():
    """Test cases for palindromic doubly linked lists"""
    solution = Solution()

    # Test case 1: Even-length palindrome
    assert solution.is_doubly_list_palindromic(*build_doubly_list([1, 2, 2, 1])) is True
    print("✓ Test 1 passed: [1, 2, 2, 1] is palindromic")

    # Test case 2: Odd-length palindrome
    assert solution.is_doubly_list_palindromic(*build_doubly_list([3, 1, 4, 1, 3])) is True
    print("✓ Test 2 passed: [3, 1, 4, 1, 3] is palindromic")

    # Test case 3: Not a palindrome
    assert solution.is_doubly_list_palindromic(*build_doubly_list([1, 2, 3])) is False
    print("✓ Test 3 passed: [1, 2, 3] is not palindromic")

    # Test case 4: Empty and single-node lists
    assert solution.is_doubly_list_palindromic(None, None) is True
    assert solution.is_doubly_list_palindromic(*build_doubly_list([8])) is True
    print("✓ Test 4 passed: Empty and single-node lists are palindromic")

    # Test case 5: Mismatch in the middle pair
    assert solution.is_doubly_list_palindromic(*build_doubly_list([1, 2, 3, 1])) is False
    print("✓ Test 5 passed: [1, 2, 3, 1] is not palindromic")

    # Test case 6: List is left unchanged
    head, tail = build_doubly_list([5, 6, 5])
    solution.is_doubly_list_palindromic(head, tail)
    values, node = [], head
    while node:
        values.append(node.data)
        node = node.next
    assert values == [5, 6, 5] and tail.prev is head.next
    print("✓ Test 6 passed: List not modified")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_doubly_list_palindromic()
