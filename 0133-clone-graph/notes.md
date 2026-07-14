# 0133. Clone Graph

**Difficulty:** Medium
**Topics:** Hash Table, Depth-First Search, Breadth-First Search, Graph
**Link:** https://leetcode.com/problems/clone-graph/

## Approach

DFS with a map original -> clone. The map doubles as the visited set,
so cycles don't cause infinite loops.

## Complexity

- Time: O(V + E)
- Space: O(V)

## Follow-ups / gotchas

- Create the clone before exploring so back-edges can point to it.
