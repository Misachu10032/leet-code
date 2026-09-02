# 0015. 3Sum

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Sorting
**Link:** https://leetcode.com/problems/3sum/

## Approach

Sort, fix the first number, then run Two Sum II (two pointers) on the rest.

## Complexity

- Time: O(n^2)
- Space: O(1) extra (ignoring sort)

## Follow-ups / gotchas

- Skip duplicate values for i and for l to avoid duplicate triplets.
- Break early once nums[i] > 0.
