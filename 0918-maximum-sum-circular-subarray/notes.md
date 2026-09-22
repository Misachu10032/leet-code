# 0918. Maximum Sum Circular Subarray

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue
**Link:** https://leetcode.com/problems/maximum-sum-circular-subarray/

## Approach

Either the best subarray doesn't wrap (plain Kadane), or it wraps - then it's total minus
the minimum subarray in the middle. Take the max of both.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- If everything is negative, total - min would be 0 (empty array) - return best_max instead.
