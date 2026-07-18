"""
LeetCode 0211 - Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Time:  O(L) add, O(26^dots * L) search
Space: O(total characters)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('mad')
    print(wd.search('pad'))  # False
    print(wd.search('bad'))  # True
    print(wd.search('.ad'))  # True
    print(wd.search('b..'))  # True
