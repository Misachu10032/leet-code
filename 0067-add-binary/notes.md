# 0067. Add Binary

**Difficulty:** Easy
**Topics:** Math, String, Bit Manipulation, Simulation
**Link:** https://leetcode.com/problems/add-binary/

## Approach

Add from the right end of both strings with a carry, like Add Two Numbers in base 2.

## Complexity

- Time: O(max(m, n))
- Space: O(max(m, n))

## Follow-ups / gotchas

- `bin(int(a, 2) + int(b, 2))[2:]` works in Python but skips the point.
