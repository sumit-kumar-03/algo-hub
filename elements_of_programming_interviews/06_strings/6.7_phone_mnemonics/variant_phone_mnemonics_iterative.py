"""
EPI 6.7 Variant - Phone Mnemonics Without Recursion

Problem:
Solve the phone mnemonics problem (EPI 6.7) without using recursion.
On a phone keypad, each digit from 2 to 9 maps to three or four letters
(0 and 1 map only to themselves). Given a phone number as a string of
digits, return every character sequence that the number could spell. The
sequences don't need to be real words.

Keypad mapping:
    0 -> "0", 1 -> "1", 2 -> "ABC", 3 -> "DEF", 4 -> "GHI",
    5 -> "JKL", 6 -> "MNO", 7 -> "PQRS", 8 -> "TUV", 9 -> "WXYZ"

Constraints:
- 1 <= len(phone_number) <= 10
- The result may be returned in any order
- No recursion (iterate instead)
- O(4^n * n) time, where n is the number of digits

How it works:
1. Start with a list containing just the empty string
2. For each digit, build a new list by appending every letter the digit
   maps to onto every string in the current list
3. After the last digit, the list holds all mnemonics
(Alternative: treat the choice of letter per digit as an odometer of
indices and increment it like a mixed-radix counter.)

Example 1:
Input: phone_number = "23"
Output: ["AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"]

Example 2:
Input: phone_number = "2276696"
Output: 3888 strings, including "ACRONYM" and "ABPOMZN"
Explanation: 3 * 3 * 4 * 3 * 3 * 4 * 3 = 3888 combinations
"""

from typing import List

MAPPING = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


class Solution:
    def phone_mnemonic_iterative(self, phone_number: str) -> List[str]:
        """
        Computes all mnemonics for a phone number without recursion.

        Args:
            phone_number: String of digits

        Returns:
            All character sequences the number could spell, in any order

        Time Complexity: O(4^n * n)
        Space Complexity: O(4^n * n) for the intermediate and final lists
        """
        # TODO: Implement iterative mnemonic generation
        pass


def test_phone_mnemonic_iterative():
    """Test cases for iterative phone mnemonics"""
    solution = Solution()

    # Test case 1: Single digit
    assert sorted(solution.phone_mnemonic_iterative("2")) == ["A", "B", "C"]
    print("✓ Test 1 passed: '2' -> A, B, C")

    # Test case 2: Two digits
    expected2 = ["AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"]
    assert sorted(solution.phone_mnemonic_iterative("23")) == expected2
    print("✓ Test 2 passed: '23' -> 9 combinations")

    # Test case 3: Four-letter key
    assert sorted(solution.phone_mnemonic_iterative("7")) == ["P", "Q", "R", "S"]
    print("✓ Test 3 passed: '7' -> P, Q, R, S")

    # Test case 4: Digits 0 and 1 map to themselves
    assert sorted(solution.phone_mnemonic_iterative("10")) == ["10"]
    assert sorted(solution.phone_mnemonic_iterative("102")) == ["10A", "10B", "10C"]
    print("✓ Test 4 passed: 0 and 1 map to themselves")

    # Test case 5: Book example
    result5 = solution.phone_mnemonic_iterative("2276696")
    assert len(result5) == 3888 and len(set(result5)) == 3888
    assert "ACRONYM" in result5 and "ABPOMZN" in result5
    print("✓ Test 5 passed: '2276696' -> 3888 mnemonics incl. ACRONYM")

    # Test case 6: Two four-letter keys
    result6 = solution.phone_mnemonic_iterative("79")
    assert len(result6) == 16 and set(result6) == {a + b for a in "PQRS" for b in "WXYZ"}
    print("✓ Test 6 passed: '79' -> 16 combinations")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_phone_mnemonic_iterative()
