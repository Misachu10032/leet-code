# 0322. Coin Change

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Breadth-First Search
**Link:** https://leetcode.com/problems/coin-change/

## Approach

dp[a] = fewest coins to make a = 1 + min(dp[a - coin]) over coins that fit.

## Complexity

- Time: O(amount * coins)
- Space: O(amount)

## Follow-ups / gotchas

- Greedy (largest coin first) fails, e.g. coins [1, 3, 4], amount 6.
- amount + 1 works as infinity since you never need more than amount coins.
