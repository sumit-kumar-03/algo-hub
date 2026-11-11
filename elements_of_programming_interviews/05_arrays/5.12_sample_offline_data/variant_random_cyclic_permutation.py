"""
EPI 5.12 Extra Variant - Uniformly Random Single-Cycle Permutation
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the Fisher-Yates swap loop, with a one-character change to the
range of the random index that changes which permutations it can produce.

Problem:
Think of a permutation P of 0..n-1 as "i points to P[i]". It is a single
cycle if starting at 0 and following the pointers visits all n positions
before returning to 0 (think of a random "secret Santa" ring). Given n,
return such a permutation chosen uniformly at random from all (n - 1)!
single-cycle permutations. Use the random module as the source of
randomness.

Constraints:
- 0 <= n <= 10^5 (n = 0 gives [], n = 1 gives [0])
- O(n) time, n - 1 random draws

How it works (Sattolo's algorithm):
1. P = [0, 1, ..., n - 1]
2. For i from n - 1 down to 1:
   - Pick r uniformly from [0, i - 1] (note: never r == i)
   - Swap P[i] and P[r]
3. Forbidding r == i means no element is ever left in place, and each
   swap merges the cycle containing i into one cycle; there are exactly
   (n - 1)! sequences of choices, one per cyclic permutation

Example 1:
Input: n = 3
Output: [1, 2, 0] or [2, 0, 1]
Explanation: 0 -> 1 -> 2 -> 0, or 0 -> 2 -> 1 -> 0; each has probability
1/2.

Example 2:
Input: n = 2
Output: [1, 0]
"""

import random
from collections import Counter
from typing import List


class Solution:
    def random_cycle(self, n: int) -> List[int]:
        """
        Returns a uniformly random permutation of 0..n-1 that is one cycle.

        Args:
            n: Number of positions

        Returns:
            A list P where following i -> P[i] from 0 visits every index

        Time Complexity: O(n)
        Space Complexity: O(n) for the output
        """
        # TODO: Implement Sattolo's algorithm
        pass


def is_single_cycle(P: List[int]) -> bool:
    """Checks that P is a permutation of 0..n-1 forming one cycle."""
    n = len(P)
    if sorted(P) != list(range(n)):
        return False
    if n == 0:
        return True
    steps, i = 0, 0
    while True:
        i = P[i]
        steps += 1
        if i == 0:
            return steps == n


def test_random_cycle():
    """Test cases for random cyclic permutations (property-based, seeded)"""
    solution = Solution()
    random.seed(77)

    # Test case 1: Tiny sizes with a single possible answer
    assert solution.random_cycle(0) == []
    assert solution.random_cycle(1) == [0]
    assert solution.random_cycle(2) == [1, 0]
    print("✓ Test 1 passed: n = 0, 1, 2")

    # Test case 2: n = 3 gives one of the two cycles
    for _ in range(20):
        assert solution.random_cycle(3) in ([1, 2, 0], [2, 0, 1])
    print("✓ Test 2 passed: n = 3 gives a 3-cycle")

    # Test case 3: Always a single cycle for many sizes
    for n in range(4, 40):
        assert is_single_cycle(solution.random_cycle(n))
    print("✓ Test 3 passed: Single cycle for n = 4..39")

    # Test case 4: All 6 cycles of length 4 are about equally likely
    counts: Counter = Counter()
    trials = 12000
    for _ in range(trials):
        P = solution.random_cycle(4)
        assert is_single_cycle(P)
        counts[tuple(P)] += 1
    assert len(counts) == 6
    assert all(1800 <= c <= 2200 for c in counts.values()), counts
    print("✓ Test 4 passed: 4-cycles are close to uniform")

    # Test case 5: Large n is a single cycle
    P = solution.random_cycle(100000)
    assert is_single_cycle(P)
    print("✓ Test 5 passed: n = 100,000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_random_cycle()
