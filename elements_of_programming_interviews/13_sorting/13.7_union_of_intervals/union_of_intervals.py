"""
EPI 13.7 - Compute the Union of Intervals

Problem:
You are given a set of intervals with integer endpoints, where each end may
be open or closed, e.g., (0, 3), [1, 1], [2, 4], [3, 4). Return their union
as a list of disjoint intervals sorted by left endpoint. Two intervals that
share an endpoint value merge if at least one of them includes that point,
e.g., [5, 7) and [7, 8) merge into [5, 8), but (1, 2) and (2, 3) stay apart.

Constraints:
- 0 <= number of intervals <= 10^5
- left.val <= right.val for every interval
- O(n log n) time, O(n) space

How it works:
1. Sort intervals by left value; on ties, put left-closed intervals first
2. Start the result with the first interval, then for each next interval:
   - If it starts before the last result interval ends, or starts exactly
     where it ends and either endpoint there is closed, extend the last
     result interval's right end if the new right end is further (or equal
     but closed)
   - Otherwise, append it as a new disjoint interval
3. Return the result

Example 1:
Input: (0, 3), [1, 1], [2, 4], [3, 4), [5, 7), [7, 8), [8, 11), (9, 11],
       [12, 14], (12, 16], (13, 15), (16, 17)
Output: (0, 4], [5, 11], [12, 17)

Example 2:
Input: (1, 2), (2, 3)
Output: (1, 2), (2, 3)
Explanation: The point 2 is in neither interval, so they stay separate.
"""

import collections
from typing import List

# An endpoint value plus whether the interval includes it.
Endpoint = collections.namedtuple("Endpoint", ("is_closed", "val"))
# An interval is a pair of Endpoints.
Interval = collections.namedtuple("Interval", ("left", "right"))


class Solution:
    def union_of_intervals(self, intervals: List[Interval]) -> List[Interval]:
        """
        Computes the union of intervals as a sorted list of disjoint intervals.

        Args:
            intervals: Intervals with open or closed endpoints

        Returns:
            Disjoint intervals covering exactly the union, sorted by left value

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement union of intervals
        pass


def make(text: str) -> Interval:
    """Parses interval notation like "[1, 4)" into an Interval."""
    text = text.strip()
    left_val, right_val = (int(x) for x in text[1:-1].split(","))
    return Interval(Endpoint(text[0] == "[", left_val), Endpoint(text[-1] == "]", right_val))


def as_text(intervals: List[Interval]) -> List[str]:
    """Formats intervals back into notation for easy comparison."""
    if intervals is None:
        return None
    return [
        ("[" if i.left.is_closed else "(") + f"{i.left.val}, {i.right.val}"
        + ("]" if i.right.is_closed else ")")
        for i in intervals
    ]


def test_union_of_intervals():
    """Test cases for union of intervals"""
    solution = Solution()

    # Test case 1: Book example
    book = ["(0, 3)", "[1, 1]", "[2, 4]", "[3, 4)", "[5, 7)", "[7, 8)", "[8, 11)",
            "(9, 11]", "[12, 14]", "(12, 16]", "(13, 15)", "(16, 17)"]
    result1 = solution.union_of_intervals([make(s) for s in book])
    assert as_text(result1) == ["(0, 4]", "[5, 11]", "[12, 17)"]
    print("✓ Test 1 passed: Book example -> (0, 4], [5, 11], [12, 17)")

    # Test case 2: Open endpoints at the same value do not merge
    result2 = solution.union_of_intervals([make("(2, 3)"), make("(1, 2)")])
    assert as_text(result2) == ["(1, 2)", "(2, 3)"]
    print("✓ Test 2 passed: (1, 2) and (2, 3) stay separate")

    # Test case 3: One closed endpoint is enough to merge
    result3 = solution.union_of_intervals([make("(1, 2]"), make("(2, 3)")])
    assert as_text(result3) == ["(1, 3)"]
    print("✓ Test 3 passed: (1, 2] and (2, 3) -> (1, 3)")

    # Test case 4: Empty input
    assert solution.union_of_intervals([]) == []
    print("✓ Test 4 passed: Empty input -> []")

    # Test case 5: Same left value, closed wins
    result5 = solution.union_of_intervals([make("(1, 5)"), make("[1, 3]")])
    assert as_text(result5) == ["[1, 5)"]
    print("✓ Test 5 passed: (1, 5) and [1, 3] -> [1, 5)")

    # Test case 6: Same right value, closed wins
    result6 = solution.union_of_intervals([make("[0, 4)"), make("(2, 4]")])
    assert as_text(result6) == ["[0, 4]"]
    print("✓ Test 6 passed: [0, 4) and (2, 4] -> [0, 4]")

    # Test case 7: Contained interval does not shrink the union
    result7 = solution.union_of_intervals([make("[0, 10]"), make("(3, 4)"), make("[11, 12)")])
    assert as_text(result7) == ["[0, 10]", "[11, 12)"]
    print("✓ Test 7 passed: Contained interval ignored")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_union_of_intervals()
