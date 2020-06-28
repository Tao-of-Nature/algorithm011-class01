class Solution:
    def isValid(self, s):

        value_stack = ['a']
        value_hash = {'(': ')', '[': ']', '{': '}', 'a': 'a'}
        for value in s:
            if value in value_hash:
                value_stack.append(value)
            elif value != value_hash[value_stack.pop()]:
                return False

        if len(value_stack) == 1:
            return True
        else:
            return False


def main():
    in_data = "["
    s = Solution()
    res = s.isValid(in_data)
    print(res)


if __name__ == '__main__':
    main()
