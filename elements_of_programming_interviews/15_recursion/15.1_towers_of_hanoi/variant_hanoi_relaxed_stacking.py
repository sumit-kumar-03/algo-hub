"""
EPI 15.1 Variant - Towers of Hanoi With a Relaxed Stacking Rule

Problem:
Peg 0 holds rings 1..num_rings (ring num_rings at the bottom, ring 1 on
top). Move all of them to peg 1, one ring at a time, using peg 2 as a
spare. The usual "never on a smaller ring" rule is relaxed: the only
requirement is that on every peg the largest ring present is the bottom
ring. Rings above the bottom may be in any order. Return a shortest
sequence of (from_peg, to_peg) moves. The final order on peg 1 does not
matter (its bottom ring will be the largest anyway).

Constraints:
- 0 <= num_rings <= 30
- A move of ring r onto a nonempty peg is legal iff r is smaller than that
  peg's bottom ring
- Minimum move counts for n = 0..6 are 0, 1, 3, 6, 10, 15, 21

How it works:
1. The largest ring can only land on an empty peg 1, so every other ring
   must first be moved to peg 2 (the largest ring stays at the bottom of
   peg 0, so it never gets in the way)
2. Moving those n - 1 rings to peg 2 is the same problem one size smaller
3. Move the largest ring to peg 1
4. Now any ring may sit on peg 1, so pop the n - 1 rings off peg 2 one by
   one straight onto peg 1
This gives T(n) = T(n - 1) + 1 + (n - 1) = n(n + 1) / 2.

Example 1:
Input: num_rings = 2
Output: [(0, 2), (0, 1), (2, 1)]

Example 2:
Input: num_rings = 3
Output: 6 moves, e.g. [(0, 1), (0, 2), (1, 2), (0, 1), (2, 1), (2, 1)]
Explanation: Ring 1 may sit on ring 2 or ring 3 regardless of order, as
long as each peg's bottom ring is its largest.
"""

from typing import List, Tuple


class Solution:
    def compute_hanoi_relaxed(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes a shortest move sequence from peg 0 to peg 1 under the
        relaxed rule (only the bottom ring of each peg must be its largest).

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(n^2), proportional to the number of moves
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement relaxed Towers of Hanoi
        pass


def simulate(num_rings: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves; checks the relaxed rule and that all rings end on peg 1."""
    pegs = [list(range(num_rings, 0, -1)), [], []]
    for src, dst in moves:
        if src == dst or not pegs[src]:
            return False
        ring = pegs[src].pop()
        if pegs[dst] and pegs[dst][0] < ring:
            return False
        pegs[dst].append(ring)
    return len(pegs[1]) == num_rings and not pegs[0] and not pegs[2]


def test_compute_hanoi_relaxed():
    """Test cases for relaxed Towers of Hanoi"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_hanoi_relaxed(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_hanoi_relaxed(1) == [(0, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 1)]")

    # Test case 3: Two rings
    moves3 = solution.compute_hanoi_relaxed(2)
    assert simulate(2, moves3) and len(moves3) == 3
    print("✓ Test 3 passed: 2 rings in 3 moves")

    # Test case 4: Three rings (classic rules would need 7)
    moves4 = solution.compute_hanoi_relaxed(3)
    assert simulate(3, moves4) and len(moves4) == 6
    print("✓ Test 4 passed: 3 rings in 6 moves")

    # Test case 5: Six rings
    moves5 = solution.compute_hanoi_relaxed(6)
    assert simulate(6, moves5) and len(moves5) == 21
    print("✓ Test 5 passed: 6 rings in 21 moves")

    # Test case 6: Twenty rings
    moves6 = solution.compute_hanoi_relaxed(20)
    assert simulate(20, moves6) and len(moves6) == 20 * 21 // 2
    print("✓ Test 6 passed: 20 rings in 210 moves")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_hanoi_relaxed()
