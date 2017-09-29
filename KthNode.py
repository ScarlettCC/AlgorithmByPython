# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.inorderlist = []
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot==None or k<=0:
            return None
        self.inorder(pRoot)
        if k>len(self.inorderlist):
            return None
        else:
            return self.inorderlist[k-1]
    def inorder(self, node):
        if not node:
            return None
        self.inorder(node.left)
        self.inorderlist.append(node)
        self.inorder(node.right)