# 0139. Word Break

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Dynamic Programming, Trie, Memoization
**Link:** https://leetcode.com/problems/word-break/

## Approach

dp[i] = can s[:i] be segmented. dp[i] is true if some word ends at i and dp[i - len(word)] is true.

## Complexity

- Time: O(n * L)
- Space: O(n)

## Follow-ups / gotchas

- Only try lengths that actually appear in the dictionary.
- Words can be reused.
