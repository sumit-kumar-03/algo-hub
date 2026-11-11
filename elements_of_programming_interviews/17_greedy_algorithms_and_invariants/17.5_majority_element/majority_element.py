"""
EPI 17.5 - Find the Majority Element

Problem:
You read a sequence of strings in which one string (the majority element)
is known to appear more than half the time. Identify it in a single pass
over the sequence, using constant extra space. The input is an iterator,
so it can only be traversed once.

Constraints:
- 1 <= number of strings <= 10^7
- A majority element is guaranteed to exist
- O(n) time, O(1) space, one pass

How it works (Boyer-Moore voting; discarding pairs keeps the majority):
1. Keep a candidate and a count, starting with count = 0
2. For each string s:
   - if count == 0: candidate = s, count = 1
   - elif s == candidate: count += 1
   - else: count -= 1 (cancel s against one copy of the candidate)
3. Return candidate

Example 1:
Input: stream = iter(["b", "a", "c", "a", "a", "b", "a", "a", "c", "a"])
Output: "a"
Explanation: "a" appears 6 out of 10 times.

Example 2:
Input: stream = iter(["x"])
Output: "x"
"""

from typing import Iterator


class Solution:
    def majority_search(self, stream: Iterator[str]) -> str:
        """
        Finds the majority element in one pass.

        Args:
            stream: Iterator over the strings (readable only once)

        Returns:
            The string that appears more than half the time

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement Boyer-Moore majority vote
        pass


def test_majority_search():
    """Test cases for majority element"""
    solution = Solution()

    # Test case 1: Book example
    seq = ["b", "a", "c", "a", "a", "b", "a", "a", "c", "a"]
    assert solution.majority_search(iter(seq)) == "a"
    print("✓ Test 1 passed: book example -> 'a'")

    # Test case 2: Single element
    assert solution.majority_search(iter(["x"])) == "x"
    print("✓ Test 2 passed: ['x'] -> 'x'")

    # Test case 3: Majority appears at the end
    assert solution.majority_search(iter(["p", "q", "r", "s", "s", "s", "s"])) == "s"
    print("✓ Test 3 passed: majority at the end -> 's'")

    # Test case 4: Majority at the start, then interleaved
    assert solution.majority_search(iter(["m", "m", "n", "m", "o"])) == "m"
    print("✓ Test 4 passed: interleaved -> 'm'")

    # Test case 5: Bare majority (n/2 + 1)
    assert solution.majority_search(iter(["a", "b", "a", "b", "a", "b", "a"])) == "a"
    print("✓ Test 5 passed: bare majority -> 'a'")

    # Test case 6: Large generator input (single pass only)
    gen = ("hot" if i % 3 else "cold" for i in range(3001))
    assert solution.majority_search(gen) == "hot"
    print("✓ Test 6 passed: generator input -> 'hot'")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_majority_search()
