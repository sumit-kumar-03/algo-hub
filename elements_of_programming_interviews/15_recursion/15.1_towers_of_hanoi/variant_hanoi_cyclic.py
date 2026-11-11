"""
EPI 15.1 Variant - Towers of Hanoi With Cyclic Moves Only

Problem:
Peg 0 holds num_rings rings (largest at the bottom) and they must all end
up on peg 1, with the usual rules (one ring at a time, never on a smaller
ring). Extra rule: a ring may only move "clockwise", that is 0 -> 1,
1 -> 2, or 2 -> 0. Return a shortest sequence of (from_peg, to_peg) moves.

Constraints:
- 0 <= num_rings <= 10
- Minimum move counts for n = 0..6 are 0, 1, 5, 15, 43, 119, 327

How it works (two mutually recursive procedures):
- one_step(n, src): move n rings one step clockwise (src -> src+1)
    1. two_step(n - 1, src): park the n - 1 smaller rings on src+2
    2. move the largest ring src -> src+1
    3. two_step(n - 1, src+2): bring the smaller rings to src+1
- two_step(n, src): move n rings two steps clockwise (src -> src+2)
    1. two_step(n - 1, src): smaller rings to src+2
    2. move the largest ring src -> src+1
    3. one_step(n - 1, src+2): smaller rings back to src (one step)
    4. move the largest ring src+1 -> src+2
    5. two_step(n - 1, src): smaller rings to src+2
(All peg arithmetic is mod 3.) The answer is one_step(num_rings, 0).

Example 1:
Input: num_rings = 1
Output: [(0, 1)]

Example 2:
Input: num_rings = 2
Output: 5 moves, e.g. [(0, 1), (1, 2), (0, 1), (2, 0), (0, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_hanoi_cyclic(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes a shortest move sequence from peg 0 to peg 1 using only
        clockwise moves (0 -> 1, 1 -> 2, 2 -> 0).

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O((1 + sqrt(3))^n), proportional to the number of moves
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement cyclic Towers of Hanoi
        pass


ALLOWED = {(0, 1), (1, 2), (2, 0)}
MIN_MOVES = [0, 1, 5, 15, 43, 119, 327, 895]


def simulate(num_rings: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves; checks legality, the clockwise rule, and the final state."""
    pegs = [list(range(num_rings, 0, -1)), [], []]
    for src, dst in moves:
        if (src, dst) not in ALLOWED or not pegs[src]:
            return False
        ring = pegs[src].pop()
        if pegs[dst] and pegs[dst][-1] < ring:
            return False
        pegs[dst].append(ring)
    return pegs[1] == list(range(num_rings, 0, -1)) and not pegs[0] and not pegs[2]


def test_compute_hanoi_cyclic():
    """Test cases for cyclic Towers of Hanoi"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_hanoi_cyclic(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_hanoi_cyclic(1) == [(0, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 1)]")

    # Test case 3: Two rings
    moves3 = solution.compute_hanoi_cyclic(2)
    assert simulate(2, moves3) and len(moves3) == MIN_MOVES[2]
    print("✓ Test 3 passed: 2 rings in 5 moves")

    # Test case 4: Three rings
    moves4 = solution.compute_hanoi_cyclic(3)
    assert simulate(3, moves4) and len(moves4) == MIN_MOVES[3]
    print("✓ Test 4 passed: 3 rings in 15 moves")

    # Test case 5: Four through seven rings
    for n in range(4, 8):
        moves = solution.compute_hanoi_cyclic(n)
        assert simulate(n, moves) and len(moves) == MIN_MOVES[n]
    print("✓ Test 5 passed: 4..7 rings with minimum move counts")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_hanoi_cyclic()
