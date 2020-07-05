class Solution:
    def intersect(self, nums1, nums2):
        res = []
        data_storage = {}
        for value in nums1:
            if value not in data_storage.keys():
                data_storage[value] = 1
            else:
                data_storage[value] += 1
        for value in nums2:
            if value in data_storage.keys():
                if data_storage[value] == 0:
                    del data_storage[value]
                else:
                    res.append(value)
                    data_storage[value] -= 1
        return res





def main():
    in_data1 = [1, 1, 2, 3]
    in_data2 = [1, 2, 1]

    s = Solution()
    res = s.intersect(in_data1, in_data2)

    print(res)


if __name__ == '__main__':
    main()
