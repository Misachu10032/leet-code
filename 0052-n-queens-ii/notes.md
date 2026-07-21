# 0052. N-Queens II

**Difficulty:** Hard
**Topics:** Backtracking
**Link:** https://leetcode.com/problems/n-queens-ii/

## Approach

Place one queen per row. Track used columns, diagonals (r - c) and anti-diagonals (r + c) in sets
so each check is O(1).

## Complexity

- Time: O(n!)
- Space: O(n)

## Follow-ups / gotchas

- r - c is constant on a \\ diagonal, r + c on a / diagonal.
- Bitmask version is faster.
