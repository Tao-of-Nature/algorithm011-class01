


class Solution:
    def moveZeroes(self, nums):

        # -----------------way1
        # lenth = len(nums)
        # j = 0
        # for i in range(lenth):
        #     if nums[i] == 0:
        #         j = min(j, i)
        #     else:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j += 1
        #
        # return

        # -----------------way2

        # for i in nums[:]:
        #     if i == 0:
        #         nums.remove(i)
        #         nums.append(0)

        # -----------------way3

        # lenth = len(nums)
        # j = 0
        # for i in range(lenth):
        #     if nums[i] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j += 1
        #
        # return
        # -----------------way4
        # offset = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         offset += 1
        #     else:
        #         nums[i-offset], nums[i] = nums[i], nums[i-offset]
        # return

        # -----------------way5
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1



def main():
    in_data = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(in_data)
    print(in_data)


if __name__ == '__main__':
    main()
