"""
EPI 13.1 Extra Variant - Intersection of k Sorted Arrays
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the two-pointer intersection of two sorted arrays, generalized
to one pointer per array that always advances toward the current maximum.

Problem:
Given k arrays, each sorted in ascending order (possibly with duplicates),
return a sorted array of the distinct values that appear in every one of
them. If k == 0, return [].

Constraints:
- 0 <= k <= 10^3
- Total number of entries N <= 10^5
- Target: O(N) time with one pointer per array (repeatedly intersecting
  pairs also works but can be slower); O(k) extra space

How it works (k pointers chasing the maximum):
1. Keep one index per array, all starting at 0
2. Let target be the largest value currently under any pointer
3. In every array, advance the pointer while its value is below target
   (if any array runs out, you are done)
4. If all pointers now show target, append it and advance every pointer
   past all copies of target; otherwise repeat with the new maximum
5. Each pointer only moves forward, so the total work is O(N) plus O(k)
   per round

Example 1:
Input: arrays = [[1, 2, 4, 5, 9], [2, 4, 4, 9, 10], [0, 2, 3, 4, 9]]
Output: [2, 4, 9]

Example 2:
Input: arrays = [[1, 2], [2, 3], [3, 4]]
Output: []
Explanation: Each pair overlaps, but no value is in all three.
"""

from typing import List


class Solution:
    def intersect_k_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        """
        Computes the distinct values common to all k sorted arrays.

        Args:
            arrays: List of k sorted arrays

        Returns:
            Sorted list of distinct values present in every array

        Time Complexity: O(N) where N is the total number of entries
        Space Complexity: O(k) extra, excluding the output
        """
        # TODO: Implement k-way sorted intersection
        pass


def test_intersect_k_sorted_arrays():
    """Test cases for k-way sorted intersection"""
    solution = Solution()

    # Test case 1: Three arrays with several common values
    arrays = [[1, 2, 4, 5, 9], [2, 4, 4, 9, 10], [0, 2, 3, 4, 9]]
    assert solution.intersect_k_sorted_arrays(arrays) == [2, 4, 9]
    print("✓ Test 1 passed: -> [2, 4, 9]")

    # Test case 2: Pairwise overlap but no common value
    assert solution.intersect_k_sorted_arrays([[1, 2], [2, 3], [3, 4]]) == []
    print("✓ Test 2 passed: No value in all three -> []")

    # Test case 3: Single array -> its distinct values
    assert solution.intersect_k_sorted_arrays([[1, 1, 2, 3, 3]]) == [1, 2, 3]
    print("✓ Test 3 passed: k=1 -> distinct values")

    # Test case 4: No arrays, or one empty array
    assert solution.intersect_k_sorted_arrays([]) == []
    assert solution.intersect_k_sorted_arrays([[1, 2], [], [1, 2]]) == []
    print("✓ Test 4 passed: k=0 / empty member -> []")

    # Test case 5: Duplicates everywhere are reported once
    assert solution.intersect_k_sorted_arrays([[5, 5, 5], [5, 5], [5, 6]]) == [5]
    print("✓ Test 5 passed: Duplicates reported once")

    # Test case 6: Negatives, different lengths
    arrays = [[-9, -4, -4, 0, 3], [-4, 0, 1, 2, 3, 7], [-10, -4, 3]]
    assert solution.intersect_k_sorted_arrays(arrays) == [-4, 3]
    print("✓ Test 6 passed: Negatives -> [-4, 3]")

    # Test case 7: Many arrays checked with sets
    arrays = [sorted((i * m) % 60 for i in range(90)) for m in [1, 2, 3, 4, 6]]
    expected = sorted(set.intersection(*(set(a) for a in arrays)))
    assert solution.intersect_k_sorted_arrays(arrays) == expected
    print("✓ Test 7 passed: Five arrays match set intersection")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_intersect_k_sorted_arrays()
