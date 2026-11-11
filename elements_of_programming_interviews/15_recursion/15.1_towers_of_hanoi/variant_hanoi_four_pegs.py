"""
EPI 15.1 Variant - Towers of Hanoi With Four Pegs

Problem:
Peg 0 holds num_rings rings (largest at the bottom). Move them all to
peg 1 with the usual rules (one ring at a time, never on a smaller ring),
but now there are two spare pegs, 2 and 3. Return a shortest sequence of
(from_peg, to_peg) moves.

Constraints:
- 0 <= num_rings <= 15
- Minimum move counts for n = 0..10 are
  0, 1, 3, 5, 9, 13, 17, 25, 33, 41, 49

How it works (Frame-Stewart algorithm):
Let F(n) be the minimum moves with four pegs; F(0) = 0.
1. For a split k (1 <= k <= n), move the top n - k rings to one spare peg
   using all four pegs: F(n - k) moves
2. Move the remaining k rings to the target with the classic three-peg
   algorithm (the peg holding the small rings is off limits): 2^k - 1 moves
3. Move the n - k small rings onto the target using all four pegs again
F(n) = min over k of 2 * F(n - k) + 2^k - 1. Memoize F and the best k,
then generate the moves recursively with that k.

Example 1:
Input: num_rings = 2
Output: [(0, 2), (0, 1), (2, 1)]

Example 2:
Input: num_rings = 3
Output: 5 moves, e.g. [(0, 2), (0, 3), (0, 1), (3, 1), (2, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_hanoi_four_pegs(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes a shortest move sequence from peg 0 to peg 1 using four pegs.

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(n^2) to choose the splits plus O(number of moves)
        Space Complexity: O(n) for memoization and recursion, excluding the output
        """
        # TODO: Implement the Frame-Stewart algorithm
        pass


MIN_MOVES = [0, 1, 3, 5, 9, 13, 17, 25, 33, 41, 49]


def simulate(num_rings: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves on four pegs and checks the rings finish on peg 1."""
    pegs = [list(range(num_rings, 0, -1)), [], [], []]
    for src, dst in moves:
        if not (0 <= src < 4 and 0 <= dst < 4) or src == dst or not pegs[src]:
            return False
        ring = pegs[src].pop()
        if pegs[dst] and pegs[dst][-1] < ring:
            return False
        pegs[dst].append(ring)
    return pegs[1] == list(range(num_rings, 0, -1)) and not (
        pegs[0] or pegs[2] or pegs[3]
    )


def test_compute_hanoi_four_pegs():
    """Test cases for four-peg Towers of Hanoi"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_hanoi_four_pegs(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_hanoi_four_pegs(1) == [(0, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 1)]")

    # Test case 3: Three rings beat the three-peg count of 7
    moves3 = solution.compute_hanoi_four_pegs(3)
    assert simulate(3, moves3) and len(moves3) == 5
    print("✓ Test 3 passed: 3 rings in 5 moves")

    # Test case 4: Six rings
    moves4 = solution.compute_hanoi_four_pegs(6)
    assert simulate(6, moves4) and len(moves4) == 17
    print("✓ Test 4 passed: 6 rings in 17 moves")

    # Test case 5: Every size up to ten
    for n in range(11):
        moves = solution.compute_hanoi_four_pegs(n)
        assert simulate(n, moves) and len(moves) == MIN_MOVES[n]
    print("✓ Test 5 passed: 0..10 rings with minimum move counts")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_hanoi_four_pegs()
