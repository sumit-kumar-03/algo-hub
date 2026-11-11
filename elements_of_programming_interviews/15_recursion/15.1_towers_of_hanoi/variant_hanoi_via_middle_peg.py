"""
EPI 15.1 Variant - Towers of Hanoi Where Every Move Involves Peg 2

Problem:
Peg 0 holds num_rings rings (largest at the bottom) and they must all end
up on peg 1, with the usual rules (one ring at a time, never on a smaller
ring). Extra rule: every move must either start or end at peg 2, so direct
transfers between pegs 0 and 1 are forbidden. Return a shortest sequence of
(from_peg, to_peg) moves.

Constraints:
- 0 <= num_rings <= 10
- A shortest solution uses exactly 3^n - 1 moves

How it works:
Think of peg 2 as the middle of a line 0 - 2 - 1. To move n rings from an
end peg `src` to the other end peg `dst`:
1. Move the top n - 1 rings from src to dst (the far end)
2. Move the largest ring from src to the middle peg 2
3. Move the n - 1 rings from dst back to src
4. Move the largest ring from peg 2 to dst
5. Move the n - 1 rings from src to dst
This gives T(n) = 3T(n - 1) + 2, which solves to 3^n - 1.

Example 1:
Input: num_rings = 1
Output: [(0, 2), (2, 1)]

Example 2:
Input: num_rings = 2
Output: 8 moves, e.g.
[(0, 2), (2, 1), (0, 2), (1, 2), (2, 0), (2, 1), (0, 2), (2, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_hanoi_via_middle_peg(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes a shortest move sequence from peg 0 to peg 1 where every
        move touches peg 2.

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(3^n)
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement the adjacent-pegs Towers of Hanoi
        pass


def simulate(num_rings: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves; checks legality, the peg-2 rule, and the final state."""
    pegs = [list(range(num_rings, 0, -1)), [], []]
    for src, dst in moves:
        if 2 not in (src, dst) or src == dst or not pegs[src]:
            return False
        ring = pegs[src].pop()
        if pegs[dst] and pegs[dst][-1] < ring:
            return False
        pegs[dst].append(ring)
    return pegs[1] == list(range(num_rings, 0, -1)) and not pegs[0] and not pegs[2]


def test_compute_hanoi_via_middle_peg():
    """Test cases for Towers of Hanoi through peg 2"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_hanoi_via_middle_peg(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_hanoi_via_middle_peg(1) == [(0, 2), (2, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 2), (2, 1)]")

    # Test case 3: Two rings
    moves3 = solution.compute_hanoi_via_middle_peg(2)
    assert simulate(2, moves3) and len(moves3) == 8
    print("✓ Test 3 passed: 2 rings in 8 moves")

    # Test case 4: Three rings
    moves4 = solution.compute_hanoi_via_middle_peg(3)
    assert simulate(3, moves4) and len(moves4) == 26
    print("✓ Test 4 passed: 3 rings in 26 moves")

    # Test case 5: Seven rings
    moves5 = solution.compute_hanoi_via_middle_peg(7)
    assert simulate(7, moves5) and len(moves5) == 3 ** 7 - 1
    print("✓ Test 5 passed: 7 rings in 2186 moves")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_hanoi_via_middle_peg()
