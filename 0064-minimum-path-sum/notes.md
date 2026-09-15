# 0064. Minimum Path Sum

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Matrix
**Link:** https://leetcode.com/problems/minimum-path-sum/

## Approach

dp[j] = cheapest cost to reach the current row's cell j = grid value + min(from above, from left).
One row of dp, updated in place.

## Complexity

- Time: O(m * n)
- Space: O(n)

## Follow-ups / gotchas

- Start the row with inf so the first row only comes from the left.
