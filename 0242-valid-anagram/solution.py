"""
LeetCode 0242 - Valid Anagram
https://leetcode.com/problems/valid-anagram/

Time:  O(n)
Space: O(1) (26 letters)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for a, b in zip(s, t):
            count[ord(a) - ord("a")] += 1
            count[ord(b) - ord("a")] -= 1
        return all(c == 0 for c in count)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram('anagram', 'nagaram'))  # True
    print(sol.isAnagram('rat', 'car'))  # False
