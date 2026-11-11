"""
EPI 13.5 - Render a Calendar

Problem:
A calendar app draws each event of a day as a rectangle spanning its start
and finish times, and overlapping events must be stacked side by side. To
size the rectangles, you need the maximum number of events that are going
on at the same moment. Given a list of events as (start, finish) pairs,
return that maximum. Events are closed intervals: an event ending at time t
and another starting at time t overlap.

Constraints:
- 0 <= number of events <= 10^5
- start <= finish for every event
- O(n log n) time, O(n) space

How it works (sweep over endpoints):
1. Create 2n endpoints: (start, is_start=True) and (finish, is_start=False)
2. Sort by time; on ties, put start endpoints before finish endpoints so
   touching events count as overlapping
3. Sweep: +1 on a start, -1 on a finish, tracking the maximum running count

Example 1:
Input: events = [(1, 5), (2, 7), (4, 5), (6, 10), (8, 9), (9, 17), (11, 13),
                 (12, 15), (14, 15)]
Output: 3
Explanation: For example, (1, 5), (2, 7), and (4, 5) all overlap at time 4.

Example 2:
Input: events = [(1, 2), (3, 4)]
Output: 1
"""

from typing import List, Tuple


class Solution:
    def find_max_simultaneous_events(self, events: List[Tuple[int, int]]) -> int:
        """
        Computes the maximum number of events taking place at the same time.

        Args:
            events: List of (start, finish) pairs, inclusive at both ends

        Returns:
            Maximum number of concurrent events (0 if there are none)

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # TODO: Implement maximum concurrent events
        pass


def test_find_max_simultaneous_events():
    """Test cases for maximum concurrent events"""
    solution = Solution()

    # Test case 1: Book example (nine events)
    events1 = [(1, 5), (2, 7), (4, 5), (6, 10), (8, 9), (9, 17), (11, 13),
               (12, 15), (14, 15)]
    assert solution.find_max_simultaneous_events(events1) == 3
    print("✓ Test 1 passed: Book example -> 3")

    # Test case 2: Disjoint events
    assert solution.find_max_simultaneous_events([(1, 2), (3, 4)]) == 1
    print("✓ Test 2 passed: Disjoint events -> 1")

    # Test case 3: No events
    assert solution.find_max_simultaneous_events([]) == 0
    print("✓ Test 3 passed: No events -> 0")

    # Test case 4: Touching endpoints count as overlapping
    assert solution.find_max_simultaneous_events([(1, 3), (3, 5), (5, 7)]) == 2
    print("✓ Test 4 passed: Touching endpoints -> 2")

    # Test case 5: Nested events
    assert solution.find_max_simultaneous_events([(1, 10), (2, 9), (3, 8), (4, 7)]) == 4
    print("✓ Test 5 passed: Nested events -> 4")

    # Test case 6: Identical events
    assert solution.find_max_simultaneous_events([(5, 6)] * 3 + [(7, 8)]) == 3
    print("✓ Test 6 passed: Identical events -> 3")

    # Test case 7: Zero-length event at another event's end
    assert solution.find_max_simultaneous_events([(1, 4), (4, 4), (0, 1)]) == 2
    print("✓ Test 7 passed: Zero-length event -> 2")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_find_max_simultaneous_events()
