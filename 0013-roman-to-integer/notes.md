# 0013. Roman to Integer

**Difficulty:** Easy
**Topics:** Hash Table, Math, String
**Link:** https://leetcode.com/problems/roman-to-integer/

## Approach

Add each symbol, but subtract it when a larger symbol follows (IV, IX, XL, ...).

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Only check the next symbol, not the rest of the string.
