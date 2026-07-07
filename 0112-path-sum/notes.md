# 0112. Path Sum

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/path-sum/

## Approach

Subtract the node value as you go down; at a leaf check if what's left equals the leaf value.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- Must end at a leaf, not any node.
- Empty tree is False even for targetSum 0.
