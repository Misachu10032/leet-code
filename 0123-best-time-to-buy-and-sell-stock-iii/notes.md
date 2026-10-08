# 0123. Best Time to Buy and Sell Stock III

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

## Approach

State machine with 4 states: after 1st buy, 1st sell, 2nd buy, 2nd sell.
Each state takes the best of staying or transitioning from the previous state at today's price.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Updating in order on the same day is fine - it just means a same-day buy/sell, which adds 0.
- Alternative: best single trade in prefix + best single trade in suffix.
