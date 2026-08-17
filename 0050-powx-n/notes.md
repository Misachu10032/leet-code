# 0050. Pow(x, n)

**Difficulty:** Medium
**Topics:** Math, Recursion
**Link:** https://leetcode.com/problems/powx-n/

## Approach

Fast exponentiation by squaring: walk the bits of n, square x each step,
multiply into the result when the bit is set.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Negative n: invert x and negate n.
- Multiplying x n times is O(n) and times out for n = 2^31.
