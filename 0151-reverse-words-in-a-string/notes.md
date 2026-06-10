# 0151. Reverse Words in a String

**Difficulty:** Medium
**Topics:** Two Pointers, String
**Link:** https://leetcode.com/problems/reverse-words-in-a-string/

## Approach

`split()` with no args drops extra spaces; reverse the words and join with single spaces.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Follow-up for mutable strings: reverse the whole array, then reverse each word in place.
- `split(' ')` keeps empty strings - don't use it here.
