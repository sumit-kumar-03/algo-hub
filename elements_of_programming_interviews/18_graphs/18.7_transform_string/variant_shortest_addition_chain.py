"""
EPI 18.7 Variant - Shortest Addition Chain Exponentiation

Problem:
To compute x^n you can start from x and repeatedly create a new power
by multiplying two powers you already have (squaring counts, since a power
may be used twice). In terms of exponents this is an addition chain:
a list starting at 1 where every later entry is the sum of two earlier
entries (possibly the same one), ending at n. Given n, return a shortest
such chain. For example, x^15 can be reached as 1, 2, 4, 5, 10, 15
(5 multiplications). Any shortest chain is accepted.

Constraints:
- 1 <= n <= 200
- The search is exponential in the worst case; iterative deepening with
  pruning keeps it fast for this range

How it works (iterative deepening DFS; each chain is a graph vertex):
1. For limit = 0, 1, 2, ...: run DFS from the chain [1]
2. In DFS, if the last entry equals n, succeed; if the chain already has
   limit steps, fail
3. Prune: if doubling the last entry for every remaining step still cannot
   reach n, fail
4. Otherwise try every sum of two entries that is larger than the last
   entry and at most n (largest first) and recurse
5. The first limit that succeeds gives a shortest chain

Example 1:
Input: n = 15
Output: [1, 2, 4, 5, 10, 15]
Explanation: 5 steps; [1, 2, 3, 6, 12, 15] is equally short.

Example 2:
Input: n = 16
Output: [1, 2, 4, 8, 16]
"""

from typing import List


class Solution:
    def shortest_addition_chain(self, n: int) -> List[int]:
        """
        Finds a shortest addition chain ending at n.

        Args:
            n: Target exponent (n >= 1)

        Returns:
            The chain of exponents, starting at 1 and ending at n

        Time Complexity: Exponential in the chain length (iterative deepening)
        Space Complexity: O(chain length) recursion depth
        """
        # TODO: Implement iterative deepening search for addition chains
        pass


def is_valid_chain(chain, n: int, expected_steps: int) -> bool:
    """Checks the chain starts at 1, ends at n, is additive, and is optimal."""
    if not isinstance(chain, list) or not chain or chain[0] != 1 or chain[-1] != n:
        return False
    for k in range(1, len(chain)):
        earlier = chain[:k]
        if not any(chain[k] - a in earlier for a in earlier):
            return False
    return len(chain) - 1 == expected_steps


def test_shortest_addition_chain():
    """Test cases for shortest addition chains"""
    solution = Solution()

    # Known optimal step counts l(n)
    cases = [(1, 0), (2, 1), (3, 2), (15, 5), (16, 4), (23, 6), (31, 7)]
    for k, (n, steps) in enumerate(cases, 1):
        chain = solution.shortest_addition_chain(n)
        assert is_valid_chain(chain, n, steps)
        print(f"✓ Test {k} passed: n={n} -> {chain} ({steps} steps)")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shortest_addition_chain()
