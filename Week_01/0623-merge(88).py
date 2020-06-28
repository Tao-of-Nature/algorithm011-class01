class Solution:
    def merge(self, nums1, m, nums2, n):

        # ------------------------------------way1
        tmp_nums = nums1
        length = len(tmp_nums)
        tmp_nums[m:] = nums2
        tmp_nums.sort()
        if length > (m+n):
            tmp = length - (n + m)
            for _ in range(tmp):
                tmp_nums.append(0)
        return

        # ------------------------------------way2



def main():
    in_data1 = [1, 2, 3, 0, 0, 0, 0, 0]
    in_data2 = [2, 5, 6]
    m = 3
    n = 3
    s = Solution()
    res = s.merge(in_data1, m, in_data2, n)
    print(res)


if __name__ == '__main__':
    main()
