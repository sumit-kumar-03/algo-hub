"""
EPI 5.12 - Sample Offline Data

Problem:
Given an array of distinct elements and a size k, pick a random subset of
k elements such that every k-element subset is equally likely. Return the
result inside the input array itself: after the call, A[:k] holds the
sample and A as a whole is still a rearrangement of the original elements.

Constraints:
- 0 <= k <= len(A) <= 10^5
- Elements of A are distinct
- Use O(1) extra space and O(k) time (k calls to the random generator)

How it works (partial Fisher-Yates shuffle):
1. For i from 0 to k - 1:
   - Pick r uniformly at random from [i, len(A) - 1]
   - Swap A[i] and A[r]
2. A[:k] now holds a uniformly random k-subset (built by extending a
   random subset of size i by one random element from the rest)

Example 1:
Input: A = [3, 7, 5, 11], k = 3
Output: A[:3] is any 3 of the 4 elements, e.g. [11, 3, 5]
Explanation: Each of the 4 possible 3-subsets appears with probability 1/4.

Example 2:
Input: A = [1, 2, 3], k = 0
Output: A[:0] == []
Explanation: An empty sample; A is just some arrangement of its elements.
"""

import random
from collections import Counter
from typing import Any, List


class Solution:
    def random_sampling(self, k: int, A: List[Any]) -> None:
        """
        Places a uniformly random k-subset of A into A[:k], in place.

        Args:
            k: Sample size, 0 <= k <= len(A)
            A: Distinct elements (rearranged in place)

        Returns:
            None (the sample is A[:k] after the call)

        Time Complexity: O(k)
        Space Complexity: O(1)
        """
        # TODO: Implement offline sampling
        pass


def is_valid_sample(original: List[Any], A: List[Any], k: int) -> bool:
    """Checks that A is a rearrangement of original and A[:k] has k distinct items."""
    return sorted(A) == sorted(original) and len(set(A[:k])) == k


def test_random_sampling():
    """Test cases for offline sampling (property-based, seeded)"""
    solution = Solution()
    random.seed(512)

    # Test case 1: Book-sized example
    A1 = [3, 7, 5, 11]
    solution.random_sampling(3, A1)
    assert is_valid_sample([3, 7, 5, 11], A1, 3)
    print(f"✓ Test 1 passed: k = 3 sample {A1[:3]}")

    # Test case 2: k = 0 and k = n
    A2 = [1, 2, 3]
    solution.random_sampling(0, A2)
    assert sorted(A2) == [1, 2, 3]
    A3 = list("abcde")
    solution.random_sampling(5, A3)
    assert is_valid_sample(list("abcde"), A3, 5)
    print("✓ Test 2 passed: k = 0 and k = n")

    # Test case 3: Larger array keeps all elements
    original = list(range(100))
    A4 = list(original)
    solution.random_sampling(10, A4)
    assert is_valid_sample(original, A4, 10)
    print(f"✓ Test 3 passed: 10 of 100 -> {sorted(A4[:10])}")

    # Test case 4: Sample is not always the same (randomness is used)
    samples = set()
    for _ in range(50):
        A5 = list(range(10))
        solution.random_sampling(3, A5)
        samples.add(frozenset(A5[:3]))
    assert len(samples) > 1
    print(f"✓ Test 4 passed: {len(samples)} distinct samples in 50 runs")

    # Test case 5: All 6 two-element subsets of 4 items are roughly equally likely
    counts: Counter = Counter()
    trials = 6000
    for _ in range(trials):
        A6 = [0, 1, 2, 3]
        solution.random_sampling(2, A6)
        assert is_valid_sample([0, 1, 2, 3], A6, 2)
        counts[frozenset(A6[:2])] += 1
    assert len(counts) == 6
    assert all(800 <= c <= 1200 for c in counts.values())
    print("✓ Test 5 passed: Subset frequencies are close to uniform")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_random_sampling()
