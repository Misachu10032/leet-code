# 0066. Plus One

**Difficulty:** Easy
**Topics:** Array, Math
**Link:** https://leetcode.com/problems/plus-one/

## Approach

From the last digit: if it's below 9, increment and stop. Otherwise set it to 0 and carry left.
If every digit was 9, prepend a 1.

## Complexity

- Time: O(n)
- Space: O(1) (O(n) when all 9s)

## Follow-ups / gotchas

- Only the all-9s case grows the array.
