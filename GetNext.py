# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        pnext = None
        if pNode is None:
            return pnext
        if pNode.right is not None:
            nextnode = pNode.right
            while nextnode and nextnode.left:
                nextnode = nextnode.left
            pnext = nextnode
        elif pNode.next:
            pcur = pNode
            pparent = pNode.next
            while pparent and pparent.left!=pcur:
                pcur = pparent
                pparent = pcur.next
            pnext = pparent
        return pnext