# 0014. Longest Common Prefix

**Difficulty:** Easy
**Topics:** String, Trie
**Link:** https://leetcode.com/problems/longest-common-prefix/

## Approach

Start with the first string as the prefix and shrink it until every other string starts with it.

## Complexity

- Time: O(S) where S = total characters
- Space: O(1)

## Follow-ups / gotchas

- Vertical scanning (compare column by column) also works.
- Sorting then comparing only first and last string is a neat trick.
