"""
LeetCode 0020 - Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid('()'))  # True
    print(sol.isValid('()[]{}'))  # True
    print(sol.isValid('(]'))  # False
    print(sol.isValid('([])'))  # True
