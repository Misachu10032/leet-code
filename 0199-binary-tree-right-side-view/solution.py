"""
LeetCode 0199 - Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Time:  O(n)
Space: O(w)
"""


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def to_list(root):
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        q = deque([root] if root else [])
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.rightSideView(build([1, 2, 3, None, 5, None, 4])))  # [1, 3, 4]
    print(sol.rightSideView(build([1, 2, 3, 4, None, None, None, 5])))  # [1, 3, 4, 5]
    print(sol.rightSideView(build([])))  # []
