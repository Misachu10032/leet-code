"""
LeetCode 0133 - Clone Graph
https://leetcode.com/problems/clone-graph/

Time:  O(V + E)
Space: O(V)
"""


from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build(adj_list):
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for node, neighbors in zip(nodes, adj_list):
        node.neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def to_adj_list(node):
    if not node:
        return []
    seen = {node.val: node}
    stack = [node]
    while stack:
        cur = stack.pop()
        for nb in cur.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                stack.append(nb)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)]


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        clones = {node: Node(node.val)}
        stack = [node]
        while stack:
            cur = stack.pop()
            for nb in cur.neighbors:
                if nb not in clones:
                    clones[nb] = Node(nb.val)
                    stack.append(nb)
                clones[cur].neighbors.append(clones[nb])
        return clones[node]


if __name__ == "__main__":
    sol = Solution()
    graph = build([[2, 4], [1, 3], [2, 4], [1, 3]])
    copy = sol.cloneGraph(graph)
    print(to_adj_list(copy))  # [[2, 4], [1, 3], [2, 4], [1, 3]]
    print(copy is not graph)  # True
