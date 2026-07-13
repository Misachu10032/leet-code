# 0098. Validate Binary Search Tree

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree
**Link:** https://leetcode.com/problems/validate-binary-search-tree/

## Approach

Pass down the allowed (low, high) range. Left child narrows high, right child narrows low.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- Checking only parent vs child is wrong - every node must respect all ancestors.
- Strict inequality: duplicates are invalid.
- Alternative: inorder traversal must be strictly increasing.
