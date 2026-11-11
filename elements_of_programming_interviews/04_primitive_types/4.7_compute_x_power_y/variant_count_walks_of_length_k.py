"""
EPI 4.7 Extra Variant - Count Walks of Exactly k Steps in a Graph
(Practice problem, not in the book. Difficulty: Hard)
Builds on: repeated squaring, applied to n x n matrices.

Problem:
You are given a directed graph on nodes 0..n-1 as an n x n adjacency
matrix adj, where adj[i][j] == 1 means there is an edge from i to j
(self-loops are allowed). A walk of length k is a sequence of k edges
where each edge starts where the previous one ended; nodes and edges may
repeat. Given source s, target t and k (up to 10^18), return the number
of walks of length exactly k from s to t, mod 1,000,000,007.

Constraints:
- 1 <= n <= 30; adj[i][j] is 0 or 1
- 0 <= s, t < n; 0 <= k <= 10^18
- A walk of length 0 exists only from a node to itself (count 1)
- O(n^3 log k) time, O(n^2) space

How it works:
1. Entry (i, j) of adj^k counts walks of length k from i to j (each
   matrix multiplication extends every walk by one edge and sums over the
   middle node)
2. Compute adj^k with repeated squaring: result = identity, base = adj;
   for each bit of k, multiply result by base when the bit is 1, then
   square base. Reduce entries mod 10^9 + 7 after each product
3. Return result[s][t]

Example 1:
Input: adj = [[0, 1, 0], [0, 0, 1], [1, 0, 0]], s = 0, t = 0, k = 3
Output: 1
Explanation: The only 3-step walk from 0 is 0 -> 1 -> 2 -> 0.

Example 2:
Input: adj = [[1, 1], [1, 1]], s = 0, t = 1, k = 3
Output: 4
Explanation: Each of the 2 middle nodes after steps 1 and 2 can be
either node, giving 2 * 2 = 4 walks.
"""

from typing import List


class Solution:
    def count_walks(self, adj: List[List[int]], s: int, t: int, k: int) -> int:
        """
        Counts walks of exactly k edges from s to t.

        Args:
            adj: n x n 0/1 adjacency matrix of a directed graph
            s: Start node
            t: End node
            k: Number of edges in the walk

        Returns:
            The number of such walks mod 1,000,000,007

        Time Complexity: O(n^3 log k)
        Space Complexity: O(n^2)
        """
        # TODO: Implement walk counting with matrix repeated squaring
        pass


def count_walks_dp(adj: List[List[int]], s: int, t: int, k: int) -> int:
    """Slow reference: step-by-step dynamic programming over k."""
    n = len(adj)
    ways = [0] * n
    ways[s] = 1
    for _ in range(k):
        nxt = [0] * n
        for i in range(n):
            if ways[i]:
                for j in range(n):
                    if adj[i][j]:
                        nxt[j] += ways[i]
        ways = nxt
    return ways[t] % (10**9 + 7)


def test_count_walks():
    """Test cases for counting walks of length k"""
    solution = Solution()
    MOD = 10**9 + 7

    # Test case 1: Examples
    cycle = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    assert solution.count_walks(cycle, 0, 0, 3) == 1
    assert solution.count_walks([[1, 1], [1, 1]], 0, 1, 3) == 4
    print("✓ Test 1 passed: Examples")

    # Test case 2: k = 0 counts only the empty walk from a node to itself
    assert solution.count_walks(cycle, 1, 1, 0) == 1
    assert solution.count_walks(cycle, 0, 1, 0) == 0
    print("✓ Test 2 passed: k = 0")

    # Test case 3: Directed cycle only returns home every 3 steps
    assert solution.count_walks(cycle, 0, 0, 10**18) == 0  # 10^18 mod 3 == 1
    assert solution.count_walks(cycle, 0, 1, 10**18) == 1
    assert solution.count_walks(cycle, 2, 2, 3 * 10**17) == 1
    print("✓ Test 3 passed: Directed 3-cycle with huge k")

    # Test case 4: Single node, no edges vs a self-loop
    assert solution.count_walks([[0]], 0, 0, 5) == 0
    assert solution.count_walks([[1]], 0, 0, 10**18) == 1
    print("✓ Test 4 passed: Single node")

    # Test case 5: Complete graph with self-loops has n^(k - 1) walks
    n = 5
    full = [[1] * n for _ in range(n)]
    k = 10**15 + 7
    assert solution.count_walks(full, 0, 4, k) == pow(n, k - 1, MOD)
    print("✓ Test 5 passed: Complete graph on 5 nodes")

    # Test case 6: Matches step-by-step DP on a mixed graph
    adj = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0],
    ]
    for k in (1, 2, 5, 17, 40, 64):
        for s in range(6):
            for t in range(6):
                assert solution.count_walks(adj, s, t, k) == count_walks_dp(adj, s, t, k)
    print("✓ Test 6 passed: Matches step-by-step DP on a 6-node graph")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_count_walks()
