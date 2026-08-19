# 0042. Trapping Rain Water

**Difficulty:** Hard
**Topics:** Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
**Link:** https://leetcode.com/problems/trapping-rain-water/

## Approach

Water at i = min(max left, max right) - height[i].
Two pointers: move the smaller side, since its max is the limiting wall.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Simpler version: precompute left_max[] and right_max[] arrays, O(n) space.
- Monotonic stack also works (fills by layers).
