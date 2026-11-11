"""
EPI 5.12 Extra Variant - Shuffle an Array Uniformly
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the partial Fisher-Yates loop from the main problem, run all
the way to the end.

Problem:
Given an array A, rearrange it in place into a uniformly random
permutation: each of the n! orderings must be equally likely. Use the
random module (random.randrange, random.randint, or random.random) as
the source of randomness.

A tempting bug: swapping A[i] with A[r] for r drawn from the whole array
[0, n - 1] at every step. That makes n^n equally likely outcomes, which
cannot split evenly over n! orderings, so some orderings come up more
often than others.

Constraints:
- 0 <= len(A) <= 10^5
- O(n) time, O(1) extra space, at most n random draws

How it works (Fisher-Yates):
1. For i from 0 to n - 2:
   - Pick r uniformly from [i, n - 1]
   - Swap A[i] and A[r]
2. Position i receives each remaining element with equal probability,
   so every ordering has probability 1 / n!

Example 1:
Input: A = [1, 2, 3]
Output: any of the 6 orderings, e.g. [2, 3, 1]
Explanation: Each ordering has probability 1/6.

Example 2:
Input: A = [42]
Output: [42]
"""

import random
from collections import Counter
from typing import Any, List


class Solution:
    def shuffle(self, A: List[Any]) -> None:
        """
        Shuffles A in place so every permutation is equally likely.

        Args:
            A: Array to shuffle in place

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Fisher-Yates shuffle
        pass


def test_shuffle():
    """Test cases for uniform shuffling (property-based, seeded)"""
    solution = Solution()
    random.seed(2024)

    # Test case 1: Empty and single-element arrays
    A1: List[Any] = []
    solution.shuffle(A1)
    assert A1 == []
    A2 = [42]
    solution.shuffle(A2)
    assert A2 == [42]
    print("✓ Test 1 passed: Empty and single element")

    # Test case 2: Result is a rearrangement of the input
    A3 = list(range(1000))
    solution.shuffle(A3)
    assert sorted(A3) == list(range(1000))
    print("✓ Test 2 passed: 1000 elements are all kept")

    # Test case 3: The array actually changes order
    A4 = list(range(50))
    solution.shuffle(A4)
    assert A4 != list(range(50))
    print("✓ Test 3 passed: Order changes")

    # Test case 4: All 6 orderings of 3 items are about equally likely
    counts: Counter = Counter()
    trials = 12000
    for _ in range(trials):
        A5 = [0, 1, 2]
        solution.shuffle(A5)
        counts[tuple(A5)] += 1
    assert len(counts) == 6
    assert all(1800 <= c <= 2200 for c in counts.values()), counts
    print("✓ Test 4 passed: 3-element orderings are close to uniform")

    # Test case 5: Each element lands in each position about equally often
    n = 5
    position_counts = [[0] * n for _ in range(n)]
    trials = 10000
    for _ in range(trials):
        A6 = list(range(n))
        solution.shuffle(A6)
        for pos, value in enumerate(A6):
            position_counts[value][pos] += 1
    assert all(1700 <= c <= 2300 for row in position_counts for c in row)
    print("✓ Test 5 passed: Positions are close to uniform for n = 5")

    # Test case 6: Works with duplicates and non-integer items
    A7 = ["a", "b", "a", "c"]
    solution.shuffle(A7)
    assert sorted(A7) == ["a", "a", "b", "c"]
    print(f"✓ Test 6 passed: {A7}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shuffle()
