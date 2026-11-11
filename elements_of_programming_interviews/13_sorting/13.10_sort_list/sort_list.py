"""
EPI 13.10 - Implement a Fast Sorting Algorithm for Lists

Problem:
Sort a singly linked list in ascending order of node data. The sort must be
stable (nodes with equal data keep their original relative order) and should
rearrange the existing nodes rather than create new ones.

Constraints:
- 0 <= number of nodes <= 10^5
- O(n log n) time, O(log n) space (recursion stack)

How it works (merge sort on lists):
1. Base case: an empty or single-node list is already sorted
2. Find the middle with slow and fast pointers and cut the list in two
3. Recursively sort both halves
4. Merge the sorted halves by relinking nodes; when data are equal, take the
   node from the left half first so the sort stays stable

Example 1:
Input: 5 -> 2 -> 9 -> 1 -> 5
Output: 1 -> 2 -> 5 -> 5 -> 9

Example 2:
Input: (empty)
Output: (empty)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def stable_sort_list(self, L: Optional[ListNode]) -> Optional[ListNode]:
        """
        Stably sorts a linked list by relinking its nodes.

        Args:
            L: Head of the list

        Returns:
            Head of the sorted list

        Time Complexity: O(n log n)
        Space Complexity: O(log n)
        """
        # TODO: Implement stable merge sort on a linked list
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


def to_nodes(head: Optional[ListNode]) -> List[ListNode]:
    """Collects the node objects of a linked list in order."""
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes


def test_stable_sort_list():
    """Test cases for stable linked-list sort"""
    solution = Solution()

    # Test case 1: Unsorted with a duplicate
    assert to_list(solution.stable_sort_list(build_list([5, 2, 9, 1, 5]))) == [1, 2, 5, 5, 9]
    print("✓ Test 1 passed: [5, 2, 9, 1, 5] -> [1, 2, 5, 5, 9]")

    # Test case 2: Empty list
    assert solution.stable_sort_list(None) is None
    print("✓ Test 2 passed: Empty list")

    # Test case 3: Single node
    single = ListNode(7)
    assert solution.stable_sort_list(single) is single and single.next is None
    print("✓ Test 3 passed: Single node")

    # Test case 4: Reverse-sorted input
    assert to_list(solution.stable_sort_list(build_list(list(range(10, 0, -1))))) == list(range(1, 11))
    print("✓ Test 4 passed: Reverse-sorted input")

    # Test case 5: Stability, equal keys keep original node order
    head5 = build_list([3, 1, 3, 2, 1, 3])
    original = to_nodes(head5)
    sorted_nodes = to_nodes(solution.stable_sort_list(head5))
    expected = sorted(original, key=lambda node: node.data)  # Python's sort is stable
    assert len(sorted_nodes) == len(expected)
    assert all(a is b for a, b in zip(sorted_nodes, expected))
    print("✓ Test 5 passed: Stable, existing nodes reused")

    # Test case 6: Negative numbers and already sorted
    assert to_list(solution.stable_sort_list(build_list([-3, -1, 0, 0, 4]))) == [-3, -1, 0, 0, 4]
    print("✓ Test 6 passed: Already sorted with negatives")

    # Test case 7: Larger input
    values7 = [(i * 37) % 101 for i in range(200)]
    assert to_list(solution.stable_sort_list(build_list(values7))) == sorted(values7)
    print("✓ Test 7 passed: 200-node list")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_stable_sort_list()
