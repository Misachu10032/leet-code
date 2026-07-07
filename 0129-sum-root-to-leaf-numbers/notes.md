# 0129. Sum Root to Leaf Numbers

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/sum-root-to-leaf-numbers/

## Approach

DFS carrying the number so far (current * 10 + val). At a leaf return it; sum both sides.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- Return 0 for None so a node with one child doesn't double count.
