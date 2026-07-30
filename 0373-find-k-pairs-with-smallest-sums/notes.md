# 0373. Find K Pairs with Smallest Sums

**Difficulty:** Medium
**Topics:** Array, Heap (Priority Queue)
**Link:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

## Approach

Like merging k sorted lists: row i is nums1[i] paired with nums2[0..].
Start with (i, 0) for the first k rows, pop the smallest, push (i, j + 1).

## Complexity

- Time: O(k log k)
- Space: O(k)

## Follow-ups / gotchas

- Only seed min(k, len(nums1)) rows.
- Pushing both (i+1, j) and (i, j+1) needs a visited set to avoid duplicates.
