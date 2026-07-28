# 0153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Approach

Compare mid with the right end. If nums[mid] > nums[hi], the drop (minimum) is to the right of mid;
otherwise the minimum is at mid or left of it.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Compare with hi, not lo - comparing with lo fails when the array isn't rotated.
