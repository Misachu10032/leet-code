# 0209. Minimum Size Subarray Sum

**Difficulty:** Medium
**Topics:** Array, Binary Search, Sliding Window, Prefix Sum
**Link:** https://leetcode.com/problems/minimum-size-subarray-sum/

## Approach

Sliding window over positive numbers: grow right, and while the sum is big enough,
record the length and shrink from the left.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Only works because all numbers are positive.
- Follow-up O(n log n): prefix sums + binary search.
