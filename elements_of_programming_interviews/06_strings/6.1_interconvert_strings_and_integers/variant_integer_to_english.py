"""
EPI 6.1 Extra Variant - Integer to English Words
(Practice problem, not in the book. Difficulty: Medium)
Builds on: taking a number apart from the least significant end with %
and //, here 1000 at a time instead of 10 at a time.

Problem:
Given a non-negative integer below 2^31, return its English name, with
words capitalized and separated by single spaces, e.g. 1234567 ->
"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven".
Do not write "and" and do not use hyphens. Zero is "Zero".

Constraints:
- 0 <= num <= 2^31 - 1
- O(number of digits) time

How it works (three digits at a time):
1. Word lists: "One".."Nineteen" for 1..19, "Twenty".."Ninety" for the
   tens, and scales "", "Thousand", "Million", "Billion"
2. Name a group 0..999: hundreds digit + "Hundred", then the rest (below
   20 is one word; otherwise a tens word plus an optional ones word)
3. Peel groups with num % 1000 and num //= 1000, attaching each nonzero
   group's scale word; skip groups that are 0 (no "Zero Thousand")
4. Join the groups from most to least significant

Example 1:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 2:
Input: num = 1000010
Output: "One Million Ten"
Explanation: The thousands group is 0, so it is skipped.
"""


class Solution:
    def number_to_words(self, num: int) -> str:
        """
        Spells out a non-negative integer in English words.

        Args:
            num: Integer in [0, 2^31 - 1]

        Returns:
            The English name, words capitalized and space-separated

        Time Complexity: O(d) where d is the number of digits
        Space Complexity: O(d)
        """
        # TODO: Implement integer to English words
        pass


def test_number_to_words():
    """Test cases for integer to English words"""
    solution = Solution()

    # Test case 1: Zero and single words
    assert solution.number_to_words(0) == "Zero"
    assert solution.number_to_words(7) == "Seven"
    assert solution.number_to_words(13) == "Thirteen"
    print("✓ Test 1 passed: 0, 7, 13")

    # Test case 2: Tens with and without ones
    assert solution.number_to_words(20) == "Twenty"
    assert solution.number_to_words(45) == "Forty Five"
    assert solution.number_to_words(90) == "Ninety"
    print("✓ Test 2 passed: 20, 45, 90")

    # Test case 3: Hundreds
    assert solution.number_to_words(100) == "One Hundred"
    assert solution.number_to_words(101) == "One Hundred One"
    assert solution.number_to_words(999) == "Nine Hundred Ninety Nine"
    print("✓ Test 3 passed: 100, 101, 999")

    # Test case 4: Examples
    assert solution.number_to_words(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert solution.number_to_words(1000010) == "One Million Ten"
    print("✓ Test 4 passed: 12345 and 1000010")

    # Test case 5: Skipped zero groups and round numbers
    assert solution.number_to_words(1000) == "One Thousand"
    assert solution.number_to_words(1000000000) == "One Billion"
    assert solution.number_to_words(2000000019) == "Two Billion Nineteen"
    assert solution.number_to_words(1234567) == (
        "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )
    print("✓ Test 5 passed: Round numbers and skipped groups")

    # Test case 6: Largest input
    assert solution.number_to_words(2**31 - 1) == (
        "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three "
        "Thousand Six Hundred Forty Seven"
    )
    print("✓ Test 6 passed: 2^31 - 1")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_number_to_words()
