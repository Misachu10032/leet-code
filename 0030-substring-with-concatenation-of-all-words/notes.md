# 0030. Substring with Concatenation of All Words

**Difficulty:** Hard
**Topics:** Hash Table, String, Sliding Window
**Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Approach

All words have the same length, so run a sliding window in steps of word_len,
once for each starting offset 0..word_len-1. Keep a counter of words in the window and shrink on overuse.

## Complexity

- Time: O(n * word_len)
- Space: O(number of words)

## Follow-ups / gotchas

- Words can repeat, so compare counts, not sets.
- Reset the window when hitting a word that isn't in the list.
