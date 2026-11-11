"""
EPI 11.4 Extra Variant - kth Smallest Entry of a Multiplication Table
(Practice problem, not in the book. Difficulty: Hard)
Builds on: binary search over candidate answers with a monotone test; the
answer is the first value whose "how many entries are <= it" count reaches
the target.

Problem:
An m x n multiplication table has the entry i * j in row i and column j
(1 <= i <= m, 1 <= j <= n). Given m, n, and k, return the kth smallest
entry of the table, counting repeated values separately.

Constraints:
- 1 <= m, n <= 3 * 10^4; 1 <= k <= m * n
- O(min(m, n) * log(m * n)) time, O(1) space; do not build the table
  (it can have 9 * 10^8 entries)

How it works (binary search on the value):
1. count(x) = number of entries <= x = sum over rows i of min(x // i, n);
   it is nondecreasing in x
2. Find the smallest x in [1, m * n] with count(x) >= k
3. That x is always an actual table entry: if it were not, count(x - 1)
   would equal count(x), contradicting minimality
4. Loop over the shorter dimension in count() to get the stated bound

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: Entries in order are 1, 2, 2, 3, 3, 4, 6, 6, 9.

Example 2:
Input: m = 2, n = 3, k = 6
Output: 6
"""


class Solution:
    def kth_smallest_entry(self, m: int, n: int, k: int) -> int:
        """
        Returns the kth smallest entry of the m x n multiplication table.

        Args:
            m: Number of rows
            n: Number of columns
            k: 1-based rank

        Returns:
            The kth smallest value of i * j

        Time Complexity: O(min(m, n) * log(m * n))
        Space Complexity: O(1)
        """
        # TODO: Implement binary search on the value with a counting test
        pass


def _slow(m: int, n: int, k: int) -> int:
    return sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))[k - 1]


def test_kth_smallest_entry():
    """Test cases for kth smallest in a multiplication table"""
    solution = Solution()

    # Test case 1: 3 x 3 table, every rank
    expected1 = [1, 2, 2, 3, 3, 4, 6, 6, 9]
    assert [solution.kth_smallest_entry(3, 3, k) for k in range(1, 10)] == expected1
    print("✓ Test 1 passed: 3 x 3, all ranks")

    # Test case 2: Last entry of a rectangular table
    assert solution.kth_smallest_entry(2, 3, 6) == 6
    print("✓ Test 2 passed: 2 x 3, k = 6")

    # Test case 3: 1 x 1 and a single row
    assert solution.kth_smallest_entry(1, 1, 1) == 1
    assert solution.kth_smallest_entry(1, 10, 7) == 7
    print("✓ Test 3 passed: Degenerate tables")

    # Test case 4: m and n swapped give the same answers
    for k in (1, 13, 40, 77):
        assert solution.kth_smallest_entry(7, 11, k) == solution.kth_smallest_entry(11, 7, k)
    print("✓ Test 4 passed: Symmetry")

    # Test case 5: Medium tables vs. sorting
    for m, n in ((9, 14), (20, 5), (17, 17)):
        for k in (1, m * n // 3, m * n // 2, m * n):
            assert solution.kth_smallest_entry(m, n, k) == _slow(m, n, k)
    print("✓ Test 5 passed: Medium tables")

    # Test case 6: Huge tables
    assert solution.kth_smallest_entry(30000, 30000, 1) == 1
    assert solution.kth_smallest_entry(30000, 30000, 900000000) == 900000000
    assert solution.kth_smallest_entry(30000, 30000, 450000000) == 168028638
    print("✓ Test 6 passed: 30000 x 30000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_smallest_entry()
