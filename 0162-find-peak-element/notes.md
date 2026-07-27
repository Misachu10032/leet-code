# 0162. Find Peak Element

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Link:** https://leetcode.com/problems/find-peak-element/

## Approach

If nums[mid] < nums[mid + 1] we're on an upward slope, so a peak exists to the right.
Otherwise a peak is at mid or to its left.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Works because the ends count as -infinity and neighbors are never equal.
- mid + 1 is always in range since lo < hi.
