"""
LeetCode 0068 - Text Justification
https://leetcode.com/problems/text-justification/

Time:  O(total characters)
Space: O(maxWidth)
"""


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line, length = [], 0
        for word in words:
            if line and length + len(line) + len(word) > maxWidth:
                gaps = len(line) - 1
                spaces = maxWidth - length
                if gaps == 0:
                    res.append(line[0] + " " * spaces)
                else:
                    q, r = divmod(spaces, gaps)
                    out = ""
                    for i in range(gaps):
                        out += line[i] + " " * (q + (1 if i < r else 0))
                    res.append(out + line[-1])
                line, length = [], 0
            line.append(word)
            length += len(word)
        last = " ".join(line)
        res.append(last + " " * (maxWidth - len(last)))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.fullJustify(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16))  # ['This    is    an', 'example  of text', 'justification.  ']
