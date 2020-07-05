学习笔记

心得一:
    不知道为什么二叉树的遍历给定义成中等难度了,而N叉树的遍历成为了简单难度.但自己实际,感觉思考多的,反而是N叉树

心得二:
    二叉树的中序遍历中,有个方法是颜色标注法.但在前序遍历上,老外有个超牛的解法.
    def preorderTraversal(self, root):
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ret.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ret
    但讲这个方法重新借鉴回中序,发现就没有那么简单了.
    