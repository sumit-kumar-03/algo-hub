"""
EPI 17.4 Variant - Count Triples with Sum at Most T

Problem:
Given an array of integers A and an integer T, count the triples of
distinct positions whose values sum to at most T. Each unordered triple of
positions is counted once (the book phrases this as tuples (p, q, r) with
A[p] <= A[q] <= A[r], which fixes one ordering per triple).

Constraints:
- 0 <= len(A) <= 10^4
- O(n^2) time

How it works (sort + two pointers that count in bulk):
1. Sort A
2. For each k, set i = k + 1, j = n - 1; while i < j:
   - if A[k] + A[i] + A[j] <= T: every j' in (i, j] also works with
     (k, i), so add j - i and move i up
   - otherwise move j down
3. Return the total

Example 1:
Input: A = [-2, 0, 1, 3], T = 2
Output: 3
Explanation: (-2, 0, 1), (-2, 0, 3), (-2, 1, 3)

Example 2:
Input: A = [5, 1, 3, 4, 7], T = 12
Output: 6
"""

from typing import List


class Solution:
    def count_three_sums_at_most(self, A: List[int], T: int) -> int:
        """
        Counts triples of distinct positions whose sum is at most T.

        Args:
            A: Input integers
            T: Upper bound on the sum

        Returns:
            Number of qualifying triples

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond sorting
        """
        # TODO: Implement counting with two pointers
        pass


def test_count_three_sums_at_most():
    """Test cases for counting triples with bounded sum"""
    solution = Solution()

    # Test case 1: Mixed signs
    assert solution.count_three_sums_at_most([-2, 0, 1, 3], 2) == 3
    print("✓ Test 1 passed: [-2, 0, 1, 3], 2 -> 3")

    # Test case 2: Unsorted input
    assert solution.count_three_sums_at_most([5, 1, 3, 4, 7], 12) == 6
    print("✓ Test 2 passed: [5, 1, 3, 4, 7], 12 -> 6")

    # Test case 3: Duplicates at different positions count separately
    assert solution.count_three_sums_at_most([1, 1, 1, 1], 3) == 4
    print("✓ Test 3 passed: [1, 1, 1, 1], 3 -> 4")

    # Test case 4: Fewer than three entries
    assert solution.count_three_sums_at_most([1, 2], 10) == 0
    print("✓ Test 4 passed: [1, 2], 10 -> 0")

    # Test case 5: Bound too small
    assert solution.count_three_sums_at_most([1, 2, 3], 5) == 0
    print("✓ Test 5 passed: [1, 2, 3], 5 -> 0")

    # Test case 6: Every triple qualifies
    assert solution.count_three_sums_at_most([1, 2, 3, 4, 5], 100) == 10
    print("✓ Test 6 passed: [1, 2, 3, 4, 5], 100 -> 10")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_three_sums_at_most()
