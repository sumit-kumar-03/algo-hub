"""
EPI 17.8 - Compute the Largest Rectangle Under the Skyline

Problem:
A skyline is a row of adjacent buildings, each one unit wide, where A[i] is
the height of building i. Return the area of the largest axis-aligned
rectangle that fits entirely inside the skyline.

Constraints:
- 0 <= len(A) <= 10^5, 0 <= A[i] <= 10^4
- O(n) time, O(n) space

How it works (monotonic stack of "still extendable" buildings):
1. For each building i the best rectangle of height A[i] extends left and
   right until a shorter building blocks it
2. Keep a stack of indices with increasing heights. When A[i] is not taller
   than the top, pop the top: its right limit is i and its left limit is
   the new top (or -1 if the stack is empty), so its width is
   i - stack_top - 1 (or i)
3. Process a sentinel height 0 at the end to flush the stack
4. Track the largest height * width seen

Example 1:
Input: A = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
Output: 20
Explanation: Height 2 spans buildings 1 through 10 (width 10).

Example 2:
Input: A = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: Height 5 across buildings 2 and 3.
"""

from typing import List


class Solution:
    def calculate_largest_rectangle(self, heights: List[int]) -> int:
        """
        Computes the area of the largest rectangle under the skyline.

        Args:
            heights: Building heights, each building one unit wide

        Returns:
            Maximum rectangle area

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement monotonic stack solution
        pass


def test_calculate_largest_rectangle():
    """Test cases for largest rectangle under the skyline"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.calculate_largest_rectangle([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]) == 20
    print("✓ Test 1 passed: book example -> 20")

    # Test case 2: Classic example
    assert solution.calculate_largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
    print("✓ Test 2 passed: [2, 1, 5, 6, 2, 3] -> 10")

    # Test case 3: Empty skyline
    assert solution.calculate_largest_rectangle([]) == 0
    print("✓ Test 3 passed: [] -> 0")

    # Test case 4: Equal heights
    assert solution.calculate_largest_rectangle([3, 3, 3, 3]) == 12
    print("✓ Test 4 passed: [3, 3, 3, 3] -> 12")

    # Test case 5: Ascending heights
    assert solution.calculate_largest_rectangle([1, 2, 3, 4, 5]) == 9
    print("✓ Test 5 passed: [1, 2, 3, 4, 5] -> 9")

    # Test case 6: Descending heights
    assert solution.calculate_largest_rectangle([5, 4, 3, 2, 1]) == 9
    print("✓ Test 6 passed: [5, 4, 3, 2, 1] -> 9")

    # Test case 7: Single building
    assert solution.calculate_largest_rectangle([7]) == 7
    print("✓ Test 7 passed: [7] -> 7")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_calculate_largest_rectangle()
