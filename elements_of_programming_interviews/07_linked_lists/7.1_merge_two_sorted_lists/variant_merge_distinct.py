"""
EPI 7.1 Extra Variant - Merge Into a List of Distinct Values
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Merging with a dummy head and a tail pointer, splicing in the
smaller head node at each step.

Problem:
Given two singly linked lists, each sorted in ascending order (duplicates
may appear within a list and across the lists), merge them into a single
ascending list in which every value appears exactly once. Reuse the
existing nodes; nodes holding repeated values are simply left out of the
result.

Constraints:
- 0 <= length of each list <= 10^4
- O(n + m) time, O(1) extra space

How it works:
1. Create a dummy head and a tail pointer to it
2. While either list is non-empty, pick the smaller head (or the only
   remaining one) and advance that list
3. Append the picked node only if tail is the dummy or the node's value
   differs from tail's value; otherwise skip it
4. Terminate the result with tail.next = None and return dummy.next

Example 1:
Input: L1 = 1 -> 3 -> 3 -> 5, L2 = 1 -> 2 -> 3
Output: 1 -> 2 -> 3 -> 5

Example 2:
Input: L1 = 4 -> 4, L2 = (empty)
Output: 4
"""

from typing import List, Optional


class ListNode:
    def __init__(self, data: int = 0, next: "Optional[ListNode]" = None):
        self.data = data
        self.next = next


class Solution:
    def merge_distinct(
        self, L1: Optional[ListNode], L2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted lists, keeping one node per distinct value.

        Args:
            L1: Head of the first sorted list
            L2: Head of the second sorted list

        Returns:
            Head of the merged list of distinct values

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement merge with duplicate removal
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


def test_merge_distinct():
    """Test cases for merging into distinct values"""
    solution = Solution()

    # Test case 1: Duplicates within and across lists
    merged1 = solution.merge_distinct(build_list([1, 3, 3, 5]), build_list([1, 2, 3]))
    assert to_list(merged1) == [1, 2, 3, 5]
    print("✓ Test 1 passed: [1,3,3,5] + [1,2,3] -> [1,2,3,5]")

    # Test case 2: Both lists empty
    assert solution.merge_distinct(None, None) is None
    print("✓ Test 2 passed: Both lists empty")

    # Test case 3: One list empty, duplicates inside the other
    merged3 = solution.merge_distinct(build_list([4, 4]), None)
    assert to_list(merged3) == [4]
    print("✓ Test 3 passed: Duplicates in a single list")

    # Test case 4: Identical lists
    merged4 = solution.merge_distinct(build_list([1, 2, 3]), build_list([1, 2, 3]))
    assert to_list(merged4) == [1, 2, 3]
    print("✓ Test 4 passed: Identical lists")

    # Test case 5: Negatives and a long run of one value
    merged5 = solution.merge_distinct(
        build_list([-3, -3, 0, 0, 0]), build_list([-5, 0, 0, 7])
    )
    assert to_list(merged5) == [-5, -3, 0, 7]
    print("✓ Test 5 passed: Negatives and long runs")

    # Test case 6: Nodes are reused, not copied
    a, b = build_list([2]), build_list([1, 2])
    merged6 = solution.merge_distinct(a, b)
    assert merged6 is b and merged6.next is not None
    assert merged6.next.data == 2 and merged6.next.next is None
    assert merged6.next is a or merged6.next is b.next
    print("✓ Test 6 passed: Original nodes reused")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_distinct()
