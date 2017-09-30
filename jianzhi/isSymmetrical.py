# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetrical_core(pRoot,pRoot)
    def isSymmetrical_core(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetrical_core(pRoot1.left,pRoot2.right) and self.isSymmetrical_core(pRoot1.right,pRoot2.left)