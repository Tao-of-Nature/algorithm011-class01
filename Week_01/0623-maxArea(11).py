class Solution:
    def maxArea(self, height):

        length = len(height)
        head = 0
        tail = length - 1
        max_area = 0

        while head < tail:
            if height[head] <= height[tail]:
                max_area = max(max_area, height[head] * (tail - head))
                head += 1
            else:
                max_area = max(max_area, height[tail] * (tail - head))
                tail -= 1

        return max_area

def main():
    in_data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    res = s.maxArea(in_data)
    print(res)


if __name__ == '__main__':
    main()
