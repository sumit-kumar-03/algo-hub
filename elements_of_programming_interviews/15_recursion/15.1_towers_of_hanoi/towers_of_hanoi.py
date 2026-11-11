"""
EPI 15.1 - The Towers of Hanoi Problem

Problem:
There are three pegs (0, 1, 2). Peg 0 holds num_rings rings, stacked from
largest at the bottom to smallest at the top. Move all rings to peg 1.
You may move only one ring at a time, and a ring may never be placed on top
of a smaller ring. Return the sequence of moves as (from_peg, to_peg) pairs.

Constraints:
- 0 <= num_rings <= 20
- Exactly 2^n - 1 moves are required

How it works:
To move n rings from peg `src` to peg `dst` using peg `via`:
1. Move the top n - 1 rings from src to via (using dst)
2. Move the largest ring from src to dst
3. Move the n - 1 rings from via to dst (using src)
Base case: 0 rings needs no moves.

Example 1:
Input: num_rings = 1
Output: [(0, 1)]

Example 2:
Input: num_rings = 2
Output: [(0, 2), (0, 1), (2, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_tower_hanoi(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes the moves that transfer all rings from peg 0 to peg 1.

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(2^n)
        Space Complexity: O(n) recursion depth, excluding the output
        """
        # TODO: Implement recursive Towers of Hanoi
        pass


def simulate(num_rings: int, moves: List[Tuple[int, int]]) -> bool:
    """Replays moves and checks that they are legal and finish on peg 1."""
    pegs = [list(range(num_rings, 0, -1)), [], []]
    for src, dst in moves:
        if not pegs[src]:
            return False
        ring = pegs[src].pop()
        if pegs[dst] and pegs[dst][-1] < ring:
            return False
        pegs[dst].append(ring)
    return pegs[1] == list(range(num_rings, 0, -1)) and not pegs[0] and not pegs[2]


def test_compute_tower_hanoi():
    """Test cases for Towers of Hanoi"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_tower_hanoi(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_tower_hanoi(1) == [(0, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 1)]")

    # Test case 3: Two rings
    moves3 = solution.compute_tower_hanoi(2)
    assert simulate(2, moves3) and len(moves3) == 3
    print(f"✓ Test 3 passed: 2 rings -> {moves3}")

    # Test case 4: Three rings
    moves4 = solution.compute_tower_hanoi(3)
    assert simulate(3, moves4) and len(moves4) == 7
    print("✓ Test 4 passed: 3 rings in 7 moves")

    # Test case 5: Ten rings
    moves5 = solution.compute_tower_hanoi(10)
    assert simulate(10, moves5) and len(moves5) == 2 ** 10 - 1
    print("✓ Test 5 passed: 10 rings in 1023 moves")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_tower_hanoi()
