class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if nums == []:
            return False
        length = len(nums)
        end = length - 1
        for i in range(length-1, -1, -1):
            if nums[i] + i >= end:
                end = i
        if end == 0:
            return True
        else:
            return False
