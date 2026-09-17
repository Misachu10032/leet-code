# 0102. Binary Tree Level Order Traversal

**Difficulty:** Medium
**Topics:** Tree, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/

## Approach

Standard BFS with a queue; process one level at a time by looping len(q) times.

## Complexity

- Time: O(n)
- Space: O(w)

## Follow-ups / gotchas

- `range(len(q))` is evaluated once, so appending children doesn't affect the current level.
