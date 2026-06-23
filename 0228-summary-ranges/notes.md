# 0228. Summary Ranges

**Difficulty:** Easy
**Topics:** Array
**Link:** https://leetcode.com/problems/summary-ranges/

## Approach

Walk the sorted array; extend while the next number is +1, then emit 'a' or 'a->b'.

## Complexity

- Time: O(n)
- Space: O(1) extra

## Follow-ups / gotchas

- Empty input returns [].
