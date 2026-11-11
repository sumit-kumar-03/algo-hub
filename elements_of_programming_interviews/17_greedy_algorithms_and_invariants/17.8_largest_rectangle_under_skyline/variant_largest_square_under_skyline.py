"""
EPI 17.8 Variant - Find the Largest Square Under the Skyline

Problem:
Same skyline as 17.8 (adjacent unit-width buildings with heights A[i]).
Return the area of the largest axis-aligned square that fits entirely
inside the skyline.

Constraints:
- 0 <= len(A) <= 10^5, 0 <= A[i] <= 10^4
- O(n) time, O(n) space

How it works (reuse the 17.8 stack):
1. For each building i, the stack pass gives the widest run w_i in which
   every building is at least A[i] tall
2. A square of side min(A[i], w_i) fits in that rectangle, and the best
   square always sits in one of these maximal rectangles
3. Return the largest min(A[i], w_i) ** 2

Example 1:
Input: A = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
Output: 9
Explanation: Side 3, e.g. over buildings 3-5 (heights 5, 6, 3).

Example 2:
Input: A = [10, 1]
Output: 1
Explanation: The tall building is only one unit wide.
"""

from typing import List


class Solution:
    def largest_square_under_skyline(self, heights: List[int]) -> int:
        """
        Computes the area of the largest square under the skyline.

        Args:
            heights: Building heights, each building one unit wide

        Returns:
            Maximum square area

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement largest square under the skyline
        pass


def test_largest_square_under_skyline():
    """Test cases for largest square under the skyline"""
    solution = Solution()

    # Test case 1: Book skyline
    assert solution.largest_square_under_skyline([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]) == 9
    print("✓ Test 1 passed: book skyline -> 9")

    # Test case 2: Rectangle answer is 10, square answer is 4
    assert solution.largest_square_under_skyline([2, 1, 5, 6, 2, 3]) == 4
    print("✓ Test 2 passed: [2, 1, 5, 6, 2, 3] -> 4")

    # Test case 3: Narrow tower
    assert solution.largest_square_under_skyline([10, 1]) == 1
    print("✓ Test 3 passed: [10, 1] -> 1")

    # Test case 4: Width limits the square
    assert solution.largest_square_under_skyline([7]) == 1
    print("✓ Test 4 passed: [7] -> 1")

    # Test case 5: Height limits the square
    assert solution.largest_square_under_skyline([3, 3, 3, 3]) == 9
    print("✓ Test 5 passed: [3, 3, 3, 3] -> 9")

    # Test case 6: Empty skyline
    assert solution.largest_square_under_skyline([]) == 0
    print("✓ Test 6 passed: [] -> 0")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_largest_square_under_skyline()
