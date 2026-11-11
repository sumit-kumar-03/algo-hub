"""
EPI 17.4 Extra Variant - Count 3-Sum Position Triples With Duplicates
(Practice problem, not in the book. Difficulty: Hard)
Builds on: sort + two pointers, extended to count every position triple
when the array holds runs of equal values (a run must be counted in bulk).

Problem:
Given an array of integers A and a target t, count the triples of positions
i < j < k with A[i] + A[j] + A[k] == t. Equal values at different
positions form different triples, so the answer can be much larger than
the number of distinct value triplets.

Constraints:
- 0 <= len(A) <= 3000, -10^5 <= A[i], t <= 10^5
- O(n^2) time; counting triples one by one is too slow when values repeat
  (e.g. 3000 zeros give about 4.5 * 10^9 triples)

How it works (sort, fix the first position, two pointers that count runs):
1. Sort A
2. For each first position k, set i = k + 1, j = n - 1, target = t - A[k];
   while i < j:
   - if A[i] + A[j] < target: i += 1; if greater: j -= 1
   - if equal and A[i] != A[j]: count the run of A[i]'s starting at i
     (length x) and the run of A[j]'s ending at j (length y); add x * y,
     then jump i and j past both runs
   - if equal and A[i] == A[j]: every pair inside [i, j] works; add
     m * (m - 1) / 2 where m = j - i + 1, and stop
3. Return the total
(Alternative: count the occurrences of each value and combine counts over
pairs of distinct values with combinatorics.)

Example 1:
Input: A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], t = 8
Output: 20
Explanation: (1, 2, 5) occurs 8 times, (1, 3, 4) 8 times, (2, 2, 4) 2 times,
and (2, 3, 3) 2 times.

Example 2:
Input: A = [1, 1, 2, 2, 2, 2], t = 5
Output: 12
Explanation: Pick one of the 2 ones and two of the 4 twos: 2 * 6 = 12.
"""

from typing import List


class Solution:
    def count_three_sum_triples(self, A: List[int], t: int) -> int:
        """
        Counts position triples i < j < k with A[i] + A[j] + A[k] == t.

        Args:
            A: Input integers (duplicates allowed)
            t: Target sum

        Returns:
            Number of position triples

        Time Complexity: O(n^2)
        Space Complexity: O(1) beyond sorting
        """
        # TODO: Implement sort + two pointers that count runs in bulk
        pass


def brute_count(A: List[int], t: int) -> int:
    """Counts triples directly (only for small inputs)."""
    n = len(A)
    return sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        for k in range(j + 1, n)
        if A[i] + A[j] + A[k] == t
    )


def test_count_three_sum_triples():
    """Test cases for counting 3-sum position triples"""
    solution = Solution()

    # Test case 1: Example 1
    assert solution.count_three_sum_triples([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8) == 20
    print("✓ Test 1 passed: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8 -> 20")

    # Test case 2: Example 2
    assert solution.count_three_sum_triples([1, 1, 2, 2, 2, 2], 5) == 12
    print("✓ Test 2 passed: [1, 1, 2, 2, 2, 2], 5 -> 12")

    # Test case 3: Too few entries
    assert solution.count_three_sum_triples([], 0) == 0
    assert solution.count_three_sum_triples([1, 2], 3) == 0
    print("✓ Test 3 passed: fewer than 3 entries -> 0")

    # Test case 4: Unsorted input with negatives
    A4 = [3, -1, 0, -2, 2, 1, -1, 0]
    assert solution.count_three_sum_triples(A4, 0) == brute_count(A4, 0)
    print(f"✓ Test 4 passed: mixed signs -> {brute_count(A4, 0)}")

    # Test case 5: All values equal
    assert solution.count_three_sum_triples([7] * 10, 21) == 120
    assert solution.count_three_sum_triples([7] * 10, 20) == 0
    print("✓ Test 5 passed: ten 7s -> C(10, 3) = 120")

    # Test case 6: Small arrays checked against brute force
    A6 = [0, 1, 2, 0, 1, 2, 3, 0, 3, 1, -1, 2, 4, -2, 0, 1]
    for target in range(-3, 10):
        assert solution.count_three_sum_triples(A6, target) == brute_count(A6, target)
    print("✓ Test 6 passed: every target from -3 to 9 matches brute force")

    # Test case 7: Large counts must be computed in bulk
    assert solution.count_three_sum_triples([0] * 3000, 0) == 4495501000
    A7 = [0] * 1500 + [1] * 1500
    assert solution.count_three_sum_triples(A7, 1) == 1500 * 1124250
    print("✓ Test 7 passed: 3000 entries with huge counts")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_three_sum_triples()
