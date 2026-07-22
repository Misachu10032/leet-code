"""
LeetCode 0022 - Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Time:  O(4^n / sqrt(n))
Space: O(n)
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))  # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(sol.generateParenthesis(1))  # ['()']
