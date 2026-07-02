"""
LeetCode 0086 - Partition List
https://leetcode.com/problems/partition-list/

Time:  O(n)
Space: O(1)
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode()
        after = after_head = ListNode()
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.partition(build([1, 4, 3, 2, 5, 2]), 3)))  # [1, 2, 2, 4, 3, 5]
    print(to_list(sol.partition(build([2, 1]), 2)))  # [1, 2]
