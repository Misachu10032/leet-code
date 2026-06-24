# 0057. Insert Interval

**Difficulty:** Medium
**Topics:** Array
**Link:** https://leetcode.com/problems/insert-interval/

## Approach

Three phases: copy intervals ending before the new one, merge everything overlapping it,
then copy the rest.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Already sorted, so no need to sort again (O(n) not O(n log n)).
