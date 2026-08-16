# 0069. Sqrt(x)

**Difficulty:** Easy
**Topics:** Math, Binary Search
**Link:** https://leetcode.com/problems/sqrtx/

## Approach

Binary search for the largest m with m * m <= x.

## Complexity

- Time: O(log x)
- Space: O(1)

## Follow-ups / gotchas

- Use the upper mid ((lo + hi + 1) // 2) since lo = mid, or the loop never ends.
- Newton's method converges faster.
