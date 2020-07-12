class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def tmp_permute(n, sub_nums):
            if len(sub_nums) == len(nums):
                res.append(sub_nums[:])
                return
            for i in range(len(nums)):
                if nums[i] not in sub_nums:
                    sub_nums.append(nums[i])
                    tmp_permute(n+1, sub_nums)
                    sub_nums.pop()
            return

        res = []
        sub_nums = []
        tmp_permute(1, sub_nums)
        return res