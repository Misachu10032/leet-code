# 0201. Bitwise AND of Numbers Range

**Difficulty:** Medium
**Topics:** Bit Manipulation
**Link:** https://leetcode.com/problems/bitwise-and-of-numbers-range/

## Approach

The AND of a range is the common binary prefix of left and right (every lower bit flips somewhere
in the range). Shift both right until equal, then shift back.

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- Looping from left to right ANDing everything times out.
- Alternative: `while right > left: right &= right - 1`.
