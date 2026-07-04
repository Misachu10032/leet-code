# 0101. Symmetric Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/symmetric-tree/

## Approach

Two subtrees are mirrors if their roots match, a.left mirrors b.right, and a.right mirrors b.left.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- Iterative: queue of pairs, push (a.left, b.right) and (a.right, b.left).
