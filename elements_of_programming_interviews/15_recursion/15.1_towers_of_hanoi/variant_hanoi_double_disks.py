"""
EPI 15.1 Variant - Towers of Hanoi With Two Disks of Each Size

Problem:
Peg 0 holds 2n disks of n different sizes, two disks of each size, stacked
so that sizes never increase going up (two of size n at the bottom, two of
size 1 on top). Move all disks to peg 1, one at a time, using peg 2 as a
spare. A disk may never be placed on a smaller disk, but it may be placed
on a disk of the same size. Return a shortest sequence of
(from_peg, to_peg) moves.

Constraints:
- 0 <= n <= 12
- A shortest solution uses exactly 2 * (2^n - 1) moves

How it works:
1. Treat each pair of equal disks as one "double ring"
2. Run the ordinary Towers of Hanoi recursion on the n double rings
3. Each time the recursion moves a double ring from src to dst, emit two
   moves (src, dst), (src, dst): the pair ends up reversed, which is fine
   because equal disks are interchangeable
This gives 2 * (2^n - 1) moves.

Example 1:
Input: n = 1
Output: [(0, 1), (0, 1)]

Example 2:
Input: n = 2
Output: [(0, 2), (0, 2), (0, 1), (0, 1), (2, 1), (2, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_hanoi_double_disks(self, n: int) -> List[Tuple[int, int]]:
        """
        Computes a shortest move sequence for 2n disks (two of each size)
        from peg 0 to peg 1.

        Args:
            n: Number of distinct disk sizes

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(2^n)
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement Towers of Hanoi with paired disks
        pass


def simulate(n: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves on disk sizes; equal sizes may stack on each other."""
    start = [size for size in range(n, 0, -1) for _ in range(2)]
    pegs = [list(start), [], []]
    for src, dst in moves:
        if src == dst or not pegs[src]:
            return False
        disk = pegs[src].pop()
        if pegs[dst] and pegs[dst][-1] < disk:
            return False
        pegs[dst].append(disk)
    return pegs[1] == start and not pegs[0] and not pegs[2]


def test_compute_hanoi_double_disks():
    """Test cases for Towers of Hanoi with two disks per size"""
    solution = Solution()

    # Test case 1: No disks
    assert solution.compute_hanoi_double_disks(0) == []
    print("✓ Test 1 passed: n=0 -> no moves")

    # Test case 2: One size (two disks)
    assert solution.compute_hanoi_double_disks(1) == [(0, 1), (0, 1)]
    print("✓ Test 2 passed: n=1 -> [(0, 1), (0, 1)]")

    # Test case 3: Two sizes
    moves3 = solution.compute_hanoi_double_disks(2)
    assert simulate(2, moves3) and len(moves3) == 6
    print("✓ Test 3 passed: n=2 in 6 moves")

    # Test case 4: Three sizes
    moves4 = solution.compute_hanoi_double_disks(3)
    assert simulate(3, moves4) and len(moves4) == 14
    print("✓ Test 4 passed: n=3 in 14 moves")

    # Test case 5: Ten sizes
    moves5 = solution.compute_hanoi_double_disks(10)
    assert simulate(10, moves5) and len(moves5) == 2 * (2 ** 10 - 1)
    print("✓ Test 5 passed: n=10 in 2046 moves")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_hanoi_double_disks()
