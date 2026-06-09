# 0058. Length of Last Word

**Difficulty:** Easy
**Topics:** String
**Link:** https://leetcode.com/problems/length-of-last-word/

## Approach

Scan from the end: skip trailing spaces, then count characters until the next space.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- One-liner: `len(s.split()[-1])`, but that's O(n) extra space.
