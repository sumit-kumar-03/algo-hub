"""
EPI 15.1 Extra Variant - K-th Symbol in a Self-Similar Grammar
(Practice problem, not in the book. Difficulty: Easy)
Builds on: Hanoi's self-similar recursion (the size-n answer is built from
the size n - 1 answer), used here to jump straight to one position.

Problem:
Build a table of rows of 0s and 1s. Row 1 is "0". Every later row is made
from the row above it by replacing each 0 with "01" and each 1 with "10".
So row 2 is "01", row 3 is "0110", and row 4 is "01101001". Given n and k,
return the k-th symbol (1-indexed) of row n as an int. Row n has 2^(n-1)
symbols, so building the row is not an option for large n.

Constraints:
- 1 <= n <= 60
- 1 <= k <= 2^(n-1)
- O(n) time, without building any row

How it works (recurse on the parent symbol):
1. Symbol k of row n was produced by symbol ceil(k / 2) of row n - 1
2. If k is odd it is the first child, which equals its parent; if k is even
   it is the second child, which is the flip of its parent
3. Base case: row 1, position 1 is 0
(Bonus: the answer is the parity of the number of 1 bits in k - 1.)

Example 1:
Input: n = 3, k = 2
Output: 1
Explanation: Row 3 is "0110".

Example 2:
Input: n = 4, k = 5
Output: 1
Explanation: Row 4 is "01101001"; its 5th symbol is 1.
"""


class Solution:
    def kth_symbol(self, n: int, k: int) -> int:
        """
        Returns the k-th symbol (1-indexed) of row n of the grammar.

        Args:
            n: Row number, starting at 1
            k: Position in the row, starting at 1

        Returns:
            0 or 1

        Time Complexity: O(n)
        Space Complexity: O(n) recursion depth (O(1) if done iteratively)
        """
        # TODO: Implement the recursion on the parent symbol
        pass


def build_row(n: int) -> str:
    """Builds row n directly (only for small n)."""
    row = "0"
    for _ in range(n - 1):
        row = "".join("01" if c == "0" else "10" for c in row)
    return row


def test_kth_symbol():
    """Test cases for the k-th symbol in the grammar"""
    solution = Solution()

    # Test case 1: The very first row
    assert solution.kth_symbol(1, 1) == 0
    print("✓ Test 1 passed: n=1, k=1 -> 0")

    # Test case 2: Row 2
    assert solution.kth_symbol(2, 1) == 0 and solution.kth_symbol(2, 2) == 1
    print("✓ Test 2 passed: row 2 is 01")

    # Test case 3: Examples from the statement
    assert solution.kth_symbol(3, 2) == 1
    assert solution.kth_symbol(4, 5) == 1
    print("✓ Test 3 passed: (3, 2) -> 1 and (4, 5) -> 1")

    # Test case 4: Every position of rows 1..10 matches a built row
    for n in range(1, 11):
        row = build_row(n)
        for k in range(1, len(row) + 1):
            assert solution.kth_symbol(n, k) == int(row[k - 1])
    print("✓ Test 4 passed: rows 1..10 match the built rows")

    # Test case 5: Last position of a huge row
    assert solution.kth_symbol(60, 2 ** 59) == 1
    print("✓ Test 5 passed: n=60, k=2^59 -> 1")

    # Test case 6: An arbitrary position of a huge row
    k6 = 123456789012345
    assert solution.kth_symbol(60, k6) == bin(k6 - 1).count("1") % 2
    print(f"✓ Test 6 passed: n=60, k={k6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_kth_symbol()
