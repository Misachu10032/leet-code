# 0135. Candy

**Difficulty:** Hard
**Topics:** Array, Greedy
**Link:** https://leetcode.com/problems/candy/

## Approach

Two passes. Left to right satisfies the left-neighbor rule, right to left satisfies the right-neighbor rule.
Take the max in the second pass so both hold.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Equal ratings don't need equal candies.
- O(1) space version counts up/down slopes but is much trickier.
