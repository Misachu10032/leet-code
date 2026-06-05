# 0274. H-Index

**Difficulty:** Medium
**Topics:** Array, Sorting, Counting Sort
**Link:** https://leetcode.com/problems/h-index/

## Approach

Sort descending. The h-index is the largest `i + 1` such that `citations[i] >= i + 1`
(the top i+1 papers all have at least i+1 citations).

## Complexity

- Time: O(n log n)
- Space: O(1)

## Follow-ups / gotchas

- O(n) version: counting sort with buckets 0..n, cap citations at n, then walk from n down summing counts.
- h can't exceed n.
