"""
EPI 5.1 Extra Variant - Three-Way Partition Around a Range
(Practice problem, not in the book. Difficulty: Easy)
Builds on: the single-pass, three-region Dutch national flag partition.

Problem:
Given an array of integers A and two values low <= high, rearrange A in
place so that it has three blocks: first every element smaller than low,
then every element in the closed range [low, high], then every element
larger than high. The order inside each block does not matter. Unlike the
main problem, the middle block can hold many different values, and low
and high need not appear in A at all.

Constraints:
- 0 <= len(A) <= 10^5; low <= high
- Must run in O(n) time with a single pass and use O(1) extra space

How it works (three regions, as in the Dutch flag partition):
1. smaller = 0, middle = 0, larger = len(A)
2. While middle < larger:
   - A[middle] < low: swap A[smaller], A[middle]; advance both
   - low <= A[middle] <= high: advance middle
   - A[middle] > high: decrement larger; swap A[middle], A[larger]
3. Blocks: [0, smaller) below, [smaller, larger) inside, [larger, n) above

Example 1:
Input: A = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], low = 10, high = 20
Output: [1, 5, 4, 2, 3, 1, 14, 20, 20, 54, 87, 98, 32] (one valid answer)
Explanation: Values below 10, then 14, 20, 20, then values above 20.

Example 2:
Input: A = [7, 3, 9], low = 4, high = 6
Output: [3, 9, 7] or [3, 7, 9]
Explanation: Nothing lies in [4, 6], so the middle block is empty.
"""

from typing import List


class Solution:
    def partition_by_range(self, A: List[int], low: int, high: int) -> None:
        """
        Partitions A in place into < low, [low, high], > high blocks.

        Args:
            A: Array to partition in place
            low: Lower end of the middle range (inclusive)
            high: Upper end of the middle range (inclusive)

        Returns:
            None (A is modified in place)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement three-way partition around a range
        pass


def is_range_partitioned(A: List[int], low: int, high: int) -> bool:
    """Checks that A is ordered as: < low, then in [low, high], then > high."""
    stage = 0
    for x in A:
        current = 0 if x < low else 1 if x <= high else 2
        if current < stage:
            return False
        stage = current
    return True


def test_partition_by_range():
    """Test cases for three-way range partition"""
    solution = Solution()

    # Test case 1: Example 1
    A1 = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    original1 = sorted(A1)
    solution.partition_by_range(A1, 10, 20)
    assert sorted(A1) == original1 and is_range_partitioned(A1, 10, 20)
    print(f"✓ Test 1 passed: {A1}")

    # Test case 2: Empty middle block
    A2 = [7, 3, 9]
    solution.partition_by_range(A2, 4, 6)
    assert sorted(A2) == [3, 7, 9] and A2[0] == 3
    print(f"✓ Test 2 passed: {A2}")

    # Test case 3: Empty array and single element
    A3: List[int] = []
    solution.partition_by_range(A3, 0, 0)
    assert A3 == []
    A4 = [5]
    solution.partition_by_range(A4, 1, 2)
    assert A4 == [5]
    print("✓ Test 3 passed: Empty and single element")

    # Test case 4: Reverse-ordered input with negatives
    A5 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]
    solution.partition_by_range(A5, -1, 4)
    assert sorted(A5) == list(range(-3, 10)) and is_range_partitioned(A5, -1, 4)
    print(f"✓ Test 4 passed: {A5}")

    # Test case 5: Range covers everything / nothing in range with duplicates
    A6 = [5, 5, 1, 9, 1, 9]
    solution.partition_by_range(A6, 0, 100)
    assert sorted(A6) == [1, 1, 5, 5, 9, 9]
    A7 = [9, 1, 9, 1, 5, 5]
    solution.partition_by_range(A7, 5, 5)
    assert A7[:2] == [1, 1] and A7[2:4] == [5, 5] and A7[4:] == [9, 9]
    print("✓ Test 5 passed: Range covering all values and a single-value range")

    # Test case 6: Larger input with many repeated values
    A8 = [(i * 37) % 101 - 50 for i in range(5000)]
    original8 = sorted(A8)
    solution.partition_by_range(A8, -10, 10)
    assert sorted(A8) == original8 and is_range_partitioned(A8, -10, 10)
    print("✓ Test 6 passed: 5000 elements")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_partition_by_range()
