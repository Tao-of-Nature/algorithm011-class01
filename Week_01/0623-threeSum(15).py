class Solution:
    def threeSum(self, nums):

        # ------------------------------------way1
        #
        # res = []
        # length = len(nums)
        # for i in range(length - 2):
        #     for j in range(i + 1, length - 1):
        #         for k in range(j + 1, length):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res_sort = sorted([nums[i], nums[j], nums[k]])
        #                 if res_sort not in res:
        #                     res.append(res_sort)
        # return res

        # -------------------------------------way3

        length = len(nums)
        if length <= 2:
            return []

        nums.sort()
        res = []
        for i in range(length - 2):
            value = nums[i]
            if i > 0 and value == nums[i - 1]:
                continue
            head = i + 1
            tail = length - 1
            while head < tail:
                if (nums[head] + nums[tail] + value) == 0:
                    res.append([nums[head], nums[tail], value])
                    head += 1
                    while nums[head] == nums[head - 1] and head < tail:
                        head += 1
                    tail -= 1
                    while nums[tail] == nums[tail + 1] and head < tail:
                        tail -= 1
                elif (nums[head] + nums[tail] + value) < 0:
                    head += 1
                else:
                    tail -= 1

        return res

        # ------------------------------------ way2
        # Result = []
        # ResultDict = {}
        # nums.sort()
        #
        # dataHash = {-x:i for i, x in enumerate(nums)}
        #
        # for index1, value1 in enumerate(nums):
        #     if index1 > 0 and value1 == nums[index1-1]:
        #         continue
        #     # if value1 > 0:
        #     #     break
        #     for index2, value2 in enumerate(nums[index1+1:]):
        #         value3 = value1 + value2
        #         if value3 in dataHash.keys():
        #             if dataHash[value3] == index1 or dataHash[value3] == index1 + index2 + 1:
        #                 continue
        #             temp = sorted([value1, value2, -value3])
        #             tempkeys = ','.join(str(x) for x in temp)
        #             if tempkeys not in ResultDict:
        #                 Result.append(temp)
        #                 ResultDict[tempkeys] = True
        # return Result


def main():
    in_data = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    s = Solution()
    res = s.threeSum(in_data)
    print(res)


if __name__ == '__main__':
    main()
