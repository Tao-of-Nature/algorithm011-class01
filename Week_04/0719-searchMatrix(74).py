class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # -------------------way 1
        # length = len(matrix)
        # if length == 0:
        #     return False
        # tmp = []
        # for son in matrix:
        #     tmp += son
        #
        # left, right = 0, len(tmp) - 1
        # while left <= right:
        #     pivot = (left + right) // 2
        #     if tmp[pivot] == target:
        #         return True
        #     elif tmp[pivot] < target:
        #         left = pivot + 1
        #     else:
        #         right = pivot - 1
        # return False

        def search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return True
                elif nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return False

        if len(matrix) == 0:
            return False
        if matrix[0] == []:
            return False

        left, right = 0, len(matrix) - 1
        while left <= right:
            pivot = (left + right) // 2
            if matrix[pivot][0] <= target <= matrix[pivot][-1]:
                return search(matrix[pivot], target)
            elif matrix[pivot][-1] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return False
