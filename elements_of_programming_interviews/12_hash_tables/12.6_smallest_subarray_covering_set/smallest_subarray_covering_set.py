"""
EPI 12.6 - Find the Smallest Subarray Covering All Values

Problem:
A search engine shows a "digest" of each result: the shortest stretch of the
page that contains every search keyword. Abstracted: given an array of
strings and a set of keywords, return the (start, end) indices (inclusive) of
a shortest subarray that contains every keyword at least once. Return
(-1, -1) if no subarray covers the set.

Constraints:
- 0 <= len(paragraph) <= 10^5
- 1 <= len(keywords)
- O(n) time, O(k) extra space where k is the number of keywords
- If several shortest subarrays exist, any one may be returned

How it works (sliding window):
1. Keep a hash table of how many times each keyword occurs in the current
   window, and a count of keywords still missing
2. Advance the right end; when it adds a missing keyword, decrement the
   missing count
3. While nothing is missing, record the window if it is the shortest so far,
   then advance the left end (updating the counts)
4. Return the best window

Example 1:
Input: paragraph = ["apple", "banana", "apple", "apple", "dog", "cat", "apple",
                    "dog", "banana", "apple", "cat", "dog"],
       keywords = {"banana", "cat"}
Output: (8, 10)

Example 2:
Input: paragraph = ["a", "b"], keywords = {"c"}
Output: (-1, -1)
Explanation: "c" never appears, so no subarray covers the keywords.
"""

from typing import List, Set, Tuple


class Solution:
    def find_smallest_subarray_covering_set(
        self, paragraph: List[str], keywords: Set[str]
    ) -> Tuple[int, int]:
        """
        Finds a shortest subarray of paragraph containing all keywords.

        Args:
            paragraph: Array of words
            keywords: Set of words that must all be covered

        Returns:
            (start, end) inclusive indices of a shortest covering subarray,
            or (-1, -1) if none exists

        Time Complexity: O(n)
        Space Complexity: O(k) where k is the number of keywords
        """
        # TODO: Implement smallest covering subarray
        pass


def _is_valid(paragraph: List[str], keywords: Set[str], result: Tuple[int, int], length: int) -> bool:
    """Checks that result is a covering subarray of the given length."""
    start, end = result
    if not (0 <= start <= end < len(paragraph)):
        return False
    return end - start + 1 == length and keywords <= set(paragraph[start:end + 1])


def test_find_smallest_subarray_covering_set():
    """Test cases for smallest covering subarray"""
    solution = Solution()

    # Test case 1: Book example
    p1 = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog",
          "banana", "apple", "cat", "dog"]
    assert tuple(solution.find_smallest_subarray_covering_set(p1, {"banana", "cat"})) == (8, 10)
    print("✓ Test 1 passed: Book example -> (8, 10)")

    # Test case 2: Keyword missing from paragraph
    assert tuple(solution.find_smallest_subarray_covering_set(["a", "b"], {"c"})) == (-1, -1)
    print("✓ Test 2 passed: Not coverable -> (-1, -1)")

    # Test case 3: Single keyword, first occurrence
    assert tuple(solution.find_smallest_subarray_covering_set(["x", "y", "z", "y"], {"y"})) in {(1, 1), (3, 3)}
    print("✓ Test 3 passed: Single keyword -> length 1")

    # Test case 4: Ties, any shortest window accepted
    p4 = ["a", "b", "x", "b", "a"]
    r4 = tuple(solution.find_smallest_subarray_covering_set(p4, {"a", "b"}))
    assert _is_valid(p4, {"a", "b"}, r4, 2)
    print("✓ Test 4 passed: Tie between two windows of length 2")

    # Test case 5: Whole array needed
    p5 = ["a", "x", "x", "b"]
    assert tuple(solution.find_smallest_subarray_covering_set(p5, {"a", "b"})) == (0, 3)
    print("✓ Test 5 passed: Whole array -> (0, 3)")

    # Test case 6: Repeated keywords inside the window
    p6 = ["a", "a", "a", "b", "c", "a", "b", "b", "c"]
    r6 = tuple(solution.find_smallest_subarray_covering_set(p6, {"a", "b", "c"}))
    assert _is_valid(p6, {"a", "b", "c"}, r6, 3)
    print("✓ Test 6 passed: Repeated keywords -> length 3")

    # Test case 7: Empty paragraph
    assert tuple(solution.find_smallest_subarray_covering_set([], {"a"})) == (-1, -1)
    print("✓ Test 7 passed: Empty paragraph -> (-1, -1)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_smallest_subarray_covering_set()
