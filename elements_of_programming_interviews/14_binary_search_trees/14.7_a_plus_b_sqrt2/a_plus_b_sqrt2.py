"""
EPI 14.7 - Enumerate Numbers of the Form a + b*sqrt(2)

Problem:
Consider all numbers a + b*sqrt(2) where a and b are nonnegative integers.
Return the k smallest such numbers in increasing order. Because sqrt(2) is
irrational, different (a, b) pairs always give different values, so the
list contains no repeats.

Constraints:
- 0 <= k <= 10^4
- Target: O(k) time with the two-pointer method (O(k log k) with a BST or
  heap of candidates is also acceptable)
- Generating all k^2 pairs and sorting them is too slow

How it works (two pointers over the result):
1. Start with result = [0] (a = 0, b = 0) and two indices i = j = 0
2. The next value is min(result[i] + 1, result[j] + sqrt(2))
3. Append it; advance i if it came from result[i] + 1, advance j if it came
   from result[j] + sqrt(2) (advance both on a tie, to avoid duplicates)
4. Repeat until the result has k values
Tip: track (a, b) pairs and compare those to avoid floating-point ties.

Example 1:
Input: k = 5
Output: [0.0, 1.0, 1.414..., 2.0, 2.414...]
Explanation: 0, 1, sqrt(2), 2, 1 + sqrt(2).

Example 2:
Input: k = 8
Output: [0.0, 1.0, 1.414..., 2.0, 2.414..., 2.828..., 3.0, 3.414...]
"""

import math
from typing import List


class Solution:
    def generate_first_k_a_b_sqrt2(self, k: int) -> List[float]:
        """
        Returns the k smallest numbers of the form a + b*sqrt(2), a, b >= 0.

        Args:
            k: How many numbers to generate

        Returns:
            The k smallest values in increasing order

        Time Complexity: O(k)
        Space Complexity: O(k)
        """
        # TODO: Implement two-pointer enumeration
        pass


def brute_force(k: int) -> List[float]:
    """Slow reference used only by the tests: sort all a, b < k."""
    values = sorted(a + b * math.sqrt(2) for a in range(k) for b in range(k))
    return values[:k]


def same_values(actual: List[float], expected: List[float]) -> bool:
    """Compares two float lists with a small tolerance."""
    return len(actual) == len(expected) and all(
        math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-9)
        for x, y in zip(actual, expected)
    )


def test_generate_first_k_a_b_sqrt2():
    """Test cases for enumerating a + b*sqrt(2)"""
    solution = Solution()
    r2 = math.sqrt(2)

    # Test case 1: k = 0
    assert solution.generate_first_k_a_b_sqrt2(0) == []
    print("✓ Test 1 passed: k=0 -> []")

    # Test case 2: k = 1
    assert same_values(solution.generate_first_k_a_b_sqrt2(1), [0.0])
    print("✓ Test 2 passed: k=1 -> [0.0]")

    # Test case 3: Book-style example
    expected3 = [0, 1, r2, 2, 1 + r2]
    assert same_values(solution.generate_first_k_a_b_sqrt2(5), expected3)
    print("✓ Test 3 passed: k=5 -> [0, 1, 1.414, 2, 2.414]")

    # Test case 4: Includes the 2*sqrt(2) vs 3 ordering
    expected4 = [0, 1, r2, 2, 1 + r2, 2 * r2, 3, 2 + r2]
    assert same_values(solution.generate_first_k_a_b_sqrt2(8), expected4)
    print("✓ Test 4 passed: k=8")

    # Test case 5: Matches brute force for a medium k
    assert same_values(solution.generate_first_k_a_b_sqrt2(60), brute_force(60))
    print("✓ Test 5 passed: k=60 matches brute force")

    # Test case 6: Larger k is strictly increasing and matches brute force
    result6 = solution.generate_first_k_a_b_sqrt2(300)
    assert all(x < y for x, y in zip(result6, result6[1:]))
    assert same_values(result6, brute_force(300))
    print("✓ Test 6 passed: k=300 strictly increasing, matches brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_generate_first_k_a_b_sqrt2()
