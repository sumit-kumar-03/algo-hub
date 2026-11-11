"""
EPI 5.1 Variant - Group Objects with Three Distinct Keys

Problem:
Given an array of objects whose keys take one of three values, rearrange
the array in place so that all objects with the same key are next to each
other. The order of the three groups does not matter. Each object is a
(key, label) tuple; the key is item[0].

Constraints:
- Keys take at most three distinct values (not known in advance)
- Must run in O(n) time and use O(1) extra space
- 0 <= len(A) <= 10^5

How it works (three-way partition around a key, no ordering needed):
1. Take the first key k1; partition so all k1 objects come first
   (swap them forward with a write pointer)
2. Among the remaining objects take the next key k2; partition again so
   all k2 objects come next
3. Whatever remains has the third key and is already contiguous

Example 1:
Input: A = [(2, 'a'), (0, 'b'), (1, 'c'), (2, 'd'), (0, 'e')]
Output: [(2, 'a'), (2, 'd'), (0, 'b'), (0, 'e'), (1, 'c')] (one valid answer)
Explanation: Each key's objects form one contiguous block.

Example 2:
Input: A = [('x', 1), ('y', 2), ('x', 3)]
Output: [('x', 1), ('x', 3), ('y', 2)] (one valid answer)
Explanation: Only two keys appear; each forms a block.
"""

from typing import Any, List, Tuple


class Solution:
    def group_three_keys(self, A: List[Tuple[Any, Any]]) -> None:
        """
        Groups objects with equal keys together, in place.

        Args:
            A: List of (key, label) tuples with at most three distinct keys

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement three-key grouping
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


def test_group_three_keys():
    """Test cases for three-key grouping"""
    solution = Solution()

    # Test case 1: Mixed three keys
    A1 = [(2, "a"), (0, "b"), (1, "c"), (2, "d"), (0, "e")]
    original1 = sorted(A1)
    solution.group_three_keys(A1)
    assert sorted(A1) == original1 and is_grouped(A1)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Alternating keys
    A2 = [(i % 3, i) for i in range(12)]
    original2 = sorted(A2)
    solution.group_three_keys(A2)
    assert sorted(A2) == original2 and is_grouped(A2)
    print("✓ Test 2 passed: Alternating keys 0, 1, 2, 0, 1, 2, ...")

    # Test case 3: Only two distinct keys (non-integer)
    A3 = [("x", 1), ("y", 2), ("x", 3), ("y", 4)]
    solution.group_three_keys(A3)
    assert sorted(A3) == [("x", 1), ("x", 3), ("y", 2), ("y", 4)] and is_grouped(A3)
    print(f"✓ Test 3 passed: Two keys -> {A3}")

    # Test case 4: Single key and empty array
    A4 = [(5, "a"), (5, "b")]
    solution.group_three_keys(A4)
    assert sorted(A4) == [(5, "a"), (5, "b")]
    A5: List[Tuple[Any, Any]] = []
    solution.group_three_keys(A5)
    assert A5 == []
    print("✓ Test 4 passed: Single key and empty array")

    # Test case 5: Already grouped in reverse key order
    A6 = [(9, "a"), (9, "b"), (4, "c"), (1, "d"), (1, "e")]
    original6 = sorted(A6)
    solution.group_three_keys(A6)
    assert sorted(A6) == original6 and is_grouped(A6)
    print(f"✓ Test 5 passed: {A6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_group_three_keys()
