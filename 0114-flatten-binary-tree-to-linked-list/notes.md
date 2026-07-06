# 0114. Flatten Binary Tree to Linked List

**Difficulty:** Medium
**Topics:** Linked List, Stack, Tree, Depth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

## Approach

Morris-style: for each node with a left child, hang the right subtree off the rightmost node
of the left subtree, move left to right, clear left. Then continue down the right.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Result must follow preorder.
- Recursive version: reverse postorder (right, left, root) with a prev pointer.
