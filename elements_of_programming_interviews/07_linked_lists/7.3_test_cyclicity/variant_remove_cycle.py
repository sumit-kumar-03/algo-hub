"""
EPI 7.3 Extra Variant - Remove the Cycle
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Locating the first node of a cycle with fast and slow
pointers.

Problem:
Given the head of a singly linked list that may contain a cycle, break the
cycle (if any) so that the list visits every one of its nodes exactly
once in the same order and then ends in None. That is, find the last node
of the cycle (the one whose next points back to the cycle's first node)
and set its next to None. Return the head.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(1) extra space
- Don't change any pointer other than the one that closes the cycle

How it works:
1. Detect the cycle with slow and fast pointers; if there is none, return
   the head unchanged
2. Find the first node of the cycle as in the main problem
3. Walk from the first node of the cycle around the loop until reaching
   the node whose next is the first node; that node closes the cycle
4. Set its next to None

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5, with 5.next pointing to node 3
Output: 1 -> 2 -> 3 -> 4 -> 5

Example 2:
Input: a single node whose next points to itself
Output: that node, with next None
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def remove_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Breaks the cycle of the list, if any, by clearing one next pointer.

        Args:
            head: Head of the list

        Returns:
            The same head, now of a cycle-free list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement cycle removal
        pass


def build_list_with_cycle(values: List[int], pos: int) -> List[ListNode]:
    """
    Builds a list from values and links the tail to the node at index pos
    (0-based). Use pos = -1 for no cycle. Returns the nodes in order.
    """
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes


def is_straight(head: Optional[ListNode], nodes: List[ListNode]) -> bool:
    """Returns True if head visits exactly nodes, in order, and then None."""
    for expected in nodes:
        if head is not expected:
            return False
        head = head.next
    return head is None


def test_remove_cycle():
    """Test cases for removing a cycle"""
    solution = Solution()

    # Test case 1: Cycle starting in the middle
    nodes1 = build_list_with_cycle([1, 2, 3, 4, 5], 2)
    assert is_straight(solution.remove_cycle(nodes1[0]), nodes1)
    print("✓ Test 1 passed: Cycle into the middle removed")

    # Test case 2: Empty list and cycle-free list
    assert solution.remove_cycle(None) is None
    nodes2 = build_list_with_cycle([1, 2, 3], -1)
    assert is_straight(solution.remove_cycle(nodes2[0]), nodes2)
    print("✓ Test 2 passed: Empty and cycle-free lists unchanged")

    # Test case 3: Self-loop on a single node
    nodes3 = build_list_with_cycle([7], 0)
    assert is_straight(solution.remove_cycle(nodes3[0]), nodes3)
    print("✓ Test 3 passed: Single-node self-loop")

    # Test case 4: Whole list is a cycle
    nodes4 = build_list_with_cycle([1, 2, 3, 4], 0)
    assert is_straight(solution.remove_cycle(nodes4[0]), nodes4)
    print("✓ Test 4 passed: Tail linked back to head")

    # Test case 5: Self-loop at the end of a long stem
    nodes5 = build_list_with_cycle(list(range(10)), 9)
    assert is_straight(solution.remove_cycle(nodes5[0]), nodes5)
    print("✓ Test 5 passed: Self-loop at the tail")

    # Test case 6: Many cycle/stem shapes
    for n in range(1, 25):
        for pos in range(-1, n):
            nodes = build_list_with_cycle(list(range(n)), pos)
            assert is_straight(solution.remove_cycle(nodes[0]), nodes)
    print("✓ Test 6 passed: Every stem/cycle split up to 24 nodes")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_remove_cycle()
