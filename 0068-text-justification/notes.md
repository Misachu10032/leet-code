# 0068. Text Justification

**Difficulty:** Hard
**Topics:** Array, String, Simulation
**Link:** https://leetcode.com/problems/text-justification/

## Approach

Greedily pack words into a line (each needs at least one space between).
When the next word doesn't fit, spread the extra spaces evenly, giving the leftover ones to the leftmost gaps.
Last line is left-justified.

## Complexity

- Time: O(total characters)
- Space: O(maxWidth)

## Follow-ups / gotchas

- Single-word line: pad on the right.
- `length + len(line)` = letters + minimum spaces if we add one more word.
