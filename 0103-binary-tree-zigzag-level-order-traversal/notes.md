# 0103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium
**Topics:** Tree, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

## Approach

Level order BFS, reversing every other level.

## Complexity

- Time: O(n)
- Space: O(w)

## Follow-ups / gotchas

- Don't change the order children are enqueued - just reverse the output level.
- Could also appendleft into a deque per level.
