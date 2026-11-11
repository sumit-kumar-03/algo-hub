"""
EPI 5.12 Extra Variant - Random Pick Avoiding a Blacklist
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the "swap the chosen slot with one from the unused tail" idea
of Fisher-Yates, done virtually with a small hash map instead of a real
array of size n.

Problem:
Design a class that is built from an integer n and a list of distinct
blacklisted integers, all in [0, n - 1]. Each call to pick() must return
an integer from [0, n - 1] that is not blacklisted, with every allowed
value equally likely. n can be up to 10^9, so you cannot list all allowed
values, and each pick() must use exactly one call to the random module
(no retrying until you miss the blacklist).

Constraints:
- 1 <= n <= 10^9; 0 <= len(blacklist) < n, values distinct, in range
- __init__: O(B) time and space, where B = len(blacklist)
- pick(): O(1) time and one random draw (e.g. random.randrange)

How it works (remap the blacklisted low slots):
1. Let m = n - B, the number of allowed values. Draw r from [0, m - 1]
2. Allowed values that are >= m number exactly as many as blacklisted
   values that are < m. Pair them up in __init__: map each blacklisted
   b < m to a distinct allowed value in [m, n - 1]
3. pick(): r = randrange(m); return mapping.get(r, r). Each allowed value
   is hit by exactly one r, so all are equally likely

Example 1:
Input: n = 7, blacklist = [2, 3, 5]
Output: pick() returns 0, 1, 4 or 6, each with probability 1/4
Explanation: m = 4. Blacklisted 2 and 3 are below m, so map them to the
allowed values 4 and 6 above m.

Example 2:
Input: n = 1, blacklist = []
Output: pick() always returns 0
"""

import random
from collections import Counter
from typing import List


class BlacklistPicker:
    def __init__(self, n: int, blacklist: List[int]) -> None:
        """
        Prepares uniform picks from [0, n - 1] minus the blacklist.

        Args:
            n: Size of the range [0, n - 1]
            blacklist: Distinct forbidden values in the range

        Time Complexity: O(B)
        Space Complexity: O(B)
        """
        # TODO: Build the remapping of blacklisted low values
        pass

    def pick(self) -> int:
        """
        Returns a uniformly random allowed value.

        Returns:
            An integer in [0, n - 1] that is not blacklisted

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement a single-draw uniform pick
        pass


def test_blacklist_picker():
    """Test cases for picking around a blacklist (property-based, seeded)"""
    random.seed(710)

    # Test case 1: Single value
    picker = BlacklistPicker(1, [])
    assert all(picker.pick() == 0 for _ in range(10))
    print("✓ Test 1 passed: n = 1 always gives 0")

    # Test case 2: Only one allowed value left
    picker = BlacklistPicker(5, [0, 1, 3, 4])
    assert all(picker.pick() == 2 for _ in range(20))
    print("✓ Test 2 passed: Only 2 is allowed")

    # Test case 3: Example 1 is uniform over {0, 1, 4, 6}
    picker = BlacklistPicker(7, [2, 3, 5])
    counts = Counter(picker.pick() for _ in range(8000))
    assert set(counts) == {0, 1, 4, 6}
    assert all(1700 <= c <= 2300 for c in counts.values()), counts
    print("✓ Test 3 passed: Uniform over {0, 1, 4, 6}")

    # Test case 4: Blacklist entirely in the upper part of the range
    picker = BlacklistPicker(10, [7, 8, 9])
    counts = Counter(picker.pick() for _ in range(7000))
    assert set(counts) == set(range(7))
    assert all(800 <= c <= 1200 for c in counts.values()), counts
    print("✓ Test 4 passed: Uniform over 0..6")

    # Test case 5: Empty blacklist
    picker = BlacklistPicker(4, [])
    counts = Counter(picker.pick() for _ in range(8000))
    assert set(counts) == {0, 1, 2, 3}
    assert all(1700 <= c <= 2300 for c in counts.values()), counts
    print("✓ Test 5 passed: Empty blacklist")

    # Test case 6: Huge n with a scattered blacklist
    n = 10**9
    blacklist = [i * 9973 for i in range(50000)] + [n - 1 - i for i in range(50000)]
    banned = set(blacklist)
    picker = BlacklistPicker(n, blacklist)
    for _ in range(20000):
        x = picker.pick()
        assert 0 <= x < n and x not in banned
    print("✓ Test 6 passed: n = 10^9 with 100,000 blacklisted values")

    # Test case 7: Small range where low values are blacklisted
    picker = BlacklistPicker(6, [0, 1, 2])
    counts = Counter(picker.pick() for _ in range(6000))
    assert set(counts) == {3, 4, 5}
    assert all(1700 <= c <= 2300 for c in counts.values()), counts
    print("✓ Test 7 passed: Uniform over {3, 4, 5}")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_blacklist_picker()
