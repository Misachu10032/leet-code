# 0199. Binary Tree Right Side View

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/binary-tree-right-side-view/

## Approach

BFS level by level; the last node in the queue for each level is the one visible from the right.

## Complexity

- Time: O(n)
- Space: O(w)

## Follow-ups / gotchas

- Not just the right spine - a deeper left node can show if the right side is shorter.
- DFS version: visit right first, record the first node seen at each depth.
