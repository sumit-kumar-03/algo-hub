"""
EPI 16.12 Variant - Return a Longest Nondecreasing Subsequence

Problem:
Instead of only the length, return an actual longest nondecreasing
subsequence of the array (as a list of values in order). If several exist,
any one of them is accepted.

Constraints:
- 0 <= len(A) <= 10^4
- O(n^2) time (O(n log n) with predecessor tracking)

How it works (DP with predecessor links):
1. L[i] = longest nondecreasing subsequence length ending at i, and
   prev[i] = the index j that achieved it (or -1)
2. L[i] = 1 + max(L[j]) over j < i with A[j] <= A[i]; record that j
3. Start at the index with the largest L and follow prev back to -1
4. Reverse the collected values

Example 1:
Input: A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
Output: [0, 4, 10, 14] (or [0, 2, 6, 9], [0, 8, 12, 14], ...)

Example 2:
Input: A = [1, 3, 2, 2, 4, 1, 5]
Output: [1, 2, 2, 4, 5]
"""

from typing import List


class Solution:
    def longest_nondecreasing_subsequence(self, A: List[int]) -> List[int]:
        """
        Finds one longest nondecreasing subsequence.

        Args:
            A: Input numbers

        Returns:
            Values of a longest nondecreasing subsequence, in order

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        # TODO: Implement LNDS with reconstruction
        pass


def is_valid_lnds(result, A: List[int], expected_length: int) -> bool:
    """Checks result is a nondecreasing subsequence of A of the optimal length."""
    if not isinstance(result, list) or len(result) != expected_length:
        return False
    it = iter(A)
    is_subsequence = all(x in it for x in result)
    return is_subsequence and all(a <= b for a, b in zip(result, result[1:]))


def test_longest_nondecreasing_subsequence():
    """Test cases for returning a longest nondecreasing subsequence"""
    solution = Solution()

    # Test case 1: Book example (many valid answers)
    A1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
    r1 = solution.longest_nondecreasing_subsequence(A1)
    assert is_valid_lnds(r1, A1, 4)
    print(f"✓ Test 1 passed: book example -> {r1}")

    # Test case 2: Unique answer using duplicates
    assert solution.longest_nondecreasing_subsequence([1, 3, 2, 2, 4, 1, 5]) == [1, 2, 2, 4, 5]
    print("✓ Test 2 passed: [1, 3, 2, 2, 4, 1, 5] -> [1, 2, 2, 4, 5]")

    # Test case 3: Empty array
    assert solution.longest_nondecreasing_subsequence([]) == []
    print("✓ Test 3 passed: [] -> []")

    # Test case 4: Decreasing array, any single element works
    A4 = [5, 4, 3, 2, 1]
    r4 = solution.longest_nondecreasing_subsequence(A4)
    assert is_valid_lnds(r4, A4, 1)
    print(f"✓ Test 4 passed: decreasing -> {r4}")

    # Test case 5: Already sorted
    assert solution.longest_nondecreasing_subsequence([1, 1, 2, 3]) == [1, 1, 2, 3]
    print("✓ Test 5 passed: sorted array returned whole")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_longest_nondecreasing_subsequence()
