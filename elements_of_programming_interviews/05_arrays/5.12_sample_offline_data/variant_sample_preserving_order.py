"""
EPI 5.12 Extra Variant - Random Sample in Original Order
(Practice problem, not in the book. Difficulty: Medium)
Builds on: building a uniform k-subset one decision at a time, but with
the decisions made left to right instead of by swapping.

Problem:
Given an array A of distinct elements and a size k, return a new list of
k elements of A chosen so that every k-element subset is equally likely,
and listed in the same relative order as they appear in A. Do not modify
A, and do not sort: make one left-to-right pass over A. Use the random
module as the source of randomness.

Constraints:
- 0 <= k <= len(A) <= 10^5; elements of A are distinct
- O(n) time, one pass, O(1) extra space beyond the output list

How it works (selection sampling):
1. needed = k. For i from 0 to n - 1 (remaining = n - i elements left,
   including A[i]):
   - Take A[i] with probability needed / remaining (e.g. compare
     random.randrange(remaining) < needed)
   - If taken, append it and decrement needed
2. When needed equals remaining every element is forced in, and when
   needed is 0 none are, so the output always has exactly k elements.
   Each subset ends up with probability 1 / C(n, k)

Example 1:
Input: A = [10, 20, 30, 40], k = 2
Output: one of [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40]
Explanation: Each pair has probability 1/6 and keeps the order of A.

Example 2:
Input: A = [5, 6, 7], k = 3
Output: [5, 6, 7]
"""

import random
from collections import Counter
from typing import Any, List


class Solution:
    def sample_in_order(self, A: List[Any], k: int) -> List[Any]:
        """
        Returns a uniformly random k-subset of A in A's order.

        Args:
            A: Distinct elements (not modified)
            k: Sample size, 0 <= k <= len(A)

        Returns:
            A list of k elements of A, in their original relative order

        Time Complexity: O(n)
        Space Complexity: O(1) beyond the output
        """
        # TODO: Implement order-preserving selection sampling
        pass


def is_ordered_sample(A: List[Any], S: List[Any], k: int) -> bool:
    """Checks that S has k items and is a subsequence of A."""
    if S is None or len(S) != k:
        return False
    it = iter(A)
    return all(any(x == y for y in it) for x in S)


def test_sample_in_order():
    """Test cases for order-preserving sampling (property-based, seeded)"""
    solution = Solution()
    random.seed(1212)

    # Test case 1: k = 0 and k = n
    assert solution.sample_in_order([1, 2, 3], 0) == []
    assert solution.sample_in_order([5, 6, 7], 3) == [5, 6, 7]
    assert solution.sample_in_order([], 0) == []
    print("✓ Test 1 passed: k = 0, k = n, empty array")

    # Test case 2: Input is not modified and output keeps the order
    A = list(range(100, 0, -1))
    S = solution.sample_in_order(A, 10)
    assert A == list(range(100, 0, -1))
    assert is_ordered_sample(A, S, 10)
    print(f"✓ Test 2 passed: 10 of 100 -> {S}")

    # Test case 3: Every run gives exactly k items in order
    for _ in range(200):
        S = solution.sample_in_order(list("abcdefgh"), 3)
        assert is_ordered_sample(list("abcdefgh"), S, 3)
    print("✓ Test 3 passed: 200 samples of size 3 are valid")

    # Test case 4: All 6 pairs of 4 items are about equally likely
    counts: Counter = Counter()
    trials = 12000
    for _ in range(trials):
        counts[tuple(solution.sample_in_order([10, 20, 30, 40], 2))] += 1
    assert set(counts) == {(10, 20), (10, 30), (10, 40), (20, 30), (20, 40), (30, 40)}
    assert all(1800 <= c <= 2200 for c in counts.values()), counts
    print("✓ Test 4 passed: Pairs are close to uniform")

    # Test case 5: Each element is chosen with probability k / n
    hits = Counter()
    trials = 5000
    for _ in range(trials):
        hits.update(solution.sample_in_order(list(range(10)), 3))
    assert all(1300 <= hits[v] <= 1700 for v in range(10)), hits
    print("✓ Test 5 passed: Inclusion rate is about 3/10 for every element")

    # Test case 6: Large input
    A = list(range(100000))
    S = solution.sample_in_order(A, 500)
    assert len(S) == 500 and S == sorted(set(S))
    print("✓ Test 6 passed: 500 of 100,000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_sample_in_order()
