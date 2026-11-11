"""
Breadth-First Search (BFS) Algorithm

Problem:
Given a graph represented as an adjacency list and a starting node, traverse 
the graph using Breadth-First Search algorithm. BFS explores all vertices at 
the present depth level before moving to vertices at the next depth level.

Constraints:
- You must implement the BFS algorithm using a queue
- 1 <= number of nodes <= 10^4
- Graph can be directed or undirected
- Graph can be connected or disconnected

How it works:
1. Start at the source node and mark it as visited
2. Add the source node to a queue
3. While the queue is not empty:
   - Dequeue a node from the front
   - Process the node
   - For each unvisited neighbor of the dequeued node:
     - Mark it as visited
     - Enqueue it

Example 1:
Input: graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 4], 3: [1], 4: [2]}, start = 0
Output: [0, 1, 2, 3, 4]
Explanation:
Starting from node 0, we visit neighbors 1 and 2.
Then from 1, we visit 3 (0 and 2 are already visited).
Then from 2, we visit 4.

Example 2:
Input: graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}, start = 0
Output: [0, 1, 2, 3, 4, 5]

Example 3 (Disconnected graph):
Input: graph = {0: [1], 1: [0], 2: [3], 3: [2]}, start = 0
Output: [0, 1]
Explanation: Nodes 2 and 3 are not reachable from node 0.
"""

from typing import List, Dict
from collections import deque


class Solution:
    def bfs(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Implement BFS traversal that returns nodes in the order they were visited.
        
        Args:
            graph: Adjacency list representation of the graph
            start: Starting node for BFS traversal
            
        Returns:
            List of nodes in BFS traversal order
            
        Time Complexity: O(V + E) where V is vertices and E is edges
        Space Complexity: O(V) for the queue and visited set
        """

        visited = set()

        queue = deque()

        queue.append(start)

        while queue:
            _node = queue.popleft()

            if _node not in visited:
                visited.add(_node)
                queue.extend(graph.get(_node,[]))

        return visited
            


def test_bfs():
    """Test cases for BFS implementation"""
    solution = Solution()
    
    # Test case 1: Basic BFS traversal
    graph1 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1],
        4: [2]
    }
    expected1 = [0, 1, 2, 3, 4]
    result1 = solution.bfs(graph1, 0)
    assert result1 == expected1
    print(f"✓ Test 1 passed: Basic BFS = {result1}")
    
    # Test case 2: Linear graph
    graph2 = {
        0: [1],
        1: [2],
        2: [3],
        3: [4],
        4: []
    }
    expected2 = [0, 1, 2, 3, 4]
    result2 = solution.bfs(graph2, 0)
    assert result2 == expected2
    print(f"✓ Test 2 passed: Linear graph = {result2}")
    
    # Test case 3: Tree structure
    graph3 = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [],
        5: []
    }
    expected3 = [0, 1, 2, 3, 4, 5]
    result3 = solution.bfs(graph3, 0)
    assert result3 == expected3
    print(f"✓ Test 3 passed: Tree structure = {result3}")
    
    # Test case 4: Single node graph
    graph4 = {0: []}
    expected4 = [0]
    result4 = solution.bfs(graph4, 0)
    assert result4 == expected4
    print("✓ Test 4 passed: Single node graph")
    
    # Test case 5: Disconnected graph
    graph5 = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    expected5 = [0, 1]
    result5 = solution.bfs(graph5, 0)
    assert result5 == expected5
    print(f"✓ Test 5 passed: Disconnected graph = {result5}")
    
    # Test case 6: Graph with cycle
    graph6 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    expected6 = [0, 1, 2, 3]
    result6 = solution.bfs(graph6, 0)
    assert result6 == expected6
    print(f"✓ Test 6 passed: Cyclic graph = {result6}")
    
    # Test case 7: Complex graph
    graph7 = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    result7 = solution.bfs(graph7, 0)
    assert len(result7) == 6
    assert result7[0] == 0
    print(f"✓ Test 7 passed: Complex graph = {result7}")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_bfs()
