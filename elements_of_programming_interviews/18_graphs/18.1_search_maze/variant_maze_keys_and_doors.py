"""
EPI 18.1 Extra Variant - Escape a Maze with Keys and Doors
(Practice problem, not in the book. Difficulty: Hard)
Builds on: BFS through a grid maze, where the search state must grow to
include which keys you hold, because the same cell can be worth revisiting
once you carry a new key.

Problem:
A maze is given as a list of equal-length strings:
- '#' is a wall, '.' is open floor
- 'S' is the start (exactly one), 'X' is the exit (exactly one)
- lowercase 'a'..'f' is a key; stepping on it picks it up (keys are never
  used up, and one key opens every door of its letter)
- uppercase 'A'..'F' is a door; you may step on it only if you already
  hold the matching lowercase key
You move one step up, down, left or right per move. Return the minimum
number of moves from S to X, or -1 if X cannot be reached.

Constraints:
- 1 <= rows, cols <= 30
- At most 6 distinct key letters ('a'..'f')
- A door may have no matching key anywhere (then it can never be opened)
- Target: O(rows * cols * 2^K) time and space, K = number of key letters

How it works (BFS over (cell, key set) states):
1. Encode the keys held as a bitmask; the start state is (S, 0)
2. BFS: from (cell, mask), try the 4 neighbors; skip walls and doors whose
   key bit is not set; stepping on a key ORs its bit into the mask
3. Track visited (row, col, mask) so a cell may be revisited only with a
   different key set
4. Return the distance when X is popped, or -1 when the queue empties

Example 1:
Input: grid = ["aSA.X"]
Output: 5
Explanation: Step left onto the key (1), back to S (2), through door A (3),
then two more steps to X (5).

Example 2:
Input: grid = ["SAaX"]
Output: -1
Explanation: The only key for door A lies behind door A.
"""

from typing import List


class Solution:
    def shortest_escape(self, grid: List[str]) -> int:
        """
        Computes the fewest moves from S to X, collecting keys as needed.

        Args:
            grid: Maze rows made of '#', '.', 'S', 'X', 'a'-'f', 'A'-'F'

        Returns:
            Minimum number of moves from S to X, or -1 if impossible

        Time Complexity: O(rows * cols * 2^K)
        Space Complexity: O(rows * cols * 2^K)
        """
        # TODO: Implement BFS over (cell, keys held) states
        pass


def test_maze_keys_and_doors():
    """Test cases for escaping a maze with keys and doors"""
    solution = Solution()

    # Test case 1: No keys or doors involved
    assert solution.shortest_escape(["S.X"]) == 2
    assert solution.shortest_escape(["S#X"]) == -1
    print("✓ Test 1 passed: Plain maze, reachable and blocked")

    # Test case 2: Grab a key behind you, then pass the door
    assert solution.shortest_escape(["aSA.X"]) == 5
    print("✓ Test 2 passed: Back-track for a key = 5")

    # Test case 3: Key locked behind its own door; door with no key at all
    assert solution.shortest_escape(["SAaX"]) == -1
    assert solution.shortest_escape(["S.C.X"]) == -1
    print("✓ Test 3 passed: Unobtainable keys = -1")

    # Test case 4: Cells must be revisited with a bigger key set
    # Fetch a (2 moves), go through A to fetch b (4), walk back past S
    # through B to X (12 in total)
    assert solution.shortest_escape(["bAa.S.B.X"]) == 12
    print("✓ Test 4 passed: Chained keys in a corridor = 12")

    # Test case 5: Using a key beats the long open way around
    grid5 = [
        "S.A.X",
        "a###.",
        ".....",
    ]
    assert solution.shortest_escape(grid5) == 6
    print("✓ Test 5 passed: Door shortcut = 6 (open detour is 8)")

    # Test case 6: Two keys from different branches open the way to X
    grid6 = [
        "S.#..X",
        ".a#B##",
        "b.A..#",
    ]
    assert solution.shortest_escape(grid6) == 11
    print("✓ Test 6 passed: Two keys, two doors = 11")

    # Test case 7: Lots of keys, but the exit needs none of them
    grid7 = [
        "SabcdefX",
        "ABCDEF..",
    ]
    assert solution.shortest_escape(grid7) == 7
    print("✓ Test 7 passed: Six keys picked up on the way = 7")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_maze_keys_and_doors()
