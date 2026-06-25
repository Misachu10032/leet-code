# 0071. Simplify Path

**Difficulty:** Medium
**Topics:** String, Stack
**Link:** https://leetcode.com/problems/simplify-path/

## Approach

Split on '/'. Skip empty parts and '.', pop on '..', push anything else. Join with '/'.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- '...' is a valid directory name, not a special token.
- '..' at root stays at root.
