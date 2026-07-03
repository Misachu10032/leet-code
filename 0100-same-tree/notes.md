# 0100. Same Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/same-tree/

## Approach

Both empty -> same. One empty -> different. Otherwise compare values and recurse on both sides.

## Complexity

- Time: O(n)
- Space: O(h)

## Follow-ups / gotchas

- `p is q` covers both-None (True) and one-None (False) in one line.
