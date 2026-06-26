# 0150. Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Topics:** Array, Math, Stack
**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Approach

Push numbers. On an operator, pop the two most recent operands, apply, push the result.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Division truncates toward zero: use int(a / b), not a // b (which floors negatives).
- Pop order: second pop is the left operand.
- '-11' is a number, not an operator.
