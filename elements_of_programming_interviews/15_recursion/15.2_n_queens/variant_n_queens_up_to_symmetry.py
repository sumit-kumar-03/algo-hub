"""
EPI 15.2 Extra Variant - Count n-Queens Solutions Up to Symmetry
(Practice problem, not in the book. Difficulty: Hard)
Builds on: n-queens backtracking, combined with a canonical form so that
placements that are rotations or reflections of each other count once.

Problem:
Two n-queens placements are considered the same if one can be turned into
the other by rotating the board (by 90, 180, or 270 degrees) or reflecting
it (horizontally, vertically, or across either diagonal). Return the number
of essentially different nonattacking placements of n queens on an n x n
board.

Constraints:
- 1 <= n <= 10
- Known counts for n = 1..10: 1, 0, 0, 1, 2, 1, 6, 12, 46, 92
- Finish in a few seconds for n = 10

How it works (enumerate, then canonicalize):
1. Generate every placement with the usual backtracking (as in 15.2)
2. For a placement p (p[r] = column of the queen in row r), the 8
   symmetric images are built from two basic moves:
   - reflect left-right: r -> n - 1 - p[r]
   - rotate 90 degrees: the queen at (r, c) moves to (c, n - 1 - r)
3. The canonical form is the smallest of the 8 images (as tuples)
4. Count the distinct canonical forms
Stretch: count orbits directly by keeping only placements that are their
own canonical form, without storing a set.

Example 1:
Input: n = 4
Output: 1
Explanation: [1, 3, 0, 2] and [2, 0, 3, 1] are mirror images.

Example 2:
Input: n = 6
Output: 1
Explanation: All four 6-queens placements are rotations or reflections of
one another.
"""


class Solution:
    def count_distinct_up_to_symmetry(self, n: int) -> int:
        """
        Counts n-queens placements, treating symmetric ones as equal.

        Args:
            n: Board size

        Returns:
            Number of placements that are distinct up to the 8 symmetries

        Time Complexity: O(n! * n) in the worst case (enumeration plus
        canonicalizing each placement)
        Space Complexity: O(n * number of distinct placements)
        """
        # TODO: Implement backtracking plus canonical forms
        pass


def test_count_distinct_up_to_symmetry():
    """Test cases for n-Queens up to symmetry"""
    solution = Solution()

    # Test case 1: Trivial board
    assert solution.count_distinct_up_to_symmetry(1) == 1
    print("✓ Test 1 passed: n=1 -> 1")

    # Test case 2: No solutions at all
    assert solution.count_distinct_up_to_symmetry(2) == 0
    assert solution.count_distinct_up_to_symmetry(3) == 0
    print("✓ Test 2 passed: n=2 and n=3 -> 0")

    # Test case 3: The two 4-queens solutions are mirror images
    assert solution.count_distinct_up_to_symmetry(4) == 1
    print("✓ Test 3 passed: n=4 -> 1")

    # Test case 4: n = 5 (10 solutions) and n = 6 (4 solutions)
    assert solution.count_distinct_up_to_symmetry(5) == 2
    assert solution.count_distinct_up_to_symmetry(6) == 1
    print("✓ Test 4 passed: n=5 -> 2, n=6 -> 1")

    # Test case 5: Classic 8 x 8 board
    assert solution.count_distinct_up_to_symmetry(8) == 12
    print("✓ Test 5 passed: n=8 -> 12")

    # Test case 6: Full table up to 10
    expected = [1, 0, 0, 1, 2, 1, 6, 12, 46, 92]
    for n in range(1, 11):
        assert solution.count_distinct_up_to_symmetry(n) == expected[n - 1]
    print("✓ Test 6 passed: n=1..10 match the known counts")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_distinct_up_to_symmetry()
