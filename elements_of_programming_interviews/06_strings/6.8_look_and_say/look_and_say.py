"""
EPI 6.8 - The Look-and-Say Problem

Problem:
The look-and-say sequence begins with "1". Each later term is produced by
reading the previous term aloud as runs of equal digits: for each run you
write the run length followed by the digit. For example, "1211" is read as
"one 1, one 2, two 1s", giving "111221". Given n, return the nth term of
the sequence as a string.

Constraints:
- 1 <= n <= 30
- O(n * 2^n) time (each term is at most twice as long as the previous one)

How it works:
1. Start with s = "1"
2. Repeat n - 1 times: scan s from left to right, count each run of equal
   consecutive digits, and append count + digit to the next term
3. Return s

Example 1:
Input: n = 5
Output: "111221"
Explanation: 1 -> 11 -> 21 -> 1211 -> 111221

Example 2:
Input: n = 8
Output: "1113213211"
Explanation: The first eight terms are 1, 11, 21, 1211, 111221, 312211,
13112221, 1113213211
"""


class Solution:
    def look_and_say(self, n: int) -> str:
        """
        Returns the nth term of the look-and-say sequence.

        Args:
            n: 1-based index of the term to compute

        Returns:
            The nth look-and-say term as a string

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) for the current term
        """
        # TODO: Implement look-and-say
        pass


def test_look_and_say():
    """Test cases for the look-and-say sequence"""
    solution = Solution()

    # Test case 1: First term
    assert solution.look_and_say(1) == "1"
    print("✓ Test 1 passed: n=1 -> '1'")

    # Test case 2: Second and third terms
    assert solution.look_and_say(2) == "11"
    assert solution.look_and_say(3) == "21"
    print("✓ Test 2 passed: n=2 -> '11', n=3 -> '21'")

    # Test case 3: Fifth term
    assert solution.look_and_say(5) == "111221"
    print("✓ Test 3 passed: n=5 -> '111221'")

    # Test case 4: First eight terms
    expected = ["1", "11", "21", "1211", "111221", "312211", "13112221", "1113213211"]
    assert [solution.look_and_say(i) for i in range(1, 9)] == expected
    print("✓ Test 4 passed: First eight terms match")

    # Test case 5: Longer term
    assert solution.look_and_say(10) == "13211311123113112211"
    print("✓ Test 5 passed: n=10")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_look_and_say()
