"""
LeetCode 0071 - Simplify Path
https://leetcode.com/problems/simplify-path/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath('/home/'))  # /home
    print(sol.simplifyPath('/home//foo/'))  # /home/foo
    print(sol.simplifyPath('/home/user/Documents/../Pictures'))  # /home/user/Pictures
    print(sol.simplifyPath('/../'))  # /
    print(sol.simplifyPath('/.../a/../b/c/../d/./'))  # /.../b/d
