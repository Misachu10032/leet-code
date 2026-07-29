# 0004. Median of Two Sorted Arrays

**Difficulty:** Hard
**Topics:** Array, Binary Search, Divide and Conquer
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Approach

Binary search a cut in the smaller array (i elements) and take j = half - i from the other.
A valid partition has every left element <= every right element; the median comes from the border values.

## Complexity

- Time: O(log(min(m, n)))
- Space: O(1)

## Follow-ups / gotchas

- Search the smaller array so j never goes out of range.
- Use +/- infinity for empty sides.
- Merging is O(m + n) - fine in practice but not what's asked.
