# 0134. Gas Station

**Difficulty:** Medium
**Topics:** Array, Greedy
**Link:** https://leetcode.com/problems/gas-station/

## Approach

If total gas >= total cost, a solution exists. Scan once; whenever the tank goes negative,
no station between start and i can work, so restart from i + 1.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Brute force tries every start: O(n^2).
- The answer is unique when it exists.
