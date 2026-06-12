# 0392. Is Subsequence

**Difficulty:** Easy
**Topics:** Two Pointers, String, Dynamic Programming
**Link:** https://leetcode.com/problems/is-subsequence/

## Approach

Walk through t, advancing a pointer in s whenever characters match.

## Complexity

- Time: O(len(t))
- Space: O(1)

## Follow-ups / gotchas

- Follow-up with many s strings: store index lists per char of t and binary search the next index.
