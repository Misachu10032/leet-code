# 0300. Longest Increasing Subsequence

**Difficulty:** Medium
**Topics:** Array, Binary Search, Dynamic Programming
**Link:** https://leetcode.com/problems/longest-increasing-subsequence/

## Approach

Patience sorting: tails[k] is the smallest possible tail of an increasing subsequence of length k + 1.
For each number, binary search where it goes - extend or replace.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Follow-ups / gotchas

- tails isn't the actual subsequence, only its length is meaningful.
- O(n^2) DP: dp[i] = 1 + max(dp[j]) for j < i with nums[j] < nums[i].
- bisect_left for strictly increasing.
