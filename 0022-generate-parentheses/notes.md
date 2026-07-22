# 0022. Generate Parentheses

**Difficulty:** Medium
**Topics:** String, Dynamic Programming, Backtracking
**Link:** https://leetcode.com/problems/generate-parentheses/

## Approach

Backtrack: add '(' while we have some left, add ')' only if it wouldn't exceed the opens.
Every complete string is then valid.

## Complexity

- Time: O(4^n / sqrt(n))
- Space: O(n)

## Follow-ups / gotchas

- The count of results is the nth Catalan number.
