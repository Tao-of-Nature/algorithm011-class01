class Solution:
    def firstUniqChar(self, s: str) -> int:

        times = {}
        for ch in s:
            times[ch] = times.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if times[ch] == 1:
                return i
        return -1