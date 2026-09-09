"""
LeetCode 0224 - Basic Calculator
https://leetcode.com/problems/basic-calculator/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                result += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append((result, sign))
                result, sign = 0, 1
            elif ch == ")":
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result
        return result + sign * num


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate('1 + 1'))  # 2
    print(sol.calculate(' 2-1 + 2 '))  # 3
    print(sol.calculate('(1+(4+5+2)-3)+(6+8)'))  # 23
    print(sol.calculate('-(2+3)'))  # -5
