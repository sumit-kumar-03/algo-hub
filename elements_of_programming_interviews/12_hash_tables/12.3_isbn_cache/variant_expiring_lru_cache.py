"""
EPI 12.3 Extra Variant - LRU Cache with Expiring Entries
(Practice problem, not in the book. Difficulty: Medium)
Builds on: the LRU ISBN cache's hash table plus recency order, with a
second ordering (by insertion time) used to discard stale prices.

Problem:
Prices go stale, so every entry now lives for a fixed time-to-live `ttl`.
Time is passed in explicitly as an integer `now`; across calls, `now` never
decreases. An entry written at time t is valid while now < t + ttl and
expired once now >= t + ttl.
- insert(key, value, now): store the entry with a fresh expiry time and make
  it the most recently used. If the key is already present (expired or
  not), overwrite its value and reset its expiry. If the key is new and the
  cache is full, first discard every expired entry; if it is still full,
  evict the least recently used entry.
- lookup(key, now): return the value if the key is present and not expired,
  making it the most recently used (this does NOT extend its expiry).
  Otherwise return -1, discarding the entry if it had expired.
- size(now): return the number of unexpired entries at time now.

Constraints:
- 1 <= capacity <= 10^5, 1 <= ttl
- O(1) amortized time per operation; scanning all entries for expired ones
  on every call is too slow

How it works:
1. Keep two insertion-ordered maps (or hash table plus two linked lists):
   one in recency order for LRU eviction, one in write-time order. Because
   every entry lives exactly ttl, write-time order is also expiry order
2. To discard expired entries, pop from the front of the write-time order
   while the front has expired, removing each popped key from both orders
3. insert on an existing key moves it to the back of both orders; lookup
   moves it to the back of the recency order only
4. Each entry is popped at most once per write, so the purging is O(1)
   amortized

Example 1:
Input: cache = ExpiringLRUCache(2, ttl=5); insert("A", 1, 0);
       insert("B", 2, 1); lookup("A", 2); insert("C", 3, 3);
       lookup("B", 3); lookup("A", 5)
Output: lookup("A", 2) -> 1, lookup("B", 3) -> -1, lookup("A", 5) -> -1
Explanation: Nothing has expired at time 3, so "C" evicts the LRU entry
"B". At time 5, "A" (written at 0) has expired.

Example 2:
Input: cache = ExpiringLRUCache(2, ttl=3); insert("A", 1, 0);
       insert("B", 2, 2); lookup("A", 2); insert("C", 3, 3); lookup("B", 3)
Output: lookup("A", 2) -> 1, lookup("B", 3) -> 2
Explanation: At time 3, "A" has expired and is discarded first, so the
cache has room for "C" without evicting "B" (even though "B" is the LRU
entry).
"""


class ExpiringLRUCache:
    def __init__(self, capacity: int, ttl: int):
        """
        Initializes an empty cache.

        Args:
            capacity: Maximum number of entries the cache can hold
            ttl: How long an entry stays valid after it is written
        """
        # TODO: Initialize the cache's data structures
        pass

    def lookup(self, key: str, now: int) -> int:
        """
        Returns the value for key if it is present and unexpired.

        Args:
            key: Entry identifier
            now: Current time

        Returns:
            The cached value, or -1 if key is absent or expired

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement lookup with expiry check
        pass

    def insert(self, key: str, value: int, now: int) -> None:
        """
        Writes key with a fresh expiry time, purging expired entries and then
        evicting the LRU entry if a new key arrives while the cache is full.

        Args:
            key: Entry identifier
            value: Value to store
            now: Current time

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        # TODO: Implement insert with expiry purge and LRU eviction
        pass

    def size(self, now: int) -> int:
        """
        Counts the unexpired entries.

        Args:
            now: Current time

        Returns:
            Number of entries still valid at time now

        Time Complexity: O(1) amortized
        Space Complexity: O(1)
        """
        # TODO: Implement size
        pass


def test_expiring_lru_cache():
    """Test cases for the expiring LRU cache"""

    # Test case 1: LRU eviction when nothing has expired; later expiry
    cache = ExpiringLRUCache(2, 5)
    cache.insert("A", 1, 0)
    cache.insert("B", 2, 1)
    assert cache.lookup("A", 2) == 1
    cache.insert("C", 3, 3)
    assert cache.lookup("B", 3) == -1
    assert cache.lookup("C", 4) == 3
    assert cache.lookup("A", 5) == -1
    print("✓ Test 1 passed: LRU eviction, then expiry")

    # Test case 2: Expired entries are discarded before any LRU eviction
    cache = ExpiringLRUCache(2, 3)
    cache.insert("A", 1, 0)
    cache.insert("B", 2, 2)
    assert cache.lookup("A", 2) == 1
    cache.insert("C", 3, 3)
    assert cache.lookup("B", 3) == 2
    assert cache.lookup("C", 3) == 3
    assert cache.lookup("A", 3) == -1
    print("✓ Test 2 passed: Expired entry purged instead of LRU")

    # Test case 3: Expiry boundary (valid while now < t + ttl)
    cache = ExpiringLRUCache(3, 4)
    cache.insert("A", 7, 10)
    assert cache.lookup("A", 13) == 7
    assert cache.lookup("A", 14) == -1
    print("✓ Test 3 passed: Expires exactly at t + ttl")

    # Test case 4: Lookup refreshes recency but not expiry
    cache = ExpiringLRUCache(3, 5)
    cache.insert("A", 1, 0)
    for t in range(1, 5):
        assert cache.lookup("A", t) == 1
    assert cache.lookup("A", 5) == -1
    print("✓ Test 4 passed: Lookups don't extend lifetime")

    # Test case 5: Re-insert resets expiry and value
    cache = ExpiringLRUCache(2, 5)
    cache.insert("A", 1, 0)
    cache.insert("A", 9, 4)
    assert cache.lookup("A", 8) == 9
    assert cache.lookup("A", 9) == -1
    cache.insert("A", 5, 20)
    assert cache.lookup("A", 21) == 5
    print("✓ Test 5 passed: Re-insert resets expiry")

    # Test case 6: size counts only unexpired entries
    cache = ExpiringLRUCache(5, 10)
    cache.insert("A", 1, 0)
    cache.insert("B", 2, 3)
    cache.insert("C", 3, 6)
    assert cache.size(6) == 3
    assert cache.size(10) == 2
    assert cache.size(13) == 1
    assert cache.size(16) == 0
    print("✓ Test 6 passed: size over time")

    # Test case 7: Re-inserting an old key moves it to the back of the
    # expiry order, so the other entry expires first
    cache = ExpiringLRUCache(2, 10)
    cache.insert("A", 1, 0)
    cache.insert("B", 2, 1)
    cache.insert("A", 3, 5)
    assert cache.lookup("B", 11) == -1
    assert cache.lookup("A", 11) == 3
    cache.insert("C", 4, 12)
    assert cache.size(12) == 2
    assert cache.lookup("A", 12) == 3
    assert cache.lookup("C", 12) == 4
    print("✓ Test 7 passed: Expiry order follows latest write")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_expiring_lru_cache()
