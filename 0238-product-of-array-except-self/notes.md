# 0238. Product of Array Except Self

**Difficulty:** Medium
**Topics:** Array, Prefix Sum
**Link:** https://leetcode.com/problems/product-of-array-except-self/

## Approach

res[i] = (product of everything left of i) * (product of everything right of i).
First pass writes prefix products, second pass multiplies in suffix products.

## Complexity

- Time: O(n)
- Space: O(1) extra (output not counted)

## Follow-ups / gotchas

- No division allowed (and division breaks with zeros anyway).
- Store prefix before multiplying nums[i] in.
