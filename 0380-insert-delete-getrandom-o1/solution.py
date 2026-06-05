"""
LeetCode 0380 - Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Time:  O(1) average per op
Space: O(n)
"""


import random


class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        i = self.pos[val]
        last = self.vals[-1]
        self.vals[i] = last
        self.pos[last] = i
        self.vals.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))  # True
    print(rs.remove(2))  # False
    print(rs.insert(2))  # True
    print(rs.remove(1))  # True
    print(rs.insert(2))  # False
    print(rs.getRandom())  # 2
