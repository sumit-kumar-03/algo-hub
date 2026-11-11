"""
EPI 12.5 - Find the Nearest Repeated Entries in an Array

Problem:
Given an array (for example, the words of a paragraph), return the smallest
distance between two equal entries, where distance is the difference of
their indices. Return -1 if no entry repeats.

Constraints:
- 0 <= len(paragraph) <= 10^5
- O(n) time, O(d) space where d is the number of distinct entries

How it works:
1. Scan left to right, keeping a hash table from each entry to the latest
   index where it was seen
2. When an entry has been seen before, the gap to its latest index is a
   candidate distance; keep the minimum
3. Update the latest index for the entry
4. Return the minimum, or -1 if none was found

Example 1:
Input: ["All", "work", "and", "no", "play", "makes", "for", "no", "work",
        "no", "fun", "and", "no", "results"]
Output: 2
Explanation: "no" appears at indices 7 and 9.

Example 2:
Input: ["a", "b", "c"]
Output: -1
"""

from typing import List


class Solution:
    def find_nearest_repetition(self, paragraph: List[str]) -> int:
        """
        Finds the distance between the closest pair of equal entries.

        Args:
            paragraph: List of words

        Returns:
            Smallest index difference between equal entries, or -1 if none

        Time Complexity: O(n)
        Space Complexity: O(d) where d is the number of distinct entries
        """
        # TODO: Implement nearest repetition search
        pass


def test_find_nearest_repetition():
    """Test cases for nearest repeated entries"""
    solution = Solution()

    # Test case 1: Book example
    words = ["All", "work", "and", "no", "play", "makes", "for", "no", "work",
             "no", "fun", "and", "no", "results"]
    assert solution.find_nearest_repetition(words) == 2
    print("✓ Test 1 passed: Book example -> 2")

    # Test case 2: No repeats
    assert solution.find_nearest_repetition(["a", "b", "c"]) == -1
    print("✓ Test 2 passed: No repeats -> -1")

    # Test case 3: Empty input
    assert solution.find_nearest_repetition([]) == -1
    print("✓ Test 3 passed: Empty input -> -1")

    # Test case 4: Adjacent duplicates
    assert solution.find_nearest_repetition(["x", "y", "y", "x"]) == 1
    print("✓ Test 4 passed: Adjacent duplicates -> 1")

    # Test case 5: Closest pair is not the first repeat found
    assert solution.find_nearest_repetition(["a", "b", "c", "d", "a", "e", "f", "e"]) == 2
    print("✓ Test 5 passed: Later pair is closer -> 2")

    # Test case 6: Must use the most recent occurrence
    assert solution.find_nearest_repetition(["a", "b", "a", "c", "c", "x", "a"]) == 1
    print("✓ Test 6 passed: Most recent occurrence used -> 1")

    # Test case 7: Case-sensitive comparison
    assert solution.find_nearest_repetition(["The", "cat", "the", "dog"]) == -1
    print("✓ Test 7 passed: Case-sensitive -> -1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_nearest_repetition()
