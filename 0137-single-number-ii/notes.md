# 0137. Single Number II

**Difficulty:** Medium
**Topics:** Array, Bit Manipulation
**Link:** https://leetcode.com/problems/single-number-ii/

## Approach

Count each bit mod 3 using two bitmasks: `ones` holds bits seen once, `twos` bits seen twice.
A third occurrence clears the bit from both.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Easier version: for each of 32 bits, sum that bit over all numbers mod 3 (handle the sign bit in Python).
