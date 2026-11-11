"""
EPI 5.15 - Compute a Random Subset

Problem:
Given a positive integer n and a size k <= n, return a size-k subset of
{0, 1, ..., n - 1} as a list. Every k-subset must be equally likely, and
every ordering of the returned list must be equally likely too. You may
use a uniform random integer generator (e.g. random.randrange).

Constraints:
- 0 <= k <= n; n can be huge (e.g. 10^12)
- Use O(k) time and O(k) space (do not build an array of size n)

How it works (Fisher-Yates on a virtual array backed by a hash table):
1. Imagine an array V with V[i] = i for all i; store only changed entries
   in a dict `changed` (missing key i means V[i] == i)
2. For i from 0 to k - 1:
   - Pick r uniformly from [i, n - 1]
   - Swap V[i] and V[r] by reading/writing through the dict
3. Return [V[0], V[1], ..., V[k - 1]]

Example 1:
Input: n = 100, k = 4
Output: e.g. [28, 42, 2, 76]
Explanation: Any 4 distinct values in [0, 99], in any order.

Example 2:
Input: n = 3, k = 3
Output: e.g. [2, 0, 1]
Explanation: All 6 orderings of {0, 1, 2} are equally likely.
"""

import random
from collections import Counter
from typing import List


class Solution:
    def random_subset(self, n: int, k: int) -> List[int]:
        """
        Returns a uniformly random size-k subset of {0, ..., n - 1}.

        Args:
            n: Size of the universe {0, ..., n - 1}
            k: Number of elements to choose, 0 <= k <= n

        Returns:
            List of k distinct integers in [0, n - 1], in uniformly random order

        Time Complexity: O(k)
        Space Complexity: O(k)
        """
        # TODO: Implement random subset with a sparse (hash table) array
        pass


def is_valid_subset(result: List[int], n: int, k: int) -> bool:
    """Checks size, range, and distinctness of the result."""
    return (
        isinstance(result, list)
        and len(result) == k
        and len(set(result)) == k
        and all(0 <= x < n for x in result)
    )


def test_random_subset():
    """Test cases for random subset (property-based, seeded)"""
    solution = Solution()
    random.seed(515)

    # Test case 1: Basic validity
    result = solution.random_subset(100, 4)
    assert is_valid_subset(result, 100, 4)
    print(f"✓ Test 1 passed: n = 100, k = 4 -> {result}")

    # Test case 2: k = 0 and k = n
    assert solution.random_subset(5, 0) == []
    full = solution.random_subset(5, 5)
    assert sorted(full) == [0, 1, 2, 3, 4]
    print("✓ Test 2 passed: k = 0 and k = n")

    # Test case 3: Huge n must not allocate O(n) memory
    big = solution.random_subset(10**12, 5)
    assert is_valid_subset(big, 10**12, 5)
    print(f"✓ Test 3 passed: n = 10^12, k = 5 -> {big}")

    # Test case 4: All 2-subsets of {0..3} are roughly equally likely
    subset_counts: Counter = Counter()
    for _ in range(6000):
        r = solution.random_subset(4, 2)
        assert is_valid_subset(r, 4, 2)
        subset_counts[frozenset(r)] += 1
    assert len(subset_counts) == 6
    assert all(800 <= c <= 1200 for c in subset_counts.values())
    print("✓ Test 4 passed: Subset frequencies are close to uniform")

    # Test case 5: All orderings are roughly equally likely
    order_counts: Counter = Counter()
    for _ in range(6000):
        order_counts[tuple(solution.random_subset(3, 3))] += 1
    assert len(order_counts) == 6
    assert all(800 <= c <= 1200 for c in order_counts.values())
    print("✓ Test 5 passed: Orderings of {0, 1, 2} are close to uniform")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_random_subset()
