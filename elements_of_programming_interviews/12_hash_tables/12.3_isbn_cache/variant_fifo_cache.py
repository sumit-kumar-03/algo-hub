"""
EPI 12.3 Extra Variant - ISBN Cache with First-In, First-Out Eviction
(Practice problem, not in the book. Difficulty: Easy)
Builds on: pairing a hash table with an ordering structure, as in the LRU
ISBN cache, but with a simpler ordering rule.

Problem:
Build a fixed-capacity cache from ISBNs to prices that evicts the entry that
was inserted earliest (first in, first out) when a new ISBN is inserted into
a full cache. Unlike LRU, lookups do NOT change the eviction order.
- lookup(isbn): return the price, or -1 if absent. Does not affect order.
- insert(isbn, price): if the ISBN is new, add it (evicting the oldest entry
  first if the cache is full). If it is already present, update its price
  but keep its original position in the eviction order.
- erase(isbn): remove the entry; return True if it was present.

Constraints:
- 1 <= capacity <= 10^5
- O(1) time per operation

How it works:
1. Keep a hash table from ISBN to price whose iteration order is insertion
   order (or a hash table plus a queue/linked list of keys)
2. Updating an existing key's price must not move it in that order
3. When inserting a new key into a full cache, remove the oldest key
4. Erase removes the key from the table (and from the order)

Example 1:
Input: cache = FIFOCache(2); insert("A", 1); insert("B", 2); lookup("A");
       insert("C", 3); lookup("A"); lookup("B")
Output: lookup("A") -> 1, then lookup("A") -> -1, lookup("B") -> 2
Explanation: "A" was inserted first, so "C" evicts it even though "A" was
just looked up.

Example 2:
Input: cache = FIFOCache(2); insert("A", 1); insert("B", 2); insert("A", 10);
       insert("C", 3); lookup("A")
Output: -1
Explanation: Updating "A" keeps it the oldest entry, so "C" evicts it.
"""


class FIFOCache:
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
        Returns the price for isbn without changing the eviction order.

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
        Inserts or updates isbn, evicting the oldest entry if a new key
        arrives while the cache is full.

        Args:
            isbn: Book identifier
            price: Price of the book

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement insert with FIFO eviction
        pass

    def erase(self, isbn: str) -> bool:
        """
        Removes isbn from the cache.

        Args:
            isbn: Book identifier

        Returns:
            True if isbn was present and removed, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement erase
        pass


def test_fifo_cache():
    """Test cases for the FIFO ISBN cache"""

    # Test case 1: Basic insert and lookup, missing key
    cache = FIFOCache(2)
    cache.insert("A", 1)
    assert cache.lookup("A") == 1
    assert cache.lookup("Z") == -1
    print("✓ Test 1 passed: Insert and lookup")

    # Test case 2: Lookup does not protect an entry from eviction
    cache = FIFOCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.lookup("A") == 1
    cache.insert("C", 3)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    assert cache.lookup("C") == 3
    print("✓ Test 2 passed: Oldest entry evicted despite lookup")

    # Test case 3: Updating a price keeps the original position
    cache = FIFOCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    cache.insert("A", 10)
    assert cache.lookup("A") == 10
    cache.insert("C", 3)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    print("✓ Test 3 passed: Update keeps FIFO position")

    # Test case 4: Erase present and absent keys
    cache = FIFOCache(3)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.erase("A") is True
    assert cache.erase("A") is False
    assert cache.erase("Z") is False
    assert cache.lookup("A") == -1
    print("✓ Test 4 passed: Erase")

    # Test case 5: Erase frees a slot; re-inserted key goes to the back
    cache = FIFOCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    cache.erase("A")
    cache.insert("A", 5)
    cache.insert("C", 3)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == 5
    assert cache.lookup("C") == 3
    print("✓ Test 5 passed: Re-inserted key is newest")

    # Test case 6: Capacity one
    cache = FIFOCache(1)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    print("✓ Test 6 passed: Capacity of one")

    # Test case 7: Long sequence keeps only the last `capacity` new keys
    cache = FIFOCache(3)
    for i in range(10):
        cache.insert(str(i), i * 100)
        cache.lookup("0")
    assert [cache.lookup(str(i)) for i in range(10)] == [-1] * 7 + [700, 800, 900]
    print("✓ Test 7 passed: Only the 3 newest keys survive")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_fifo_cache()
