# 0005. Longest Palindromic Substring

**Difficulty:** Medium
**Topics:** Two Pointers, String, Dynamic Programming
**Link:** https://leetcode.com/problems/longest-palindromic-substring/

## Approach

Expand around each center. There are 2n - 1 centers: each character (odd length)
and each gap between characters (even length).

## Complexity

- Time: O(n^2)
- Space: O(1)

## Follow-ups / gotchas

- Don't forget even-length palindromes like 'bb'.
- DP table is also O(n^2) but uses O(n^2) space. Manacher's is O(n).
