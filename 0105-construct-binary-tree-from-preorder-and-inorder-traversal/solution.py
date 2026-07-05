"""
LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Time:  O(n)
Space: O(n)
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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        index = {val: i for i, val in enumerate(inorder)}
        pre = iter(preorder)

        def helper(lo, hi):
            if lo > hi:
                return None
            val = next(pre)
            node = TreeNode(val)
            mid = index[val]
            node.left = helper(lo, mid - 1)
            node.right = helper(mid + 1, hi)
            return node

        return helper(0, len(inorder) - 1)


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))  # [3, 9, 20, None, None, 15, 7]
    print(to_list(sol.buildTree([-1], [-1])))  # [-1]
