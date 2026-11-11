"""
EPI 5.1 Variant - Group Objects with Four Distinct Keys

Problem:
Given an array of objects whose keys take one of four values, rearrange
the array in place so that all objects with the same key are next to each
other. The order of the groups does not matter. Each object is a
(key, label) tuple; the key is item[0].

Constraints:
- Keys take at most four distinct values (not known in advance)
- Must run in O(n) time and use O(1) extra space
- 0 <= len(A) <= 10^5

How it works (repeated partition passes):
1. Keep a write pointer `start` = 0
2. While start < len(A): let k = A[start][0]; scan the rest of the array
   and swap every object with key k to position `start`, advancing it
3. Each pass fixes one key's block; at most four passes are needed,
   so the total time is O(4n) = O(n)

Example 1:
Input: A = [(3, 'a'), (1, 'b'), (0, 'c'), (2, 'd'), (1, 'e'), (3, 'f')]
Output: [(3, 'a'), (3, 'f'), (1, 'b'), (1, 'e'), (0, 'c'), (2, 'd')] (one valid answer)
Explanation: Each key's objects form one contiguous block.

Example 2:
Input: A = [(0, 'a'), (0, 'b')]
Output: [(0, 'a'), (0, 'b')]
Explanation: Only one key appears.
"""

from typing import Any, List, Tuple


class Solution:
    def group_four_keys(self, A: List[Tuple[Any, Any]]) -> None:
        """
        Groups objects with equal keys together, in place.

        Args:
            A: List of (key, label) tuples with at most four distinct keys

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement four-key grouping
        pass


def is_grouped(A: List[Tuple[Any, Any]]) -> bool:
    """Checks that every key's objects form one contiguous block."""
    seen = set()
    for i, (key, _) in enumerate(A):
        if i > 0 and key == A[i - 1][0]:
            continue
        if key in seen:
            return False
        seen.add(key)
    return True


def test_group_four_keys():
    """Test cases for four-key grouping"""
    solution = Solution()

    # Test case 1: Mixed four keys
    A1 = [(3, "a"), (1, "b"), (0, "c"), (2, "d"), (1, "e"), (3, "f")]
    original1 = sorted(A1)
    solution.group_four_keys(A1)
    assert sorted(A1) == original1 and is_grouped(A1)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Round-robin keys
    A2 = [(i % 4, i) for i in range(20)]
    original2 = sorted(A2)
    solution.group_four_keys(A2)
    assert sorted(A2) == original2 and is_grouped(A2)
    print("✓ Test 2 passed: Round-robin keys 0, 1, 2, 3, 0, ...")

    # Test case 3: String keys
    A3 = [("d", 1), ("a", 2), ("c", 3), ("b", 4), ("a", 5), ("d", 6), ("c", 7)]
    original3 = sorted(A3)
    solution.group_four_keys(A3)
    assert sorted(A3) == original3 and is_grouped(A3)
    print(f"✓ Test 3 passed: {A3}")

    # Test case 4: Single key
    A4 = [(0, "a"), (0, "b")]
    solution.group_four_keys(A4)
    assert sorted(A4) == [(0, "a"), (0, "b")]
    print("✓ Test 4 passed: Single key")

    # Test case 5: Empty and single-element arrays
    A5: List[Tuple[Any, Any]] = []
    solution.group_four_keys(A5)
    A6 = [(7, "z")]
    solution.group_four_keys(A6)
    assert A5 == [] and A6 == [(7, "z")]
    print("✓ Test 5 passed: Empty and single element")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_group_four_keys()
