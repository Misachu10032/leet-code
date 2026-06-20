# 0242. Valid Anagram

**Difficulty:** Easy
**Topics:** Hash Table, String, Sorting
**Link:** https://leetcode.com/problems/valid-anagram/

## Approach

Count array of 26: +1 for chars in s, -1 for chars in t. All zeros means anagram.

## Complexity

- Time: O(n)
- Space: O(1) (26 letters)

## Follow-ups / gotchas

- Unicode follow-up: use a Counter / dict instead of a fixed array.
- Sorting both is O(n log n).
