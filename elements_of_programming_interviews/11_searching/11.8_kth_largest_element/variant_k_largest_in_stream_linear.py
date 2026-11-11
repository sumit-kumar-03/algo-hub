"""
EPI 11.8 Extra Variant - k Largest of a Stream in Linear Time
(Practice problem, not in the book. Difficulty: Hard)
Builds on: quickselect partitioning, applied repeatedly to a bounded buffer
so a stream can be processed in expected O(n) total time with O(k) memory.

Problem:
Numbers arrive as a stream that can be read only once and is too long to
store. Given k, return the k largest numbers of the stream (any order;
duplicates count separately). If the stream has fewer than k numbers,
return all of them.

A min-heap of size k solves this in O(n log k) time. Do better: expected
O(n) time, independent of k, while still using only O(k) memory.

Constraints:
- 1 <= k; the stream may be shorter than k
- Expected O(n) time and O(k) extra space
- Read the stream once; do not convert it to a list

How it works (buffer of 2k, prune with quickselect):
1. Keep a buffer with room for 2k - 1 numbers
2. Append incoming numbers; when the buffer is full, run quickselect to
   move the k largest to the front and discard the other k - 1
3. Each prune costs O(k) expected and happens once per k - 1 new numbers,
   so the total cost is O(n) expected
4. When the stream ends, run one final selection on the buffer and return
   its k largest (or everything if there are fewer than k)
(Use three-way partitioning so many equal values cannot stall the pruning.)

Example 1:
Input: stream = [5, 1, 9, 3, 7, 6, 2], k = 3
Output: [9, 7, 6]   (in any order)

Example 2:
Input: stream = [4, 4], k = 5
Output: [4, 4]
"""

from typing import Iterable, Iterator, List


class Solution:
    def k_largest_from_stream(self, stream: Iterable[int], k: int) -> List[int]:
        """
        Returns the k largest numbers of a stream.

        Args:
            stream: Iterable of numbers, read once
            k: How many of the largest numbers to return (k >= 1)

        Returns:
            The min(k, n) largest numbers, in any order

        Time Complexity: O(n) expected
        Space Complexity: O(k)
        """
        # TODO: Implement with a 2k buffer pruned by quickselect
        pass


class OneShot:
    """Iterator that fails loudly if someone tries to read it twice."""

    def __init__(self, values: Iterable[int]):
        self._it = iter(values)
        self._started = False

    def __iter__(self) -> Iterator[int]:
        assert not self._started, "stream may be read only once"
        self._started = True
        return self._it


def _expected(values: List[int], k: int) -> List[int]:
    return sorted(values, reverse=True)[:k]


def _sorted_desc(result: List[int]) -> List[int]:
    return sorted(result, reverse=True) if result is not None else None


def test_k_largest_from_stream():
    """Test cases for the k largest numbers of a stream"""
    solution = Solution()

    # Test case 1: Example
    data1 = [5, 1, 9, 3, 7, 6, 2]
    assert _sorted_desc(solution.k_largest_from_stream(OneShot(data1), 3)) == [9, 7, 6]
    print("✓ Test 1 passed: [9, 7, 6]")

    # Test case 2: Fewer numbers than k
    assert _sorted_desc(solution.k_largest_from_stream(OneShot([4, 4]), 5)) == [4, 4]
    print("✓ Test 2 passed: Fewer than k")

    # Test case 3: Empty stream and k = 1
    assert _sorted_desc(solution.k_largest_from_stream(OneShot([]), 2)) == []
    assert _sorted_desc(solution.k_largest_from_stream(OneShot([3, -2, 8, 0]), 1)) == [8]
    print("✓ Test 3 passed: Empty stream and k = 1")

    # Test case 4: Increasing stream (every new number survives a prune)
    data4 = list(range(1000))
    result4 = solution.k_largest_from_stream(OneShot(data4), 10)
    assert _sorted_desc(result4) == _expected(data4, 10)
    print("✓ Test 4 passed: Increasing stream")

    # Test case 5: Many duplicates and negatives
    data5 = [(-1) ** i * (i % 5) for i in range(3000)]
    result5 = solution.k_largest_from_stream(OneShot(data5), 700)
    assert _sorted_desc(result5) == _expected(data5, 700)
    print("✓ Test 5 passed: Duplicates and negatives")

    # Test case 6: Long generator stream with a large k
    data6 = [(i * 7919) % 100003 for i in range(200000)]
    result6 = solution.k_largest_from_stream(OneShot(x for x in data6), 5000)
    assert _sorted_desc(result6) == _expected(data6, 5000)
    print("✓ Test 6 passed: 200,000-number stream, k = 5000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_k_largest_from_stream()
