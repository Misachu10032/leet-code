# 0017. Letter Combinations of a Phone Number

**Difficulty:** Medium
**Topics:** Hash Table, String, Backtracking
**Link:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Approach

Backtracking: for each digit choose one of its letters, recurse to the next digit.

## Complexity

- Time: O(4^n * n)
- Space: O(n)

## Follow-ups / gotchas

- Empty input returns [], not [''].
- 7 and 9 have 4 letters.
