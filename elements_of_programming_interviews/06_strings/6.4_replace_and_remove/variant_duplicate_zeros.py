"""
EPI 6.4 Extra Variant - Duplicate Zeros In a Fixed-Length Array
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Count first, then rewrite from the back, as in replace and
remove, but now the array cannot grow and the result must be truncated.

Problem:
Given an integer array arr of fixed length, write every 0 twice, shifting
the later elements to the right. Elements pushed past the end of the array
are lost. Modify arr in place and return nothing.

Constraints:
- 0 <= len(arr) <= 10^5
- 0 <= arr[i] <= 9
- O(n) time, O(1) extra space

How it works:
1. Forward pass: walk the array while tracking how many slots the output
   would use so far, and stop at the last element that (at least partly)
   fits
2. Edge case: if that last element is a 0 and only one of its two copies
   fits, write a single 0 in the last slot and step back
3. Backward pass: copy elements from that last fitting element down to
   the front, writing from the end of the array backward and writing
   each 0 twice

Example 1:
Input: arr = [1, 0, 2, 3, 0, 4, 5, 0]
Output: arr == [1, 0, 0, 2, 3, 0, 0, 4]

Example 2:
Input: arr = [8, 4, 5, 0, 0, 0, 0, 7]
Output: arr == [8, 4, 5, 0, 0, 0, 0, 0]
Explanation: The second 0's copies fill the last two slots
"""

from typing import List


class Solution:
    def duplicate_zeros(self, arr: List[int]) -> None:
        """
        Writes every 0 twice in place, dropping elements pushed off the end.

        Args:
            arr: Array of digits, modified in place

        Returns:
            None

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place zero duplication
        pass


def test_duplicate_zeros():
    """Test cases for duplicating zeros"""
    solution = Solution()

    # Test case 1: Classic example
    a1 = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicate_zeros(a1)
    assert a1 == [1, 0, 0, 2, 3, 0, 0, 4]
    print("✓ Test 1 passed: [1,0,2,3,0,4,5,0] -> [1,0,0,2,3,0,0,4]")

    # Test case 2: No zeros, unchanged
    a2 = [1, 2, 3]
    solution.duplicate_zeros(a2)
    assert a2 == [1, 2, 3]
    print("✓ Test 2 passed: No zeros")

    # Test case 3: Empty and single-element arrays
    a3: List[int] = []
    solution.duplicate_zeros(a3)
    a3b = [0]
    solution.duplicate_zeros(a3b)
    assert a3 == [] and a3b == [0]
    print("✓ Test 3 passed: Empty array and [0]")

    # Test case 4: All zeros
    a4 = [0, 0, 0, 0, 0]
    solution.duplicate_zeros(a4)
    assert a4 == [0, 0, 0, 0, 0]
    print("✓ Test 4 passed: All zeros")

    # Test case 5: Only one copy of the last zero fits
    a5 = [1, 5, 2, 0, 6, 8, 0, 6, 0]
    solution.duplicate_zeros(a5)
    assert a5 == [1, 5, 2, 0, 0, 6, 8, 0, 0]
    a5b = [1, 2, 0]
    solution.duplicate_zeros(a5b)
    assert a5b == [1, 2, 0]
    a5c = [0, 1, 7, 6, 0, 2, 0, 7]
    solution.duplicate_zeros(a5c)
    assert a5c == [0, 0, 1, 7, 6, 0, 0, 2]
    print("✓ Test 5 passed: Truncated zero at the boundary")

    # Test case 6: Both copies fill the last two slots exactly
    a6 = [8, 4, 5, 0, 0, 0, 0, 7]
    solution.duplicate_zeros(a6)
    assert a6 == [8, 4, 5, 0, 0, 0, 0, 0]
    print("✓ Test 6 passed: Copies end exactly at the boundary")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_duplicate_zeros()
