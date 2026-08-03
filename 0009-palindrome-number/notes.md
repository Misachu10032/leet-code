# 0009. Palindrome Number

**Difficulty:** Easy
**Topics:** Math
**Link:** https://leetcode.com/problems/palindrome-number/

## Approach

Reverse only the second half of the digits and compare it with the first half (no string conversion).

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Negatives and numbers ending in 0 (except 0) are never palindromes.
- Odd length: drop the middle digit with reversed_half // 10.
