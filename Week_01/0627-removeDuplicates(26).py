class Solution:
    def removeDuplicates(self, nums):

        # --------------------------------way1
        length = len(nums)

        if length < 2:
            return length

        i = 1
        while i < length:
            if nums[i-1] == nums[i]:
                del nums[i-1]
                length -= 1
            else:
                i += 1

        return len(nums)

        # -----------------------------------way2
        length = len(nums)
        if length < 2:
            return length
        i = 1
        new_len = 1
        while i < length:
            if nums[i-1] != nums[i]:
                nums[new_len] = nums[i]
                new_len += 1
            i += 1
        return new_len


        # -----------------------------------way3




def main():

    in_data = [1, 1]
    s = Solution()
    res = s.removeDuplicates(in_data)
    print(res)


if __name__ == '__main__':
    main()
