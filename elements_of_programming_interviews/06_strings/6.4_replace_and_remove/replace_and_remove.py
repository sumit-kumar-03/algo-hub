"""
EPI 6.4 - Replace and Remove

Problem:
You are given an array of characters and an integer size. Only the first
size entries are meaningful. Apply two rules to those entries: every 'b' is
deleted, and every 'a' is replaced by two 'd's. Do the work in place and
return the number of valid entries in the result. The array is guaranteed
to have enough room for the result; entries beyond the result don't matter.

Constraints:
- 0 <= size <= len(s)
- len(s) is large enough to hold the final result
- O(n) time, O(1) extra space

How it works:
1. Forward pass: copy every non-'b' character toward the front (dropping
   the 'b's) and count the 'a's
2. The final length is (number of kept characters) + (number of 'a's)
3. Backward pass: walk from the last kept character to the front, writing
   from the final end of the array backward; write "dd" for each 'a' and
   copy everything else
4. Return the final length

Example 1:
Input: size = 7, s = ['a', 'c', 'd', 'b', 'b', 'c', 'a']
Output: 7, s starts with ['d', 'd', 'c', 'd', 'c', 'd', 'd']
Explanation: Both 'b's are removed and both 'a's become "dd"

Example 2:
Input: size = 4, s = ['a', 'b', 'a', 'c', '']
Output: 5, s == ['d', 'd', 'd', 'd', 'c']
Explanation: The 'b' is removed, and each 'a' grows into two 'd's
"""

from typing import List


class Solution:
    def replace_and_remove(self, size: int, s: List[str]) -> int:
        """
        Removes each 'b' and replaces each 'a' with "dd", in place.

        Args:
            size: Number of leading entries of s to process
            s: Character array with enough room for the result

        Returns:
            Number of valid entries in s after the transformation

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement in-place replace and remove
        pass


def test_replace_and_remove():
    """Test cases for replace and remove"""
    solution = Solution()

    # Test case 1: Book example with equal numbers of 'a's and 'b's
    s1 = ["a", "c", "d", "b", "b", "c", "a"]
    n1 = solution.replace_and_remove(7, s1)
    assert n1 == 7 and s1[:n1] == ["d", "d", "c", "d", "c", "d", "d"]
    print("✓ Test 1 passed: acdbbca -> ddcdcdd")

    # Test case 2: Result grows into the spare slot
    s2 = ["a", "b", "a", "c", ""]
    n2 = solution.replace_and_remove(4, s2)
    assert n2 == 5 and s2[:n2] == ["d", "d", "d", "d", "c"]
    print("✓ Test 2 passed: abac -> ddddc")

    # Test case 3: Empty input
    s3: List[str] = []
    assert solution.replace_and_remove(0, s3) == 0
    print("✓ Test 3 passed: Empty input")

    # Test case 4: Only 'b's are removed completely
    s4 = ["b", "b", "b"]
    assert solution.replace_and_remove(3, s4) == 0
    print("✓ Test 4 passed: All 'b's removed")

    # Test case 5: Only 'a's, every one doubles
    s5 = ["a", "a", "", ""]
    n5 = solution.replace_and_remove(2, s5)
    assert n5 == 4 and s5[:n5] == ["d", "d", "d", "d"]
    print("✓ Test 5 passed: aa -> dddd")

    # Test case 6: No 'a' or 'b', unchanged
    s6 = ["x", "y", "z"]
    n6 = solution.replace_and_remove(3, s6)
    assert n6 == 3 and s6[:n6] == ["x", "y", "z"]
    print("✓ Test 6 passed: No changes needed")

    # Test case 7: Entries past size are ignored
    s7 = ["c", "a", "b", "a", ""]
    n7 = solution.replace_and_remove(2, s7)
    assert n7 == 3 and s7[:n7] == ["c", "d", "d"]
    print("✓ Test 7 passed: Only the first size entries are processed")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_replace_and_remove()
