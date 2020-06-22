class Solution:


    def climbStairs(self, n):

        # --------------------------------------way1
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #
        #     res = [0]*n
        #     res[0] = 1
        #     res[1] = 2
        #     for i in range(2, n):
        #         res[i] = res[i-1] + res[i-2]
        #
        #     return res[n-1]

        # ---------------------------------------way2
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #
        #     pre2_res = 1
        #     pre1_res = 2
        #     for i in range(3, n+1):
        #         res = pre1_res + pre2_res
        #         pre1_res, pre2_res = res, pre1_res
        #
        #     return res

        # ----------------------------------------way3

        # tmp_res = [None] * n
        # tmp_res[0] = 1
        # if n >= 2:
        #     tmp_res[1] = 2
        #
        # def climb_child(n):
        #     if tmp_res[n-1] is None:
        #         tmp_res[n-1] = climb_child(n-1) + climb_child(n-2)
        #     return tmp_res[n-1]
        # return climb_child(n)
        #
        # -----------------------------------------way4

        use = {0: 1, 1: 1}

        def cb(n):
            if n not in use.keys():
                rst = cb(n - 1) + cb(n - 2)
                use[n] = rst
            return use[n]

        return cb(n)



def main():
    in_data = 90
    s = Solution()
    print(s.climbStairs(in_data))


if __name__ == '__main__':
    main()
