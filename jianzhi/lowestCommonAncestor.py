# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    '''
    @:param root: The root of the binary tree
    @:param nodeA and nodeB:two nodes in a BInary
    @:return :return the least common ancestor of the two nodes
    '''
    #二叉搜索树最低公共祖先
    def findParent(self, root, nodeA, nodeB):
        if root==None or nodeA == None or nodeB == None:
            return False
        if nodeA == nodeB:
            return False
        while root != None:
            if root.val > nodeA.val and root.val > nodeB.val:
                root = root.left
            elif root.val < nodeA.val and root.val < nodeB.val:
                root = root.right
            else:
                return root
        return False
    #普通二叉树中两节点最低公共祖先
    def lowestCommonAncestor(self, root, nodeA, nodeB):
        if root==None or nodeA == None or nodeB == None:
            return False
        pathA = self.findPath(root, nodeA)
        pathB = self.findPath(root, nodeB)
        lenA = len(pathA)
        lenB = len(pathB)
        diff = abs(lenA-lenB)
        if lenA>lenB:
            markA = lenA-diff-1
            markB = lenB-1
        else:
            markA = lenA-1
            markB = lenB-diff-1
        while markA >=0 and markB >= 0:
            if pathA[markA] == pathB[markB]:
                return pathA[markA]
            markB-=1
            markA-=1
        return None
    def findPath(self, root, targetnode):
        path = []
        if root==None or targetnode == None:
            return path
        elif targetnode.val == root.val:
            path.append(root)
            return path
        if root.left:
            pathleft = self.findPath(root.left, targetnode)
            if len(pathleft) != 0:
                path.append(root)
                path.extend(pathleft)
        if root.right:
            pathright = self.findPath(root.right, targetnode)
            if len(pathright) != 0:
                path.append(root)
                path.extend(pathright)
        return path
pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)
pNode8 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
S = Solution()
#print S.findParent(pNode1, pNode7, pNode3).val
print S.lowestCommonAncestor(pNode1, pNode4, pNode8)