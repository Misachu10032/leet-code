# 0290. Word Pattern

**Difficulty:** Easy
**Topics:** Hash Table, String
**Link:** https://leetcode.com/problems/word-pattern/

## Approach

Same as Isomorphic Strings, but mapping letters <-> words. Two dicts for a bijection.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Check the lengths first; zip silently stops at the shorter one.
