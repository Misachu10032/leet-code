# 0012. Integer to Roman

**Difficulty:** Medium
**Topics:** Hash Table, Math, String
**Link:** https://leetcode.com/problems/integer-to-roman/

## Approach

Greedy from largest value down. Include the subtractive pairs (CM, XC, IX, ...) in the table
so they're handled like normal symbols.

## Complexity

- Time: O(1)
- Space: O(1)

## Follow-ups / gotchas

- Input is capped at 3999, so time is constant.
