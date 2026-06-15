# 0003. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Topics:** Hash Table, String, Sliding Window
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Approach

Sliding window with a map of last index per char. On a repeat inside the window,
jump the left edge past the previous occurrence.

## Complexity

- Time: O(n)
- Space: O(min(n, alphabet))

## Follow-ups / gotchas

- Check `last_seen[ch] >= l` so old occurrences outside the window don't move l backwards.
