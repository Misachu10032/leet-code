# 0035. Search Insert Position

**Difficulty:** Easy
**Topics:** Array, Binary Search
**Link:** https://leetcode.com/problems/search-insert-position/

## Approach

Lower bound binary search: find the first index with nums[i] >= target.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- hi = len(nums) (not len - 1) so inserting at the end works.
- Same as bisect.bisect_left.
