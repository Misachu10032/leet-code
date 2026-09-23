# 0190. Reverse Bits

**Difficulty:** Easy
**Topics:** Divide and Conquer, Bit Manipulation
**Link:** https://leetcode.com/problems/reverse-bits/

## Approach

Take the lowest bit of n 32 times and push it onto res from the right.

## Complexity

- Time: O(1) (32 iterations)
- Space: O(1)

## Follow-ups / gotchas

- Always loop 32 times so leading zeros become trailing zeros.
- Called many times: cache reversed bytes and combine 4 lookups.
