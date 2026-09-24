# 0063. Unique Paths II

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Matrix
**Link:** https://leetcode.com/problems/unique-paths-ii/

## Approach

paths(cell) = paths(above) + paths(left), and 0 on an obstacle. One dp row is enough.

## Complexity

- Time: O(m * n)
- Space: O(n)

## Follow-ups / gotchas

- Obstacle on the start cell means 0 paths - handled since dp[0] gets zeroed.
