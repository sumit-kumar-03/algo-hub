"""
EPI 12.5 Extra Variant - Distance to the Nearest Equal Entry for Every Index
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the "latest index seen" hash table from nearest repeated
entries, applied in both directions to answer a question per position.

Problem:
Given an array A, return an array D of the same length where D[i] is the
smallest |i - j| over all j != i with A[j] == A[i], or -1 if A[i] appears
nowhere else.

Constraints:
- 0 <= len(A) <= 10^5
- O(n) time, O(n) space; comparing every pair is O(n^2) and too slow

How it works:
1. Left-to-right pass with a table of latest indices: the nearest equal
   entry to the left of i is at last[A[i]], if any
2. Right-to-left pass with a fresh table: the nearest equal entry to the
   right of i is at next_seen[A[i]], if any
3. D[i] is the smaller of the two gaps (or -1 if neither exists)
4. Alternatively, a single pass can fill both: when A[i] is seen again at
   index i with previous index p, gap i - p is a candidate for both D[i]
   and D[p]

Example 1:
Input: A = [3, 1, 3, 3, 1]
Output: [2, 3, 1, 1, 3]
Explanation: The 3 at index 2 has neighbors at 0 and 3; the closer is 3.

Example 2:
Input: A = ["x", "y", "z"]
Output: [-1, -1, -1]
"""

from typing import Hashable, List


class Solution:
    def nearest_equal_distances(self, A: List[Hashable]) -> List[int]:
        """
        Computes, for every index, the distance to the nearest equal entry.

        Args:
            A: Array of hashable entries

        Returns:
            List D with D[i] = min |i - j| over j != i with A[j] == A[i], or -1

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement per-index nearest equal distance
        pass


def test_nearest_equal_distances():
    """Test cases for per-index nearest equal distance"""
    solution = Solution()

    # Test case 1: Mixed repeats
    assert solution.nearest_equal_distances([3, 1, 3, 3, 1]) == [2, 3, 1, 1, 3]
    print("✓ Test 1 passed: [3, 1, 3, 3, 1] -> [2, 3, 1, 1, 3]")

    # Test case 2: No repeats
    assert solution.nearest_equal_distances(["x", "y", "z"]) == [-1, -1, -1]
    print("✓ Test 2 passed: All distinct -> all -1")

    # Test case 3: Empty and single element
    assert solution.nearest_equal_distances([]) == []
    assert solution.nearest_equal_distances([42]) == [-1]
    print("✓ Test 3 passed: Empty / single")

    # Test case 4: All equal
    assert solution.nearest_equal_distances([0, 0, 0, 0]) == [1, 1, 1, 1]
    print("✓ Test 4 passed: All equal -> all 1")

    # Test case 5: Nearer neighbor on the right for one index, left for another
    #   'a' at 0, 4, 5: index 0 -> 4, index 4 -> 1, index 5 -> 1
    A = ["a", "b", "c", "b", "a", "a"]
    assert solution.nearest_equal_distances(A) == [4, 2, -1, 2, 1, 1]
    print("✓ Test 5 passed: Left/right neighbors chosen correctly")

    # Test case 6: Negative numbers
    assert solution.nearest_equal_distances([-5, 2, -5, 7, 2]) == [2, 3, 2, -1, 3]
    print("✓ Test 6 passed: Negative values")

    # Test case 7: Larger input checked against brute force
    A = [(i * 37) % 11 for i in range(60)] + [(i * 5) % 13 for i in range(40)]
    expected = []
    for i in range(len(A)):
        gaps = [abs(i - j) for j in range(len(A)) if j != i and A[j] == A[i]]
        expected.append(min(gaps) if gaps else -1)
    assert solution.nearest_equal_distances(A) == expected
    print("✓ Test 7 passed: 100-entry array matches brute force")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_nearest_equal_distances()
