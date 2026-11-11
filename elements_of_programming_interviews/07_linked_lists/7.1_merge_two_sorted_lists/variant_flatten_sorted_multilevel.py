"""
EPI 7.1 Extra Variant - Flatten a Multilevel Sorted List
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Merging two sorted lists by relinking nodes, applied
repeatedly and in a balanced order.

Problem:
Each node has a value and two pointers, next and down. The nodes reached
from the head by next pointers form the top row. Each top-row node starts
a column: the chain of nodes reached from it by down pointers (the
top-row node itself included). Every column is sorted in ascending order;
the top row itself need not be. Flatten the structure into a single
ascending list linked through down pointers, with every next pointer set
to None, and return its head. Reuse the existing nodes.

Constraints:
- 0 <= number of columns k <= 10^3, total number of nodes N <= 10^5
- O(N log k) time, O(k) extra space at most (for holding column heads);
  merging columns one by one into a growing result is O(N k), so beat it

How it works:
1. Treat each column as a sorted list linked by down pointers
2. Merge columns in pairs like the bottom-up rounds of merge sort: merge
   columns 1 and 2, 3 and 4, ..., then merge those results in pairs, and
   so on until one list is left; each node takes part in O(log k) merges
3. Each merge is the two-pointer merge with a dummy head, using down as
   the link field
4. Clear next on every node (detach the top row) before or while merging

Example 1:
Input:  5 -> 10 -> 19 -> 28     (top row, via next)
        |    |     |     |
        7    20    22    35     (down)
        |          |     |
        8          50    40
        |                |
        30               45
Output: 5 7 8 10 19 20 22 28 30 35 40 45 50 (linked via down)

Example 2:
Input: 3 -> 1 (two single-node columns)
Output: 1 3
"""

from typing import List, Optional


class MultiNode:
    def __init__(
        self,
        data: int = 0,
        next: "Optional[MultiNode]" = None,
        down: "Optional[MultiNode]" = None,
    ):
        self.data = data
        self.next = next
        self.down = down


class Solution:
    def flatten(self, head: Optional[MultiNode]) -> Optional[MultiNode]:
        """
        Flattens a list of sorted columns into one sorted down-linked list.

        Args:
            head: First node of the top row (None if empty)

        Returns:
            Head of the flattened list, linked through down pointers

        Time Complexity: O(N log k) for N nodes in k columns
        Space Complexity: O(1) extra (O(k) is acceptable for holding heads)
        """
        # TODO: Implement balanced pairwise merging of the columns
        pass


def build_multilevel(columns: List[List[int]]) -> Optional[MultiNode]:
    """Builds the structure from a list of columns (each non-empty)."""
    tops = []
    for column in columns:
        nodes = [MultiNode(v) for v in column]
        for upper, lower in zip(nodes, nodes[1:]):
            upper.down = lower
        tops.append(nodes[0])
    for left, right in zip(tops, tops[1:]):
        left.next = right
    return tops[0] if tops else None


def collect_all(head: Optional[MultiNode]) -> List[MultiNode]:
    """Returns every node of the structure (before flattening)."""
    nodes = []
    while head:
        node = head
        while node:
            nodes.append(node)
            node = node.down
        head = head.next
    return nodes


def flattened_values(head: Optional[MultiNode]) -> List[int]:
    """Reads the flattened list, checking that every next pointer is None."""
    values = []
    while head:
        assert head.next is None, "next pointers must be cleared"
        values.append(head.data)
        head = head.down
    return values


def test_flatten():
    """Test cases for flattening a multilevel sorted list"""
    solution = Solution()

    # Test case 1: Classic example
    columns = [[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]]
    head1 = build_multilevel(columns)
    nodes1 = collect_all(head1)
    result1 = solution.flatten(head1)
    assert flattened_values(result1) == sorted(v for c in columns for v in c)
    print("✓ Test 1 passed: Four columns flattened")

    # Test case 2: Empty structure
    assert solution.flatten(None) is None
    print("✓ Test 2 passed: Empty structure")

    # Test case 3: Single column is already the answer
    result3 = solution.flatten(build_multilevel([[1, 2, 3]]))
    assert flattened_values(result3) == [1, 2, 3]
    print("✓ Test 3 passed: Single column")

    # Test case 4: Top row not sorted, single-node columns
    result4 = solution.flatten(build_multilevel([[3], [1], [2]]))
    assert flattened_values(result4) == [1, 2, 3]
    print("✓ Test 4 passed: Unsorted top row")

    # Test case 5: Duplicates and negatives
    columns5 = [[0, 0, 4], [-2, 0], [-2, 9], [4]]
    result5 = solution.flatten(build_multilevel(columns5))
    assert flattened_values(result5) == [-2, -2, 0, 0, 0, 4, 4, 9]
    print("✓ Test 5 passed: Duplicates and negatives")

    # Test case 6: Nodes are reused
    flat_ids = []
    node = result1
    while node:
        flat_ids.append(id(node))
        node = node.down
    assert sorted(flat_ids) == sorted(id(n) for n in nodes1)
    print("✓ Test 6 passed: Original nodes reused")

    # Test case 7: Many columns
    columns7 = [[i, i + 1000, i + 2000] for i in range(500, 0, -1)]
    result7 = solution.flatten(build_multilevel(columns7))
    assert flattened_values(result7) == sorted(v for c in columns7 for v in c)
    print("✓ Test 7 passed: 500 columns")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_flatten()
