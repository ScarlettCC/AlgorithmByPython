# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = []
        queuetree = []
        queuetree.append(root)
        while len(queuetree):
            currentnode = queuetree.pop(0)   #默认移除列表最后一个
            result.append(currentnode.val)
            if currentnode.left:
                queuetree.append(currentnode.left)
            if currentnode.right:
                queuetree.append(currentnode.right)
        return result

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.PrintFromTopToBottom(pNode1))