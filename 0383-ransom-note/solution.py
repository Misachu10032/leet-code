"""
LeetCode 0383 - Ransom Note
https://leetcode.com/problems/ransom-note/

Time:  O(m + n)
Space: O(1) (26 letters)
"""


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        for ch in ransomNote:
            if available[ch] == 0:
                return False
            available[ch] -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct('a', 'b'))  # False
    print(sol.canConstruct('aa', 'ab'))  # False
    print(sol.canConstruct('aa', 'aab'))  # True
