"""
EPI 12.5 Extra Variant - Shortest Subarray Where Some Entry Repeats t Times
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the nearest repeated entries scan, which is the t = 2 case
(the shortest window holding two equal entries has length distance + 1).
Here the hash table must remember more than one earlier index per entry.

Problem:
Given an array A and an integer t >= 1, return the length of the shortest
contiguous subarray in which at least one entry occurs t or more times.
Return -1 if no entry occurs t times anywhere in A.

Constraints:
- 0 <= len(A) <= 10^5
- 1 <= t <= 10^5
- O(n) time, O(n) space

How it works:
1. Scan left to right, keeping for each entry a queue of its most recent
   (up to t) indices
2. When an entry's queue holds t indices, the window from the oldest of
   them to the current index contains t copies; its length is
   current - oldest + 1, a candidate answer
3. Drop the oldest index when the queue would exceed t entries
4. Return the minimum candidate, or -1

Example 1:
Input: A = ["a", "b", "a", "c", "a", "a"], t = 3
Output: 4
Explanation: "a" appears at 0, 2, 4, 5. The window [2..5] holds three
copies and has length 4.

Example 2:
Input: A = [1, 2, 1, 2], t = 3
Output: -1
"""

from typing import Hashable, List


class Solution:
    def shortest_window_with_repeats(self, A: List[Hashable], t: int) -> int:
        """
        Finds the shortest subarray in which some entry occurs t times.

        Args:
            A: Array of hashable entries
            t: Required number of occurrences (t >= 1)

        Returns:
            Length of the shortest such subarray, or -1 if none exists

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement shortest window with t repeats
        pass


def test_shortest_window_with_repeats():
    """Test cases for shortest window with t repeats"""
    solution = Solution()

    # Test case 1: Example with t = 3
    assert solution.shortest_window_with_repeats(["a", "b", "a", "c", "a", "a"], 3) == 4
    print("✓ Test 1 passed: t=3 -> 4")

    # Test case 2: Not enough copies
    assert solution.shortest_window_with_repeats([1, 2, 1, 2], 3) == -1
    print("✓ Test 2 passed: No entry occurs 3 times -> -1")

    # Test case 3: t = 2 matches nearest repetition distance + 1
    words = ["All", "work", "and", "no", "play", "makes", "for", "no", "work",
             "no", "fun", "and", "no", "results"]
    assert solution.shortest_window_with_repeats(words, 2) == 3
    print("✓ Test 3 passed: t=2 on the book paragraph -> 3")

    # Test case 4: t = 1 is any single element; empty array
    assert solution.shortest_window_with_repeats([9, 8], 1) == 1
    assert solution.shortest_window_with_repeats([], 1) == -1
    print("✓ Test 4 passed: t=1 / empty")

    # Test case 5: Best window comes from a different entry than the first found
    A = [5, 0, 0, 5, 5, 7, 7, 7]
    assert solution.shortest_window_with_repeats(A, 3) == 3
    print("✓ Test 5 passed: Later entry gives the tightest window")

    # Test case 6: Whole array needed
    assert solution.shortest_window_with_repeats([4, 1, 4, 2, 4], 3) == 5
    print("✓ Test 6 passed: Whole array is the only window")

    # Test case 7: Brute-force cross-check for several t
    A = [(i * i) % 7 for i in range(40)]
    for t in range(1, 8):
        best = -1
        for i in range(len(A)):
            counts = {}
            for j in range(i, len(A)):
                counts[A[j]] = counts.get(A[j], 0) + 1
                if counts[A[j]] >= t:
                    if best == -1 or j - i + 1 < best:
                        best = j - i + 1
                    break
        assert solution.shortest_window_with_repeats(A, t) == best
    print("✓ Test 7 passed: Matches brute force for t = 1..7")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shortest_window_with_repeats()
