


class Solution:
    def twoSum(self, nums, target):

        # -----------------way1
        # for i in range(len(nums)):
        #     if target - nums[i] in nums[i+1:]:
        #         return [i, nums.index(target - nums[i], i+1)]

        # -----------------way2
        value_store = {}
        for i, value in enumerate(nums):
            if target - value in value_store.keys():
                return [i, value_store[target - value]]
            else:
                value_store[value] = i
        return []




def main():
    in_data = [3,2,4]
    s = Solution()
    res = s.twoSum(in_data, 6)
    print(res)


if __name__ == '__main__':
    main()
