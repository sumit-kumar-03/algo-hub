"""
EPI 13.5 Variant - Peak Bandwidth Usage

Problem:
Users 1, 2, ..., n share an Internet connection. User i consumes b_i units of
bandwidth from time s_i through time f_i, inclusive. Return the peak total
bandwidth in use at any single moment.

Constraints:
- 0 <= n <= 10^5
- s_i <= f_i, b_i >= 0
- O(n log n) time, O(n) space

How it works (weighted sweep over endpoints):
1. Create endpoints (s_i, start, b_i) and (f_i, finish, b_i)
2. Sort by time; on ties, process starts before finishes because usage is
   inclusive at both ends
3. Sweep: add b_i at a start, subtract b_i at a finish, and track the
   maximum running total

Example 1:
Input: usages = [(1, 5, 10), (2, 7, 20), (6, 8, 5)]
Output: 30
Explanation: During [2, 5], the first two users consume 10 + 20 = 30.

Example 2:
Input: usages = [(1, 3, 4), (3, 6, 6)]
Output: 10
Explanation: Both users are active at time 3.
"""

from typing import List, Tuple


class Solution:
    def peak_bandwidth(self, usages: List[Tuple[int, int, int]]) -> int:
        """
        Computes the peak total bandwidth used at any moment.

        Args:
            usages: List of (start, finish, bandwidth), inclusive at both ends

        Returns:
            Maximum total bandwidth in use at any time (0 if there are no users)

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement peak bandwidth computation
        pass


def test_peak_bandwidth():
    """Test cases for peak bandwidth usage"""
    solution = Solution()

    # Test case 1: Two overlapping users
    assert solution.peak_bandwidth([(1, 5, 10), (2, 7, 20), (6, 8, 5)]) == 30
    print("✓ Test 1 passed: Overlapping users -> 30")

    # Test case 2: Touching intervals overlap (inclusive)
    assert solution.peak_bandwidth([(1, 3, 4), (3, 6, 6)]) == 10
    print("✓ Test 2 passed: Touching endpoints -> 10")

    # Test case 3: No users
    assert solution.peak_bandwidth([]) == 0
    print("✓ Test 3 passed: No users -> 0")

    # Test case 4: One heavy user beats several light overlapping users
    assert solution.peak_bandwidth([(0, 10, 1), (1, 9, 1), (2, 8, 1), (20, 21, 50)]) == 50
    print("✓ Test 4 passed: Heavy isolated user -> 50")

    # Test case 5: Disjoint intervals
    assert solution.peak_bandwidth([(1, 2, 7), (3, 4, 8), (5, 6, 3)]) == 8
    print("✓ Test 5 passed: Disjoint intervals -> 8")

    # Test case 6: Peak is not where the most users overlap
    usages6 = [(0, 4, 1), (1, 4, 1), (2, 4, 1), (5, 9, 2), (6, 9, 2)]
    assert solution.peak_bandwidth(usages6) == 4
    print("✓ Test 6 passed: Weighted peak -> 4")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_peak_bandwidth()
