# 0105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium
**Topics:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree
**Link:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Approach

Preorder gives roots in order. The root's position in inorder splits left and right subtrees.
Use a value -> index map for O(1) lookups and consume preorder with an iterator.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Build left before right since preorder is root, left, right.
- Slicing arrays each call makes it O(n^2).
