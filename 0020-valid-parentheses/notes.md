# 0020. Valid Parentheses

**Difficulty:** Easy
**Topics:** String, Stack
**Link:** https://leetcode.com/problems/valid-parentheses/

## Approach

Push opening brackets; on a closing bracket the top of the stack must be its match.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Stack must be empty at the end.
- Closing bracket on an empty stack is invalid.
