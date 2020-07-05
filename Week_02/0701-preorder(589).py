class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # ----------------------------way1
        if root is None:
            return []
        res = []
        def pre_order(root, res):

            res.append(root.val)
            for child in root.children:
                pre_order(child, res)
            return res

        res = pre_order(root, res)
        return res


        # -------------------------------way2
        # if root is None:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     current = stack.pop()
        #     start = len(stack)
        #     if current is not None:
        #         res.append(current.val)
        #     for child in current.children:
        #         stack.insert(start, child)
        # return res
