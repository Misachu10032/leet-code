# 0049. Group Anagrams

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Sorting
**Link:** https://leetcode.com/problems/group-anagrams/

## Approach

Anagrams share the same letter counts. Use the 26-count tuple as a dict key and group strings under it.

## Complexity

- Time: O(n * k)
- Space: O(n * k)

## Follow-ups / gotchas

- `tuple(sorted(s))` as key is simpler but O(k log k) per string.
- Lists aren't hashable - convert to tuple.
