"""
EPI 7.3 Extra Variant - One-Direction Loop in a Circular Array
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Fast and slow pointers on an implicit list (next index computed
from the current entry), extended with extra conditions on the cycle.

Problem:
You are given a circular array A of nonzero integers. From index i you
jump A[i] positions: forward if A[i] > 0, backward if A[i] < 0, wrapping
around the ends. Every index has exactly one jump, so walking from any
index eventually loops. Report whether there is a loop that
  - contains more than one index (a jump landing back on its own index
    does not count), and
  - uses jumps that all go in the same direction (all forward or all
    backward).
Return True if such a loop exists, otherwise False.

Constraints:
- 1 <= len(A) <= 10^4
- -1000 <= A[i] <= 1000, A[i] != 0
- O(n) time, O(1) extra space (you may overwrite entries of A)

How it works:
1. next(i) = (i + A[i]) % n
2. From each start index run slow and fast pointers, but only along
   indices whose jumps have the same sign as A[start]; stop when the
   direction changes
3. If they meet, check the loop length: the meeting index must not jump
   to itself
4. Every index visited from a start that failed cannot be on a valid
   loop, so mark those indices (for example set them to 0) to skip them
   later; this keeps the total work O(n)

Example 1:
Input: A = [2, -1, 1, 2, 2]
Output: True
Explanation: 0 -> 2 -> 3 -> 0 is a forward loop of length 3

Example 2:
Input: A = [-1, 2]
Output: False
Explanation: 0 -> 1 -> 1: index 1 only loops to itself, and the
0 -> 1 jump changes direction
"""

from typing import List


class Solution:
    def circular_array_loop(self, A: List[int]) -> bool:
        """
        Detects a one-direction loop longer than one index.

        Args:
            A: Circular array of nonzero jumps (may be modified)

        Returns:
            True if a valid loop exists, otherwise False

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement loop detection in a circular array
        pass


def test_circular_array_loop():
    """Test cases for loops in a circular array"""
    solution = Solution()

    # Test case 1: Forward loop of length 3
    assert solution.circular_array_loop([2, -1, 1, 2, 2]) is True
    print("✓ Test 1 passed: [2,-1,1,2,2] has a forward loop")

    # Test case 2: Only self-loops and mixed directions
    assert solution.circular_array_loop([-1, 2]) is False
    assert solution.circular_array_loop([-2, 1, -1, -2, -2]) is False
    print("✓ Test 2 passed: Self-loops and direction changes don't count")

    # Test case 3: Single element is always a self-loop
    assert solution.circular_array_loop([1]) is False
    assert solution.circular_array_loop([-5]) is False
    print("✓ Test 3 passed: Single element")

    # Test case 4: Backward loop
    assert solution.circular_array_loop([-1, -1, -1]) is True
    assert solution.circular_array_loop([-1, -2, -3, -4, -5, 6]) is False
    print("✓ Test 4 passed: Backward loop found; mixed one rejected")

    # Test case 5: Large jumps wrap around several times
    assert solution.circular_array_loop([3, 1, 2]) is True  # 1 -> 2 -> 1
    assert solution.circular_array_loop([1, -1, 5, 1, 4]) is True  # 3 -> 4 -> 3
    print("✓ Test 5 passed: Wrap-around jumps")

    # Test case 6: Even indices broken by one backward jump; odd loop survives
    A6 = [2] * 1000
    A6[0] = -1
    assert solution.circular_array_loop(A6) is True  # 1 -> 3 -> ... -> 999 -> 1
    print("✓ Test 6 passed: Long forward loop over the odd indices")

    # Test case 7: Larger input without any valid loop
    A7 = [1, -1] * 2000
    assert solution.circular_array_loop(A7) is False
    print("✓ Test 7 passed: Alternating directions everywhere")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_circular_array_loop()
