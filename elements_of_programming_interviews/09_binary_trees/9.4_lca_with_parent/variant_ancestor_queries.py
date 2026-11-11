"""
EPI 9.4 Extra Variant - Fast kth-Ancestor and LCA Queries
(Practice problem, not in the book. Difficulty: Hard)
Builds on: the main problem's two steps (lift the deeper node to equal
depth, then lift both until they meet), done in O(log n) jumps instead of
one parent step at a time.

Problem:
Every node in a binary tree stores a pointer to its parent (None for the
root). You will receive many queries on the same, unchanging tree, so you
may preprocess it once. Design a class that answers:
- kth_ancestor(node, k): the node reached by following k parent pointers
  from node (k = 0 returns node itself), or None if that climbs past the root
- lca(a, b): the lowest common ancestor of two nodes

Constraints:
- 1 <= number of nodes <= 10^5; the tree may be a long chain, so avoid
  deep recursion
- Preprocessing: O(n log n) time and space
- Each query: O(log n) time
- Node keys may repeat; use node objects (e.g., as dictionary keys)

How it works (binary lifting / jump pointers):
1. Traverse the tree once (iteratively) to record each node's depth and
   up[0][node] = node.parent
2. Build jump tables: up[j][node] = up[j - 1][up[j - 1][node]], i.e., the
   2^j-th ancestor
3. kth_ancestor: for every set bit j of k, jump with up[j]
4. lca: lift the deeper node by the depth difference; if the nodes are now
   equal, done; otherwise, for j from high to low, jump both whenever
   up[j] differs for them; the answer is then their parent

Example 1 (Figure 9.1 in the book):
Input: kth_ancestor(M, 3), lca(M, P)
Output: node J (key 2), node I (key 6)
Explanation: M -> L -> K -> J; the LCA is the same as in the main problem.

Example 2:
Input: kth_ancestor(M, 6)
Output: None
Explanation: M has depth 5, so it has only 5 proper ancestors.
"""

import random
from typing import Dict, List, Optional


class BinaryTreeNode:
    def __init__(
        self,
        data: int = 0,
        left: "Optional[BinaryTreeNode]" = None,
        right: "Optional[BinaryTreeNode]" = None,
        parent: "Optional[BinaryTreeNode]" = None,
    ):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class AncestorQueries:
    def __init__(self, root: BinaryTreeNode):
        """
        Preprocesses the tree for fast ancestor queries.

        Args:
            root: Root of the tree (parent pointers are already set)

        Time Complexity: O(n log n)
        Space Complexity: O(n log n)
        """
        # TODO: Implement preprocessing (depths and jump tables)
        pass

    def kth_ancestor(self, node: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
        """
        Returns the ancestor k levels above node.

        Args:
            node: A node in the tree
            k: Number of levels to climb (k >= 0)

        Returns:
            The kth ancestor, or None if k exceeds the node's depth

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement kth ancestor with jump pointers
        pass

    def lca(self, a: BinaryTreeNode, b: BinaryTreeNode) -> BinaryTreeNode:
        """
        Returns the lowest common ancestor of a and b.

        Args:
            a: A node in the tree
            b: Another node in the same tree

        Returns:
            The deepest node that is an ancestor of both

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement LCA with jump pointers
        pass


def set_parents(root: BinaryTreeNode) -> None:
    """Fills in the parent field of every node (iteratively)."""
    root.parent = None
    stack = [root]
    while stack:
        node = stack.pop()
        for child in (node.left, node.right):
            if child:
                child.parent = node
                stack.append(child)


def build_figure_9_1() -> Dict[str, BinaryTreeNode]:
    """Builds the Figure 9.1 tree and returns its nodes keyed by letter."""
    N = BinaryTreeNode
    t = {}
    t["D"], t["E"] = N(28), N(0)
    t["C"] = N(271, t["D"], t["E"])
    t["H"] = N(17)
    t["G"] = N(3, t["H"])
    t["F"] = N(561, None, t["G"])
    t["B"] = N(6, t["C"], t["F"])
    t["M"] = N(641)
    t["L"] = N(401, None, t["M"])
    t["N"] = N(257)
    t["K"] = N(1, t["L"], t["N"])
    t["J"] = N(2, None, t["K"])
    t["P"] = N(28)
    t["O"] = N(271, None, t["P"])
    t["I"] = N(6, t["J"], t["O"])
    t["A"] = N(314, t["B"], t["I"])
    set_parents(t["A"])
    return t


def _random_tree(n: int, seed: int) -> List[BinaryTreeNode]:
    """Builds a random binary tree with n nodes; returns all nodes."""
    rng = random.Random(seed)
    nodes = [BinaryTreeNode(0)]
    open_slots = [(nodes[0], "left"), (nodes[0], "right")]
    for i in range(1, n):
        idx = rng.randrange(len(open_slots))
        parent, side = open_slots[idx]
        open_slots[idx] = open_slots[-1]
        open_slots.pop()
        child = BinaryTreeNode(i % 7)  # repeated keys on purpose
        setattr(parent, side, child)
        nodes.append(child)
        open_slots += [(child, "left"), (child, "right")]
    set_parents(nodes[0])
    return nodes


def _slow_kth(node: Optional[BinaryTreeNode], k: int) -> Optional[BinaryTreeNode]:
    while node is not None and k > 0:
        node, k = node.parent, k - 1
    return node


def _slow_lca(a: BinaryTreeNode, b: BinaryTreeNode) -> BinaryTreeNode:
    seen = set()
    while a is not None:
        seen.add(id(a))
        a = a.parent
    while id(b) not in seen:
        b = b.parent
    return b


def test_ancestor_queries():
    """Test cases for jump-pointer ancestor queries"""
    # Test case 1: Book tree, kth ancestor
    t = build_figure_9_1()
    q = AncestorQueries(t["A"])
    assert q.kth_ancestor(t["M"], 0) is t["M"]
    assert q.kth_ancestor(t["M"], 3) is t["J"]
    assert q.kth_ancestor(t["M"], 5) is t["A"]
    assert q.kth_ancestor(t["M"], 6) is None
    print("✓ Test 1 passed: kth ancestor on Figure 9.1")

    # Test case 2: Book tree, LCA queries
    assert q.lca(t["M"], t["P"]) is t["I"]
    assert q.lca(t["M"], t["N"]) is t["K"]
    assert q.lca(t["B"], t["H"]) is t["B"]
    assert q.lca(t["D"], t["P"]) is t["A"]
    assert q.lca(t["G"], t["G"]) is t["G"]
    print("✓ Test 2 passed: LCA on Figure 9.1")

    # Test case 3: Single-node tree
    lone = BinaryTreeNode(1)
    q3 = AncestorQueries(lone)
    assert q3.kth_ancestor(lone, 0) is lone
    assert q3.kth_ancestor(lone, 1) is None
    assert q3.lca(lone, lone) is lone
    print("✓ Test 3 passed: Single node")

    # Test case 4: Long chain (no deep recursion allowed)
    chain = [BinaryTreeNode(0)]
    for i in range(1, 20000):
        nxt = BinaryTreeNode(i)
        chain[-1].left = nxt
        chain.append(nxt)
    set_parents(chain[0])
    q4 = AncestorQueries(chain[0])
    assert q4.kth_ancestor(chain[19999], 19999) is chain[0]
    assert q4.kth_ancestor(chain[19999], 12345) is chain[19999 - 12345]
    assert q4.kth_ancestor(chain[100], 101) is None
    assert q4.lca(chain[19999], chain[7]) is chain[7]
    print("✓ Test 4 passed: 20,000-node chain")

    # Test case 5: Random trees, checked against slow climbing
    for seed in range(3):
        nodes = _random_tree(2000, seed)
        qr = AncestorQueries(nodes[0])
        rng = random.Random(100 + seed)
        for _ in range(500):
            a, b = rng.choice(nodes), rng.choice(nodes)
            k = rng.randrange(0, 40)
            assert qr.kth_ancestor(a, k) is _slow_kth(a, k)
            assert qr.lca(a, b) is _slow_lca(a, b)
    print("✓ Test 5 passed: Random trees")

    # Test case 6: Many queries on a deep chain finish quickly
    for i in range(0, 20000, 7):
        assert q4.lca(chain[i], chain[19999 - i]) is chain[min(i, 19999 - i)]
    print("✓ Test 6 passed: Many queries on a deep chain")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_ancestor_queries()
