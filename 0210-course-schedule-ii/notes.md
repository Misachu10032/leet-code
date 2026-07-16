# 0210. Course Schedule II

**Difficulty:** Medium
**Topics:** Depth-First Search, Breadth-First Search, Graph, Topological Sort
**Link:** https://leetcode.com/problems/course-schedule-ii/

## Approach

Same as Course Schedule, but record the order courses are popped from Kahn's queue.

## Complexity

- Time: O(V + E)
- Space: O(V + E)

## Follow-ups / gotchas

- Return [] when there's a cycle (order shorter than numCourses).
- Any valid topological order is accepted.
