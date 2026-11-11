"""
EPI 15.2 Extra Variant - Complete a Partial n-Queens Placement
(Practice problem, not in the book. Difficulty: Easy)
Builds on: row-by-row backtracking with column and diagonal checks, but
stopping at the first success instead of enumerating everything.

Problem:
Queens have already been placed in the first k rows of an n x n board:
prefix[i] is the column of the queen in row i, for i < k. Extend the
placement to all n rows so that no two queens share a row, a column, or a
diagonal. Return one complete placement (a list of n columns that starts
with prefix), or an empty list if the prefix already has two attacking
queens or cannot be completed.

Constraints:
- 1 <= n <= 14, 0 <= len(prefix) <= n, 0 <= prefix[i] < n
- Any valid completion is accepted
- Stop the search as soon as one completion is found

How it works (backtracking that returns early):
1. Check the prefix itself: record its columns and both diagonals
   (row - col and row + col) in sets; if any repeats, return []
2. From row k on, try each free column, recurse, and undo on failure
3. As soon as row n is reached, return the placement up the call chain
4. If every choice fails, return []

Example 1:
Input: n = 4, prefix = [1]
Output: [1, 3, 0, 2]

Example 2:
Input: n = 4, prefix = [0]
Output: []
Explanation: Neither 4-queens solution has a queen in the corner.
"""

from typing import List


class Solution:
    def complete_queens(self, n: int, prefix: List[int]) -> List[int]:
        """
        Extends a partial placement of queens to a full nonattacking one.

        Args:
            n: Board size
            prefix: Columns of the queens already placed in rows 0..k-1

        Returns:
            A full placement starting with prefix, or [] if impossible

        Time Complexity: O(n!) in the worst case, usually far less
        Space Complexity: O(n)
        """
        # TODO: Implement early-exit backtracking from row len(prefix)
        pass


def is_valid_placement(n: int, placement: List[int]) -> bool:
    """Checks that a placement has n queens and no two attack each other."""
    if len(placement) != n or any(not 0 <= c < n for c in placement):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if placement[i] == placement[j] or abs(placement[i] - placement[j]) == j - i:
                return False
    return True


def is_completion(n: int, prefix: List[int], result) -> bool:
    """Checks result is a valid placement that extends prefix."""
    return (
        isinstance(result, list)
        and is_valid_placement(n, result)
        and result[: len(prefix)] == prefix
    )


def test_complete_queens():
    """Test cases for completing a partial n-Queens placement"""
    solution = Solution()

    # Test case 1: Single square
    assert solution.complete_queens(1, []) == [0]
    assert solution.complete_queens(1, [0]) == [0]
    print("✓ Test 1 passed: n=1 -> [0]")

    # Test case 2: Examples from the statement
    assert solution.complete_queens(4, [1]) == [1, 3, 0, 2]
    assert solution.complete_queens(4, [0]) == []
    print("✓ Test 2 passed: n=4, [1] -> [1, 3, 0, 2]; [0] -> []")

    # Test case 3: No solution exists at all
    assert solution.complete_queens(3, []) == []
    print("✓ Test 3 passed: n=3 -> []")

    # Test case 4: Prefix already has attacking queens
    assert solution.complete_queens(8, [0, 1]) == []
    assert solution.complete_queens(8, [2, 5, 2]) == []
    print("✓ Test 4 passed: attacking prefixes -> []")

    # Test case 5: A completable prefix on 8 x 8
    r5 = solution.complete_queens(8, [0, 4])
    assert is_completion(8, [0, 4], r5)
    print(f"✓ Test 5 passed: n=8, [0, 4] -> {r5}")

    # Test case 6: Full prefix is returned as is
    full = [2, 4, 1, 7, 0, 6, 3, 5]
    assert solution.complete_queens(8, full) == full
    print("✓ Test 6 passed: complete valid prefix returned unchanged")

    # Test case 7: Larger board from scratch and with a prefix
    assert is_completion(14, [], solution.complete_queens(14, []))
    assert is_completion(12, [11, 9], solution.complete_queens(12, [11, 9]))
    print("✓ Test 7 passed: n=14 and n=12 completions are valid")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_complete_queens()
