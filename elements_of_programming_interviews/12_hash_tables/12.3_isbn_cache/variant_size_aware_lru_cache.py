"""
EPI 12.3 Extra Variant - Size-Aware LRU Cache
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the LRU ISBN cache (hash table plus recency order), but capacity
is measured in total size rather than number of entries, so one insert may
evict several entries.

Problem:
Each cached entry now has a size (for example, the bytes needed to store a
book's record). The cache's capacity limits the SUM of the sizes of its
entries.
- lookup(key): return the value, or -1 if absent. A hit makes the entry the
  most recently used.
- insert(key, value, size): if size > capacity, reject the insert, leave the
  cache unchanged, and return False. Otherwise store (or replace) the entry
  with the new value and size, make it the most recently used, then evict
  least recently used entries (never the one just inserted) until the total
  size is at most capacity, and return True.
- total_size(): return the sum of the sizes of the cached entries.

Constraints:
- 1 <= capacity <= 10^9, 1 <= size
- O(1) amortized time per operation (each entry is evicted at most once
  per insertion of it)

How it works:
1. Keep a hash table from key to (value, size) in recency order (an
   OrderedDict, or a hash table plus a doubly linked list), and a running
   total of sizes
2. On insert, reject oversized entries; otherwise remove any old version of
   the key (subtract its size), add the new one at the most recent end, and
   add its size
3. While the total exceeds capacity, pop from the least recent end and
   subtract the popped entry's size

Example 1:
Input: cache = SizeAwareLRUCache(10); insert("A", 1, 4); insert("B", 2, 4);
       insert("C", 3, 5); lookup("A"); lookup("B"); total_size()
Output: lookup("A") -> -1, lookup("B") -> 2, total_size() -> 9
Explanation: Adding "C" brings the total to 13, so the LRU entry "A" is
evicted, leaving 4 + 5 = 9.

Example 2:
Input: cache = SizeAwareLRUCache(10); insert("A", 1, 3); insert("B", 2, 3);
       insert("C", 3, 3); insert("D", 4, 8); total_size()
Output: 8
Explanation: Inserting "D" makes the total 17; evicting "A", "B", and "C"
(in that order) brings it down to 8.
"""


class SizeAwareLRUCache:
    def __init__(self, capacity: int):
        """
        Initializes an empty cache.

        Args:
            capacity: Maximum total size of all cached entries
        """
        # TODO: Initialize the cache's data structures
        pass

    def lookup(self, key: str) -> int:
        """
        Returns the value for key and marks it most recently used.

        Args:
            key: Entry identifier

        Returns:
            The cached value, or -1 if key is not in the cache

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement lookup
        pass

    def insert(self, key: str, value: int, size: int) -> bool:
        """
        Inserts or replaces key, then evicts LRU entries until the total
        size fits within capacity.

        Args:
            key: Entry identifier
            value: Value to store
            size: Size of the entry (>= 1)

        Returns:
            False if size exceeds capacity (cache unchanged), True otherwise

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        # TODO: Implement insert with size-based LRU eviction
        pass

    def total_size(self) -> int:
        """
        Returns the sum of the sizes of the cached entries.

        Returns:
            Current total size

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement total_size
        pass


def test_size_aware_lru_cache():
    """Test cases for the size-aware LRU cache"""

    # Test case 1: One eviction frees enough space
    cache = SizeAwareLRUCache(10)
    assert cache.insert("A", 1, 4) is True
    assert cache.insert("B", 2, 4) is True
    assert cache.insert("C", 3, 5) is True
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    assert cache.total_size() == 9
    print("✓ Test 1 passed: Single eviction")

    # Test case 2: One insert evicts several entries
    cache = SizeAwareLRUCache(10)
    for key, value in [("A", 1), ("B", 2), ("C", 3)]:
        cache.insert(key, value, 3)
    cache.insert("D", 4, 8)
    assert [cache.lookup(k) for k in "ABCD"] == [-1, -1, -1, 4]
    assert cache.total_size() == 8
    print("✓ Test 2 passed: Multiple evictions")

    # Test case 3: Lookup changes which entries get evicted
    cache = SizeAwareLRUCache(9)
    for key, value in [("A", 1), ("B", 2), ("C", 3)]:
        cache.insert(key, value, 3)
    assert cache.lookup("A") == 1
    cache.insert("D", 4, 3)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == 1
    assert cache.total_size() == 9
    print("✓ Test 3 passed: Lookup refreshes recency")

    # Test case 4: Oversized insert is rejected and changes nothing
    cache = SizeAwareLRUCache(5)
    cache.insert("A", 1, 2)
    assert cache.insert("Big", 9, 6) is False
    assert cache.lookup("Big") == -1
    assert cache.lookup("A") == 1
    assert cache.total_size() == 2
    print("✓ Test 4 passed: Oversized entry rejected")

    # Test case 5: Replacing a key updates value and size
    cache = SizeAwareLRUCache(10)
    cache.insert("A", 1, 3)
    cache.insert("B", 2, 3)
    cache.insert("A", 7, 6)
    assert cache.total_size() == 9
    assert cache.lookup("A") == 7
    cache.insert("C", 3, 5)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == -1
    assert cache.lookup("C") == 3
    assert cache.total_size() == 5
    print("✓ Test 5 passed: Replacement adjusts total size")

    # Test case 6: Entry exactly equal to capacity evicts everything else
    cache = SizeAwareLRUCache(6)
    cache.insert("A", 1, 1)
    cache.insert("B", 2, 2)
    assert cache.insert("C", 3, 6) is True
    assert [cache.lookup(k) for k in "ABC"] == [-1, -1, 3]
    assert cache.total_size() == 6
    print("✓ Test 6 passed: Full-capacity entry")

    # Test case 7: Empty cache
    cache = SizeAwareLRUCache(3)
    assert cache.total_size() == 0
    assert cache.lookup("A") == -1
    print("✓ Test 7 passed: Empty cache")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_size_aware_lru_cache()
