# 0097. Interleaving String

**Difficulty:** Medium
**Topics:** String, Dynamic Programming
**Link:** https://leetcode.com/problems/interleaving-string/

## Approach

dp[i][j] = can s1[:i] and s2[:j] interleave into s3[:i + j]. The last char of s3 came from
either s1 (dp[i - 1][j]) or s2 (dp[i][j - 1]). Rolled into one row.

## Complexity

- Time: O(m * n)
- Space: O(n)

## Follow-ups / gotchas

- Check the lengths first.
- Two pointers with greedy choice fails when both strings match the next char.
