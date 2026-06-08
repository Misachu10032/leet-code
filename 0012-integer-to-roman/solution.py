"""
LeetCode 0012 - Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Time:  O(1)
Space: O(1)
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
        ]
        res = []
        for value, symbol in pairs:
            count, num = divmod(num, value)
            res.append(symbol * count)
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3749))  # MMMDCCXLIX
    print(sol.intToRoman(58))  # LVIII
    print(sol.intToRoman(1994))  # MCMXCIV
