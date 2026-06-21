"""
LeetCode 0049 - Group Anagrams
https://leetcode.com/problems/group-anagrams/

Time:  O(n * k)
Space: O(n * k)
"""


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord("a")] += 1
            groups[tuple(key)].append(s)
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
