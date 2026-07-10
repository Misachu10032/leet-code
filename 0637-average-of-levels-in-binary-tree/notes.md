# 0637. Average of Levels in Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/average-of-levels-in-binary-tree/

## Approach

BFS by level: sum the values in each level and divide by the level size.

## Complexity

- Time: O(n)
- Space: O(w)

## Follow-ups / gotchas

- Snapshot len(q) before the loop since the queue grows while iterating.
