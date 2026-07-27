# 0033. Search in Rotated Sorted Array

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Approach

One half around mid is always sorted. Check if the target lies in that sorted half;
if yes search there, otherwise search the other half.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Use <= in nums[lo] <= nums[mid] for when lo == mid.
