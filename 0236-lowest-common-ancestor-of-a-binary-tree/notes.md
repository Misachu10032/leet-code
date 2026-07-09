# 0236. Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## Approach

Return p or q if found, else None. If both sides return something, this node is the LCA.
Otherwise pass up whichever side found something.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- A node can be its own ancestor (p is ancestor of q -> answer p).
- For a BST (235) you can just compare values instead.
