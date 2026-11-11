"""
EPI 15.1 Variant - The Towers of Hanoi Problem Without Recursion

Problem:
Solve the Towers of Hanoi problem without using recursion. Peg 0 holds
num_rings rings (largest at the bottom). Move them all to peg 1, one ring
at a time, never placing a ring on a smaller one. Peg 2 is the spare.
Return the moves as (from_peg, to_peg) pairs.

Constraints:
- 0 <= num_rings <= 20
- No recursive calls: use a loop (and an explicit stack if you like)
- Exactly 2^n - 1 moves are required

How it works (explicit stack):
1. Push the task (n, src=0, dst=1, via=2) onto a stack
2. Pop a task. If n == 0, skip it. Otherwise push, in REVERSE order of
   execution: (n-1, via, dst, src), the single move (src -> dst), and
   (n-1, src, via, dst)
3. When a "single move" item is popped, append it to the result
Alternative: the classic loop that alternates moving the smallest ring
cyclically with the only other legal move.

Example 1:
Input: num_rings = 2
Output: [(0, 2), (0, 1), (2, 1)]

Example 2:
Input: num_rings = 3
Output: a sequence of 7 legal moves, e.g.
[(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1)]
"""

from typing import List, Tuple


class Solution:
    def compute_tower_hanoi_iterative(self, num_rings: int) -> List[Tuple[int, int]]:
        """
        Computes the moves that transfer all rings from peg 0 to peg 1 iteratively.

        Args:
            num_rings: Number of rings initially on peg 0

        Returns:
            List of (from_peg, to_peg) moves

        Time Complexity: O(2^n)
        Space Complexity: O(n) for the explicit stack, excluding the output
        """
        # TODO: Implement Towers of Hanoi with a loop instead of recursion
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


def test_compute_tower_hanoi_iterative():
    """Test cases for iterative Towers of Hanoi"""
    solution = Solution()

    # Test case 1: No rings
    assert solution.compute_tower_hanoi_iterative(0) == []
    print("✓ Test 1 passed: 0 rings -> no moves")

    # Test case 2: One ring
    assert solution.compute_tower_hanoi_iterative(1) == [(0, 1)]
    print("✓ Test 2 passed: 1 ring -> [(0, 1)]")

    # Test case 3: Two rings
    moves3 = solution.compute_tower_hanoi_iterative(2)
    assert simulate(2, moves3) and len(moves3) == 3
    print(f"✓ Test 3 passed: 2 rings -> {moves3}")

    # Test case 4: Three rings
    moves4 = solution.compute_tower_hanoi_iterative(3)
    assert simulate(3, moves4) and len(moves4) == 7
    print("✓ Test 4 passed: 3 rings in 7 moves")

    # Test case 5: Twelve rings
    moves5 = solution.compute_tower_hanoi_iterative(12)
    assert simulate(12, moves5) and len(moves5) == 2 ** 12 - 1
    print("✓ Test 5 passed: 12 rings in 4095 moves")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_compute_tower_hanoi_iterative()
