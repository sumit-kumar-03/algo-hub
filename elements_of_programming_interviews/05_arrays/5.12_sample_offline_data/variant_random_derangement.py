"""
EPI 5.12 Extra Variant - Uniformly Random Derangement
(Practice problem, not in the book. Difficulty: Medium)
Builds on: Fisher-Yates sampling plus rejection, and knowing why a
"cleverer" tweak of the swap range is not uniform.

Problem:
A derangement of 0..n-1 is a permutation P with P[i] != i for every i
(nobody draws their own name in a gift exchange). Given n >= 2, return a
derangement chosen uniformly at random from all derangements of size n.
Use the random module as the source of randomness.

Watch out: Sattolo's algorithm (always swapping with a strictly smaller
index) does produce derangements, but only single-cycle ones, so it
never returns e.g. [1, 0, 3, 2] and is not uniform over all derangements.

Constraints:
- 2 <= n <= 10^5
- Expected O(n) time

How it works (shuffle and retry):
1. Shuffle P = [0, 1, ..., n - 1] with Fisher-Yates
2. If some P[i] == i, throw it away and shuffle again
3. Every permutation is equally likely, so conditioning on "no fixed
   point" leaves every derangement equally likely. About 1/e of all
   permutations are derangements, so the expected number of tries is
   about e (under 3); you can also stop a try early at the first fixed
   point

Example 1:
Input: n = 2
Output: [1, 0]
Explanation: The only derangement of size 2.

Example 2:
Input: n = 3
Output: [1, 2, 0] or [2, 0, 1]
Explanation: Each with probability 1/2.
"""

import random
from collections import Counter
from typing import List


class Solution:
    def random_derangement(self, n: int) -> List[int]:
        """
        Returns a uniformly random permutation of 0..n-1 with no fixed point.

        Args:
            n: Size of the permutation, n >= 2

        Returns:
            A list P with P[i] != i for all i

        Time Complexity: O(n) expected
        Space Complexity: O(n) for the output
        """
        # TODO: Implement uniform random derangement
        pass


def is_derangement(P: List[int], n: int) -> bool:
    """Checks that P is a permutation of 0..n-1 with no fixed point."""
    return (
        P is not None
        and sorted(P) == list(range(n))
        and all(P[i] != i for i in range(n))
    )


def test_random_derangement():
    """Test cases for random derangements (property-based, seeded)"""
    solution = Solution()
    random.seed(9)

    # Test case 1: n = 2 has one answer
    assert solution.random_derangement(2) == [1, 0]
    print("✓ Test 1 passed: n = 2 -> [1, 0]")

    # Test case 2: n = 3 gives one of two answers
    for _ in range(20):
        assert solution.random_derangement(3) in ([1, 2, 0], [2, 0, 1])
    print("✓ Test 2 passed: n = 3")

    # Test case 3: Valid for many sizes
    for n in range(2, 60):
        assert is_derangement(solution.random_derangement(n), n)
    print("✓ Test 3 passed: Valid for n = 2..59")

    # Test case 4: All 9 derangements of size 4 are about equally likely,
    # including the two-swap ones like [1, 0, 3, 2]
    counts: Counter = Counter()
    trials = 9000
    for _ in range(trials):
        P = solution.random_derangement(4)
        assert is_derangement(P, 4)
        counts[tuple(P)] += 1
    assert len(counts) == 9
    assert counts[(1, 0, 3, 2)] > 0
    assert all(800 <= c <= 1200 for c in counts.values()), counts
    print("✓ Test 4 passed: Size-4 derangements are close to uniform")

    # Test case 5: Large n
    P = solution.random_derangement(100000)
    assert is_derangement(P, 100000)
    print("✓ Test 5 passed: n = 100,000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_random_derangement()
