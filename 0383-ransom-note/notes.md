# 0383. Ransom Note

**Difficulty:** Easy
**Topics:** Hash Table, String, Counting
**Link:** https://leetcode.com/problems/ransom-note/

## Approach

Count letters in magazine, then spend them on the ransom note. Fail if any count runs out.

## Complexity

- Time: O(m + n)
- Space: O(1) (26 letters)

## Follow-ups / gotchas

- One-liner: `not Counter(ransomNote) - Counter(magazine)`.
