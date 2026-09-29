# 0072. Edit Distance

**Difficulty:** Medium
**Topics:** String, Dynamic Programming
**Link:** https://leetcode.com/problems/edit-distance/

## Approach

dp[i][j] = edits to turn word1[:i] into word2[:j]. Same last char -> dp[i-1][j-1].
Otherwise 1 + min(delete dp[i-1][j], insert dp[i][j-1], replace dp[i-1][j-1]).

## Complexity

- Time: O(m * n)
- Space: O(n)

## Follow-ups / gotchas

- Base cases: turning a prefix into '' takes i deletions, '' into a prefix takes j inserts.
