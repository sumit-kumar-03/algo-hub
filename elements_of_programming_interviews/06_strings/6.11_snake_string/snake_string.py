"""
EPI 6.11 - Write a String Sinusoidally

Problem:
Write a string in a zigzag ("sinusoidal") pattern across three rows: the
first character goes in the middle row, the next in the top row, the next
in the middle row, the next in the bottom row, and so on, repeating with
period 4. For "Hello World!" the layout is (_ marks the blank character):

     e   _   l
    H l o W r d
       l   o   !

The snakestring is the concatenation of the top, middle and bottom rows,
each read left to right. Return the snakestring of s.

Constraints:
- 0 <= len(s) <= 10^5
- O(n) time

How it works:
1. The top row holds s[1], s[5], s[9], ... (indices 1 mod 4)
2. The middle row holds s[0], s[2], s[4], ... (even indices)
3. The bottom row holds s[3], s[7], s[11], ... (indices 3 mod 4)
4. Concatenate the three rows in that order

Example 1:
Input: s = "Hello World!"
Output: "e lHloWrdlo!"
Explanation: top = "e l", middle = "HloWrd", bottom = "lo!"

Example 2:
Input: s = "123456789"
Output: "261357948"
Explanation: top = "26", middle = "13579", bottom = "48"
"""


class Solution:
    def snake_string(self, s: str) -> str:
        """
        Computes the snakestring of s.

        Args:
            s: Input string

        Returns:
            The top, middle and bottom rows of the sinusoidal layout,
            concatenated

        Time Complexity: O(n)
        Space Complexity: O(n) for the output
        """
        # TODO: Implement snakestring
        pass


def test_snake_string():
    """Test cases for writing a string sinusoidally"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.snake_string("Hello World!") == "e lHloWrdlo!"
    print("✓ Test 1 passed: 'Hello World!' -> 'e lHloWrdlo!'")

    # Test case 2: Digits
    assert solution.snake_string("123456789") == "261357948"
    print("✓ Test 2 passed: '123456789' -> '261357948'")

    # Test case 3: Empty string
    assert solution.snake_string("") == ""
    print("✓ Test 3 passed: Empty string")

    # Test case 4: Single character goes to the middle row
    assert solution.snake_string("a") == "a"
    print("✓ Test 4 passed: 'a' -> 'a'")

    # Test case 5: Two characters
    assert solution.snake_string("ab") == "ba"
    print("✓ Test 5 passed: 'ab' -> 'ba'")

    # Test case 6: Exactly one period
    assert solution.snake_string("abcd") == "bacd"
    print("✓ Test 6 passed: 'abcd' -> 'bacd'")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_snake_string()
