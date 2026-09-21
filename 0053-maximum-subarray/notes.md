# 0053. Maximum Subarray

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Dynamic Programming
**Link:** https://leetcode.com/problems/maximum-subarray/

## Approach

Kadane's algorithm: the best subarray ending here either extends the previous one or starts fresh.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Initialize with nums[0], not 0, so all-negative arrays work.
- Divide and conquer follow-up is O(n log n).
