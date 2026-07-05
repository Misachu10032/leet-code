# 0106. Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium
**Topics:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree
**Link:** https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

## Approach

Same as 105 but postorder read backwards gives roots in order root, right, left.
So pop from the end and build the right subtree first.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Right before left - easy to mix up.
- pop() mutates the input list.
