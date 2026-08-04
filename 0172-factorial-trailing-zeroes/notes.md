# 0172. Factorial Trailing Zeroes

**Difficulty:** Medium
**Topics:** Math
**Link:** https://leetcode.com/problems/factorial-trailing-zeroes/

## Approach

Each trailing zero comes from a factor 10 = 2 * 5, and 5s are the limiting factor.
Count multiples of 5, 25, 125, ... in 1..n.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- 25 contributes two 5s, 125 three, etc. - that's why we keep dividing.
- Never compute n! itself.
