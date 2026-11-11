"""
EPI 12.6 Variant - Rearrange to Maximize the Shortest Covering Subarray

Problem:
Given an array A, return a rearrangement of its elements such that the
shortest subarray containing every distinct value of A is as long as
possible.

Constraints:
- 0 <= len(A) <= 10^5
- O(n log n) time (O(n) with counting), O(n) space
- Any rearrangement achieving the maximum is accepted

How it works:
1. Count the occurrences of each distinct value
2. Group equal values into contiguous blocks
3. A covering subarray must reach from inside the first block to inside the
   last block, so it always contains every middle block in full plus one
   element of each end block
4. To make this as long as possible, put the two least frequent values at
   the two ends and everything else in between; the shortest covering
   subarray then has length n - c1 - c2 + 2, where c1 <= c2 are the two
   smallest counts (or 1 if there is only one distinct value)

Example 1:
Input: A = [1, 2, 3, 3, 3, 2]
Output: [1, 3, 3, 3, 2, 2] (or another arrangement of equal quality)
Explanation: The shortest subarray holding 1, 2, and 3 is [1, 3, 3, 3, 2],
of length 5, which is the best possible.

Example 2:
Input: A = [7, 7, 7]
Output: [7, 7, 7]
Explanation: With one distinct value, every arrangement gives length 1.
"""

from typing import List


class Solution:
    def maximize_shortest_covering_subarray(self, A: List[int]) -> List[int]:
        """
        Rearranges A so its shortest all-values subarray is as long as possible.

        Args:
            A: Input array

        Returns:
            A rearrangement of A achieving the maximum possible length for the
            shortest subarray containing all distinct values

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement rearrangement maximizing the shortest covering subarray
        pass


def _shortest_covering_length(A: List[int]) -> int:
    """Brute-force length of the shortest subarray containing all distinct values."""
    distinct = len(set(A))
    best = len(A)
    for i in range(len(A)):
        seen = set()
        for j in range(i, len(A)):
            seen.add(A[j])
            if len(seen) == distinct:
                best = min(best, j - i + 1)
                break
    return best


def _check(A: List[int], result: List[int], expected_length: int) -> bool:
    """Checks result is a permutation of A with the expected shortest length."""
    return (
        result is not None
        and sorted(result) == sorted(A)
        and _shortest_covering_length(result) == expected_length
    )


def test_maximize_shortest_covering_subarray():
    """Test cases for maximizing the shortest covering subarray"""
    solution = Solution()

    # Test case 1: Book-style small example
    A1 = [1, 2, 3, 3, 3, 2]
    assert _check(A1, solution.maximize_shortest_covering_subarray(list(A1)), 5)
    print("✓ Test 1 passed: [1, 2, 3, 3, 3, 2] -> length 5")

    # Test case 2: Single distinct value
    A2 = [7, 7, 7]
    assert _check(A2, solution.maximize_shortest_covering_subarray(list(A2)), 1)
    print("✓ Test 2 passed: One distinct value -> length 1")

    # Test case 3: Two distinct values
    A3 = [1, 2, 1, 2, 1]
    assert _check(A3, solution.maximize_shortest_covering_subarray(list(A3)), 2)
    print("✓ Test 3 passed: Two distinct values -> length 2")

    # Test case 4: All distinct values, whole array is needed
    A4 = [4, 2, 9, 1]
    assert _check(A4, solution.maximize_shortest_covering_subarray(list(A4)), 4)
    print("✓ Test 4 passed: All distinct -> length 4")

    # Test case 5: Mixed counts
    A5 = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4]
    assert _check(A5, solution.maximize_shortest_covering_subarray(list(A5)), 9)
    print("✓ Test 5 passed: Mixed counts -> length 9")

    # Test case 6: Empty array
    assert solution.maximize_shortest_covering_subarray([]) == []
    print("✓ Test 6 passed: Empty array -> []")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_maximize_shortest_covering_subarray()
