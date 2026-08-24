# 0198. House Robber

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming
**Link:** https://leetcode.com/problems/house-robber/

## Approach

At each house: skip it (keep cur) or rob it (prev + num, where prev excludes the neighbor).
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]).

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Circular version (213): run twice, excluding the first or the last house.
