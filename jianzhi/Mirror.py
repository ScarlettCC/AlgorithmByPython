# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        p=root.left
        root.left=root.right
        root.right=p
        self.Mirror(root.left)
        self.Mirror(root.right)
    def Mirror2(self, root):
        if not root:
            return
        stacknode = []
        stacknode.append(root)
        while len(stacknode):
            num = len(stacknode)
            rootnode=stacknode[num-1]
            stacknode.pop()
            if rootnode.left or rootnode.right:
                rootnode.left,rootnode.right=rootnode.right,rootnode.left
            if rootnode.left:
                stacknode.append(rootnode.left)
            if rootnode.right:
                stacknode.append(rootnode.right)
    def Mirror3(self, root):
        if not root:return
        que = [root]
        while len(que)>0:
            proot=que.pop(0)
            proot.left,proot.right = proot.right,proot.left
            if proot.left:
                que.append(proot.left)
            if proot.right:
                que.append(proot.right)

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
S.Mirror3(pNode1)
print(pNode1.right.val)