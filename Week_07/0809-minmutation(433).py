import string
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if end not in bank or not bank: return -1
        hair = {start}
        foot = {end}
        bank = set(bank)
        res = 0
        while hair and foot:
            res += 1
            next_hair = set()
            for word in hair:
                for i in range(len(word)):
                    for char in string.ascii_uppercase:
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in foot:
                            return res
                        if new_word in bank:
                            next_hair.add(new_word)
                            bank.remove(new_word)
            hair = next_hair
            if len(hair) > len(foot):
                hair, foot = foot, hair
        return -1