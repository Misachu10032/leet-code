# 0230. Kth Smallest Element in a BST

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## Approach

Iterative inorder traversal; the kth node popped is the answer. Stops early.

## Complexity

- Time: O(h + k)
- Space: O(h)

## Follow-ups / gotchas

- Follow-up with frequent inserts: store subtree sizes in each node to answer in O(h).
