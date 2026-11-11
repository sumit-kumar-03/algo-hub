"""
EPI 12.3 - Implement an ISBN Cache

Problem:
Build a fixed-capacity cache that maps ISBNs (10-character book identifiers)
to prices. Support lookup, insert, and erase, evicting the least recently
used (LRU) entry when inserting into a full cache.
- lookup(isbn): return the price, or -1 if absent. A hit makes the entry the
  most recently used.
- insert(isbn, price): add the entry. If the ISBN is already present, keep the
  existing price but mark the entry as most recently used.
- erase(isbn): remove the entry; return True if it was present.

Constraints:
- 1 <= capacity <= 10^5
- O(1) time per operation

How it works:
1. Keep a hash table from ISBN to a node in a doubly linked list (or use an
   insertion-ordered map) that orders entries by recency
2. On lookup/insert of an existing key, move its node to the most recent end
3. When inserting a new key into a full cache, evict the node at the least
   recent end and remove it from the hash table
4. Erase removes the key from both structures

Example 1:
Input: cache = LRUCache(2); insert("A", 1); insert("B", 2); lookup("A");
       insert("C", 3); lookup("B")
Output: lookup("A") -> 1, lookup("B") -> -1
Explanation: Looking up "A" makes "B" the LRU entry, so "C" evicts "B".

Example 2:
Input: cache = LRUCache(1); insert("A", 5); insert("A", 9); lookup("A")
Output: 5
Explanation: Re-inserting an existing ISBN does not change its price.
"""


class LRUCache:
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
        Returns the price for isbn and marks it most recently used.

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
        Inserts isbn with price, evicting the LRU entry if the cache is full.
        If isbn is already present, its price is left unchanged but it becomes
        the most recently used entry.

        Args:
            isbn: Book identifier
            price: Price of the book

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement insert with LRU eviction
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


def test_lru_cache():
    """Test cases for the ISBN LRU cache"""

    # Test case 1: Basic insert and lookup, missing key
    cache = LRUCache(2)
    cache.insert("0262033844", 80)
    assert cache.lookup("0262033844") == 80
    assert cache.lookup("0131103628") == -1
    print("✓ Test 1 passed: Insert and lookup")

    # Test case 2: Evicts least recently inserted when nothing was looked up
    cache = LRUCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    cache.insert("C", 3)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    assert cache.lookup("C") == 3
    print("✓ Test 2 passed: Oldest entry evicted")

    # Test case 3: Lookup refreshes recency
    cache = LRUCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.lookup("A") == 1
    cache.insert("C", 3)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == 1
    assert cache.lookup("C") == 3
    print("✓ Test 3 passed: Lookup makes entry most recently used")

    # Test case 4: Re-insert keeps price but refreshes recency
    cache = LRUCache(2)
    cache.insert("A", 5)
    cache.insert("B", 6)
    cache.insert("A", 99)
    assert cache.lookup("A") == 5
    cache.insert("C", 7)
    assert cache.lookup("B") == -1
    assert cache.lookup("A") == 5
    print("✓ Test 4 passed: Re-insert keeps price, refreshes recency")

    # Test case 5: Erase present and absent keys
    cache = LRUCache(3)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.erase("A") is True
    assert cache.erase("A") is False
    assert cache.erase("Z") is False
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    print("✓ Test 5 passed: Erase")

    # Test case 6: Erase frees capacity so nothing else is evicted
    cache = LRUCache(2)
    cache.insert("A", 1)
    cache.insert("B", 2)
    cache.erase("A")
    cache.insert("C", 3)
    assert cache.lookup("B") == 2
    assert cache.lookup("C") == 3
    print("✓ Test 6 passed: Erase frees a slot")

    # Test case 7: Capacity one
    cache = LRUCache(1)
    cache.insert("A", 1)
    cache.insert("B", 2)
    assert cache.lookup("A") == -1
    assert cache.lookup("B") == 2
    print("✓ Test 7 passed: Capacity of one")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_lru_cache()
