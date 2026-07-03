# 0104. Maximum Depth of Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Approach

Depth = 1 + max(depth of left, depth of right). Empty tree has depth 0.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- BFS version: count levels.
- Recursion depth can hit the limit on a skewed tree of 10^4 nodes; iterative stack avoids it.
