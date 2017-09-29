# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def PrintByZigzag(self, pRoot):
        # write code here
        res, temp = [], []
        if pRoot is None:
            return res
        temp = [pRoot]
        right = True
        while temp:
            curstack,nextstack = [],[]
            if right:
                for node in temp:
                    curstack.append(node.val)
                    if node.left:
                        nextstack.append(node.left)
                    if node.right:
                        nextstack.append(node.right)
            else:
                for node in temp:
                    curstack.append(node.val)
                    if node.right:
                        nextstack.append(node.right)
                    if node.left:
                        nextstack.append(node.left)
            nextstack.reverse()
            temp = nextstack
            right = not right
            res.append(curstack)
        return res
    def PrintByZigzag2(self,pRoot):
        res,temp = [],[]
        if not pRoot:
            return res
        temp = [pRoot]
        lefttoright = True
        while temp:
            cur, nextstack = [], []
            for node in temp:
                cur.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            if not lefttoright:
                cur.reverse()
            res.append(cur)
            temp = nextstack
            lefttoright = not lefttoright
        return res
    def PrintToSeveralLevel(self, pRoot):
        # write code here
        res,temp = [],[]
        if pRoot is None:
            return res
        temp = [pRoot]
        while temp:
            curstack, nextstack = [],[]
            for node in temp:
                curstack.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
            res.append(curstack)
            temp = nextstack
        return res
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
aList = S.PrintByZigzag2(pNode1)
print(aList)