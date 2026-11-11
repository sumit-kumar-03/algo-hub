"""
EPI 7.11 - Test Whether a Singly Linked List Is Palindromic

Problem:
Determine whether the sequence of values stored in a singly linked list
reads the same forward and backward.

Constraints:
- 0 <= length of the list <= 10^5
- O(n) time, O(1) extra space (you may temporarily modify the list)

How it works:
1. Use slow and fast pointers to find the start of the second half
2. Reverse the second half in place
3. Compare the first half with the reversed second half node by node
4. (Optionally) reverse the second half again to restore the list

Example 1:
Input: L = 1 -> 2 -> 3 -> 2 -> 1
Output: True

Example 2:
Input: L = 1 -> 2 -> 3
Output: False
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def is_linked_list_a_palindrome(self, L: Optional[ListNode]) -> bool:
        """
        Tests whether the list's values form a palindrome.

        Args:
            L: Head of the list

        Returns:
            True if the list is palindromic, False otherwise

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement palindrome check by reversing the second half
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


def test_is_linked_list_a_palindrome():
    """Test cases for palindromic linked lists"""
    solution = Solution()

    # Test case 1: Odd-length palindrome
    assert solution.is_linked_list_a_palindrome(build_list([1, 2, 3, 2, 1])) is True
    print("✓ Test 1 passed: [1, 2, 3, 2, 1] is palindromic")

    # Test case 2: Even-length palindrome
    assert solution.is_linked_list_a_palindrome(build_list([4, 7, 7, 4])) is True
    print("✓ Test 2 passed: [4, 7, 7, 4] is palindromic")

    # Test case 3: Not a palindrome
    assert solution.is_linked_list_a_palindrome(build_list([1, 2, 3])) is False
    print("✓ Test 3 passed: [1, 2, 3] is not palindromic")

    # Test case 4: Empty and single-node lists
    assert solution.is_linked_list_a_palindrome(None) is True
    assert solution.is_linked_list_a_palindrome(build_list([5])) is True
    print("✓ Test 4 passed: Empty and single-node lists are palindromic")

    # Test case 5: Mismatch near the middle only
    assert solution.is_linked_list_a_palindrome(build_list([1, 2, 3, 4, 2, 1])) is False
    print("✓ Test 5 passed: [1, 2, 3, 4, 2, 1] is not palindromic")

    # Test case 6: Two nodes
    assert solution.is_linked_list_a_palindrome(build_list([1, 2])) is False
    assert solution.is_linked_list_a_palindrome(build_list([3, 3])) is True
    print("✓ Test 6 passed: Two-node lists")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_is_linked_list_a_palindrome()
