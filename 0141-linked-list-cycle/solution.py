"""
LeetCode 0141 - Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    head = build([3, 2, 0, -4])
    head.next.next.next.next = head.next
    print(sol.hasCycle(head))  # True
    print(sol.hasCycle(build([1])))  # False
