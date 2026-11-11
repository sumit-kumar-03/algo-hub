"""
EPI 18.7 Extra Variant - Open a Combination Lock Avoiding Jam Codes
(Practice problem, not in the book. Difficulty: Medium)
Builds on: BFS over strings where neighbors differ in one position; here
the graph is implicit (no dictionary), and some vertices are forbidden.

Problem:
A lock has 4 wheels, each showing a digit '0'..'9'. One move turns a
single wheel one notch up or down, and the wheels wrap around ('9' up is
'0', '0' down is '9'). The lock starts at "0000". Some codes are jam
codes: if the wheels ever show one of them, the lock seizes, so you may
never move onto a jam code (and if "0000" itself is a jam code you are
stuck from the start). Return the minimum number of moves to reach the
target code, or -1 if it is impossible.

Constraints:
- 0 <= len(jams) <= 500, every code is 4 digits
- target is not a jam code
- Target: O(10^4 * 4 * 2) time, O(10^4) space

How it works (BFS on the implicit graph of codes):
1. If "0000" is a jam code return -1; otherwise BFS from "0000"
2. Neighbors of a code: for each of the 4 wheels, turn it up or down
3. Skip neighbors that are jam codes or already visited
4. Return the distance when target is popped, or -1 when BFS ends

Example 1:
Input: jams = ["0201", "0101", "0102", "1212", "2002"], target = "0202"
Output: 6
Explanation: e.g. 0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202;
the direct 4-move routes all pass through a jam code.

Example 2:
Input: jams = ["0001", "0009", "0010", "0090", "0100", "0900", "1000",
               "9000"], target = "8888"
Output: -1
Explanation: Every neighbor of "0000" is a jam code.
"""

from typing import List


class Solution:
    def open_lock(self, jams: List[str], target: str) -> int:
        """
        Computes the fewest wheel turns from "0000" to target.

        Args:
            jams: Codes that must never appear on the wheels
            target: Code to reach

        Returns:
            Minimum number of moves, or -1 if target is unreachable

        Time Complexity: O(10^4 * 8)
        Space Complexity: O(10^4)
        """
        # TODO: Implement BFS over 4-digit codes
        pass


def test_open_the_lock():
    """Test cases for opening a combination lock"""
    solution = Solution()

    # Test case 1: Jam codes force a detour
    jams1 = ["0201", "0101", "0102", "1212", "2002"]
    assert solution.open_lock(jams1, "0202") == 6
    print("✓ Test 1 passed: Detour around jam codes = 6")

    # Test case 2: Wrap-around is shorter than turning up
    assert solution.open_lock([], "0009") == 1
    assert solution.open_lock([], "9999") == 4
    assert solution.open_lock([], "5555") == 20
    print("✓ Test 2 passed: Wheels wrap around")

    # Test case 3: Target is the starting code
    assert solution.open_lock(["1111"], "0000") == 0
    print("✓ Test 3 passed: Already open = 0")

    # Test case 4: Fully boxed in at the start
    boxed = ["0001", "0009", "0010", "0090", "0100", "0900", "1000", "9000"]
    assert solution.open_lock(boxed, "8888") == -1
    print("✓ Test 4 passed: Boxed in = -1")

    # Test case 5: Start code jams the lock
    assert solution.open_lock(["0000"], "8888") == -1
    print("✓ Test 5 passed: Start is a jam code = -1")

    # Test case 6: Target boxed in by its own neighbors
    around = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    assert solution.open_lock(around, "8888") == -1
    print("✓ Test 6 passed: Target surrounded = -1")

    # Test case 7: Blocking the short way forces a detour on another wheel
    assert solution.open_lock([], "0008") == 2
    # 0000 -> 0010 -> 0019 -> 0018 -> 0008 beats 8 upward turns
    assert solution.open_lock(["0009"], "0008") == 4
    print("✓ Test 7 passed: Detour through a neighboring wheel = 4")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_open_the_lock()
