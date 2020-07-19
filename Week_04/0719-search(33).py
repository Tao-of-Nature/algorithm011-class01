class Solution:
    def search(self, nums: List[int], target: int) -> int:

        res = -1
        if nums == []:
            return res

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[left] <= target < nums[pivot] or \
                    (nums[left] > nums[pivot] and (target >= nums[left] or target <= nums[pivot])):
                right = pivot - 1
            else:
                left = pivot + 1
        return res