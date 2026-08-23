# 0070. Climbing Stairs

**Difficulty:** Easy
**Topics:** Math, Dynamic Programming, Memoization
**Link:** https://leetcode.com/problems/climbing-stairs/

## Approach

ways(n) = ways(n - 1) + ways(n - 2) - it's Fibonacci. Keep just the last two values.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Plain recursion without memo is O(2^n).
