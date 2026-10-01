# 0136. Single Number

**Difficulty:** Easy
**Topics:** Array, Bit Manipulation
**Link:** https://leetcode.com/problems/single-number/

## Approach

XOR everything: pairs cancel out (x ^ x = 0) and the single number is left.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- A set or Counter works but is O(n) space.
