# 0146. LRU Cache

**Difficulty:** Medium
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List
**Link:** https://leetcode.com/problems/lru-cache/

## Approach

Hash map key -> node, plus a doubly linked list ordered by recency (front = most recent).
get/put move the node to the front; evict from the back when over capacity.

## Complexity

- Time: O(1) per op
- Space: O(capacity)

## Follow-ups / gotchas

- Store the key in the node so eviction can delete it from the map.
- Sentinel head/tail nodes remove all edge cases.
- Python shortcut: OrderedDict with move_to_end / popitem(last=False).
