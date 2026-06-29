"""
LeetCode 0138 - Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/

Time:  O(n)
Space: O(n)
"""


from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def build(pairs):
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, rand) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand is not None:
            nodes[i].random = nodes[rand]
    return nodes[0] if nodes else None


def to_list(head):
    index = {}
    node, i = head, 0
    while node:
        index[node] = i
        node, i = node.next, i + 1
    out = []
    node = head
    while node:
        out.append([node.val, index.get(node.random)])
        node = node.next
    return out


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copies = {None: None}
        node = head
        while node:
            copies[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            copies[node].next = copies[node.next]
            copies[node].random = copies[node.random]
            node = node.next
        return copies[head]


if __name__ == "__main__":
    sol = Solution()
    head = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copy = sol.copyRandomList(head)
    print(to_list(copy))  # [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    print(copy is not head)  # True
