"""
EPI 15.1 Variant - Towers of Hanoi Without Direct Transfers From Peg 0 to Peg 1

Problem:
Peg 0 holds num_rings rings (largest at the bottom) and they must all end
up on peg 1, with the usual rules (one ring at a time, never on a smaller
ring). Extra rule: a ring may never move directly from peg 0 to peg 1.
Every other move, including 1 -> 0, is allowed. Return a shortest sequence
of (from_peg, to_peg) moves.

Constraints:
- 0 <= num_rings <= 10
- Minimum move counts for n = 0..8 are 0, 2, 7, 19, 47, 113, 267, 629, 1475

How it works (cheapest tower move for every ordered pair of pegs):
Let cost(n, a, b) be the fewest moves to carry an n-ring tower from peg a
to peg b (x is the third peg). The largest ring moves either:
1. Directly a -> b (only if allowed): cost(n-1, a, x) + 1 + cost(n-1, x, b)
2. In two hops a -> x -> b: the smaller rings go to b, then back to a while
   the largest ring sits on x, then to b again:
   cost(n-1, a, b) + 1 + cost(n-1, b, a) + 1 + cost(n-1, a, b)
Take the cheaper option (memoize cost), then generate the moves by
following the choice made at each level. For 0 -> 1 only option 2 exists.

Example 1:
Input: num_rings = 1
Output: [(0, 2), (2, 1)]

Example 2:
Input: num_rings = 2
Output: 7 moves, e.g.
[(0, 2), (2, 1), (0, 2), (1, 0), (2, 1), (0, 2), (2, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_hanoi_no_direct(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes a shortest move sequence from peg 0 to peg 1 that never
        moves a ring directly from peg 0 to peg 1.

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(number of moves), which grows roughly like 2.3^n
        Space Complexity: O(n) for memoized costs and recursion, excluding the output
        """
        # TODO: Implement restricted Towers of Hanoi
        pass


MIN_MOVES = [0, 2, 7, 19, 47, 113, 267, 629, 1475]


def simulate(num_rings: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves; checks legality, the 0 -> 1 ban, and the final state."""
    pegs = [list(range(num_rings, 0, -1)), [], []]
    for src, dst in moves:
        if (src, dst) == (0, 1) or src == dst or not pegs[src]:
            return False
        ring = pegs[src].pop()
        if pegs[dst] and pegs[dst][-1] < ring:
            return False
        pegs[dst].append(ring)
    return pegs[1] == list(range(num_rings, 0, -1)) and not pegs[0] and not pegs[2]


def test_compute_hanoi_no_direct():
    """Test cases for Towers of Hanoi without direct 0 -> 1 transfers"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_hanoi_no_direct(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_hanoi_no_direct(1) == [(0, 2), (2, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 2), (2, 1)]")

    # Test case 3: Two rings
    moves3 = solution.compute_hanoi_no_direct(2)
    assert simulate(2, moves3) and len(moves3) == MIN_MOVES[2]
    print("✓ Test 3 passed: 2 rings in 7 moves")

    # Test case 4: Three rings
    moves4 = solution.compute_hanoi_no_direct(3)
    assert simulate(3, moves4) and len(moves4) == MIN_MOVES[3]
    print("✓ Test 4 passed: 3 rings in 19 moves")

    # Test case 5: Four through eight rings
    for n in range(4, 9):
        moves = solution.compute_hanoi_no_direct(n)
        assert simulate(n, moves) and len(moves) == MIN_MOVES[n]
    print("✓ Test 5 passed: 4..8 rings with minimum move counts")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_hanoi_no_direct()
