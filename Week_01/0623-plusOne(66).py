class Solution:
    def plusOne(self, digits):

        # --------------------------------way1
        # length = len(digits)
        # digits[-1] += 1
        # for i in range(length - 1, -1, -1):
        #     if digits[i] >= 10:
        #         up_v = digits[i] // 10
        #         digits[i] = digits[i] % 10
        #         if (i - 1) >= 0:
        #             digits[i - 1] += 1
        #         else:
        #             digits.insert(0, up_v)
        # return digits

        # -----------------------------------way2
        length = len(digits)
        up_v = 1
        for i in range(length-1, -1, -1):
            if digits[i] < 9:
                digits[i] += up_v
                return digits
            else:
                digits[i] = 0
        digits.insert(0, up_v)
        return digits

        # -----------------------------------way3
        # digits.reverse()
        # length = len(digits)
        # up_v = 1
        # for i in range(length):
        #     digits[i] += up_v
        #     if digits[i] // 10 > 0:
        #         digits[i] = digits[i] % 10
        #         if i == length - 1:
        #             digits.append(up_v)
        #     else:
        #         break
        # digits.reverse()
        # return digits



def main():
    in_data = [9, 9, 9, 9]
    s = Solution()
    res = s.plusOne(in_data)
    print(res)


if __name__ == '__main__':
    main()
