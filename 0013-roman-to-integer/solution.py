"""
LeetCode 0013 - Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, ch in enumerate(s):
            if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
                total -= values[ch]
            else:
                total += values[ch]
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt('III'))  # 3
    print(sol.romanToInt('LVIII'))  # 58
    print(sol.romanToInt('MCMXCIV'))  # 1994
