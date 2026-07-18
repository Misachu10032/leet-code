"""
LeetCode 0208 - Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Time:  O(L) per op
Space: O(total characters)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))  # True
    print(trie.search('app'))  # False
    print(trie.startsWith('app'))  # True
    trie.insert('app')
    print(trie.search('app'))  # True
