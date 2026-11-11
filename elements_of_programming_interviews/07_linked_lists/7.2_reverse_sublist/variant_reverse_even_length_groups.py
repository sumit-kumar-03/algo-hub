"""
EPI 7.2 Extra Variant - Reverse Groups of Even Length
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Reversing a sublist in place between a node before it and a
node after it, done repeatedly while walking the list.

Problem:
Split a singly linked list into consecutive groups whose intended sizes
are 1, 2, 3, 4, ...: the first node forms group 1, the next two nodes
group 2, the next three group 3, and so on. The last group may be shorter
than intended because the list runs out. Reverse every group whose actual
length is even, leave odd-length groups alone, and return the head.
Change only next pointers.

Constraints:
- 0 <= length of the list <= 10^5
- O(n) time, O(1) extra space

How it works:
1. Keep a pointer prev to the node just before the current group, and
   the intended size of the current group
2. Count the actual group length by walking at most that many nodes
   (the final group can be shorter)
3. If the actual length is even, reverse exactly that many nodes after
   prev and reconnect both ends, as in reversing a sublist
4. Move prev to the group's last node (which, after a reversal, is the
   group's original first node) and grow the intended size by one

Example 1:
Input: L = 5 -> 2 -> 6 -> 3 -> 9 -> 1 -> 7 -> 3 -> 8 -> 4
Output: 5 -> 6 -> 2 -> 3 -> 9 -> 1 -> 4 -> 8 -> 3 -> 7
Explanation: Groups [5], [2, 6], [3, 9, 1], [7, 3, 8, 4]; the groups of
length 2 and 4 are reversed

Example 2:
Input: L = 1 -> 1 -> 0 -> 6 -> 5
Output: 1 -> 0 -> 1 -> 5 -> 6
Explanation: Groups [1], [1, 0], [6, 5]; the last group was meant to have
three nodes but has two, so it is reversed
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def reverse_even_length_groups(
        self, L: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Reverses every group of even actual length (group sizes 1, 2, 3, ...).

        Args:
            L: Head of the list

        Returns:
            Head of the updated list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement even-length group reversal
        pass


def build_list(values: List[int]) -> Optional[ListNode]:
    """Builds a linked list from a Python list."""
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode], limit: int = 10**6) -> List[int]:
    """Converts a linked list back to a Python list (stops on a cycle)."""
    result = []
    while head and len(result) < limit:
        result.append(head.data)
        head = head.next
    return result


def test_reverse_even_length_groups():
    """Test cases for reversing even-length groups"""
    solution = Solution()

    # Test case 1: Classic example, complete last group
    result1 = solution.reverse_even_length_groups(
        build_list([5, 2, 6, 3, 9, 1, 7, 3, 8, 4])
    )
    assert to_list(result1, 20) == [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]
    print("✓ Test 1 passed: Groups of 2 and 4 reversed")

    # Test case 2: Short last group of even length is reversed
    result2 = solution.reverse_even_length_groups(build_list([1, 1, 0, 6, 5]))
    assert to_list(result2, 20) == [1, 0, 1, 5, 6]
    print("✓ Test 2 passed: Short even last group reversed")

    # Test case 3: Short last group of odd length is kept
    result3 = solution.reverse_even_length_groups(build_list([1, 1, 0, 6]))
    assert to_list(result3, 20) == [1, 0, 1, 6]
    print("✓ Test 3 passed: Short odd last group kept")

    # Test case 4: Empty, one and two nodes
    assert solution.reverse_even_length_groups(None) is None
    assert to_list(solution.reverse_even_length_groups(build_list([8]))) == [8]
    assert to_list(solution.reverse_even_length_groups(build_list([2, 1]))) == [2, 1]
    print("✓ Test 4 passed: Tiny lists")

    # Test case 5: Several complete groups plus a partial one
    values = list(range(1, 14))  # groups [1] [2,3] [4,5,6] [7..10] [11,12,13]
    result5 = solution.reverse_even_length_groups(build_list(values))
    assert to_list(result5, 30) == [1, 3, 2, 4, 5, 6, 10, 9, 8, 7, 11, 12, 13]
    print("✓ Test 5 passed: Partial fifth group of odd length")

    # Test case 6: Nodes reused, tail terminated
    head = build_list([1, 2, 3])
    n1, n2, n3 = head, head.next, head.next.next
    result6 = solution.reverse_even_length_groups(head)
    assert result6 is n1 and n1.next is n3 and n3.next is n2 and n2.next is None
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_reverse_even_length_groups()
