class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root is None:
            return []
        res = {}

        def level_Order(root, level):
            if level not in res.keys():
                res[level] = [root.val]
            else:
                res[level].append(root.val)

            for child in root.children:
                level_Order(child, level - 1)
            return

        level_Order(root, 0)
        output = [x for x in res.values()]
        return output
