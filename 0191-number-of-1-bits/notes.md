# 0191. Number of 1 Bits

**Difficulty:** Easy
**Topics:** Divide and Conquer, Bit Manipulation
**Link:** https://leetcode.com/problems/number-of-1-bits/

## Approach

n & (n - 1) clears the lowest set bit. Count how many times until n is 0.

## Complexity

- Time: O(number of set bits)
- Space: O(1)

## Follow-ups / gotchas

- Simple version: check n & 1 and shift, 32 iterations.
