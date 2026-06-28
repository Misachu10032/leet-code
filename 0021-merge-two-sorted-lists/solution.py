"""
LeetCode 0021 - Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Time:  O(m + n)
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
    print(to_list(sol.mergeTwoLists(build([]), build([]))))  # []
