# 0028. Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Topics:** Two Pointers, String, String Matching
**Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Approach

Try every start position and compare the window with needle.

## Complexity

- Time: O(n * m)
- Space: O(1)

## Follow-ups / gotchas

- KMP gets O(n + m) using the longest-prefix-suffix table.
- Range is n - m + 1 so the last window fits.
