"""
EPI 11.10 - Find the Duplicate and Missing Elements

Problem:
An array of n integers contains values from 0 to n - 1. Exactly one value
appears twice, so exactly one value in 0..n - 1 is missing. Return the
duplicate and the missing value.

Constraints:
- 2 <= n <= 10^5
- O(n) time, O(1) extra space: no hash set, no sorting, do not modify A
- Avoid sum-of-squares or product tricks (huge intermediate numbers)

How it works (XOR):
1. XOR all indices 0..n - 1 together with all entries: everything cancels
   except missing ^ duplicate (nonzero, since they differ)
2. Pick any set bit of that XOR (e.g., the lowest); missing and duplicate
   differ in that bit
3. XOR only the indices and the entries that have that bit set; the result is
   either the missing or the duplicate value
4. One more pass tells which: if it appears in A it is the duplicate;
   the other value is the first XOR combined with this one

Example 1:
Input: A = [5, 3, 0, 3, 1, 2]
Output: (3, 4)
Explanation: 3 appears twice, 4 never appears.

Example 2:
Input: A = [0, 0]
Output: (0, 1)
"""

from typing import List, Tuple


class Solution:
    def find_duplicate_missing(self, A: List[int]) -> Tuple[int, int]:
        """
        Finds the duplicated and the missing value.

        Args:
            A: n integers in [0, n - 1] with one duplicate and one missing

        Returns:
            (duplicate, missing)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement with XOR and bit partitioning
        pass


def test_find_duplicate_missing():
    """Test cases for duplicate and missing elements"""
    solution = Solution()

    # Test case 1: Book example
    A = [5, 3, 0, 3, 1, 2]
    original = list(A)
    assert tuple(solution.find_duplicate_missing(A)) == (3, 4)
    assert A == original
    print("✓ Test 1 passed: Book example -> (3, 4), input unchanged")

    # Test case 2: Smallest input
    assert tuple(solution.find_duplicate_missing([0, 0])) == (0, 1)
    assert tuple(solution.find_duplicate_missing([1, 1])) == (1, 0)
    print("✓ Test 2 passed: n = 2")

    # Test case 3: Missing 0
    assert tuple(solution.find_duplicate_missing([1, 2, 3, 3])) == (3, 0)
    print("✓ Test 3 passed: Missing 0")

    # Test case 4: Missing the largest value
    assert tuple(solution.find_duplicate_missing([0, 1, 2, 3, 2])) == (2, 4)
    print("✓ Test 4 passed: Missing n - 1")

    # Test case 5: Duplicate and missing differing in a high bit
    n = 1000
    B = [i for i in range(n) if i != 1] + [512]
    B = B[::-1]
    assert tuple(solution.find_duplicate_missing(B)) == (512, 1)
    print("✓ Test 5 passed: n = 1000")

    # Test case 6: Exhaustive small cases
    for n in range(2, 9):
        for dup in range(n):
            for miss in range(n):
                if dup == miss:
                    continue
                C = [x for x in range(n) if x != miss] + [dup]
                C = C[1::2] + C[0::2]
                assert tuple(solution.find_duplicate_missing(C)) == (dup, miss)
    print("✓ Test 6 passed: All (duplicate, missing) pairs for n = 2..8")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_duplicate_missing()
