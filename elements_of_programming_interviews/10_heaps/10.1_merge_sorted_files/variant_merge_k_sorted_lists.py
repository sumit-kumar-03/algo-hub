"""
EPI 10.1 Extra Variant - Merge k Sorted Linked Lists
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the k-way merge with a min-heap that holds one "front" element
per input.

Problem:
Given k singly linked lists, each sorted in ascending order, splice them
into one sorted linked list and return its head. Reuse the existing nodes
(relink their next pointers) instead of creating new ones.

Constraints:
- 0 <= k <= 10^3, total nodes n <= 10^5; some lists may be empty (None)
- O(n log k) time, O(k) extra space
- Node values can repeat, and node objects are not comparable, so the heap
  entries need a tie-breaker (for example, the list index)

How it works:
1. Push (head.data, i, head) for every nonempty list i onto a min-heap
2. Keep a dummy head and a tail pointer
3. Pop the smallest entry, attach its node to the tail, and push that
   node's successor (if any) with the same index i
4. Return dummy.next

Example 1:
Input: [1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6]
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Example 2:
Input: [None, None]
Output: None
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted list.

        Args:
            lists: Heads of k sorted linked lists (None for an empty list)

        Returns:
            Head of the merged list, built from the original nodes

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # TODO: Implement k-way merge of linked lists with heapq
        pass


def build(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head and len(out) <= 10 ** 6:
        out.append(head.data)
        head = head.next
    return out


def test_merge_k_lists():
    """Test cases for merging k sorted linked lists"""
    solution = Solution()

    # Test case 1: Three lists with overlaps
    result1 = solution.merge_k_lists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])
    assert to_list(result1) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("✓ Test 1 passed: Three lists")

    # Test case 2: No lists, and only empty lists
    assert solution.merge_k_lists([]) is None
    assert solution.merge_k_lists([None, None]) is None
    print("✓ Test 2 passed: No nodes at all")

    # Test case 3: One nonempty list among empties
    assert to_list(solution.merge_k_lists([None, build([2, 7]), None])) == [2, 7]
    print("✓ Test 3 passed: Single nonempty list")

    # Test case 4: Equal values in every list (needs a tie-breaker)
    lists4 = [build([5, 5]) for _ in range(4)]
    assert to_list(solution.merge_k_lists(lists4)) == [5] * 8
    print("✓ Test 4 passed: All values equal")

    # Test case 5: Original nodes are reused
    a, b = build([1, 3]), build([2])
    nodes = {id(a), id(a.next), id(b)}
    merged = solution.merge_k_lists([a, b])
    seen = set()
    node = merged
    while node:
        seen.add(id(node))
        node = node.next
    assert seen == nodes
    print("✓ Test 5 passed: Nodes are relinked, not copied")

    # Test case 6: Negatives and many lists
    lists6 = [build(list(range(-i, 50, 7))) for i in range(30)]
    expected6 = sorted(v for i in range(30) for v in range(-i, 50, 7))
    assert to_list(solution.merge_k_lists(lists6)) == expected6
    print("✓ Test 6 passed: 30 lists with negatives")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_k_lists()
