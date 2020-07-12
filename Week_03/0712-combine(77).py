class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine_internal(start, tmp):
            if len(tmp) == k:
                result.append(tmp[:])
                return
            for i in range(start, n+1):
                tmp.append(i)
                combine_internal(i+1, tmp)
                tmp.pop()
            return

        tmp = []
        result = []
        combine_internal(1, tmp)
        return result