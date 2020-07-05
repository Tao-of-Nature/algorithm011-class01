class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # ----------------------------way1
        # res = []
        # def post_order(root, res):
        #     if root is None:
        #         return []
        #     for child in root.children:
        #         post_order(child, res)
        #     res.append(root.val)
        #     return res
        # res = post_order(root, res)
        # return res

        # -------------------------------way2
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp is not None:
                res.append(tmp.val)
            for child in tmp.children:
                stack.append(child)
        res = res[::-1]
        return res
