# 0224. Basic Calculator

**Difficulty:** Hard
**Topics:** Math, String, Stack, Recursion
**Link:** https://leetcode.com/problems/basic-calculator/

## Approach

Keep a running result and the sign of the next number. On '(' save (result, sign) on a stack
and start fresh; on ')' finish the inner result and fold it back with the saved sign.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Multi-digit numbers: build num across characters.
- Unary minus like '-(2+3)' works since result starts at 0.
- Spaces are just skipped.
