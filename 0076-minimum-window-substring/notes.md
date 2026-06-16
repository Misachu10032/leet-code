# 0076. Minimum Window Substring

**Difficulty:** Hard
**Topics:** Hash Table, String, Sliding Window
**Link:** https://leetcode.com/problems/minimum-window-substring/

## Approach

Expand right until the window covers t (missing == 0), then shrink left while chars are surplus
(need < 0). Record the window, then drop one required char to keep searching.

## Complexity

- Time: O(m + n)
- Space: O(alphabet)

## Follow-ups / gotchas

- `need` going negative means extra copies in the window.
- r is 1-based here so s[l:r] is the window.
