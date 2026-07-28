# 0034. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Approach

Two lower-bound searches: first index >= target, and first index >= target + 1 (minus one).

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Integer trick target + 1 only works for ints; otherwise write a separate upper bound.
- Check start is in range before reading nums[start].
