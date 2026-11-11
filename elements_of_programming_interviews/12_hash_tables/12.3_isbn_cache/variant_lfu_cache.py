"""
EPI 12.3 Extra Variant - ISBN Cache with Least Frequently Used Eviction
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the LRU ISBN cache's hash table plus recency list, generalized
to one recency list per access count so eviction stays O(1).

Problem:
Build a fixed-capacity cache from ISBNs to prices that evicts the entry
used the fewest times. Each entry has a use count: inserting a new ISBN sets
its count to 1, and every successful lookup or insert of an existing ISBN
adds 1. When a new ISBN is inserted into a full cache, evict the entry with
the smallest use count; if several share that count, evict the least
recently used among them.
- lookup(isbn): return the price, or -1 if absent.
- insert(isbn, price): if present, update the price (and count the use);
  otherwise add it, evicting first if the cache is full.

Constraints:
- 1 <= capacity <= 10^5
- O(1) time per operation; finding the minimum count by scanning is too slow

How it works:
1. Hash table from ISBN to (price, count)
2. Hash table from count to an insertion-ordered set of ISBNs with that
   count, kept in recency order (an OrderedDict, or a doubly linked list)
3. Track min_count, the smallest count currently present
4. A use moves the ISBN from bucket c to the most recent end of bucket c+1;
   if bucket c becomes empty and c == min_count, min_count becomes c+1
5. To evict, pop the least recent ISBN from bucket min_count; a newly
   inserted ISBN then goes into bucket 1 and min_count resets to 1

Example 1:
Input: cache = LFUCache(2); insert("A", 1); insert("B", 2); lookup("A");
       insert("C", 3); lookup("B"); lookup("C")
Output: lookup("A") -> 1, lookup("B") -> -1, lookup("C") -> 3
Explanation: "A" has count 2 and "B" count 1, so "C" evicts "B".

Example 2:
Input: cache = LFUCache(2); insert("A", 1); insert("B", 2); lookup("A");
       lookup("B"); insert("C", 3); lookup("A")
Output: lookup("A") at the end -> -1
Explanation: "A" and "B" both have count 2; "A" was used less recently, so
it is evicted.
"""


class LFUCache:
    def __init__(self, capacity: int):
        """
        Initializes an empty cache.

        Args:
            capacity: Maximum number of entries the cache can hold
        """
        # TODO: Initialize the cache's data structures
        pass

    def lookup(self, isbn: str) -> int:
        """
        Returns the price for isbn and counts the use.

        Args:
            isbn: Book identifier

        Returns:
            The cached price, or -1 if isbn is not in the cache

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement lookup
        pass

    def insert(self, isbn: str, price: int) -> None:
        """
        Inserts or updates isbn, evicting the least frequently used entry
        (ties broken by least recent use) if a new key arrives when full.

        Args:
            isbn: Book identifier
            price: Price of the book

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement insert with LFU eviction
        pass


def test_lfu_cache():
    """Test cases for the LFU ISBN cache"""

    # Test case 1: Evict the lowest count
    cache = LFUCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.lookup("A") == 1
    cache.insert("C", 3)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == 1
    assert cache.lookup("C") == 3
    print("✓ Test 1 passed: Lowest count evicted")

    # Test case 2: Tie on count -> evict least recently used
    cache = LFUCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    cache.lookup("A")
    cache.lookup("B")
    cache.insert("C", 3)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    print("✓ Test 2 passed: Tie broken by recency")

    # Test case 3: Updating an existing key counts as a use
    cache = LFUCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    cache.insert("A", 10)
    cache.insert("C", 3)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == 10
    print("✓ Test 3 passed: Update increments count")

    # Test case 4: Missing lookups don't change anything
    cache = LFUCache(1)
    assert cache.lookup("A") == -1
    cache.insert("A", 1)
    assert cache.lookup("Z") == -1
    assert cache.lookup("A") == 1
    print("✓ Test 4 passed: Missing keys")

    # Test case 5: Capacity one always replaces
    cache = LFUCache(1)
    cache.insert("A", 1)
    cache.lookup("A")
    cache.lookup("A")
    cache.insert("B", 2)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    print("✓ Test 5 passed: Capacity one")

    # Test case 6: A new entry (count 1) is the next victim
    cache = LFUCache(3)
    for key, value in [("A", 1), ("B", 2), ("C", 3)]:
        cache.insert(key, value)
        cache.lookup(key)
    cache.insert("D", 4)
    assert cache.lookup("A") == -1
    cache.insert("E", 5)
    assert cache.lookup("D") == -1
    assert cache.lookup("B") == 2
    assert cache.lookup("E") == 5
    print("✓ Test 6 passed: min count resets to 1 after insert")

    # Test case 7: Longer scripted sequence against a naive simulation
    class NaiveLFU:
        def __init__(self, capacity):
            self.capacity, self.tick, self.data = capacity, 0, {}

        def _use(self, key):
            self.tick += 1
            value, count, _ = self.data[key]
            self.data[key] = [value, count + 1, self.tick]

        def lookup(self, key):
            if key not in self.data:
                return -1
            self._use(key)
            return self.data[key][0]

        def insert(self, key, value):
            if key in self.data:
                self._use(key)
                self.data[key][0] = value
                return
            if len(self.data) == self.capacity:
                victim = min(self.data, key=lambda k: (self.data[k][1], self.data[k][2]))
                del self.data[victim]
            self.tick += 1
            self.data[key] = [value, 1, self.tick]

    cache, naive = LFUCache(3), NaiveLFU(3)
    for i in range(400):
        key = "K" + str((i * i + 3 * i) % 7)
        if i % 3 == 0:
            cache.insert(key, i)
            naive.insert(key, i)
        else:
            assert cache.lookup(key) == naive.lookup(key)
    print("✓ Test 7 passed: 400 operations match a naive LFU")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_lfu_cache()
