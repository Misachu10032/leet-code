"""
LeetCode 0117 - Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Time:  O(n)
Space: O(1)
"""


from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build(vals):
    if not vals:
        return None
    root = Node(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = Node(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = Node(vals[i])
            q.append(node.right)
        i += 1
    return root


def levels_by_next(root):
    out = []
    leftmost = root
    while leftmost:
        node, next_level = leftmost, None
        while node:
            out.append(node.val)
            next_level = next_level or node.left or node.right
            node = node.next
        out.append("#")
        leftmost = next_level
    return out


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        leftmost = root
        while leftmost:
            dummy = tail = Node()
            node = leftmost
            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                node = node.next
            leftmost = dummy.next
        return root


if __name__ == "__main__":
    sol = Solution()
    print(levels_by_next(sol.connect(build([1, 2, 3, 4, 5, None, 7]))))  # [1, '#', 2, 3, '#', 4, 5, 7, '#']
