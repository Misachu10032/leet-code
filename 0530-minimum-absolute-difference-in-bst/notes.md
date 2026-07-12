# 0530. Minimum Absolute Difference in BST

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
**Link:** https://leetcode.com/problems/minimum-absolute-difference-in-bst/

## Approach

Inorder traversal of a BST is sorted, so the min difference is between consecutive inorder values.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- Check `prev is not None`, not `if prev` - a value of 0 is valid.
