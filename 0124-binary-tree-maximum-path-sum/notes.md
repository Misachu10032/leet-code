# 0124. Binary Tree Maximum Path Sum

**Difficulty:** Hard
**Topics:** Dynamic Programming, Tree, Depth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Approach

gain(node) = best downward path starting at node (can only pick one side).
At each node, the best path that bends through it is val + left gain + right gain - update the global max.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- Clamp negative gains to 0 (just don't take that branch).
- All-negative tree: answer is the largest single node, so start best at -inf.
