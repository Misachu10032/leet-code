# 0207. Course Schedule

**Difficulty:** Medium
**Topics:** Depth-First Search, Breadth-First Search, Graph, Topological Sort
**Link:** https://leetcode.com/problems/course-schedule/

## Approach

Cycle detection via Kahn's topological sort: repeatedly take courses with no remaining prereqs.
If we can't take all courses, there's a cycle.

## Complexity

- Time: O(V + E)
- Space: O(V + E)

## Follow-ups / gotchas

- Edge direction: [a, b] means b -> a.
- DFS with 3 colors (unvisited / visiting / done) also detects cycles.
