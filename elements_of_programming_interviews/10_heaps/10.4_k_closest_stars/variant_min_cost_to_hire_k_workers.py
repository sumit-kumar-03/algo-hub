"""
EPI 10.4 Extra Variant - Minimum Cost to Hire a Team of k
(Practice problem, not in the book. Difficulty: Hard)
Builds on: a bounded max-heap of size k that always evicts its largest
element, maintained while scanning candidates in a chosen order.

Problem:
There are n workers. Worker i has a quality q[i] and a minimum wage w[i].
You must hire exactly k of them under two rules:
1. Everyone in the team is paid in proportion to their quality (if one
   worker has twice the quality of another, they are paid twice as much)
2. Every hired worker is paid at least their minimum wage
Return the least total amount of money needed to hire such a team.

Constraints:
- 1 <= k <= n <= 10^4; 1 <= q[i], w[i] <= 10^4
- O(n log n) time, O(n) space
- Answers within 1e-6 of the true value are accepted

How it works (fix the "captain", keep the k smallest qualities):
1. A team paid at rate r per unit of quality costs r * (sum of qualities),
   and r must be at least max(w[i] / q[i]) over the team; so the worker
   with the highest ratio sets the rate
2. Sort workers by ratio w[i] / q[i] ascending; scan them, treating the
   current worker as the one with the highest ratio
3. Keep a max-heap of the qualities seen so far and their sum; when it has
   more than k entries, pop the largest quality (it costs the most)
4. Whenever the heap holds exactly k qualities, the cost is
   ratio * quality_sum; keep the minimum

Example 1:
Input: q = [10, 20, 5], w = [70, 50, 30], k = 2
Output: 105.0
Explanation: Hire workers 0 and 2 at rate 7 per unit: 70 + 35.

Example 2:
Input: q = [3, 1, 10, 10, 1], w = [4, 8, 2, 2, 7], k = 3
Output: 30.666666...
Explanation: Hire workers 0, 2, 3 at rate 4/3: 4 + 13.33... + 13.33....
"""

import math
from typing import List


class Solution:
    def min_cost_to_hire(self, q: List[int], w: List[int], k: int) -> float:
        """
        Returns the minimum total pay to hire exactly k workers.

        Args:
            q: Quality of each worker
            w: Minimum wage of each worker
            k: Team size

        Returns:
            The least possible total pay

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement with ratio sorting and a max-heap of qualities
        pass


def _brute(q: List[int], w: List[int], k: int) -> float:
    """Tries every worker as the rate setter; picks the k cheapest eligible."""
    best = math.inf
    for c in range(len(q)):
        rate = w[c] / q[c]
        eligible = sorted(q[i] for i in range(len(q)) if w[i] / q[i] <= rate and i != c)
        if len(eligible) >= k - 1:
            best = min(best, rate * (q[c] + sum(eligible[: k - 1])))
    return best


def test_min_cost_to_hire():
    """Test cases for minimum cost to hire k workers"""
    solution = Solution()

    # Test case 1: Example 1
    assert math.isclose(solution.min_cost_to_hire([10, 20, 5], [70, 50, 30], 2), 105.0)
    print("✓ Test 1 passed: 105.0")

    # Test case 2: Example 2 (fractional answer)
    result2 = solution.min_cost_to_hire([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3)
    assert math.isclose(result2, 92 / 3)
    print(f"✓ Test 2 passed: {result2:.6f}")

    # Test case 3: k = 1 picks the smallest minimum wage
    assert math.isclose(solution.min_cost_to_hire([5, 1, 9], [10, 3, 4], 1), 3.0)
    print("✓ Test 3 passed: k = 1")

    # Test case 4: k = n hires everyone at the highest ratio
    q4, w4 = [2, 4, 1], [6, 4, 5]
    assert math.isclose(solution.min_cost_to_hire(q4, w4, 3), 5.0 * 7)
    print("✓ Test 4 passed: k = n")

    # Test case 5: Equal ratios everywhere
    assert math.isclose(solution.min_cost_to_hire([1, 2, 3, 4], [2, 4, 6, 8], 2), 6.0)
    print("✓ Test 5 passed: Equal ratios")

    # Test case 6: Deterministic larger input vs. brute force
    q6 = [(i * 37) % 50 + 1 for i in range(120)]
    w6 = [(i * 91) % 70 + 1 for i in range(120)]
    for k in (1, 7, 60, 120):
        assert math.isclose(solution.min_cost_to_hire(q6, w6, k), _brute(q6, w6, k))
    print("✓ Test 6 passed: 120 workers vs. brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_min_cost_to_hire()
