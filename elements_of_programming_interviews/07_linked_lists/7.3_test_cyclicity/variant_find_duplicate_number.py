"""
EPI 7.3 Extra Variant - Find the Repeated Number Without Extra Space
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Finding the first node of a cycle with fast and slow pointers,
applied to an array viewed as a linked list.

Problem:
You are given a read-only array A of n + 1 integers, each between 1 and n
inclusive. By the pigeonhole principle some value appears at least twice.
Exactly one value is repeated (it may appear two or more times). Return
it without modifying A and using O(1) extra space.

Constraints:
- 1 <= n <= 10^5, len(A) == n + 1, 1 <= A[i] <= n
- Exactly one value appears more than once
- O(n) time, O(1) extra space, A must not be changed (so no sorting and
  no marking entries)

How it works:
1. Treat each index i as a node whose next pointer is A[i]. Index 0 has
   no incoming pointer (values are at least 1), so start there.
2. Following pointers from 0 must eventually loop, and the repeated value
   is an index with two or more incoming pointers: the first node of the
   cycle
3. Find that first node exactly as in the main problem: meet with slow
   and fast pointers, then advance one pointer from index 0 and one from
   the meeting point at the same speed until they meet

Example 1:
Input: A = [1, 3, 4, 2, 2]
Output: 2

Example 2:
Input: A = [3, 1, 3, 4, 2]
Output: 3
"""

from typing import List


class Solution:
    def find_duplicate(self, A: List[int]) -> int:
        """
        Finds the repeated value in A without changing A.

        Args:
            A: n + 1 integers in the range 1..n, read only

        Returns:
            The value that occurs more than once

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement duplicate search with fast and slow pointers
        pass


def test_find_duplicate():
    """Test cases for finding the repeated number"""
    solution = Solution()

    # Test case 1: Classic example
    A1 = [1, 3, 4, 2, 2]
    assert solution.find_duplicate(A1) == 2
    assert A1 == [1, 3, 4, 2, 2]
    print("✓ Test 1 passed: [1,3,4,2,2] -> 2, array unchanged")

    # Test case 2: Repeated value at the front
    assert solution.find_duplicate([3, 1, 3, 4, 2]) == 3
    print("✓ Test 2 passed: [3,1,3,4,2] -> 3")

    # Test case 3: Smallest input
    assert solution.find_duplicate([1, 1]) == 1
    print("✓ Test 3 passed: [1,1] -> 1")

    # Test case 4: Value repeated many times
    A4 = [2, 2, 2, 2, 2]
    assert solution.find_duplicate(A4) == 2
    assert A4 == [2, 2, 2, 2, 2]
    print("✓ Test 4 passed: All entries equal")

    # Test case 5: Repeated value is the largest possible
    assert solution.find_duplicate([5, 1, 2, 3, 4, 5]) == 5
    print("✓ Test 5 passed: Duplicate equals n")

    # Test case 6: Large shuffled input
    import random

    rng = random.Random(7)
    n = 100000
    A6 = list(range(1, n + 1)) + [31337]
    rng.shuffle(A6)
    snapshot = list(A6)
    assert solution.find_duplicate(A6) == 31337
    assert A6 == snapshot
    print("✓ Test 6 passed: n = 100000, array unchanged")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_duplicate()
