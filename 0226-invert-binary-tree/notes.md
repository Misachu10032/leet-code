# 0226. Invert Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/invert-binary-tree/

## Approach

Swap left and right children at every node, recursively.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- The tuple assignment evaluates both recursive calls before assigning, so no temp variable needed.
