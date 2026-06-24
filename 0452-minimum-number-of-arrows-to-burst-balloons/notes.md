# 0452. Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium
**Topics:** Array, Greedy, Sorting
**Link:** https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

## Approach

Sort by end. Shoot at the end of the first balloon; it pops everything starting before that point.
Only shoot again when a balloon starts after the last arrow.

## Complexity

- Time: O(n log n)
- Space: O(1) extra

## Follow-ups / gotchas

- Same idea as interval scheduling / non-overlapping intervals.
- Touching counts as overlapping, so use `>` not `>=`.
