import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not wordList: return 0

        hair = {beginWord}
        foot = {endWord}
        wordList = set(wordList)
        res = 1
        while hair and foot:
            res += 1
            next_hair = set()
            for word in hair:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in foot:
                            return res
                        if new_word in wordList:
                            next_hair.add(new_word)
                            wordList.remove(new_word)
            hair = next_hair
            if len(hair) > len(foot):
                hair, foot = foot, hair
        return 0