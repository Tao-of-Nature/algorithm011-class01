class Solution:
    def isAnagram(self, s, t):

        # ------------------------------------way1
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # if s == t:
        #     return True
        # else:
        #     return False

        # ------------------------------------way2

        storage = {}
        s = list(s)
        t = list(t)
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        for value in s:
            if value not in storage.keys():
                storage[value] = 1
            else:
                storage[value] += 1
        for value in t:
            if value not in storage.keys():
                return False
            else:
                storage[value] -= 1

        for value in storage.keys():
            if storage[value] != 0:
                return False
        return True




def main():
    in_data1 = 'anagram'
    in_data2 = 'nagaram'

    s = Solution()
    res = s.isAnagram(in_data1, in_data2)

    print(res)


if __name__ == '__main__':
    main()
