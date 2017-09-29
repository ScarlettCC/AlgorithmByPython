# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if (len(pre) == 0) or (len(tin) == 0):
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

# 输出树某层
def printTreeNodeAtLevel(treeNode, level):
    if not TreeNode or level < 0:
        return None
    if level == 0:
        print treeNode.val
        return 1
    else:
        print printTreeNodeAtLevel(treeNode.left, --level)
        print printTreeNodeAtLevel(treeNode.right, --level)


# 已知树深按层输出
def printTreeByLevel(treehead, high):
    if not TreeNode or high < 0:
        return None
    for i in range(high):
        printTreeNodeAtLevel(treehead, i)


pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]

test = Solution()
newtree = test.reConstructBinaryTree(pre, tin)
printTreeByLevel(newtree, 2)
