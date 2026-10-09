# 0188. Best Time to Buy and Sell Stock IV

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

## Approach

Generalize III to k transactions: buy[t] / sell[t] = best balance after the t-th buy / sell.

## Complexity

- Time: O(n * k)
- Space: O(k)

## Follow-ups / gotchas

- If k >= n / 2 it's the unlimited case (122) - just sum every upward step.
