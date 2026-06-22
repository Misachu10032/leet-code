# 0128. Longest Consecutive Sequence

**Difficulty:** Medium
**Topics:** Array, Hash Table, Union Find
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

## Approach

Put everything in a set. Only start counting from numbers that begin a run (num - 1 missing),
so each number is visited at most twice overall.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Iterate the set, not nums, so duplicates don't redo work.
- Sorting is O(n log n), which the problem disallows.
