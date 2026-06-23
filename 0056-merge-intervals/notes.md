# 0056. Merge Intervals

**Difficulty:** Medium
**Topics:** Array, Sorting
**Link:** https://leetcode.com/problems/merge-intervals/

## Approach

Sort by start. If an interval starts before the last merged one ends, extend it; otherwise start a new one.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Follow-ups / gotchas

- Use max for the end - an interval can be fully inside the previous one.
- Touching intervals ([1,4],[4,5]) count as overlapping.
