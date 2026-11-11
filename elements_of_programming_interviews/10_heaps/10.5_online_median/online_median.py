"""
EPI 10.5 - Compute the Median of Online Data

Problem:
Numbers arrive one at a time as a stream; you cannot go back to earlier
values. After each number is read, output the median of all numbers read so
far (for an even count, the average of the two middle values).

Constraints:
- 0 <= n <= 10^5
- O(log n) time per element, O(n) space
- Do not re-sort the data after every element

How it works (two heaps):
1. Keep a max-heap for the smaller half and a min-heap for the larger half
2. For each new number, route it through one heap into the other so the
   halves stay ordered, then rebalance so the min-heap has the same number
   of elements as the max-heap or exactly one more
3. The median is the min-heap top (odd count) or the average of both tops
   (even count)

Example 1:
Input: [1, 0, 3, 5, 2, 0, 1]
Output: [1, 0.5, 1, 2, 2, 1.5, 1]

Example 2:
Input: [7]
Output: [7]
"""

import math
from typing import Iterable, List


class Solution:
    def online_median(self, sequence: Iterable[float]) -> List[float]:
        """
        Computes the running median of a stream.

        Args:
            sequence: Iterable of numbers, read once

        Returns:
            List whose ith entry is the median of the first i + 1 numbers

        Time Complexity: O(n log n) total, O(log n) per element
        Space Complexity: O(n)
        """
        # TODO: Implement with a max-heap and a min-heap
        pass


def _close(a: List[float], b: List[float]) -> bool:
    return a is not None and len(a) == len(b) and all(math.isclose(x, y) for x, y in zip(a, b))


def test_online_median():
    """Test cases for the running median"""
    solution = Solution()

    # Test case 1: Book example
    result1 = solution.online_median(iter([1, 0, 3, 5, 2, 0, 1]))
    assert _close(result1, [1, 0.5, 1, 2, 2, 1.5, 1])
    print(f"✓ Test 1 passed: Book example -> {result1}")

    # Test case 2: Single element
    assert _close(solution.online_median(iter([7])), [7])
    print("✓ Test 2 passed: Single element")

    # Test case 3: Empty stream
    assert solution.online_median(iter([])) == []
    print("✓ Test 3 passed: Empty stream")

    # Test case 4: Decreasing stream
    assert _close(solution.online_median(iter([5, 4, 3, 2, 1])), [5, 4.5, 4, 3.5, 3])
    print("✓ Test 4 passed: Decreasing stream")

    # Test case 5: Negatives and duplicates
    result5 = solution.online_median(iter([-2, -2, 10, -8]))
    assert _close(result5, [-2, -2, -2, -2])
    print(f"✓ Test 5 passed: Negatives/duplicates -> {result5}")

    # Test case 6: Longer generator checked against sorting
    data = [(i * 7919) % 1000 - 500 for i in range(300)]
    expected = []
    for i in range(1, len(data) + 1):
        s = sorted(data[:i])
        expected.append(s[i // 2] if i % 2 else (s[i // 2 - 1] + s[i // 2]) / 2)
    assert _close(solution.online_median(x for x in data), expected)
    print("✓ Test 6 passed: 300-element generator")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_online_median()
