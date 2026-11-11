"""
EPI 18.5 - Clone a Graph

Problem:
A directed graph is made of GraphVertex objects, each with an integer label
and a list of outgoing edges (references to other vertices). Given a
reference to a vertex u, build a deep copy of the part of the graph
reachable from u and return the copy of u. The copy must use brand-new
vertex objects: no vertex of the clone may be a vertex of the original.
Cycles, self-loops, and duplicate labels are all possible.

Constraints:
- 0 <= number of reachable vertices <= 10^4
- Return None when u is None
- O(V + E) time

How it works (BFS with an original -> clone map):
1. Map u to a new vertex with the same label and enqueue u
2. Pop v; for each edge v -> e:
   - If e is not in the map yet, create its clone and enqueue e
   - Append map[e] to map[v].edges (keeping the edge order)
3. Return map[u]

Example 1:
Input: 0 -> 1, 1 -> 2, 2 -> 0 (a 3-cycle), u = vertex 0
Output: a new 3-cycle 0' -> 1' -> 2' -> 0'

Example 2:
Input: a single vertex 7 with a self-loop
Output: a new vertex 7' whose only edge points to itself
"""

from collections import deque
from typing import List, Optional


class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List["GraphVertex"] = []


class Solution:
    def clone_graph(self, vertex: Optional[GraphVertex]) -> Optional[GraphVertex]:
        """
        Deep-copies the graph reachable from vertex.

        Args:
            vertex: Starting vertex of the original graph (may be None)

        Returns:
            The clone of vertex, or None if vertex is None

        Time Complexity: O(V + E)
        Space Complexity: O(V) for the map and queue
        """
        # TODO: Implement BFS graph cloning
        pass


def is_valid_clone(original: GraphVertex, clone) -> bool:
    """
    Checks the clone is structurally identical to the graph reachable from
    original (same labels, same edge order) and shares no vertex objects.
    """
    if not isinstance(clone, GraphVertex):
        return False
    mapping = {original: clone}
    queue = deque([original])
    while queue:
        v = queue.popleft()
        c = mapping[v]
        if c.label != v.label or len(c.edges) != len(v.edges):
            return False
        for e, ce in zip(v.edges, c.edges):
            if e in mapping:
                if mapping[e] is not ce:
                    return False
            else:
                mapping[e] = ce
                queue.append(e)
    clones = list(mapping.values())
    distinct_clones = len({id(c) for c in clones}) == len(clones)
    no_sharing = not ({id(v) for v in mapping} & {id(c) for c in clones})
    return distinct_clones and no_sharing


def build_graph(n: int, edges) -> List[GraphVertex]:
    """Creates vertices labeled 0..n-1 and adds the directed edges in order."""
    vertices = [GraphVertex(i) for i in range(n)]
    for a, b in edges:
        vertices[a].edges.append(vertices[b])
    return vertices


def test_clone_graph():
    """Test cases for cloning a graph"""
    solution = Solution()

    # Test case 1: Directed 3-cycle
    g1 = build_graph(3, [(0, 1), (1, 2), (2, 0)])
    assert is_valid_clone(g1[0], solution.clone_graph(g1[0]))
    print("✓ Test 1 passed: 3-cycle cloned")

    # Test case 2: Self-loop
    g2 = build_graph(1, [(0, 0)])
    c2 = solution.clone_graph(g2[0])
    assert is_valid_clone(g2[0], c2) and c2.edges[0] is c2
    print("✓ Test 2 passed: self-loop cloned")

    # Test case 3: None input
    assert solution.clone_graph(None) is None
    print("✓ Test 3 passed: None -> None")

    # Test case 4: Diamond with shared target (must not duplicate vertex 3)
    g4 = build_graph(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    c4 = solution.clone_graph(g4[0])
    assert is_valid_clone(g4[0], c4) and c4.edges[0].edges[0] is c4.edges[1].edges[0]
    print("✓ Test 4 passed: diamond cloned with shared vertex")

    # Test case 5: Only reachable vertices are copied
    g5 = build_graph(4, [(1, 0), (0, 2), (3, 1)])
    c5 = solution.clone_graph(g5[1])
    assert is_valid_clone(g5[1], c5)
    print("✓ Test 5 passed: unreachable vertex 3 ignored")

    # Test case 6: Duplicate labels and parallel edges
    g6 = [GraphVertex(5), GraphVertex(5)]
    g6[0].edges = [g6[1], g6[1], g6[0]]
    g6[1].edges = [g6[0]]
    assert is_valid_clone(g6[0], solution.clone_graph(g6[0]))
    print("✓ Test 6 passed: duplicate labels and parallel edges")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_clone_graph()
