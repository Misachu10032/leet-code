# 0222. Count Complete Tree Nodes

**Difficulty:** Easy
**Topics:** Binary Search, Bit Manipulation, Tree, Binary Tree
**Link:** https://leetcode.com/problems/count-complete-tree-nodes/

## Approach

If the leftmost and rightmost depths match, the tree is perfect: 2^h - 1 nodes.
Otherwise recurse; one of the two subtrees is always perfect, so it returns fast.

## Complexity

- Time: O(log^2 n)
- Space: O(log n)

## Follow-ups / gotchas

- Plain traversal is O(n) and passes, but misses the point.
- Binary search on the last level is another O(log^2 n) approach.
