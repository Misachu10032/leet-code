# 0173. Binary Search Tree Iterator

**Difficulty:** Medium
**Topics:** Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
**Link:** https://leetcode.com/problems/binary-search-tree-iterator/

## Approach

Controlled inorder traversal: stack holds the left spine. next() pops the smallest,
then pushes the left spine of its right child.

## Complexity

- Time: O(1) amortized
- Space: O(h)

## Follow-ups / gotchas

- Flattening to a list up front is O(n) space; the stack keeps it O(h).
- Each node is pushed and popped once, so next() is O(1) amortized.
