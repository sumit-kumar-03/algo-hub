"""
EPI 13.8 - Partitioning and Sorting an Array with Many Repeated Entries

Problem:
You are given an array of Person objects, each with an integer age. Reorder
the array in place so that people of the same age are next to each other.
The order of the age groups does not matter. As a follow-up, produce an
arrangement where the age groups also appear in ascending order of age.

Constraints:
- 0 <= len(people) <= 10^6, with few distinct ages (m << n)
- group_by_age: O(n) time, O(m) extra space, in place
- sort_by_age: O(n + m log m) time, O(m) extra space

How it works (in-place counting partition):
1. Count how many people have each age (hash table age -> count)
2. Assign each age a contiguous block: its offset is the sum of the counts of
   the ages placed before it
3. Repeatedly take the next unfilled slot of some age's block, look at the
   person currently there, and swap that person into the next free slot of
   their own age's block; drop an age once its block is full
4. For sorted order, assign the block offsets in ascending order of age

Example 1:
Input: [(Greg, 14), (John, 12), (Andy, 11), (Jim, 13), (Phil, 12), (Bob, 13),
        (Chip, 13), (Tim, 14)]
Output (group_by_age): e.g. [(Greg, 14), (Tim, 14), (John, 12), (Phil, 12),
        (Andy, 11), (Jim, 13), (Bob, 13), (Chip, 13)]

Example 2:
Input: same as Example 1
Output (sort_by_age): ages appear as [11, 12, 12, 13, 13, 13, 14, 14]
"""

import collections
from typing import List

Person = collections.namedtuple("Person", ("age", "name"))


class Solution:
    def group_by_age(self, people: List[Person]) -> None:
        """
        Reorders people in place so that equal ages are contiguous.

        Args:
            people: List of Person(age, name)

        Returns:
            None; people is modified in place

        Time Complexity: O(n)
        Space Complexity: O(m) where m is the number of distinct ages
        """
        # TODO: Implement in-place grouping by age
        pass

    def sort_by_age(self, people: List[Person]) -> None:
        """
        Reorders people in place so equal ages are contiguous and the age
        groups appear in ascending order.

        Args:
            people: List of Person(age, name)

        Returns:
            None; people is modified in place

        Time Complexity: O(n + m log m)
        Space Complexity: O(m) where m is the number of distinct ages
        """
        # TODO: Implement in-place counting sort by age
        pass


def _is_grouped(people: List[Person]) -> bool:
    """True if every age forms one contiguous block."""
    seen = set()
    for i, p in enumerate(people):
        if i > 0 and p.age != people[i - 1].age:
            if p.age in seen:
                return False
        seen.add(p.age)
    return True


def _sample() -> List[Person]:
    return [Person(14, "Greg"), Person(12, "John"), Person(11, "Andy"), Person(13, "Jim"),
            Person(12, "Phil"), Person(13, "Bob"), Person(13, "Chip"), Person(14, "Tim")]


def test_group_by_age():
    """Test cases for grouping and sorting by age"""
    solution = Solution()

    # Test case 1: Book example, grouped
    people1 = _sample()
    solution.group_by_age(people1)
    assert sorted(people1) == sorted(_sample()) and _is_grouped(people1) is True
    print("✓ Test 1 passed: Book example grouped by age")

    # Test case 2: Book example, sorted by age
    people2 = _sample()
    solution.sort_by_age(people2)
    assert sorted(people2) == sorted(_sample())
    assert [p.age for p in people2] == [11, 12, 12, 13, 13, 13, 14, 14]
    print("✓ Test 2 passed: Book example sorted by age")

    # Test case 3: Empty list
    people3 = []
    solution.group_by_age(people3)
    solution.sort_by_age(people3)
    assert people3 == []
    print("✓ Test 3 passed: Empty list")

    # Test case 4: Single age
    people4 = [Person(30, "A"), Person(30, "B"), Person(30, "C")]
    solution.group_by_age(people4)
    assert sorted(people4) == [Person(30, "A"), Person(30, "B"), Person(30, "C")]
    print("✓ Test 4 passed: Single age")

    # Test case 5: Alternating ages, many repeats
    people5 = [Person(20 + (i % 3), f"P{i}") for i in range(30)]
    original5 = list(people5)
    solution.group_by_age(people5)
    assert sorted(people5) == sorted(original5) and _is_grouped(people5) is True
    print("✓ Test 5 passed: Alternating ages grouped")

    # Test case 6: Sorted order with descending input
    people6 = [Person(age, f"Q{i}") for i, age in enumerate([9, 9, 7, 5, 7, 5, 1])]
    original6 = list(people6)
    solution.sort_by_age(people6)
    assert sorted(people6) == sorted(original6)
    assert [p.age for p in people6] == [1, 5, 5, 7, 7, 9, 9]
    print("✓ Test 6 passed: Sorted order")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_group_by_age()
