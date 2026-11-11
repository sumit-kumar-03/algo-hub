"""
EPI 11.9 - Find the Missing IP Address

Problem:
A huge file holds up to about a billion 32-bit IP addresses (as integers).
RAM is only a few megabytes, but the file can be read more than once. Return
any 32-bit address that does not appear in the file.

Here the "file" is a re-iterable Python object: every `for x in addresses`
starts a fresh pass over the same data, like reopening the file.

Constraints:
- 0 <= every address < 2^32; duplicates allowed
- Fewer than 2^32 addresses, so at least one is missing
- O(n) time over a constant number of passes
- O(2^16) extra memory: never build a set or bitmap of all addresses
- Any missing address is accepted

How it works (two passes, bucket by the upper 16 bits):
1. Pass 1: count how many addresses fall into each of the 2^16 buckets given
   by the upper 16 bits
2. Some bucket has fewer than 2^16 entries, so it is missing a value; pick it
3. Pass 2: mark which lower-16-bit values occur within that bucket
4. Return (bucket << 16) | (first unmarked lower value)

Example 1:
Input: [0, 1, 2, 3]
Output: any address other than 0..3, e.g. 4

Example 2:
Input: every address 0 .. 65535 (all of bucket 0)
Output: any address >= 65536, e.g. 65536
"""

from typing import Callable, Iterable, Iterator


class Solution:
    def find_missing_ip(self, addresses: Iterable[int]) -> int:
        """
        Finds a 32-bit value absent from a large re-readable collection.

        Args:
            addresses: Re-iterable collection of 32-bit integers (each
                iteration is one pass over the "file")

        Returns:
            A 32-bit integer not present in the collection

        Time Complexity: O(n)
        Space Complexity: O(2^16)
        """
        # TODO: Implement two-pass bucket counting
        pass


class _File:
    """Re-iterable stream: each iteration regenerates the data (like re-reading a file)."""

    def __init__(self, factory: Callable[[], Iterator[int]]):
        self.factory = factory
        self.passes = 0

    def __iter__(self):
        self.passes += 1
        return self.factory()


def _valid(result, present_check: Callable[[int], bool]) -> bool:
    return isinstance(result, int) and 0 <= result < (1 << 32) and not present_check(result)


def test_find_missing_ip():
    """Test cases for the missing IP address"""
    solution = Solution()

    # Test case 1: Small file
    data1 = [0, 1, 2, 3]
    r1 = solution.find_missing_ip(_File(lambda: iter(data1)))
    assert _valid(r1, lambda x: x in set(data1)) is True
    print(f"✓ Test 1 passed: Small file -> {r1}")

    # Test case 2: Empty file
    r2 = solution.find_missing_ip(_File(lambda: iter([])))
    assert _valid(r2, lambda x: False) is True
    print(f"✓ Test 2 passed: Empty file -> {r2}")

    # Test case 3: Bucket 0 completely full
    r3 = solution.find_missing_ip(_File(lambda: iter(range(1 << 16))))
    assert _valid(r3, lambda x: x < (1 << 16)) is True
    print(f"✓ Test 3 passed: Full first bucket -> {r3}")

    # Test case 4: Contains the maximum address (max + 1 overflows)
    data4 = [(1 << 32) - 1, (1 << 32) - 2, 12345]
    r4 = solution.find_missing_ip(_File(lambda: iter(data4)))
    assert _valid(r4, lambda x: x in set(data4)) is True
    print(f"✓ Test 4 passed: Max address present -> {r4}")

    # Test case 5: Bucket 0 full plus most of bucket 1, with duplicates
    def gen5():
        yield from range(1 << 16)
        yield from range((1 << 16), (2 << 16) - 1)  # bucket 1 missing only its last value
        yield from (5, 5, 70000)
    r5 = solution.find_missing_ip(_File(gen5))
    assert _valid(r5, lambda x: x < (2 << 16) - 1) is True
    print(f"✓ Test 5 passed: Nearly full low buckets -> {r5}")

    # Test case 6: Scattered addresses from a generator
    data6 = [(i * 2654435761) % (1 << 32) for i in range(5000)]
    present6 = set(data6)
    r6 = solution.find_missing_ip(_File(lambda: iter(data6)))
    assert _valid(r6, lambda x: x in present6) is True
    print(f"✓ Test 6 passed: Scattered addresses -> {r6}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_missing_ip()
