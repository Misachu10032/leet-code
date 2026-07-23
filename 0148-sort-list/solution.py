"""
LeetCode 0148 - Sort List
https://leetcode.com/problems/sort-list/

Time:  O(n log n)
Space: O(log n)
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        dummy = tail = ListNode()
        while left and right:
            if left.val <= right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left or right
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.sortList(build([4, 2, 1, 3]))))  # [1, 2, 3, 4]
    print(to_list(sol.sortList(build([-1, 5, 3, 4, 0]))))  # [-1, 0, 3, 4, 5]
    print(to_list(sol.sortList(build([]))))  # []
