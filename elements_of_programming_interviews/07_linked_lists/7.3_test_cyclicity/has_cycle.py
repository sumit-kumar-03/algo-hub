"""
EPI 7.3 - Test for Cyclicity

Problem:
A singly linked list normally ends in None, but a node's next field may
instead point back to an earlier node, creating a cycle. Given the head of
a list (whose length is unknown), return None if the list has no cycle, or
the first node of the cycle if it has one. Don't modify the list.

Constraints:
- 0 <= number of nodes <= 10^4
- O(n) time, O(1) extra space

How it works:
1. Advance a slow pointer one step and a fast pointer two steps at a time;
   if the fast pointer reaches the end there is no cycle
2. If they meet, the list has a cycle; walk around it from the meeting
   point to count its length C
3. Start two pointers at the head, advance one of them C steps, then move
   both one step at a time; they meet at the start of the cycle

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5, with 5.next pointing to node 3
Output: the node holding 3

Example 2:
Input: 1 -> 2 -> 3
Output: None
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the first node of a cycle in a singly linked list.

        Args:
            head: Head of the list

        Returns:
            The first node on the cycle, or None if the list is cycle-free

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement cycle detection with fast and slow pointers
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


def test_has_cycle():
    """Test cases for cycle detection"""
    solution = Solution()

    # Test case 1: No cycle
    nodes1 = build_list_with_cycle([1, 2, 3], -1)
    assert solution.has_cycle(nodes1[0]) is None
    print("✓ Test 1 passed: Cycle-free list -> None")

    # Test case 2: Empty list
    assert solution.has_cycle(None) is None
    print("✓ Test 2 passed: Empty list -> None")

    # Test case 3: Cycle starting in the middle
    nodes3 = build_list_with_cycle([1, 2, 3, 4, 5], 2)
    assert solution.has_cycle(nodes3[0]) is nodes3[2]
    print("✓ Test 3 passed: Cycle starts at the third node")

    # Test case 4: Single node pointing to itself
    nodes4 = build_list_with_cycle([7], 0)
    assert solution.has_cycle(nodes4[0]) is nodes4[0]
    print("✓ Test 4 passed: Self-loop")

    # Test case 5: Whole list is a cycle
    nodes5 = build_list_with_cycle([1, 2, 3, 4], 0)
    assert solution.has_cycle(nodes5[0]) is nodes5[0]
    print("✓ Test 5 passed: Tail links back to head")

    # Test case 6: Tail points to itself after a long stem
    nodes6 = build_list_with_cycle(list(range(10)), 9)
    assert solution.has_cycle(nodes6[0]) is nodes6[9]
    print("✓ Test 6 passed: Self-loop at the tail")

    # Test case 7: Two-node cycle after a stem
    nodes7 = build_list_with_cycle(list(range(7)), 5)
    assert solution.has_cycle(nodes7[0]) is nodes7[5]
    print("✓ Test 7 passed: Two-node cycle after a stem")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_has_cycle()
