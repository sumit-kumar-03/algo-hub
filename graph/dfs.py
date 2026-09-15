"""
Depth-First Search (DFS) Algorithm

Problem:
Given a graph represented as an adjacency list and a starting node, traverse 
the graph using Depth-First Search algorithm. DFS explores as far as possible 
along each branch before backtracking.

Constraints:
- You can implement DFS using recursion or a stack
- 1 <= number of nodes <= 10^4
- Graph can be directed or undirected
- Graph can be connected or disconnected

How it works (Recursive):
1. Mark the current node as visited
2. Process the current node
3. For each unvisited neighbor:
   - Recursively call DFS on that neighbor

How it works (Iterative with Stack):
1. Start at the source node and push it onto a stack
2. While the stack is not empty:
   - Pop a node from the stack
   - If not visited, mark it as visited and process it
   - Push all unvisited neighbors onto the stack

Example 1:
Input: graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 4], 3: [1], 4: [2]}, start = 0
Output: [0, 1, 2, 4, 3] (or similar, order depends on traversal)
Explanation:
Starting from node 0, we go deep into path 0->1->2->4, then backtrack to visit 3.

Example 2:
Input: graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}, start = 0
Output: [0, 1, 3, 4, 2, 5] (or similar)

Example 3 (Disconnected graph):
Input: graph = {0: [1], 1: [0], 2: [3], 3: [2]}, start = 0
Output: [0, 1]
Explanation: Nodes 2 and 3 are not reachable from node 0.
"""

from typing import List, Dict


class Solution:
    def dfs_recursive(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Implement DFS traversal (recursive) that returns nodes in the order they were visited.
        
        Args:
            graph: Adjacency list representation of the graph
            start: Starting node for DFS traversal
            
        Returns:
            List of nodes in DFS traversal order
            
        Time Complexity: O(V + E) where V is vertices and E is edges
        Space Complexity: O(V) for the recursion stack and visited set
        """
        # TODO: Implement recursive DFS
        pass
    
    def dfs_iterative(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Implement DFS traversal (iterative with stack) that returns nodes in the order they were visited.
        
        Args:
            graph: Adjacency list representation of the graph
            start: Starting node for DFS traversal
            
        Returns:
            List of nodes in DFS traversal order
            
        Time Complexity: O(V + E) where V is vertices and E is edges
        Space Complexity: O(V) for the stack and visited set
        """
        # TODO: Implement iterative DFS using a stack
        pass


def test_dfs():
    """Test cases for DFS implementation"""
    solution = Solution()
    
    # Test case 1: Basic DFS traversal (recursive)
    graph1 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1],
        4: [2]
    }
    result1_rec = solution.dfs_recursive(graph1, 0)
    assert len(result1_rec) == 5
    assert result1_rec[0] == 0
    print(f"✓ Test 1 (Recursive) passed: Basic DFS = {result1_rec}")
    
    result1_iter = solution.dfs_iterative(graph1, 0)
    assert len(result1_iter) == 5
    assert result1_iter[0] == 0
    print(f"✓ Test 1 (Iterative) passed: Basic DFS = {result1_iter}")
    
    # Test case 2: Linear graph
    graph2 = {
        0: [1],
        1: [2],
        2: [3],
        3: [4],
        4: []
    }
    expected2 = [0, 1, 2, 3, 4]
    result2_rec = solution.dfs_recursive(graph2, 0)
    assert result2_rec == expected2
    print(f"✓ Test 2 (Recursive) passed: Linear graph = {result2_rec}")
    
    result2_iter = solution.dfs_iterative(graph2, 0)
    assert result2_iter == expected2
    print(f"✓ Test 2 (Iterative) passed: Linear graph = {result2_iter}")
    
    # Test case 3: Tree structure
    graph3 = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [],
        5: []
    }
    result3_rec = solution.dfs_recursive(graph3, 0)
    assert len(result3_rec) == 6
    assert result3_rec[0] == 0
    print(f"✓ Test 3 (Recursive) passed: Tree structure = {result3_rec}")
    
    result3_iter = solution.dfs_iterative(graph3, 0)
    assert len(result3_iter) == 6
    assert result3_iter[0] == 0
    print(f"✓ Test 3 (Iterative) passed: Tree structure = {result3_iter}")
    
    # Test case 4: Single node graph
    graph4 = {0: []}
    expected4 = [0]
    result4_rec = solution.dfs_recursive(graph4, 0)
    assert result4_rec == expected4
    print("✓ Test 4 (Recursive) passed: Single node graph")
    
    result4_iter = solution.dfs_iterative(graph4, 0)
    assert result4_iter == expected4
    print("✓ Test 4 (Iterative) passed: Single node graph")
    
    # Test case 5: Disconnected graph
    graph5 = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    expected5 = [0, 1]
    result5_rec = solution.dfs_recursive(graph5, 0)
    assert result5_rec == expected5
    print(f"✓ Test 5 (Recursive) passed: Disconnected graph = {result5_rec}")
    
    result5_iter = solution.dfs_iterative(graph5, 0)
    assert result5_iter == expected5
    print(f"✓ Test 5 (Iterative) passed: Disconnected graph = {result5_iter}")
    
    # Test case 6: Graph with cycle
    graph6 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    result6_rec = solution.dfs_recursive(graph6, 0)
    assert len(result6_rec) == 4
    assert result6_rec[0] == 0
    print(f"✓ Test 6 (Recursive) passed: Cyclic graph = {result6_rec}")
    
    result6_iter = solution.dfs_iterative(graph6, 0)
    assert len(result6_iter) == 4
    assert result6_iter[0] == 0
    print(f"✓ Test 6 (Iterative) passed: Cyclic graph = {result6_iter}")
    
    # Test case 7: Complex graph
    graph7 = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    result7_rec = solution.dfs_recursive(graph7, 0)
    assert len(result7_rec) == 6
    assert result7_rec[0] == 0
    print(f"✓ Test 7 (Recursive) passed: Complex graph = {result7_rec}")
    
    result7_iter = solution.dfs_iterative(graph7, 0)
    assert len(result7_iter) == 6
    assert result7_iter[0] == 0
    print(f"✓ Test 7 (Iterative) passed: Complex graph = {result7_iter}")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_dfs()
